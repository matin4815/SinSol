from django.db import models


class ProductCategory(models.Model):
  title = models.CharField(max_length=150)
  name = models.CharField(max_length=150)


  def __str__(self):
    return self.title
