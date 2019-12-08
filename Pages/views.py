from django.shortcuts import render
def Documentation(request):
    return render(request,'Pages/Documentation.html')
def Single(request):
    return render(request,'Pages/Single.html')
def Complete(request):
    return render(request,'Pages/Complete.html')
def Future(request):
    return render(request,'Pages/Future.html')