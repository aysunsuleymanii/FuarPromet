# fuar_promet/context_processors.py
from .models import Category


def navbar_categories(request):
    """
    Context processor to make categories available in all templates
    for the navbar mega menu
    """
    # Define decorative category names - MUST MATCH EXACTLY with database
    decorative_names = [
        'PVC Duvar Paneli',
        'BAMBOO PANEL',
        'PVC UV',
    ]

    # Get regular product categories (exclude decorative ones)
    product_categories = Category.objects.exclude(
        name__in=decorative_names
    ).order_by('name')

    # Get decorative categories (only these specific ones)
    decorative_categories = Category.objects.filter(
        name__in=decorative_names
    ).order_by('name')

    return {
        'product_categories': product_categories,
        'decorative_categories': decorative_categories,
    }