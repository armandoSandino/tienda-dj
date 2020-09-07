from django.shortcuts import render
#
from django.views.generic import TemplateView

class LoginUser(TemplateView):

    template_name = 'users/login.html'

    def get_context_data(self, **kwargs):
        context = super(LoginUser, self).get_context_data(**kwargs)
        return context
    