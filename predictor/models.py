from django.db import models


class Prediction(models.Model):
    DISEASE_CHOICES = [
        ('healthy', 'Healthy Leaf'),
        ('leaf_scorch', 'Leaf Scorch'),
        ('powdery_mildew', 'Powdery Mildew'),
        ('angular_leaf', 'Angular Leaf Spot'),
    ]

    image = models.ImageField(upload_to='predictions/')
    disease_type = models.CharField(max_length=50, choices=DISEASE_CHOICES)
    confidence = models.FloatField(help_text="Confidence percentage")
    created_at = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "Predictions"

    def __str__(self):
        return f"{self.get_disease_type_display()} - {self.created_at.strftime('%Y-%m-%d %H:%M')}"

    def disease_name(self):
        return self.get_disease_type_display()

    def confidence_percentage(self):
        return f"{self.confidence:.2f}%"
