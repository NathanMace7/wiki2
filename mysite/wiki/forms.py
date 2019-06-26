from django.forms import ModelForm
from .models import UserFileUpload
    
#Uploads your files
class UploadFileForm(ModelForm):
    class Meta:
        model = UserFileUpload
        fields = ['upload' ]