from django.urls import path
from django.views.generic import TemplateView

app_name = 'pages'

handler404 = 'pages.views.page_not_found'
handler500 = 'pages.views.server_error'

urlpatterns = [
    path(
        'about/',
        TemplateView.as_view(template_name='pages/about.html'),
        name='about'),
    path(
        'rules/',
        TemplateView.as_view(template_name='pages/rules.html'),
        name='rules'),
]
