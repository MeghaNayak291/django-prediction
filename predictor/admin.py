from django.contrib import admin
<<<<<<< HEAD
from .models import Prediction


@admin.register(Prediction)
class PredictionAdmin(admin.ModelAdmin):
    list_display = ('disease_name', 'confidence_percentage', 'created_at')
    list_filter = ('disease_type', 'created_at')
    search_fields = ('disease_type',)
    readonly_fields = ('created_at', 'image')
=======


from .models import Prediction

admin.site.register(Prediction)

>>>>>>> 009df0ffc57ddd5736de8738092067bf21f48c79
