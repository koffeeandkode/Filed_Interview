from django.http import HttpResponse
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status

import datetime

from django.shortcuts import render

from .models import song, podcast, audiobook
from audio_server_webApp.serializers import songSerializer, podcastSerializer, audiobookSerializer
from rest_framework.decorators import api_view

audiofiletype = {"song": song, "audiobook": audiobook, "podcast": podcast}
audio_serializer = {"song": songSerializer, "audiobook": audiobookSerializer, "podcast": podcastSerializer}

def index(request):
    latest_song_list = song.objects.order_by('-upload_time')[:5]
    context = {'latest_song_list': latest_song_list}
    return render(request, 'audio_server_webApp/index.html', context)


@api_view(['GET', 'POST', 'DELETE'])
def create_api(request):

	if request.method == 'POST':

		request_data = JSONParser().parse(request)
		audio_type = request_data.get("audioFileType", None)

		if audio_type is None:
			return JsonResponse({'message': 'The request is invalid: 400 bad request 1'})

		audio_file_obj = audiofiletype.get(audio_type)
		audio_metadata = request_data.get("audioFileMetadata")

		if audio_metadata["duration_in_sec"] <= 0:
			audio_metadata["duration_in_sec"] = 0

		audio_metadata["upload_time"] = datetime.datetime.utcnow()


		serializer_obj = audio_serializer.get(audio_type)
		audio_serializer_obj = serializer_obj(data = audio_metadata)
		print(audio_serializer_obj)
		
		if audio_serializer_obj.is_valid():
			audio_serializer_obj.save()
			return JsonResponse(audio_serializer_obj.data, status=status.HTTP_201_CREATED)

		
	return JsonResponse({'message': 'The request is invalid: 400 bad request 2'})

	

@api_view(['DELETE', 'GET'])
def delete_api(request, audioFileType, audioFileID):

	if (request.method):

		if audioFileType not in audiofiletype:
			return JsonResponse({'message': 'The request is invalid: 400 bad request 1'})

		audio_file_obj = audiofiletype.get(audioFileType)

		try:

			queryset = audio_file_obj.objects.filter(id = int(audioFileID))

			#if not queryset.one():
			#	return JsonResponse({'message': 'The request is invalid: 400 bad request 2'})

			queryset.delete()
			return JsonResponse({'message': 'The record has been deleted'})

		except Exception as e:
			print(queryset)
			print(e)
			return JsonResponse({'message': 'The request is invalid: 400 bad request 3'})

	return JsonResponse({'message': 'The request is invalid: 400 bad request 4'})


@api_view(['GET', 'PUT', 'DELETE'])
def update_api(request, audioFileType, audioFileID):

	if request.method == "PUT":

		request_data = JSONParser().parse(request)
		audio_type = request_data.get("audioFileType", None)

		if audio_type not in audiofiletype:
			return JsonResponse({'message': 'The request is invalid: 400 bad request 1'})

		audio_file_obj = audiofiletype.get(audio_type)
		audio_metadata = request_data.get("audioFileMetadata")
		audio_metadata["upload_time"] = datetime.datetime.utcnow()

		try:
			
			if audioFileID is not None:

				queryset = audio_file_obj.objects.get(id = audioFileID)

				if not audio_metadata:

					return  JsonResponse({'message': 'The request is invalid: 400 bad request 1'})

				serializer_obj = audio_serializer.get(audio_type)
				audio_serializer_obj = serializer_obj(queryset, data = audio_metadata)
		
				if audio_serializer_obj.is_valid():
					audio_serializer_obj.save()
					return JsonResponse(audio_serializer_obj.data, status=status.HTTP_201_CREATED)

				return JsonResponse(audio_serializer_obj.errors, status=status.HTTP_400_BAD_REQUEST)

		except Exception as e:
				print(queryset)
				print(e)
				return JsonResponse({'message': 'The request is invalid: 400 bad request 2'})


	return JsonResponse({'message': 'The request is invalid: 400 bad request 3'})




@api_view(['GET', 'PUT', 'DELETE'])
def get_api(request, audioFileType, audioFileID = None):

	if (request.method == "GET"):

		print(audioFileType)
		print(audioFileID)

		if audioFileType not in audiofiletype:
			return JsonResponse({'message': 'The request is invalid: 400 bad request'})

		audio_obj = audiofiletype.get(audioFileType)
		serializer_obj = audio_serializer.get(audioFileType)
		data = None

		try:
			if audioFileID is not None:
				queryset = audio_obj.objects.filter(id = audioFileID)

			else: 
				queryset = audio_obj.objects.all()

			final_data = serializer_obj(queryset, many=True)
			return JsonResponse(final_data.data, safe=False)

		except:

			return JsonResponse({'message': 'The request is invalid: 400 bad request'})

		return JsonResponse({'message': 'The request is invalid: 400 bad request'})
