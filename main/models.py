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


class Genre(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

class Meta:
    verbose_name = 'жанр'
    verbose_name_plural = 'жанры'
    ordering = ['name']



class Reviews(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField()
    text = models.TextField()
    parent = models.ForeignKey(
        'self', verbose_name='Родитель', 
        on_delete=models.SET_NULL, blank=True, null=True)
    movie = models.ForeignKey(Movie, verbose_name='фильм', on_delete=models.CASCADE)

def __str__(self):
    return f"{self.name} - {self.movie}"

class Meta:
    verbose_name = 'Отзыв'
    verbose_name_plural = 'Отзывы'
    ordering = ['name']


class News(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    author = models.CharField(max_length=60)
    movie = models.ForeignKey(Movie, verbose_name='фильм', on_delete=models.CASCADE)


    def __str__(self):
        return self.name

class Meta:
    verbose_name = 'Новость'
    verbose_name_plural = 'Новости'
    ordering = ['name']
