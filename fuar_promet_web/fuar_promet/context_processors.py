from .models import Category


def navbar_categories(request):
    """
    Provides navbar categories based on category hierarchy.
    Products and Decorative Products are main categories.
    """

    products_main = Category.objects.filter(
        parent__isnull=True,
        name="Products"
    ).first()

    decorative_main = Category.objects.filter(
        parent__isnull=True,
        name="Decorative Products"
    ).first()

    return {
        "product_categories": products_main.subcategories.all() if products_main else [],
        "decorative_categories": decorative_main.subcategories.all() if decorative_main else [],
    }
