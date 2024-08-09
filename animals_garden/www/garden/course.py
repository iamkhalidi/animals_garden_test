import frappe 

def get_context(context):

    article = frappe.get_doc("Article_Garden", "ali garden")

    context = {
        "article" : article
    }

    return context