from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
]

urlpatterns +=[
    path('catalog/', include('catalog.urls')),
]

# Adding URL maps to redirect the base URL to the application
from django.views.generic import RedirectView

urlpatterns +=[
    path('', RedirectView.as_view(url='catalog/', permanent=True)),
]

# Use static () to add URL mapping to serve static files during development (only)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
