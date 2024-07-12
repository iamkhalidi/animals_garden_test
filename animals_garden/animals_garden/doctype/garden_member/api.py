import frappe


# permission to make you use it, whitelist : allows the function to be 
# accessible from outside, it's allows you to have api key
# allow_guest : 
#allow_guest=True
@frappe.whitelist()
def get_all_members():
    members = frappe.db.sql(f"""SELECT full_name,email_address FROM `tabGarden Member`;""", as_dict=True)
    return members

@frappe.whitelist(allow_guest=True)
def get_member():
    name_id = '267fktvfso'
    member_details = frappe.db.sql(f"""SELECT full_name,email_address FROM `tabGarden Member` WHERE name='{name_id}';""", as_dict=True)

    print(member_details)
    return  member_details


# @frappe.whitelist(allow_guest=True)
# def get_member(member_id):
#     member_details = frappe.db.sql(f"""SELECT full_name,email_address FROM `tabGarden Member` WHERE name='{member_id}';""", as_dict=True)
    
#     if(member_details):
#         return  member_details
#     else:
#         return "member doesn't exist"