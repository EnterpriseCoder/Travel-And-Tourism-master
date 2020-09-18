from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView
from django.http import HttpResponse
from . import models
from myapp.forms import NewUserForm


class IndexView(TemplateView):
    template_name = 'index.html'
class IndexView1(TemplateView):
    template_name = 'index1.html'
class IndexView2(TemplateView):
    template_name = 'index11.html'

class IView(TemplateView):
    template_name = 'auto.html'

class PackageListView(ListView):
    template_name = 'index.html'
    model = models.Package

class PackageDetailView(DetailView):
    context_object_name = 'package_detail'
    model = models.Package
    template_name = 'myapp/package_detail.html'

def index(request):
    return render(request,'index.html')

def index2(request):
    return render(request,'index2.html')

def index12(request):
    return render(request,'index12.html')
    

def users(request):
    form = NewUserForm()

    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('Error Form Invalid!')

    return render(request,'users.html',{'form':form})
