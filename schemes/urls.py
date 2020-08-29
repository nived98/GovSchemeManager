from django.urls import path
from schemes.views import(
    create_centre_scheme_list_view,
    create_state_scheme_list_view,
    edit_centre_scheme_view,
    edit_state_scheme_view,
    detail_centre_scheme_list_view,
    detail_state_scheme_list_view,
)

app_name = 'schemes'

urlpatterns = [
    path('state/create_state_listing/', create_state_scheme_list_view,
         name="create_state_listing"),
    path('centre/create_centre_listing/', create_centre_scheme_list_view,
         name="create_state_listing"),
    path('state/<slug>/', detail_state_scheme_list_view,
         name="detail_state_scheme_list_view"),
    path('centre/<slug>/', detail_centre_scheme_list_view,
         name="detail_centre_scheme_list_view"),
    path('state/<slug>/edit', edit_state_scheme_view,
         name="edit_state_scheme_view"),
    path('centre/<slug>/edit', edit_centre_scheme_view,
         name="edit_centre_scheme_view"),
]
