from django.contrib import admin

from issues.models import Issue


@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    pass
