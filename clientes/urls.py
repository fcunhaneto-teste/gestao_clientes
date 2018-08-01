from django.urls import path
from . import views


urlpatterns = [
    path('list/', views.persons_list, name="person_list"),
    path('new/', views.persons_new, name="person_new"),
    path('update/<int:id>/', views.persons_update, name="persons_update"),
    path('delete/<int:id>/', views.persons_delete, name="persons_delete"),
    path('person_list/', views.PersonList.as_view(), name="persons_list_cbv"),
    path('person_detail/<int:pk>/', views.PersonDetail.as_view(), name="persons_detail_cbv"),
    path('person_new/', views.PersonCreate.as_view(), name="persons_new_cbv"),
    path('person_update/<int:pk>/', views.PersonUpdate.as_view(), name="persons_update_cbv"),
    path('person_delete/<int:pk>/', views.PersonDelete.as_view(), name="persons_delete_cbv"),
]