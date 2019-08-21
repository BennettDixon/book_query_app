from django.db import models

# Create your models here.


class Author(models.Model):
    """
        Author class for graphql api test
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Book(models.Model):
    """
         Movie class for graphql api test
    """
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_year = models.IntegerField

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)
