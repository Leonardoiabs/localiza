from django.views.generic import TemplateView


class HomeCarro(TemplateView):
    template_name = '01_carro/home.html'
    # template_name = '01_carro/home.html'

    def get_context_data(self, **kwargs):
        return dict(
            super().get_context_data(**kwargs),
            nome='Leonardo'
        )