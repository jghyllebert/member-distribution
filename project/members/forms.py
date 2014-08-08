from django import forms
from .models import Member


class MemberForm(forms.ModelForm):

    class Meta:
        model = Member
        exclude = ('personal_shopper', 'ordered_recently')