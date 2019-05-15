from django.forms import ModelForm
from .models import UserFileUpload
    
class UploadFileForm(ModelForm):
    class Meta:
        model = UserFileUpload
        fields = ['upload' ]