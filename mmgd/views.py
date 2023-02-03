from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.http import Http404

from .models import Orcamento

from django.views.decorators.clickjacking import xframe_options_deny
from django.views.decorators.clickjacking import xframe_options_sameorigin

def dashboard(request):
    #lista_orcs_estimados = Orc_estimado.query.filter_by(USER_ID=current_user.id).all()
    lista_orcs = Orcamento.objects.all()
    return render(request, 'mmgd/dashboard.html', {'orcs': lista_orcs})


def estimado(request):
    #context = {'alm.NOME_USINA': 1,}
    return render(request, 'mmgd/estimado.html')


def details(request, process_id):
    processo = get_object_or_404(Orcamento, pk=process_id)
    return render(request, 'mmgd/details.html', {'Orcamento': processo})


def map(request):
    return render(request, 'mmgd/maps/map.html')
