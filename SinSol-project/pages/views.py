from django.shortcuts import render
from categories.models import ProductCategory
from products.models import Product
from django.views.generic import ListView
from django.http import Http404

def index(request):
  categories = ProductCategory.objects.all()

  context = {
    'categories': categories,

  }

  return render(request, 'pages/index.html', context)

class CategoryView(ListView):
  template_name = 'pages/index.html'
  paginate_by = 12
  
  def get_queryset(self):
    category_name = self.kwargs['category_name']
    category = ProductCategory.objects.filter(name__iexact=category_name).first()
    if category is None: 
      raise Http404("category not found")
  
    return Product.objects.get_product_by_category(category_name)


def about(request):
  return render(request, 'pages/about.html')