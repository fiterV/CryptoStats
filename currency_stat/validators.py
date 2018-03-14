from .models import *
from django.forms import ValidationError


def if_currency_exists(shortcode):
	cur = Currency.objects.filter(shortcode=shortcode).first()

	if not cur:
		raise ValidationError("{} doesn't exist as a currency".format(shortcode))
	return shortcode