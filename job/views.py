from django.shortcuts import render
# Create your views here.
from .models import Job


from django.core.paginator import Paginator

def job_list(request):
    job_list=Job.objects.all()


    paginator = Paginator(job_list,2) # Show 2 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    contaxt={'jobs':page_obj}
    return render(request,'job/job_list.html',contaxt)




def job_detail(request, id ):
    job_detail=Job.objects.get(id=id)
    contaxt={'job':job_detail}
    return render(request,'job/job_detail.html',contaxt)
