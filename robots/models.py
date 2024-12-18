from django.db import models


class Robot(models.Model):
    serial = models.CharField(max_length=5, blank=False, null=False)
    model = models.CharField(max_length=2, blank=False, null=False)
    version = models.CharField(max_length=2, blank=False, null=False)
    created = models.DateTimeField(blank=False, null=False)

    def save(self, *args, **kwargs):
        if not self.serial:
            self.serial = f'{self.model}-{self.version}'
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Робот {self.serial} создан {self.created}.'
