from django import forms

from .models import ContactMessage


class ContactForm(forms.ModelForm):
    """Contact form backed by the ContactMessage model."""

    class Meta:
        model = ContactMessage
        fields = ["name", "email", "phone", "message"]
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Your name"}),
            "email": forms.EmailInput(attrs={"placeholder": "you@email.com"}),
            "phone": forms.TextInput(attrs={"placeholder": "+91 …"}),
            "message": forms.Textarea(attrs={"placeholder": "How can we help?", "rows": 5}),
        }
