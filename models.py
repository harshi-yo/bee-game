from django.db import models

class HighScore(models.Model):
    score = models.IntegerField(default=0)

    def __str__(self):
        return str(self.score)
