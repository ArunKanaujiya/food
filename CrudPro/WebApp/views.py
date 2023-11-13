from django.shortcuts import render,get_list_or_404,get_object_or_404
from django.http import HttpResponseRedirect
from WebApp.models import Company
from WebApp.forms import CompanyForm

# Create your views here.
def Home(request):
    orglist=Company.objects.all()
    return render(request,'myapp/home.html',{'orglist':orglist})

def org_create(request):
    form=CompanyForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        instance=form.save()
        instance.save()
        return HttpResponseRedirect('/')
    context={'form':form}
    return render(request,'myapp/create.html',context)

def org_update(request,id=None):
	instance = get_object_or_404(Company,id=id)
	form = CompanyForm(request.POST or None,request.FILES or None ,instance=instance)
	if form.is_valid():
		instance = form.save()
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())
	context ={'instance':instance,'form':form}
	return  render(request,"myapp/update.html" , context)

def org_delete(request,id=None):
	instance =get_object_or_404(Company,id=id)
	instance.delete()
	return render(request,"myapp/delete.html")

def org_retrive(request,id=None):
    instance=get_object_or_404(Company,id=id)
    context={'instance':instance}
    return render(request,'myapp/retrive.html',context)