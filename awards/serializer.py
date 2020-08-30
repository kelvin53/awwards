from rest_framework import serializers
from .models import Project,Profile


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('title','image','description','profile','link','design','usability','content')

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('profile_photo','user','bio','contact')
