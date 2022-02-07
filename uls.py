from app.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
]
