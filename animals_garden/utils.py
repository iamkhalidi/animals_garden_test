import frappe



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
    print(f"-------------------- {doc} -------------{event}-----------------")






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