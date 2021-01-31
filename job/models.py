from django.db import models

# Create your models here.
worktime=(
    ('Full time','Full time'),
    ('Part time','Part time'),
)
class Job(models.Model):
    title=models.CharField(max_length=50)
    job_type=models.CharField(max_length=10,choices=worktime)
    description=models.TextField(max_length=500)
    date=models.DateTimeField(auto_now=True)
    Vacancy=models.IntegerField(default=1)
    salary=models.IntegerField(default=0)
    experience=models.IntegerField(max_length=2)



    def __str__(self):
        return(self.title)
        