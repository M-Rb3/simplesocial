from django.views.generic import TemplateView
from django.views.generic.list import ListView
from posts.models import Post


class HomePage(ListView):
    template_name = 'index.html'
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class TestPage(TemplateView):
    template_name = 'test.html'


class ThanksPage(TemplateView):
    template_name = 'thanks.html'
