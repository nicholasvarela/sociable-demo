from django.forms import ModelForm
from .models import Handle

class handleSearchForm(ModelForm):
    class Meta:
        model = Handle 
        fields = "__all__"