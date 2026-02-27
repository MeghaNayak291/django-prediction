from django.contrib import admin
from .models import Prediction


@admin.register(Prediction)
class PredictionAdmin(admin.ModelAdmin):
    list_display = ('disease_name', 'confidence_percentage', 'created_at')
    list_filter = ('disease_type', 'created_at')
    search_fields = ('disease_type',)
    readonly_fields = ('created_at', 'image')
