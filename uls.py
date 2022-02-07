from django.contrib import admin
from django.urls import path
from app.views import home, form

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('form/', form),
]

from app.views import home, form, create, view

urlpatterns = [
    path('create/', create, name='create'),
    path('view//', view, name='view'),
]
