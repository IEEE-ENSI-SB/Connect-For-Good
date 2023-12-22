from django.forms import ModelForm
from .models import *


class InvitationForm(ModelForm):
    class Meta:
        model = Invitation 
        fields = ['body']
