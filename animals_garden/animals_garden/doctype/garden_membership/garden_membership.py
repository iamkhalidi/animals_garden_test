# Copyright (c) 2024, khalid and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class GardenMembership(Document):
	def before_save(self):
		if(self.garden_member == 'lpupbu8kl9'):
			self.paid = 1
		else:
			self.paid = 0  

