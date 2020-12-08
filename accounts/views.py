from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from accounts.forms import ProfileForm, RegisterForm, LoginForm
from accounts.models import ProfileUser


def redirect_user(request):
    url = f'/furniture/'
    return HttpResponseRedirect(url)


@login_required
def user_detail(request):
    pk = request.user.id
    profile_user = [i for i in ProfileUser.objects.all() if i.user_id == pk][0]
    print(profile_user)
    context = {
        'user': request.user,
        'profile_user': profile_user}
    return render(request, 'accounts/user_profile.html', context)


def register_user(request):
    if request.method == 'GET':
        context = {
            'user_form': RegisterForm(),
            'profile_form': ProfileForm()}
        return render(request, 'accounts/signup.html', context)
    else:
        user_form = RegisterForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            login(request, user)
            return redirect('login')
        context = {
            'user_form': RegisterForm(),
            'profile_form': ProfileForm()}
        return render(request, 'accounts/signup.html', context)


def login_user(request):
    if request.method == 'GET':
        context = {'login_form': LoginForm()}
        return render(request, 'registration/login.html', context)
    else:
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                # user_id_is = user.id  # az
                # profile_user = [i for i in ProfileUser.objects.all() if i.user_id == user_id_is][0]  # az
                login(request, user)
                return redirect('furniture')
                # return render(request, 'common/landing_page.html', {'profile_user': profile_user})  # az
        context = {'login_form': login_form}
        return render(request, 'registration/login.html', context)
