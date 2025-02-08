from django.db import models

# Create your models here.



# create table for accepting pdf files.
class Upload(models.Model):
    doc = models.FileField(upload_to='Docs/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.doc
    
