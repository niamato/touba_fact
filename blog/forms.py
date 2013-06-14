#-*-coding:utf-8-*
from django import forms
from models import Article

class ContactForm(forms.Form):
    sujet = forms.CharField(max_length=100, label="Sujet:", required=True)
    message = forms.CharField(widget=forms.Textarea, label="Message:", required=True)
    envoyeur = forms.EmailField(label="Votre adresse mail:", required=True)
    renvoi = forms.BooleanField(help_text="Cochez si vous souhaitez obtenir une copie du mail envoyé.", required=False)


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article

class LoginForm(forms.Form):
    username = forms.CharField(max_length=35, label='Username: ')
    password = forms.CharField(label='Password: ', widget=forms.PasswordInput)