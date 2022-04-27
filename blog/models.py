from django.db import models

class BaseModel(models.Model):
    creation_date = models.DateField(auto_now_add=True)
    updation_date = models.DateField(auto_now=True)
    class Meta:
        abstract =True


class Blog(BaseModel):
    title = models.CharField(max_length=100)
    details = models.TextField(max_length=1000)

    def __str__(self):
        return self.title
