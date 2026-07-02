from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("menu/", views.menu, name="menu"),
    path("menu/accordion/", views.menu_accordion, name="menu_accordion"),
    path("logo-selection/", views.logo_selection, name="logo_selection"),
    path("about/", views.about, name="about"),
    path("gallery/", views.gallery, name="gallery"),
    path("contact/", views.contact, name="contact"),
    path("menu/print/", views.print_menu, name="print_menu"),

    # Design variants (each has a full set of pages)
    path("variants/", views.variants_index, name="variants_index"),
    path("variants/<slug:variant>/", views.variant_home, name="variant_home"),
    path("variants/<slug:variant>/menu/", views.variant_menu, name="variant_menu"),
    path("variants/<slug:variant>/about/", views.variant_about, name="variant_about"),
    path("variants/<slug:variant>/gallery/", views.variant_gallery, name="variant_gallery"),
    path("variants/<slug:variant>/contact/", views.variant_contact, name="variant_contact"),
]
