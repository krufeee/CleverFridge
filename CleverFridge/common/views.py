from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views import generic

from CleverFridge.common.models import HomepageWellcomeTextModel


class IndexView(generic.TemplateView):
    template_name = 'common/index.html'

    def get_context_data(self, **kwargs):
        result = super().get_context_data(**kwargs)

        result['description'] = HomepageWellcomeTextModel.objects.get()
        return result

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('homepage')
        return super(IndexView, self).dispatch(request, *args, **kwargs)


class HomepageView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'common/homepage.html'
