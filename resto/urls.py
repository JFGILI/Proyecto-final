
from django.contrib import admin
from django.urls import path, include

from django.conf import  settings
from django.conf.urls.static import static


from resto.views import index

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),

    
    path ('products/', include ('products.urls')),
] + static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
