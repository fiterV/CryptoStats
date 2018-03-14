from django import forms
from .validators import *
from .models import *


class PairOfCurrenciesForm(forms.Form):
	base = forms.CharField(max_length=10, required=True, validators=[if_currency_exists], 
						   widget=forms.TextInput(attrs={'class':'form-control'}))
	target = forms.CharField(max_length=10, required=True, validators=[if_currency_exists],
							 widget=forms.TextInput(attrs={'class':'form-control'}))

	def is_valid(self):
		parent_check = super(PairOfCurrenciesForm, self).is_valid()
		if not parent_check:
			return False

		base = self.cleaned_data.get('base')
		target = self.cleaned_data.get('target')

		if base == target:
			self.errors['equality']="Type two different values"
			return False

		qs = PairOfCurrencies.objects.filter(base__shortcode=base, target__shortcode=target) 

		if qs:
			self.errors['present_in_db']="Already monitoring these two"
			return False
		return True

	def save(self):
		base = Currency.objects.get(shortcode=self.cleaned_data['base'])
		target = Currency.objects.get(shortcode=self.cleaned_data['target'])
		pair = PairOfCurrencies(base = base, target = target)
		pair.save()


