from django.db import models
from django.urls import reverse


#This is the Page model.
class Page(models.Model):
    title = models.CharField(max_length=64, primary_key=True)
    content = models.TextField()
    counter = models.IntegerField(default=0)
    
    #Navigates URL with name page
    def __str__(self):
        return self.title

    #Detail Page for the title
    def get_absolute_url(self):
        return reverse('wiki:detail', args=[self.title])

#This is where the user uploads their files. 
class UserFileUpload(models.Model):
    upload = models.FileField(upload_to='uploads/')
    #file will be saved to MEDIA_ROOT/uploads
    
    #Sets upload name to the name of the file that has been uploaded
    def __str__(self):
        return self.upload.name

    #This section deletes the files uploaded
    def delete(self, *args, **kwargs):
        path = os.path.join(settings.MEDIA_ROOT, self.upload.name)
        if os.path.exists(path):
            os.remove(path)
        super().delete(*args, **kwargs)