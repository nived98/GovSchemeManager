from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from schemes.models import StateSchemeList, CentreSchemeList
from schemes.forms import CreateCentreSchemeListForm, CreateStateSchemeListForm, UpdateStateSchemeListForm, UpdateCentreSchemeListForm
from accounts.models import UserProfile, CentreAdminProfile, StateAdminProfile
from django.contrib.auth.models import User

from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt


def create_state_scheme_list_view(request):
    context = {}
    user = request.user
    user = User.objects.get(username=user)
    if not user.is_authenticated:
        return redirect('must_authenticate')

    form = CreateStateSchemeListForm(
        request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.owner = user
        obj.state = user.state
        obj.ministry = user.ministry
        obj.save()
        form = CreateStateSchemeListForm()
    else:
        print(form.errors)
        print("main \n\n\n\n\n\n\\n")
    context['form'] = form
    return render(request, "schemes/create_state_scheme.html", context)


def create_centre_scheme_list_view(request):
    context = {}
    user = request.user
    user = User.objects.get(username=user)
    if not user.is_authenticated:
        return redirect('must_authenticate')

    form = CreateCentreSchemeListForm(
        request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.owner = user
        obj.ministry = user.ministry
        obj.save()
        form = CreateCentreSchemeListForm()
    else:
        print(form.errors)
        print("main \n\n\n\n\n\n\\n")
    context['form'] = form
    return render(request, "schemes/create_centre_scheme.html", context)


def detail_state_scheme_list_view(request, slug):
    context = {}
    user = request.user
    state_scheme_listing = get_object_or_404(StateSchemeList, slug=slug)
    lists = StateSchemeList.objects.filter()
    context['lists'] = lists
    context['state_scheme_listing'] = state_scheme_listing
    context['user'] = user
    return render(request, 'schemes/detail_state_scheme.html', context)


def detail_centre_scheme_list_view(request, slug):
    context = {}
    user = request.user
    centre_scheme_listing = get_object_or_404(CentreSchemeList, slug=slug)
    lists = CentreSchemeList.objects.filter()
    context['lists'] = lists
    context['centre_scheme_listing'] = centre_scheme_listing
    context['user'] = user
    return render(request, 'schemes/detail_centre_scheme.html', context)


def edit_state_scheme_view(request, slug):
    context = {}
    user = request.user
    if not user.is_authenticated:
        return redirect("must_authenticate")
    state_scheme_listing = get_object_or_404(StateSchemeList, slug=slug)

    if state_scheme_listing.owner != user:
        return HttpResponse('You are not the owner of that scheme.')
    if request.POST:
        form = UpdateStateSchemeListForm(
            request.POST or None, request.FILES or None, instance=state_scheme_listing)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            context['success_message'] = "Updated"
            state_scheme_listing = obj

    form = UpdateStateSchemeListForm(
        initial={
            "title": state_scheme_listing.title,
            "body": state_scheme_listing.body,
            # "image": state_scheme_listing.image,
        }
    )

    context['form'] = form
    return render(request, 'scheme/edit_state_scheme_listing.html', context)


def edit_centre_scheme_view(request, slug):
    context = {}
    user = request.user
    if not user.is_authenticated:
        return redirect("must_authenticate")
    centre_scheme_listing = get_object_or_404(CentreSchemeList, slug=slug)

    if centre_scheme_listing.owner != user:
        return HttpResponse('You are not the owner of that scheme.')
    if request.POST:
        form = UpdateCentreSchemeListForm(
            request.POST or None, request.FILES or None, instance=centre_scheme_listing)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            context['success_message'] = "Updated"
            centre_scheme_listing = obj

    form = UpdateCentreSchemeListForm(
        initial={
            "title": centre_scheme_listing.title,
            "body": centre_scheme_listing.body,
            # "image": state_scheme_listing.image,
        }
    )

    context['form'] = form
    return render(request, 'scheme/edit_centre_scheme_listing.html', context)

# register and unregister, check eligibility
