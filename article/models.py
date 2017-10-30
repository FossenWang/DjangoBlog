from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=16)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=16)

    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    pub_date = models.DateTimeField('published date')
    
    author = models.ForeignKey(Author, default=1, on_delete=models.SET_DEFAULT)
    category = models.ForeignKey(Category, default=1, on_delete=models.SET_DEFAULT)
    tags = models.ManyToManyField(Tag)
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    content = models.CharField(max_length=500)
    pub_date = models.DateTimeField('published date')

    article = models.ForeignKey(Article,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.content