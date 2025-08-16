from django.shortcuts import render, redirect
from .forms import UploadFileForm
import pandas as pd
import os

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
                
                #Original Preview
                preview_html=df.head().to_html(classes='table table-striped', index=False)
                
                #File processing(Uppercase column names and dropping missing rows)
                df.columns=[col.upper() for col in df.columns]
                
                df.dropna(axis=0,how='any')
                
                #Processed preview
                processed_preview_html=df.head().to_html(classes='table table-striped', index=False)
                
                #Saving processed file
                processed_filename = f"processed_{os.path.basename(file_path).replace('.','_')}.xlsx"
                processed_path = os.path.join('media', 'processed_files', processed_filename)
                df.to_excel(processed_path, index=False)

                processed_file_url = f"/media/processed_files/{processed_filename}"
            
            except Exception as e:
                preview_html=f"<p style='color:red;'>Could not preview file: {str(e)}</p>"
            
            form=UploadFileForm()
            
        return render(request,'core/home.html',{'form':form,'preview_html':preview_html,'processed_preview_html': processed_preview_html,
        'processed_file_url': processed_file_url,})
    
    else:
        form = UploadFileForm()
        
    return render(request,'core/home.html',{'form':form})


