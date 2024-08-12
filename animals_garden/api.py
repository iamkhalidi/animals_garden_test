import frappe



# lesson 10 content pagination
def paginate(doctype, page=0):

    # default buttons is zero
    prev = 0
    next = 0

    conditions = ""

    query = f""" SELECT name, article_name, owner1, article_cost, publisher FROM `tab{doctype}` {conditions}"""

    # if it has page and not just the home page
    if(page):
        page = int(page)
        articles = frappe.db.sql(query + f""" LIMIT {(page*3)-3} ,3 """, as_dict=True)
        next_page = frappe.db.sql(query + f""" LIMIT {page*3} ,3 """, as_dict=True)

        # if i have data
        if(next_page):
            prev, next = page-1, page+1  # if i prev i'm going to be in 0 , if next page +1
        else:
            prev, next = page-1, 0

    else:
        count= frappe.db.sql(f""" SELECT COUNT(name) as count FROM `tab{doctype}`; """, as_dict=True )[0].count

        if(count > 3):
            prev = 0
            next = 2
        else:
            pass

        articles = frappe.db.sql(query + """ LIMIT 3 """, as_dict=True)

    return {
        "aritcles": articles,
        "prev": prev,
        "next": next
    }

