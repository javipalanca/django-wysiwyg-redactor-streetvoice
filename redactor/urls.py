
from django.urls import path

from redactor.views import RedactorUploadView
from redactor.forms import FileForm, ImageForm


urlpatterns = [
    path(r'^upload/image/(?P<upload_to>.*)',
        RedactorUploadView.as_view(form_class=ImageForm),
        name='redactor_upload_image'),

    path(r'^upload/file/(?P<upload_to>.*)',
        RedactorUploadView.as_view(form_class=FileForm),
        name='redactor_upload_file'),
]
