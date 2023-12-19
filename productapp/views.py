from django.shortcuts import render
from django.views import View
from .models import Product
from django.http import HttpResponse
# Create your views here.
class Home(View):
    def get(self,request):
        return render(request,'home.html')
class InsertInput(View):
    def get(self,request):
        return render(request,'insertinput.html')
class Insert(View):
    def get(self,request):
        p_id=int(request.GET["t1"])
        p_name = request.GET["t2"]
        p_cost = float(request.GET["t3"])
        p_mfdt = request.GET["t4"]
        p_expdt = request.GET["t5"]
        p1=Product(pid=p_id,pname=p_name,pcost=p_cost,pmfdt=p_mfdt,pexpdt=p_expdt)
        p1.save()
        return HttpResponse("Product Inserted Successfully")
class Display(View):
    def get(self,request):
        qs=Product.objects.all()
        con_dict={'records':qs}
        return render(request,'display.html',context=con_dict)
class UpdateInput(View):
    def get(self,request):
        qs = Product.objects.all()
        con_dict = {'records': qs}
        return render(request, 'updateinput.html', context=con_dict)
class Update(View):
    def get(self,request):
        p1=Product.objects.get(pid=int(request.GET["t1"]))
        p1.name=request.GET["t2"]
        p1.cost=float(request.GET["t3"])
        p1.pmfdt=request.GET["t4"]
        p1.expdt=request.GET["t5"]
        p1.save()
        return HttpResponse("Product Updated Successfully")
class DeleteInput(View):
    def get(self,request):
        qs = Product.objects.all()
        con_dict = {'records': qs}
        return render(request, 'deleteinput.html', context=con_dict)
class Delete(View):
    def get(self,request):
        p1=Product.objects.get(pid=int(request.GET["t1"]))
        p1.delete()
        return HttpResponse("Product Deleted Successfully")