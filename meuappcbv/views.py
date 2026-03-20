from email.policy import default
from venv import create

from django.urls import reverse_lazy
import requests
from django.shortcuts import render
from django.views.generic import FormView, ListView, DetailView, DateDetailView
from .forms import ViaCep
from .forms import ViaCepForm

class ViaCepView(FormView):
    template_name = ""
    form_class = ViaCepForm
    success_url = reverse_lazy("viacep:list")

    def form_valid(self, form):
        cep = form.cleaned_data['cep'].replaced("-","").strip()
        url = f'https://viacep.com.br/ws{cep}/json/'
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            if "erro" not in data:
                cep_obj, created = ViaCep.objects.update_or_create(
                    cep=cep,
                    defaults={
                        'logradouro': data.get('logradouro', ''),
                        'bairro': data.get('bairro', ''),
                        'localidade': data.get('localidade', ''),
                        'uf': data.get('uf', ''),
                    }
                )
                 
                self.object = cep_obj
            else:
                form.add_error('cep', 'CEP não encontrado na API')
                return self.form_invalid(form)

        else:
            form.add_error('cep', 'Error ao consultar a API')
            return self.form_invalid(form)
        return super().form_valid(form)



# Create your views here.
