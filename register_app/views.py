from django.http import HttpResponse
from django.shortcuts import render

from .models import Person


# Create your views here.
def main(request):
    if request.POST:
        model = Person()
        model.first_name = request.POST.get('first_name','')
        model.last_name = request.POST.get('last_name','')
        model.company = request.POST.get('company', '')
        model.email = request.POST.get('email', '')
        model.phone = request.POST.get('area_code', '') + request.POST.get('phone', '')
        model.course_type = request.POST.get('course_type', '')
        model.subject = request.POST.get('subject', '')
        model.exist = request.POST.get('exist', '')
        model.save()
        print(request.POST)
    return render(request,'index.html')

def get_info(request):
    queryset = Person.objects.all().values('first_name','last_name','company','email','phone')
    persons_list = ""
    for q in queryset:
        persons_list += f"<li>{q}</li>"
    return HttpResponse(f"<ul>{persons_list}</ul>")
