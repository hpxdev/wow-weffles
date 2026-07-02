from .models import CafeInfo, Category


def site(request):
    """Make café details and menu categories available to every template
    (used by the shared header, footer and 'visit us' band)."""
    try:
        cafe = CafeInfo.get()
        categories = list(Category.objects.all())
    except Exception:
        # Database not ready yet (e.g. before the first migrate).
        cafe = None
        categories = []
    return {"cafe": cafe, "nav_categories": categories}
