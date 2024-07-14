from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from app.views import CustomLoginView  

urlpatterns = [
    path('', include('app.urls')),
    path('accounts/login/', CustomLoginView.as_view(), name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
