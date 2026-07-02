from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.http import Http404
from django.shortcuts import redirect, render

from .forms import ContactForm
from .models import Category, MenuItem


def home(request):
    featured = MenuItem.objects.filter(is_featured=True, is_available=True)[:5]
    return render(request, "cafe/home.html", {"featured_items": featured})


def menu(request):
    categories = Category.objects.prefetch_related("items")
    return render(request, "cafe/menu.html", {"categories": categories})


def about(request):
    return render(request, "cafe/about.html")


def gallery(request):
    return render(request, "cafe/gallery.html")


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            msg = form.save()
            send_mail(
                subject=f"New website message from {msg.name}",
                message=(
                    f"From: {msg.name} <{msg.email}>\n"
                    f"Phone: {msg.phone or 'not provided'}\n\n"
                    f"{msg.message}"
                ),
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.CONTACT_NOTIFY_EMAIL],
                fail_silently=True,
            )
            messages.success(
                request,
                "Thanks! Your message has been sent. We’ll get back to you soon.",
            )
            return redirect("contact")
    else:
        form = ContactForm()
    return render(request, "cafe/contact.html", {"form": form})


def print_menu(request):
    """Standalone printable bifold menu. Categories are split across the two
    inside panels."""
    cats = list(Category.objects.prefetch_related("items"))
    mid = (len(cats) + 1) // 2
    return render(
        request,
        "cafe/print_menu.html",
        {"left_categories": cats[:mid], "right_categories": cats[mid:]},
    )


# ---------------------------------------------------------------------------
# Design variants: alternative site looks (same palette, different style).
# Each variant has a full set of pages sharing one base template per variant.
# ---------------------------------------------------------------------------

VARIANT_HOME_TEMPLATES = {
    "editorial": "variants/v1_editorial.html",
    "playful": "variants/v2_playful.html",
    "premium": "variants/v3_premium.html",
    "book": "variants/v4_book.html",
}
VARIANT_BASES = {
    "editorial": "variants/bases/editorial.html",
    "playful": "variants/bases/playful.html",
    "premium": "variants/bases/premium.html",
    "book": "variants/bases/book.html",
}


def _variant_context():
    return {
        "featured_items": MenuItem.objects.filter(is_featured=True, is_available=True)[:6],
        "categories": Category.objects.prefetch_related("items"),
    }


def _base_or_404(variant):
    base = VARIANT_BASES.get(variant)
    if base is None:
        raise Http404("Unknown design variant.")
    return base


def variants_index(request):
    return render(request, "variants/index.html")


def variant_home(request, variant):
    template = VARIANT_HOME_TEMPLATES.get(variant)
    if template is None:
        raise Http404("Unknown design variant.")
    ctx = _variant_context()
    ctx.update(base_template=VARIANT_BASES[variant], variant=variant)
    return render(request, template, ctx)


def variant_menu(request, variant):
    base = _base_or_404(variant)
    template = "variants/pages/menu_book.html" if variant == "book" else "variants/pages/menu.html"
    return render(request, template, {
        "base_template": base, "variant": variant,
        "categories": Category.objects.prefetch_related("items"),
    })


def variant_about(request, variant):
    base = _base_or_404(variant)
    return render(request, "variants/pages/about.html", {"base_template": base, "variant": variant})


def variant_gallery(request, variant):
    base = _base_or_404(variant)
    return render(request, "variants/pages/gallery.html", {"base_template": base, "variant": variant})


def variant_contact(request, variant):
    base = _base_or_404(variant)
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            msg = form.save()
            send_mail(
                subject=f"New website message from {msg.name}",
                message=(
                    f"From: {msg.name} <{msg.email}>\n"
                    f"Phone: {msg.phone or 'not provided'}\n\n{msg.message}"
                ),
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.CONTACT_NOTIFY_EMAIL],
                fail_silently=True,
            )
            messages.success(request, "Thanks! Your message has been sent. We’ll get back to you soon.")
            return redirect("variant_contact", variant=variant)
    else:
        form = ContactForm()
    return render(request, "variants/pages/contact.html", {
        "base_template": base, "variant": variant, "form": form,
    })
