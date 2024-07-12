# Copyright (c) 2024, khalid and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from animals_garden.utils import sendMail


class Article_Garden(Document):
	  
	# def before_save(self):
	# 	self.total_cost = int(self.article_cost) + int(self.ticket_delivery_cost)
	#   message = f"A new garden area with the name {doc.article_name} added to your account"
	# sendMail(doc, ['0sqf11@gmail.com', 'test@gmail.com'], message, "New Garden Area Created")
	# frappe.msgprint("Garden Area (Article) Saved and Email sent!")

	def validate(self):
		if(self.custom_track_buyers == 0):
			
			if(self.custom_buyers_ct):
				# if child table "buyers" has anything
				frappe.throw(f'This Area does not track buyers. {self.custom_track_buyers}')


	def before_save(doc):
		pass
