from django.db import models


class CafeInfo(models.Model):
    """Single row of café details shown across the site (footer, contact, band).

    Editable from the admin so the owner can update address/hours/socials
    without touching any code.
    """

    name = models.CharField(max_length=80, default="Wow Weffles")
    tagline = models.CharField(max_length=160, default="Dulera · Café & Waffle Bar")
    address = models.CharField(max_length=200, default="Main Road, Dulera")
    address_note = models.CharField(
        max_length=200, blank=True,
        default="(add exact street address & landmark)",
    )
    phone = models.CharField(max_length=40, default="+91 00000 00000")
    email = models.EmailField(default="hello@wowweffles.cafe")
    hours = models.CharField(max_length=120, default="Mon–Sun · 9:00 AM – 11:00 PM")
    instagram = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    whatsapp = models.URLField(blank=True)
    map_embed = models.TextField(
        blank=True,
        help_text="Paste the Google Maps <iframe> embed code for your location.",
    )

    class Meta:
        verbose_name = "Café info"
        verbose_name_plural = "Café info"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.pk = 1  # enforce a single row
        super().save(*args, **kwargs)

    @classmethod
    def get(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj

    @property
    def phone_href(self):
        return "tel:" + self.phone.replace(" ", "")


class Category(models.Model):
    """A menu section, e.g. Tea & Chai, Coffee, Waffles."""

    name = models.CharField(max_length=80)
    slug = models.SlugField(
        unique=True,
        help_text="Used for the on-page anchor/URL, e.g. 'tea'.",
    )
    icon = models.CharField(
        max_length=8, blank=True,
        help_text="Emoji shown beside the heading, e.g. 🍵",
    )
    tagline = models.CharField(
        max_length=120, blank=True,
        help_text="Small note by the heading, e.g. 'Brewed to order'.",
    )
    order = models.PositiveIntegerField(default=0, help_text="Lower numbers show first.")

    class Meta:
        ordering = ["order", "name"]
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

    @property
    def available_items(self):
        return self.items.filter(is_available=True)


class MenuItem(models.Model):
    """A single dish or drink."""

    category = models.ForeignKey(
        Category, related_name="items", on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=120)
    description = models.CharField(max_length=200, blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    is_veg = models.BooleanField(default=False, verbose_name="Vegetarian")
    is_featured = models.BooleanField(
        default=False,
        help_text="Show in 'crowd favourites' on the home page.",
    )
    is_available = models.BooleanField(
        default=True,
        help_text="Uncheck to hide the item (e.g. sold out).",
    )
    order = models.PositiveIntegerField(default=0, help_text="Lower numbers show first.")

    class Meta:
        ordering = ["order", "name"]

    def __str__(self):
        return f"{self.name} (₹{self.price_display})"

    @property
    def price_display(self):
        """'60.00' -> '60', '60.50' -> '60.50' for clean menu prices."""
        if self.price == self.price.to_integral_value():
            return f"{self.price:.0f}"
        return f"{self.price:.2f}"


class ContactMessage(models.Model):
    """A message submitted through the contact form."""

    name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=40, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    handled = models.BooleanField(
        default=False, help_text="Tick once you've responded.",
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name}, {self.created_at:%d %b %Y}"
