from django.db import models

# Create your models here.


class Feed(models.Model):
    id = models.IntegerField(primary_key=True)
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    body = models.TextField()

    class Meta:
        verbose_name = 'Publicación'
        verbose_name_plural = 'Publicaciones'

    def __str__(self):
        return self.author
