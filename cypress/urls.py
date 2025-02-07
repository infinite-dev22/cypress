"""cypress URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.urls import path, include

from . import settings

urlpatterns = [
                  # path('admin/', admin.site.urls),
                  path('', include('dashboard.urls')),
                  path("admin/", include("admin_panel.urls")),
                  path("access/", include("accounts.urls")),
                  path("echelon/", include("echelon.urls")),
                  path("subject/", include("subject.urls")),
                  path("users/", include("users.urls")),
                  path("assessment/", include("assessment.urls")),
                  path("timetable/", include("timetable.urls")),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
    # + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
