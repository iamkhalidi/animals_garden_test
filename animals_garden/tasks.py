import frappe
from frappe.utils.background_jobs import enqueue
#import urllib.request as urllib2



def all():
    pass

def cron():

    print("\n\n\nSending message now!\n\n\n")
    
    phone_number = "+966592283947"
    message = "Hi, scheduler you set up for cron tab is working fine!"

def cron2():
    
    print("\n\n\nthe second cron method worked successfuly!\n\n\n")

