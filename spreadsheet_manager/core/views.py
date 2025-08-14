from django.shortcuts import render, redirect
from .forms import UploadFileForm
import pandas as pd

def home(request):
    preview_html = None
    
    if request.method == 'POST':
        form=UploadFileForm(request.POST, request.FILES)
        
        if form.is_valid():
            uploaded_file=form.save()
            
            file_path=uploaded_file.file.path
            
            try:
                if file_path.endswith('.csv'):
                    df = pd.read_csv(file_path)
                else:
                    df=pd.read_excel(file_path)
                
                preview_html=df.head().to_html(classes='table table-striped', index=False)
            
            except Exception as e:
                preview_html=f"<p style='color:red;'>Could not preview file: {str(e)}</p>"
        
        return render(request,'core/home.html',{'form':form,'preview_html':preview_html})
    
    else:
        form = UploadFileForm()
        
    return render(request,'core/home.html',{'form':form})


