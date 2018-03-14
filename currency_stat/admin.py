from django.contrib import admin
from .models import *

@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
	list_display=('shortcode', 'name')
	search_fields=('shortcode', )

@admin.register(Rate)
class RateAdmin(admin.ModelAdmin):
	list_display=('currencies', 'price', 'timestamp', 'pk')


@admin.register(PairOfCurrencies)
class PairOfCurrenciesAdmin(admin.ModelAdmin):
	list_display=('base', 'target', 'timestamp')
