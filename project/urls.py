
from django.contrib import admin
from django.urls import path
from tickets import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('django/jsonresponsenomodel/',views.no_rest_no_model),
    path('django/jsonresponsefrommodel/',views.no_rest_from_model),
    path('rest/fbvlist/',views.fbv_list),
    path('rest/fbvlist/<int:pk>',views.fbv_pk),
    path('rest/CBV_LIST/',views.CBV_LIST.as_view()),
]
