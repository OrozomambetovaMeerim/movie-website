from django.db import models


class Movie(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    genre = models.CharField(max_length=255)
    produser = models.CharField(max_length=255)
    year = models.IntegerField()
    img = models.ImageField(upload_to='main', null=True, blank=True )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    views_count = models.IntegerField(default=0)
    is_publicated = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'фильм'
        verbose_name_plural = 'Фильмы'
        ordering = ['name']

