from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from fuar_promet.models import *
from django.conf import settings

# ---------- BASIC PAGES ----------

def home(request):
    return render(request, "home.html", {"languages": settings.LANGUAGES})


def contact(request):
    return render(request, "contact.html")


def about(request):
    return render(request, "about.html")


def our_work(request):
    return render(request, "our_work.html")


# ---------- PRODUCTS ----------

# ALL PRODUCTS
def products_list(request):
    products = Product.objects.all().order_by("-created_at")
    categories = Category.objects.filter(parent__isnull=True)

    return render(request, "products.html", {
        "products": products,
        "categories": categories,
        "page_title": "All Products",
    })




# ALL DECORATIVE PRODUCTS
def decorative_products_list(request):
    decorative_root = Category.objects.filter(
        parent__isnull=True,
        name__iexact="decorative products"
    ).first()

    products = Product.objects.filter(
        category__in=decorative_root.subcategories.all()
    ) if decorative_root else Product.objects.none()

    categories = decorative_root.subcategories.all() if decorative_root else []

    return render(request, "products.html", {
        "products": products,
        "categories": categories,
        "page_title": "Decorative Products",
    })




def category_products(request, category_id):
    category = get_object_or_404(Category, id=category_id)

    if category.subcategories.exists():
        products = Product.objects.filter(
            category__in=category.subcategories.all()
        )
        categories = category.subcategories.all()
    else:
        products = Product.objects.filter(category=category)
        categories = [category]

    return render(request, "products.html", {
        "products": products,
        "categories": categories,
        "page_title": category.name,
    })




# ---------- SERVICES ----------

def services(request):
    services = Service.objects.all()
    return render(request, "services.html", {"services": services})


class ServicesListView(ListView):
    model = Service
    template_name = "services.html"
    context_object_name = "services"


class ServiceDetailView(DetailView):
    model = Service
    template_name = "service_detail.html"
    context_object_name = "service"


# ---------- PRODUCT DETAIL ----------

class ProductDetailView(DetailView):
    model = Product
    template_name = "product_detail.html"
    context_object_name = "product"


# ---------- OTHER ----------

def kitchen_view(request):
    woods = Product.objects.all()
    return render(request, "kitchen_color.html", {"woods": woods})