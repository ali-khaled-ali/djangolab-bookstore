from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# Create your models here.

class Category(models.Model):
    class Meta:
        verbose_name_plural = "categories"
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        name = self.name
        if len(name) < 2:
            raise ValidationError("min category name must be bigger than 2 charachters")

    def __str__(self):
        return self.name
class Isbn(models.Model):
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    isbn_no = models.AutoField(primary_key=True)

    def clean(self):
        title = self.title
        if len(title) < 10 or len(title) > 50:
            raise ValidationError("title Must be between 10 & 50")

    def __str__(self):
        return f"author: {self.author}| title: {self.title}  | no#: {self.isbn_no} "

class Book(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True, related_name='books')
    content = models.TextField(max_length=2048)
    categories = models.ManyToManyField(Category)
    isbn = models.OneToOneField(Isbn,on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return self.isbn.title
