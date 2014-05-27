from django.shortcuts import render, render_to_response
from django.core.context_processors import csrf
from django.template import RequestContext

from home.models import Citas
from home.forms import CitaForm, RegistroForm

# reporte de citas
def home(request):
	cita = Citas.objects.all().order_by('fecha')

	ctx = { 
		'cita' :cita,
	}

	return render_to_response('home/index.html', ctx, context_instance=RequestContext(request))

# agregar usuario
def add_user(request):
	save = False
	if request.method == 'POST':
		form = RegistroForm(request.POST)
		if form.is_valid():
			save = True
			form.save()

	else:
		form = RegistroForm()

	ctx = { 
		'save': save,
		'form': form,
	}
	
	return render_to_response('home/registro.html', ctx, context_instance=RequestContext(request))

# agregar cita
def add_cita(request):
	save = False
	if request.method == 'POST':
		form = CitaForm(request.POST)
		if form.is_valid():
			save = True
			form.save()

	else:
		form = CitaForm()

	ctx = { 
		'form': form,
		'save': save
	}

	return render_to_response('home/add_cita.html', ctx, context_instance=RequestContext(request))

# buscar cita
def search_cita(request):
	cita = ''
	buscar = request.POST.get('buscador')

	if request.method == 'POST':

		cita = Citas.objects.filter(titulo=buscar).order_by('fecha')

	ctx = { 
		'cita' :cita,
	}

	return render_to_response('home/buscar.html', ctx, context_instance=RequestContext(request))