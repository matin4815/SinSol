from django.contrib import admin
from .models import Tag


class ProductTagAdmin(admin.ModelAdmin):
  list_display = ['__str__', 'slug']

  class Meta:
    model = Tag


admin.site.register(Tag, ProductTagAdmin)
