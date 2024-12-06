# controle_ac/urls.py
from django.contrib import admin
from django.urls import include, path
from django.http import HttpResponseRedirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('controle/', include('esp_control.urls')),
    path('', lambda request: HttpResponseRedirect('/controle/')),  # Redireciona para /controle/
]
