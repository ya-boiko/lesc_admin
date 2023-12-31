from django.urls import path

from . import views


methods = {
    "get": "list",
    "post": "create",
    "delete": "remove",
    "patch": "update",
}

urlpatterns = [
    path('api/places/', views.GetPlacesView.as_view({"get": "list", "post": "create"})),
    path('api/members/', views.GetMembersView.as_view({"get": "list", "post": "create"})),
    path('api/meetings/', views.GetMeetingsView.as_view({"get": "list", "post": "create"})),
    path('api/tickets/', views.GetTicketsView.as_view({"get": "list", "post": "create"})),
    path('api/bookings/', views.GetBookingsView.as_view(methods)),
]
