from django import forms
from .models import Experian, Comment

class AddSheet(forms.ModelForm):
    class Meta:
        model = Experian
        fields = '__all__'
        widgets = {
            'title':forms.TextInput(attrs={'class': 'form-control'}),
            'ex_month':forms.TextInput(attrs={'class': 'form-control'}),
        }
class SendComment(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['where', 'ratting']

    def __init__(seft, *args, **kwargs):
        super(SendComment, seft).__init__(*args, **kwargs)
        seft.fields['comment'].error_messages = {
            'required': 'Blank comment!'
        }

