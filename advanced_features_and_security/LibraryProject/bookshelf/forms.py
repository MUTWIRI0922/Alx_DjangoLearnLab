from django import forms


class ExampleForm(forms.Form):
    """
    Example form used to demonstrate secure form handling.
    CSRF protection is enforced in templates using {% csrf_token %}.
    """
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
