from django.db import models


class Movie(models.Model):
    name = models.CharField(max_length=200, verbose_name="movie_name")
    writer = models.CharField(max_length=200, verbose_name="movie_writer_name")
    released = models.BooleanField(default=True, verbose_name="is_movie_released")
    producer = models.CharField(blank=True, null=True, verbose_name="movie_producer_name")
    director = models.CharField(blank=True, null=True, verbose_name="movie_director_name")

    def __str__(self):
        print(self.name)

