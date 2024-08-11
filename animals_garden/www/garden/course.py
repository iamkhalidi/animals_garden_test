import frappe 

def get_context(context):

    article = frappe.get_doc("Article_Garden", frappe.form_dict.name)

    context = {
        "article" : article
    }

    return context