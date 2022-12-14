from django.contrib import admin

from CleverFridge.common.models import HomepageWellcomeTextModel


@admin.register(HomepageWellcomeTextModel)
class HomepageWellcomeTextAdmin(admin.ModelAdmin):
    pass
