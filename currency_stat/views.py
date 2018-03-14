from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from .models import *
from .forms import PairOfCurrenciesForm


def index(request):
	context={}
	context["all"]={}
	
	context["form"]=PairOfCurrenciesForm(request.POST or None)
	if request.POST:
		form = PairOfCurrenciesForm(request.POST)
		if form.is_valid():
			form.save()
		else:
			context['errors']=form.errors
	all_pairs = PairOfCurrencies.objects.all()
	for pair in all_pairs:
		context["all"][pair] = Rate.objects.filter(currencies=pair)
	
	
	return render(request, "currency_stat/all.html", context)

def specific_rate(request, base, target):
	pair = get_object_or_404(PairOfCurrencies, base__shortcode=base, target__shortcode=target)

	context={}
	context["all"]={}
	context["all"][pair] = Rate.objects.filter(currencies=pair)

	return render(request, "currency_stat/all.html", context)

