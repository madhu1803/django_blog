from django.urls import path
from . import views
from crudblog.settings import DEBUG, STATIC_URL, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static
from .views import Index,Details,Create,Delete,Update
urlpatterns = [
    path("", views.Index.as_view(), name="index"),
    path("upload/", Create.as_view(), name="upload-post"),
    path('update/<slug:slug>/', Update.as_view(),name="update-post"),
    path("<slug:slug>/", views.Details.as_view(), name="detail-post"),
    path('delete/<slug:slug>/', Delete.as_view(),name="delete-post"),
]
# DataFlair
if DEBUG:
    urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
