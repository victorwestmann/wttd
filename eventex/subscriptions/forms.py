# coding: utf-8
from django import forms

class SubscriptionForm(forms.Form):
	name = forms.CharField()
	cpf = forms.CharField()
	email = forms.CharField()
	phone = forms.CharField()