from django.shortcuts import render
from .forms import *
from django.views.generic.edit import CreateView, UpdateView
from schemes.models import StateAdminProfile, CentreAdminProfile, StateSchemeList, CentreSchemeList

# Create your views here.


def home():
    context = {}
    user = request.user
    if not user.is_authenticated:
        centre_schemes_listing = CentreSchemeList.objects.all()

    state_scheme_listing = StateSchemeList.objects.filter(state=user.state)
    centre_schemes_listing = CentreSchemeList.objects.all()

    context = {'state_scheme_listing': state_scheme_listing,
               'centre_schemes_listing': centre_schemes_listing}
    return render(request, 'home.html', context)


class UserProfileCreate(CreateView):
    model = UserProfile
    fields = '__all__'


class UserProfileUpdate(UpdateView):
    model = UserProfile
    fields = '__all__'
    template_name_suffix = '_update_form'
