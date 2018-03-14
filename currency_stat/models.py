from django.db import models

class Currency(models.Model):
	name = models.CharField(max_length=50)
	shortcode = models.CharField(max_length=10)

	class Meta:
		verbose_name_plural = "Currencies"

	def __str__(self):
		return "{} ( {} )".format(self.shortcode, self.name)

class PairOfCurrencies(models.Model):
	base = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name="currency_rate_base")
	target = models.ForeignKey(Currency, on_delete=models.CASCADE)
	timestamp = models.DateTimeField(auto_now=True)	

	def __str__(self):
		return "{} - {}".format(self.base, self.target)

class Rate(models.Model):
	currencies = models.ForeignKey(PairOfCurrencies, on_delete=models.DO_NOTHING, default=None)
	price = models.DecimalField(max_digits=30, decimal_places=15)
	timestamp = models.DateTimeField(auto_now=True)	

