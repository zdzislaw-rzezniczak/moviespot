from django import forms

MOVIE_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddMovieForm(forms.Form):
    quantity = forms.TypedChoiceField(
                                choices=MOVIE_QUANTITY_CHOICES,
                                coerce=int)
    override = forms.BooleanField(required=False,
                                  initial=False,
                                  widget=forms.HiddenInput)
