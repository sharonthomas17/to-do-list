from django.contrib import admin
from django.urls import path
from sample import views



urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('',include('sample.urls'))
   # path('',views.dis),
    path('',views.fetch),
    path('view/',views.view),
    path('delete/<pk>',views.delete),
]
    