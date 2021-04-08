from rest_framework import serializers 
from audio_server_webApp.models import song, podcast, audiobook
 
 
class songSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = song
        fields = ('id',
                  'song_name',
                  'duration_in_sec',
                  'upload_time')


class podcastSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = podcast
        fields = ('id',
                  'podcast_name',
                  'duration_in_sec',
                  'upload_time',
                  'host')

class audiobookSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = audiobook
        fields = ('id',
                  'audiobook_name',
                  'author_name',
                  'narrator',
                  'duration_in_sec',
                  'upload_time')