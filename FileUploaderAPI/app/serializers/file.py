from rest_framework import serializers
from FileUploaderAPI.app.models.file import File


class FileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = File
        fields = ('title')

