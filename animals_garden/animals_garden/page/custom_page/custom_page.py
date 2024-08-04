import frappe

@frappe.whitelist(allow_guest=True)
def get_article_count():
    result = frappe.db.sql(""" SELECT COUNT(*) FROM `tabArticle_Garden`; """)
    return result   

