from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from .form import ReservationForms
from .models import Team, About, Portfolio, Services, Partners
from django.shortcuts import redirect

class HomePage(TemplateView):
    template_name = 'main.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['teams'] = Team.objects.filter(is_visible=True)
        context['abouts'] = About.objects.filter(is_visible=True)
        context['portfolioes'] = Portfolio.objects.filter(is_visible=True)
        context['serviceses'] = Services.objects.filter(is_visible=True)
        context['partntrs'] = Partners.objects.all()
        context['reservation'] = ReservationForms()
        return context

    def post(self, request, *args, **kwargs):
        reservation_form = ReservationForms(request.POST)
        if reservation_form.is_valid():
            reservation_form.save()
            return redirect('main:home')
        else:
            # Обработка случая, когда форма не валидна
            context = self.get_context_data()
            context['reservation'] = reservation_form
            return self.render_to_response(context)
