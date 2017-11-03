import django
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from market.models import UserProfile, Translations, MarketStand

class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=20, required=True)
    last_name = forms.CharField(max_length=20, required=True)
    identity = forms.CharField(widget=forms.RadioSelect, required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'first_name', 'last_name')

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        if commit:
            user.save()

        user_profile = UserProfile(user=user)
        user_profile.save()
        return user


class TransForm(forms.ModelForm):
    buyer_tmp = forms.CharField(max_length=20, required=True)
    marketStand_tmp = forms.IntegerField(required=True)

    class Meta:
        model = Translations
        fields = ('charge', 'add_bonus', 'used_bonus', 'desc')

    def save(self, commit=True, *args, **kargs):
        trans = super(TransForm, self).save(commit=False, *args, **kargs)
        try:
            username = User.objects.get(username=self.cleaned_data['buyer_tmp'])
        except Exception as e:
            raise forms.ValidationError("無此買家!")

        marketStand = MarketStand.objects.get(id=self.cleaned_data['marketStand_tmp'])
        trans.buyer = username.profile
        trans.marketStand = marketStand
        if commit:
            trans.save()

        add_bonus = trans.add_bonus
        used_bonus = trans.used_bonus
        now_bonus = username.profile.bonus
        username.profile.bonus = now_bonus + add_bonus - used_bonus
        username.profile.save()
        return trans


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']


