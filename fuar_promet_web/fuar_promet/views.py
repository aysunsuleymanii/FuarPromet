from django.shortcuts import render
from django.views.generic import ListView, DetailView

from fuar_promet.models import *
from django.conf import settings


def home(request):
    return render(request, "home.html", {"languages": settings.LANGUAGES})


def contact(request):
    return render(request, "contact.html")


def about(request):
    return render(request, "about.html")


def our_work(request):
    return render(request, "our_work.html")


def products(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'products.html', {'products': products, 'categories': categories})


def services(request):
    services = Service.objects.all()
    return render(request, 'services.html', {'services': services})


class ServicesListView(ListView):
    model = Service
    template_name = 'services.html'
    context_object_name = 'services'


class ServiceDetailView(DetailView):
    model = Service
    template_name = 'service_detail.html'
    context_object_name = 'service'


class ProductListView(ListView):
    model = Product
    template_name = 'products.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'


# def kitchen_view(request):
#     woods = Product.objects.all()
#     return render(request, 'kitchen_color.html', {'woods': woods})

# In your views.py (conceptual example)
def kitchen_view(request):
    # This list of objects must be available in the template context
    wood_options = Product.objects.all()
    context = {'woods': wood_options}
    return render(request, 'kitchen_color.html', context)
