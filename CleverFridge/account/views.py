from django.contrib.auth import get_user_model, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from CleverFridge.account.forms import UserCreateForm

UserModel = get_user_model()


class SignUpView(CreateView):
    template_name = 'account/register-page.html'
    form_class = UserCreateForm


    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result


class SignInView(LoginView):
    template_name = 'account/login-page.html'
    success_url = reverse_lazy('details user')


class SignOutView(LoginRequiredMixin, LogoutView):
    next_page = reverse_lazy('index')


class UserDetailsView(LoginRequiredMixin, DetailView):
    template_name = 'account/profile-details-page.html'
    model = UserModel

    def get_context_data(self, **kwargs):
        result = super().get_context_data(**kwargs)

        result['is_owner'] = self.request.user == self.object
        return result


class UserEditView(LoginRequiredMixin, UpdateView):
    template_name = 'account/profile-edit-page.html'
    model = UserModel
    fields = ('first_name', 'last_name', 'gender', 'email',)

    def get_success_url(self):
        return reverse_lazy('details user', kwargs={
            'pk': self.request.user.pk,

        })


class UserDeleteView(DeleteView):
    template_name = 'account/profile-delete-page.html'
    model = UserModel
    success_url = reverse_lazy('index')
