from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from fuar_promet.models import *
from django.conf import settings
from django.db.models import Q


# ---------- BASIC PAGES ----------

def home(request):
    best_sellers = [
        {'image': '1.jpg', 'name': 'Calcutta'},
        {'image': '2.jpg', 'name': 'Cashmere'},
        {'image': '3.png', 'name': 'Elvira'},
        {'image': '4.jpg', 'name': 'Afrika'},
        {'image': '5.png', 'name': 'Efes'},
        {'image': '6.png', 'name': 'Kumsal'},
        {'image': '7.jpeg', 'name': 'Traverten'},
        {'image': '8.jpg', 'name': 'İyon'},
        {'image': '9.jpg', 'name': 'Dor'},
        {'image': '10.jpg', 'name': 'Resif'},
    ]

    context = {
        'best_sellers': best_sellers
    }
    return render(request, 'home.html', context)


def contact(request):
    return render(request, "contact.html")


def about(request):
    return render(request, "about.html")


def our_work(request):
    return render(request, "our_work.html")


# ALL PRODUCTS
def products_list(request):
    products = Product.objects.all().order_by("-created_at")
    categories = Category.objects.filter(parent__isnull=True)

    return render(request, "products.html", {
        "products": products,
        "categories": categories,
        "page_title": "All Products",
        "is_decorative": False,  # ADD THIS
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
        "is_decorative": True,  # ADD THIS
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

    # Determine if this category belongs to Decorative Products
    is_decorative = False
    current_cat = category
    while current_cat.parent:
        if current_cat.parent.name.lower() == "decorative products":
            is_decorative = True
            break
        current_cat = current_cat.parent

    # Check if the category itself is Decorative Products
    if category.name.lower() == "decorative products":
        is_decorative = True

    return render(request, "products.html", {
        "products": products,
        "categories": categories,
        "category": category,  # ADD THIS
        "page_title": category.name,
        "is_decorative": is_decorative,  # ADD THIS
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

# ---------- SEARCH ----------

def search(request):
    query = request.GET.get("q", "").strip()

    products = Product.objects.none()

    if query:
        # Find matching categories first
        matching_categories = Category.objects.filter(
            name__icontains=query
        )

        products = Product.objects.select_related(
            "category", "brand"
        ).filter(
            Q(name__icontains=query) |
            Q(code__icontains=query) |
            Q(brand__name__icontains=query) |
            Q(category__in=matching_categories)
        ).distinct()

    return render(request, "search_results.html", {
        "query": query,
        "products": products,
        "page_title": f"Search results for '{query}'" if query else "Search",
    })

# ---------- OTHER ----------

def kitchen_view(request):
    woods = Product.objects.all()
    return render(request, "kitchen_color.html", {"woods": woods})