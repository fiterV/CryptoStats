from __future__ import absolute_import, unicode_literals
from celery import task
from .models import *
from decimal import Decimal
import requests
import json



@task()
def currency_update():
	all_pairs = PairOfCurrencies.objects.all()
	for pair in all_pairs:
		base = (pair.base.shortcode)
		target = (pair.target.shortcode)
		print("Grabbed pair {} - {}".format(base,target))
		req = requests.get('https://api.cryptonator.com/api/ticker/{}-{}'.format(base, target))
		print("Status request ", req.status_code)
		print("Content ", req.content)

		data = req.json()
		print("Json = ", json.dumps(data, indent=4))

		if data['success']:
			rate = Rate(currencies=pair, price=Decimal(data['ticker']['price']))
			rate.save()

		else:
			print('Something went wrong with {}', pair)