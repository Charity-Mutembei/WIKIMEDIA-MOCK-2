from django.urls import path
#now import the views.py file into this code
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[    
  path('',views.welcome)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)