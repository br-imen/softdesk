from django.forms import ValidationError
from rest_framework import serializers
from .models import Project
from user.models import User


class ContributorSerializer(serializers.ModelSerializer):
    def validate(self, value):
        pass

    class Meta:
        model = User
        fields = ["id"]


class ProjectSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only=True)
    contributors = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), many=True, required=False
    )

    def create(self, validated_data):
        try:
            request = self.context.get("request")

            contributors = validated_data.pop("contributors", [])
            project = Project.objects.create(
                **validated_data, author=request.user
            )
            project.contributors.set(contributors)
            project.contributors.add(request.user)
        except ValueError:
            raise ValidationError(
                "Request context is required for creating projects."
            )
        return project

    class Meta:
        model = Project
        fields = [
            "id",
            "name",
            "description",
            "type",
            "author",
            "contributors",
            "time_created",
        ]
        read_only_fields = ["id", "author"]
