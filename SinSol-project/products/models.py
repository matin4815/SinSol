from django.db import models
from SinSol.utils import unique_slug_generator
from django.db.models.signals import pre_save
from categories.models import ProductCategory

class ProductsManager(models.Manager):
  def get_product_by_category(self, category_name):
    return self.get_queryset().filter(categories__name__iexact=category_name)




class Product(models.Model):
  title = models.CharField(max_length=100)
  pub_date = models.DateTimeField(auto_now_add=True)
  image = models.ImageField(upload_to='images/')
  slug = models.SlugField(unique=True, max_length=100, blank=True)
  categories = models.ManyToManyField(ProductCategory, blank=True)


  objects = ProductsManager()

  def __str__(self):
    return self.title


def slug_generator(sender, instance, *args, **kwargs):
  if not instance.slug:
    instance.slug = unique_slug_generator(instance)

pre_save.connect(slug_generator, sender=Product)
