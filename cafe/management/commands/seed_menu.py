"""Populate the database with the starter café info + placeholder menu.

Idempotent: run it as many times as you like. It updates existing rows
rather than creating duplicates.

    python manage.py seed_menu
"""

from django.core.management.base import BaseCommand

from cafe.models import CafeInfo, Category, MenuItem

CATEGORIES = [
    ("tea", "Tea & Chai", "🍵", "Brewed to order"),
    ("coffee", "Coffee", "☕", "Freshly roasted beans"),
    ("juice", "Juice & Health", "🥤", "Cold-pressed daily"),
    ("shakes", "Shakes & Cold", "🥛", "Thick & chilled"),
    ("waffles", "Waffles", "🧇", "Our namesake"),
    ("bites", "Savoury Bites", "🥪", "To go with your cup"),
]

# category_slug: [ (name, description, price, is_veg, is_featured), ... ]
ITEMS = {
    "tea": [
        ("Kulhad Masala Chai", "Fresh ginger, cardamom, in a clay cup", 60, True, True),
        ("Classic Cutting Chai", "Strong, milky, everyday favourite", 30, True, False),
        ("Elaichi Chai", "Cardamom-forward and aromatic", 50, True, False),
        ("Green Tea", "Light, clean, honey on request", 70, True, False),
        ("Lemon & Ginger Tea", "Zesty, warming, no milk", 70, True, False),
        ("Kesar Badam Chai", "Saffron, almond, a little luxe", 90, True, False),
    ],
    "coffee": [
        ("Espresso", "A quick, bold single shot", 90, True, False),
        ("Cappuccino", "Espresso, steamed milk, soft foam", 130, True, False),
        ("Café Latte", "Smooth, milky, easy-going", 140, True, False),
        ("Hazelnut Latte", "Double shot with a nutty finish", 150, True, True),
        ("Cold Brew", "Slow-steeped 16 hours, over ice", 160, True, False),
        ("Mocha", "Coffee meets chocolate", 170, True, False),
    ],
    "juice": [
        ("Cold-Pressed Orange", "Pure squeezed, nothing added", 120, True, True),
        ("Watermelon Cooler", "Fresh melon, mint, lime", 110, True, False),
        ("Green Detox Smoothie", "Spinach, apple, mint & lime", 160, True, True),
        ("Banana Peanut Smoothie", "Creamy, filling, protein-rich", 170, True, False),
        ("Fresh Fruit Bowl", "Seasonal fruit, honey drizzle", 150, True, False),
        ("ABC Juice", "Apple, beetroot, carrot", 140, True, False),
    ],
    "shakes": [
        ("Cold Coffee", "Classic blended, extra frothy", 150, True, False),
        ("Oreo Shake", "Cookies & cream, crushed topping", 170, True, False),
        ("Chocolate Shake", "Rich cocoa, whipped cream", 170, True, False),
        ("Mango Shake", "Seasonal, thick & sweet", 160, True, False),
        ("Strawberry Shake", "Creamy with real fruit", 160, True, False),
        ("Iced Lemon Tea", "Refreshing and light", 90, True, False),
    ],
    "waffles": [
        ("Belgian Choco Waffle", "Crisp waffle, molten chocolate drizzle", 180, True, True),
        ("Maple & Butter", "Simple, warm, classic", 160, True, False),
        ("Nutella Banana", "Hazelnut spread, fresh banana", 200, True, False),
        ("Biscoff Crumble", "Speculoos sauce & crunch", 220, True, False),
        ("Savoury Cheese Waffle", "Herbed cheese, not sweet", 190, True, False),
        ("Ice-Cream Waffle", "Warm waffle, cold vanilla scoop", 210, True, False),
    ],
    "bites": [
        ("Grilled Veg Sandwich", "Loaded veggies, herbed butter", 130, True, False),
        ("Cheese Corn Toastie", "Melty, sweet-corn filling", 140, True, False),
        ("Peri Peri Fries", "Crisp, spicy, moreish", 120, True, False),
        ("Paneer Tikka Wrap", "Smoky paneer, mint mayo", 170, True, False),
        ("Garlic Bread", "Toasted, buttery, cheesy option", 110, True, False),
        ("Choco Lava Cake", "Warm, gooey centre", 120, True, False),
    ],
}


class Command(BaseCommand):
    help = "Seed café info and a placeholder menu (idempotent)."

    def handle(self, *args, **options):
        CafeInfo.get()  # ensure the singleton exists with defaults
        self.stdout.write("Cafe info ready.")

        for order, (slug, name, icon, tagline) in enumerate(CATEGORIES):
            category, _ = Category.objects.update_or_create(
                slug=slug,
                defaults={"name": name, "icon": icon, "tagline": tagline, "order": order},
            )
            for item_order, (iname, desc, price, is_veg, feat) in enumerate(ITEMS[slug]):
                MenuItem.objects.update_or_create(
                    category=category,
                    name=iname,
                    defaults={
                        "description": desc,
                        "price": price,
                        "is_veg": is_veg,
                        "is_featured": feat,
                        "is_available": True,
                        "order": item_order,
                    },
                )
            self.stdout.write(f"  {name}: {len(ITEMS[slug])} items")

        self.stdout.write(self.style.SUCCESS("Menu seeded successfully."))
