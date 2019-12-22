from django.shortcuts import render
from django.shortcuts import redirect
from .models import Dept

def Documentation(request):
    return render(request,'Pages/Documentation.html')

def Single(request):
    x=Dept.objects.get(Uid=9)
    print(x)
    if request.method== "POST" :
        No=request.POST.get('Dept_id')
        return redirect('/Dept/UID='+No)
    return render(request,'Pages/Single.html')

def Complete(request):
    return render(request,'Pages/Complete.html')

def Unknown(request):
    return render(request,'Pages/Unknown.html')
    
def Department(request,UID):
    x=Dept.objects.get(Uid=UID)
    params={'Pro':x}
    return render(request,'Pages/Department.html',params)