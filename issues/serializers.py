from project.models import Project
from  rest_framework import serializers
from rest_framework import status
from .models import Issue
from user.models import User

class IssueSerializer(serializers.ModelSerializer):
    assignee = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.none()
    )

    class Meta:
        model = Issue
        fields = ['id', 'name', 'description', 'priority', 'type', 'status', 'author', 'assignee', 'project', 'time_created']
        read_only_fields = ['id', 'author', 'time_created']

    
    def __init__(self, *args, **kwargs):
        super(IssueSerializer, self).__init__(*args, **kwargs)
        # Dynamically adjust the queryset for the 'assignee' field based on the 'project' context
        project_pk = self.context.get('project_pk', None)
        if project_pk:
            project = Project.objects.get(pk=project_pk)
            self.fields['assignee'].queryset = project.contributors.all()

    def create(self, validated_data):
        issue = Issue.objects.create(**validated_data, author=self.context['request'].user)
        return issue

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.priority = validated_data.get('priority', instance.priority)
        instance.type = validated_data.get('type', instance.type)
        instance.status = validated_data.get('status', instance.status)
        instance.assignee = validated_data.get('assignee', instance.assignee)
        instance.save()
        return instance
