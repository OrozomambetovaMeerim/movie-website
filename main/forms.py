from django import forms
from .models import Movie, Message
# from snowpenguin.django.recaptcha3.fields import ReCaptchaField

# from .models import Reviews, Rating, RatingStar


# class ReviewForm(forms.ModelForm):
#     """Форма отзывов"""
#     captcha = ReCaptchaField()

#     class Meta:
#         model = Reviews
#         fields = ("name", "email", "text", "captcha")
#         widgets = {
#             "name": forms.TextInput(attrs={"class": "form-control border"}),
#             "email": forms.EmailInput(attrs={"class": "form-control border"}),
#             "text": forms.Textarea(attrs={"class": "form-control border"})
#         }


# class RatingForm(forms.ModelForm):
#     """Форма добавления рейтинга"""
#     star = forms.ModelChoiceField(
#         queryset=RatingStar.objects.all(), widget=forms.RadioSelect(), empty_label=None
#     )

#     class Meta:
#         model = Rating
#         fields = ("star",)


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['img', 'description']


class SearchForm(forms.Form):
    query = forms.CharField()


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['message', 'email', 'author_name']
    

