from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.models import ProfileUser
from .models import Furniture
from .forms import CreateForm


def has_access_to_modify(current_user, furniture):
    if current_user.is_superuser:
        return True
    elif current_user.id == furniture.user.id:
        return True
    return False


class FurnitureList(generic.ListView):
    model = Furniture
    template_name = 'furnitures/furniture_list.html'
    context_object_name = 'furniture'


class FurnitureDetail(LoginRequiredMixin, generic.DetailView):
    model = Furniture
    login_url = '/accounts/registration/login/'
    context_object_name = 'furniture'
    template_name = 'furnitures/furniture_detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(FurnitureDetail, self).get_context_data(**kwargs)
        owner = context['object'].user
        current_user = self.request.user
        if has_access_to_modify(current_user, owner):
            context['is_user_furniture'] = True
            return context
        context['is_user_furniture'] = False
        return context


class UserFurnitureList(LoginRequiredMixin, generic.ListView):
    model = Furniture
    template_name = 'furnitures/furniture_list.html'
    context_object_name = 'furniture'

    def get_queryset(self):
        user_id = int(self.request.user.id)

        try:
            user = ProfileUser.objects.all().filter(user__pk=user_id)[0]
            furniture = Furniture.objects.all().filter(user=user.pk)
            return furniture
        except:
            return []


class Create(LoginRequiredMixin, generic.CreateView):
    model = Furniture
    template_name = 'furnitures/create.html'
    form_class = CreateForm
    success_url = '/furniture/'

    def form_valid(self, form):
        user = ProfileUser.objects.all().filter(user__pk=self.request.user.id)[0]
        form.instance.user = user
        return super().form_valid(form)


class Edit(LoginRequiredMixin, generic.UpdateView):
    model = Furniture
    form_class = CreateForm
    template_name = 'furnitures/edit.html'
    success_url = '/furniture/'

    def form_valid(self, form):
        user = ProfileUser.objects.all().filter(user__pk=self.request.user.id)[0]
        form.instance.user = user
        return super().form_valid(form)

    def get(self, request, pk):
        instance = Furniture.objects.get(pk=pk)
        form = CreateForm(request.POST or None, instance=instance)
        return render(request, 'furnitures/edit.html', {'form': form})


class Delete(LoginRequiredMixin, generic.DeleteView):
    model = Furniture
    login_url = '/accounts/registration/login/'

    def get(self, request, pk):
        return render(request, 'furnitures/delete.html', {'furniture': self.get_object()})

    def post(self, request, pk):
        furniture = self.get_object()
        furniture.delete()
        return HttpResponseRedirect('/furniture/')
