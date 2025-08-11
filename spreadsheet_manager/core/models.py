from django.db import models

class UploadedFile(models.Model):
    file = models.FileField(upload_to='spreadsheets/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Spreadsheet {self.id} uploaded at {self.uploaded_at}"
