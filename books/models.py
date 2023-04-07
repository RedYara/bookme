from django.db import models

# Create your models here.
class Authors(models.Model):
    name = models.CharField(verbose_name="name", max_length=100)
    surname = models.CharField(verbose_name="surname", max_length=100)
    patronymic = models.CharField(verbose_name="patronymic", max_length=100)

    class Meta:
        verbose_name = "author"
        verbose_name_plural = "authors"

    def __str__(self) -> str:
        return self.name

class Genres(models.Model):
    name = models.CharField(verbose_name="name", max_length=100)

    class Meta:
        verbose_name = "genre"
        verbose_name_plural = "genres"

    def __str__(self) -> str:
        return self.name

class Books(models.Model):
    name = models.CharField(verbose_name="name", unique=True, max_length=100)
    photo = models.ImageField(verbose_name="photo",upload_to="photos/")
    description = models.TextField(verbose_name="description")
    genre = models.ManyToManyField(Genres,verbose_name="genre", max_length=100)
    author = models.ManyToManyField(Authors,verbose_name="author", max_length=100)
    ispopular = models.BooleanField("ispopular")

    class Meta:
        verbose_name = "book"
        verbose_name_plural = "books"

    def __str__(self) -> str:
        return self.name
    