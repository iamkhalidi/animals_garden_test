import frappe


def get_context(context):

    articles = frappe.db.sql(""" SELECT * FROM `tabArticle_Garden`; """, as_dict=True)


    context = {
        "articles" : articles
    }

    return context