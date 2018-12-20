from django.contrib import admin
from django.urls import re_path, path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('project/', include('project.urls', namespace='project')),
    re_path(r'^froala_editor/', include('froala_editor.urls')),
    path('', include)
]


from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)