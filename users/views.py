from django.contrib import messages
# Create your views here.
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.db import transaction
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView

from articles.models import Article
from team_work.mixin import BaseClassContextMixin, UserLoginCheckMixin
from users.forms import UserLoginForm, UserRegistrationForm, UserForm, UserProfileForm
from users.models import User
from users.rating_counter import user_rating


# Аутентификация пользователя
class AuthorizationView(BaseClassContextMixin, LoginView):
    title = 'Авторизация'
    form_class = UserLoginForm
    template_name = 'users/authorization.html'


# Регистрация пользователя
class RegistrationView(BaseClassContextMixin, SuccessMessageMixin, CreateView):
    model = User
    title = 'Регистрация'
    form_class = UserRegistrationForm
    template_name = 'users/registration.html'
    success_url = reverse_lazy('users:authorization')
    success_message = 'You have successfully registered'


# Профиль
class UserProfileView(BaseClassContextMixin, UserLoginCheckMixin, UpdateView, SuccessMessageMixin):
    model = User
    title = 'Профиль'
    form_class = UserForm
    template_name = 'users/lk_users.html'
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return get_object_or_404(User, pk=self.request.user.id)

    def get_context_data(self, **kwargs):
        context = super(UserProfileView, self).get_context_data(**kwargs)
        context['profile'] = UserProfileForm(instance=self.request.user.userprofile)
        context['articles'] = Article.objects.filter(author_id=self.request.user.id)
        return context

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        form = UserForm(data=request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, files=request.FILES, instance=request.user.userprofile)
        if form.is_valid() and profile_form.is_valid():
            messages.success(self.request, 'Данные успешно обновлены!')
            form.save()
        else:
            messages.warning(self.request, 'Что-то пошло не так')
        return redirect(self.success_url)


class UserLogoutView(BaseClassContextMixin, UserLoginCheckMixin, LogoutView):
    pass


class PublicUserProfileView(BaseClassContextMixin, DetailView):
    """
    класс выводит публичный профиль пользователя
    """
    model = User
    title = 'Профиль пользователя'
    template_name = 'users/public_profile.html'
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super(PublicUserProfileView, self).get_context_data(**kwargs)
        context['user_rating'] = user_rating(self.kwargs["pk"])  # подсчет рейтинга пользователя
        return context
