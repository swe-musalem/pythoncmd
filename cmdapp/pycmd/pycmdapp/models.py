from django.db import models

# Create your models here.

class Cmd(models.Model):
    command = models.TextField()

    def __str__(self) -> str:
        return f"{self.command}"