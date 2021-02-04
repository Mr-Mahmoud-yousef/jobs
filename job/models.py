from django.db import models
from django.utils.text import slugify
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
    slug=models.SlugField(null=True,blank=True)

    def save(self,*args, **kwargs):
        self.slug=slugify(self.title)
        super(Job,self).save(*args, **kwargs)


    def __str__(self):
        return(self.title)



class Category(models.Model):
    name=models.CharField(max_length=25)

    def __str__(self):
        return self.name


sex=(('Male','Male'),
     ('Female','Female') ,
)
class Apply(models.Model):
    job=models.ForeignKey(Job,related_name='apply_job',on_delete=models.CASCADE)
    name=models.CharField(max_length=25)
    gendar=models.CharField(max_length=10,choices=sex)
    email=models.EmailField()
    website=models.URLField()
    CV=models.FileField(upload_to='Applyer/')
    info=models.TextField(max_length=400)
    create_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
