from django.db import models

class HomepageWellcomeTextModel(models.Model):
    description = models.TextField(
        null=False,
        blank=False,
    )
    class Meta:
        verbose_name = 'Add Welcome text'