import frappe


def get_context(context):


    # lesson 10 content pagination
    # dict : is passing by the parameter with the below sql
    print(f"\n\n\n {frappe.form_dict} \n\n\n")

    articles = frappe.db.sql(""" SELECT * FROM `tabArticle_Garden`; """, as_dict=True)


    context = {
        "articles" : articles
    }

    return context