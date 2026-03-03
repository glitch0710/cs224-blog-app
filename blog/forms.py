from django.forms import ModelForm, TextInput, Select

from .models import Song

class SongForm(ModelForm):
    class Meta:
        model = Song
        fields = '__all__'

        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'album': Select(attrs={'class': 'form-select'}),
        }