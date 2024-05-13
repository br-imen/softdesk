from  rest_framework import serializers
from rest_framework import status
from .models import Issue
from user.models import User

class IssueSerializer(serializers.ModelSerializer):
    assignees = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=User.objects.all()
    )

    class Meta:
        model = Issue
        fields = ['id', 'name', 'description', 'priority', 'type', 'status', 'author', 'assignees', 'project', 'time_created']
        read_only_fields = ['id', 'author', 'time_created']

    def create(self, validated_data):
        assignees_data = validated_data.pop('assignees')
        issue = Issue.objects.create(**validated_data, author=self.context['request'].user)
        issue.assignees.set(assignees_data)
        return issue

    def update(self, instance, validated_data):
        if instance.author != self.context['request'].user:
            raise serializers.ValidationError("You are not allowed to update this issue.", code=status.HTTP_403_FORBIDDEN)
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.priority = validated_data.get('priority', instance.priority)
        instance.type = validated_data.get('type', instance.type)
        instance.status = validated_data.get('status', instance.status)
        assignees_data = validated_data.get('assignees')
        if assignees_data is not None:
            instance.assignees.set(assignees_data)
        instance.save()
        return instance
