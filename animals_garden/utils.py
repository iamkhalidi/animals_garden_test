import frappe


# github keypass
# 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



def sendMail(doc, recepients, msg, title, attachments=None):
    print('test print method in python with email sender in frappe ********* ****************************************************************************************')
    email_args = {
        "recepients": recepients,
        "message" : msg,
        "subject" : title,
        "reference_doctype" : doc.doctype,
        "reference_name" : doc.name
    }
    if attachments:email_args["attachments"] = attachments
    # 3

    frappe.enqueue(method=frappe.sendmail, queue="short", timeout=300, **email_args)
    # 4


def test_hook(doc, event):
    print(f"--------{doc.owner1}--------")
    frappe.msgprint("this is msgprint in test_hook function")
    # you can reach to any field by writing its doc.name




def save_note(doc, event):


    doc_title = doc.article_name

    new_note = frappe.get_doc({
        "doctype" : "Note",
        "title" : doc_title
    })

    new_note.insert()
    # frappe.db.commit()
    # sometimes insert doesn't work so use this



# lesson 4 advanced
@frappe.whitelist()
def get_owner_articles(owner1 = None, publisher= None): # or you can just not pass any arg in the  parameter to get all the articles

    print("")

    articles = frappe.db.sql(f""" SELECT * FROM `tabArticle_Garden` WHERE owner1='{owner1}'; """, as_dict=True)
    return articles

    # after passing the parameter you can call it from the frontend file   





# 1-
# doc: is about your specific doctype
# doc.name is the primary key name

# 2-
# recepients : wh o would get the email
# msg : the body of email, title : the title of email

# 3-
# attachment : like image or video or any uploaded file.
# if email has any attach then create a key in email_args ,
#   and set the value in it like:
#       attachments:email_args["attachments"] = attachments

# 4-
# enqueue : if you want to send many emails, it's going to 
#               freeze your system
#           it makes the sent emails ordered to not making crashing,
#           queue="short" : if your email not very important write long.
#           **email_args : it would give you the key elements of our email
#               address.

# 5-
# http://127.0.0.1:8000/api/method/animals_garden.utils.get_owner_articles
#   you can use api method from the browser




