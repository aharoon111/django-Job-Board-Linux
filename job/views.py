from django.shortcuts import render
from .models import Job
from django.core.paginator import Paginator
from .forms import Appliedfrom
# Create your views here.


def job_list(request):
    job_list = Job.objects.all()    
    paginator = Paginator(job_list, 1) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)    
    context = {'jobs':page_obj}
    return render(request,'jobs/job_list.html',context)
    





def job_details(request , slug):
    job_details = Job.objects.get(slug=slug)    
    if request.method == 'POST':
        form = Appliedfrom(request.POST , request.FILES)
        print("test")
        if form.is_valid:
            form.save()
    else:
        form = Appliedfrom()
    
    
    context = {'job':job_details , 'form':form}
    return render(request, 'jobs/job_details.html', context)



