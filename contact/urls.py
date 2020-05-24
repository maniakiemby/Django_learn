from django.urls import path

from .views import (
    ContactView,
    ContactListView,
    MyListView,
    ContactCreateView,
    ContactUpdateView,
    ContactDeleteView
)

app_name = 'contact'
urlpatterns = [
    path('', ContactListView.as_view(), name='contact-list'),
    path('my/', MyListView.as_view(), name='my-list'),
    path('<int:id>/', ContactView.as_view(), name='contact-detail'),
    path('create/', ContactCreateView.as_view(), name='contact-create'),
    path('<int:id>/update/', ContactUpdateView.as_view(), name='contact-update'),
    path('<int:id>/delete/', ContactDeleteView.as_view(), name='contact-delete')
]