from django.db import models

# Create your models here.
worktime=(
    ('Full time','Full time'),
    ('Part time','Part time'),
)
def image_upload(instance,filename):
    imagename ,extension =filename.split(".")
    return "jobs/%s/%s.%s"%(instance.id,instance.id,extension)
class Job(models.Model):
    title=models.CharField(max_length=50)
    job_type=models.CharField(max_length=10,choices=worktime)
    description=models.TextField(max_length=500)
    date=models.DateTimeField(auto_now=True)
    Vacancy=models.IntegerField(default=1)
    salary=models.IntegerField(default=0)
    experience=models.IntegerField()
    category=models.ForeignKey('Category',on_delete=models.CASCADE)
    image =models.ImageField(upload_to =image_upload)



    def __str__(self):
        return(self.title)



class Category(models.Model):
    name=models.CharField(max_length=25)

    def __str__(self):
        return self.name