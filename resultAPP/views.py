from django.shortcuts import render

from resultAPP.forms import std_form

from resultAPP.models import student

def studentRESULT(request):
    result=None
    error=None
    if request.method=="POST":
        form=std_form(request.POST)
        if form.is_valid():
            hall=form.cleaned_data['hall_ticket']
            try:
                result=student.objects.get(hall_ticket=hall)
            except student.DoesNotExist:
                error="no student found"
    else:form=std_form()
    return render(request,'result.html',{'result':result,'error':error,'form':form})

