from django.db import models


# Create your models here.
class Article(models.Model):
    article_title = models.TextField(max_length=30)
    article_date = models.DateField()
    article_text = models.CharField(max_length=10000000)
    article_img = models.ImageField('blog_images/')
