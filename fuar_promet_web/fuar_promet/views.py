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

def products_list(request):
    """
    Optional: show ALL products (no category pre-selected)
    """
    products = Product.objects.all().order_by("-created_at")

    context = {
        "products": products,
        "categories": Category.objects.filter(subcategories__isnull=True),
    }
    return render(request, "products.html", context)


def category_products(request, category_id):
    """
    Show products for a SINGLE category (used by navbar & category pages)
    """
    category = get_object_or_404(Category, id=category_id)

    # Only allow leaf categories
    if category.subcategories.exists():
        # Optional: redirect or show empty page
        products = Product.objects.none()
    else:
        products = Product.objects.filter(category=category)

    # Filters
    brand_param = request.GET.get("brand")
    stock_param = request.GET.get("stock")

    if brand_param:
        products = products.filter(brand_id=brand_param)

    if stock_param == "in-stock":
        products = products.filter(stock__gt=0)
    elif stock_param == "out-of-stock":
        products = products.filter(stock=0)

    products = products.order_by("-created_at")

    context = {
        "category": category,
        "products": products,
    }
    return render(request, "category_products.html", context)


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