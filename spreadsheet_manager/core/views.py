from django.shortcuts import render, redirect
from .forms import UploadFileForm

def home(request):
    
    if request.method == 'POST':
        form=UploadFileForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            return redirect('home')
    
    else:
        form = UploadFileForm()
        
    return render(request,'core/home.html',{'form':form})


