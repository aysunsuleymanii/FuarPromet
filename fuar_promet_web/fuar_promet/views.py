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
    """View for products page with filtering"""
    # Get all categories for the filter sidebar
    categories = Category.objects.all().order_by('name')

    # Get all products
    products = Product.objects.all()

    # Get filter parameters from URL
    category_param = request.GET.get('category')
    brand_param = request.GET.get('brand')
    surface_param = request.GET.get('surface')
    stock_param = request.GET.get('stock')

    # Apply category filter
    if category_param:
        try:
            # Filter by category ID
            if category_param.isdigit():
                products = products.filter(category_id=category_param)
            else:
                # Filter by category name (case insensitive)
                products = products.filter(category__name__iexact=category_param)
        except:
            pass

    # Apply brand filter
    if brand_param:
        products = products.filter(brand=brand_param)

    # Apply surface filter
    if surface_param:
        products = products.filter(surface=surface_param)

    # Apply stock filter
    if stock_param:
        if stock_param == 'in-stock':
            products = products.filter(stock__gt=0)
        elif stock_param == 'out-of-stock':
            products = products.filter(stock=0)

    # Order products by creation date (newest first)
    products = products.order_by('-created_at')

    context = {
        'products': products,
        'categories': categories,
    }

    return render(request, 'products.html', context)


def services(request):
    services = Service.objects.all()
    return render(request, 'services.html', {'services': services})


def decorative_products(request):
    """View for decorative products page with filtering"""
    # Use the EXACT category names from your database
    decorative_category_names = [
        'PVC Duvar Paneli',
        'BAMBOO PANEL',
        'PVC UV',
    ]

    decorative_categories = Category.objects.filter(
        name__in=decorative_category_names
    ).order_by('name')

    # Get products from decorative categories
    products = Product.objects.filter(category__in=decorative_categories)

    # Get filter parameters
    category_param = request.GET.get('category')
    brand_param = request.GET.get('brand')
    surface_param = request.GET.get('surface')
    stock_param = request.GET.get('stock')

    # Apply category filter
    if category_param:
        try:
            if category_param.isdigit():
                products = products.filter(category_id=category_param)
            else:
                products = products.filter(category__name__iexact=category_param)
        except:
            pass

    # Apply brand filter
    if brand_param:
        products = products.filter(brand=brand_param)

    # Apply surface filter
    if surface_param:
        products = products.filter(surface=surface_param)

    # Apply stock filter
    if stock_param:
        if stock_param == 'in-stock':
            products = products.filter(stock__gt=0)
        elif stock_param == 'out-of-stock':
            products = products.filter(stock=0)

    products = products.order_by('-created_at')

    context = {
        'products': products,
        'categories': decorative_categories,
    }

    return render(request, 'decorative_products.html', context)


# Class-based views (keep these for backward compatibility if needed)
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

    def get_queryset(self):
        """Override to add filtering"""
        queryset = super().get_queryset()

        # Get filter parameters
        category_param = self.request.GET.get('category')
        brand_param = self.request.GET.get('brand')
        surface_param = self.request.GET.get('surface')
        stock_param = self.request.GET.get('stock')

        # Apply filters
        if category_param:
            if category_param.isdigit():
                queryset = queryset.filter(category_id=category_param)
            else:
                queryset = queryset.filter(category__name__iexact=category_param)

        if brand_param:
            queryset = queryset.filter(brand=brand_param)

        if surface_param:
            queryset = queryset.filter(surface=surface_param)

        if stock_param:
            if stock_param == 'in-stock':
                queryset = queryset.filter(stock__gt=0)
            elif stock_param == 'out-of-stock':
                queryset = queryset.filter(stock=0)

        return queryset.order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'


def kitchen_view(request):
    """Kitchen color selection view"""
    wood_options = Product.objects.all()
    context = {'woods': wood_options}
    return render(request, 'kitchen_color.html', context)

