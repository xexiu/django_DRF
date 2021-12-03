from django.urls import path
from django.views.generic import TemplateView

app_name = 'darvel'

urlpatterns = [
    path('', TemplateView.as_view(template_name="darvel/index.html"))
]