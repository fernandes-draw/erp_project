from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("users.urls")),
    path("", include("core.urls")),
    path("materials/", include("materials.urls")),
    path("suppliers/", include("suppliers.urls")),
    path("customers/", include("customers.urls")),
]
