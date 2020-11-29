from django.urls import path

from app.core.erp.views import myFirstView
from app.core.erp.views import mySecondView

app_name = 'erp'

urlpatterns = [
    path('uno/', myFirstView, name='vista1'),
    path('dos/', mySecondView, name='vista2')
]
