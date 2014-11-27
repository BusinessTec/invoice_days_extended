#-*- coding: utf-8 -*- 
from openerp import models, fields, api
from datetime import datetime


class invoice_days(models.Model):
	
	_inherit = "account.invoice"
	over_days = fields.Integer(string='Atrasado',compute="days_over",readonly=True)

	@api.one
	@api.depends('state','date_due','date_invoice')
	def days_over(self):
		if self.state == 'open'
			if payment_term:
				self.over_days=(today-self.date_due).days
			else:
				self.over_days=(today-self.date_invoice).days-30
		else
			self.over_days=0
