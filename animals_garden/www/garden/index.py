import frappe
from animals_garden.api import paginate


def get_context(context):


    # lesson 10 content pagination
    # dict : is passing by the parameter with the below sql
    # print(f"\n\n\n {frappe.form_dict} \n\n\n")
    # articles = frappe.db.sql(""" SELECT * FROM `tabArticle_Garden`; """, as_dict=True)

    
    page = frappe.form_dict.page  # paginate function in apy.py file
    pagination = paginate("Article_Garden", page)  # pagination = dictionary has returned in bench console, *1 below



    articles = pagination.get('articles') 
    prev = pagination.get('prev')
    next = pagination.get('next')


    context = {
        "articles" : articles,
        "prev" : prev,
        "next" : next,

    }

    return context







# 1 -
# In [3]: paginate("Article_Garden", 2)
# Out[3]: 

# {'aritcles': [{'name': 'Monkey Garden',
#    'article_name': 'Monkey Garden',
#    'owner1': 'shams',
#    'article_cost': 15,
#    'publisher': 'shams'},
#   {'name': 'Noah',
#    'article_name': 'Noah',
#    'owner1': 'noah',
#    'article_cost': 95,
#    'publisher': 'naoh'},
#   {'name': 'Rabbit Garden',
#    'article_name': 'Rabbit Garden',
#    'owner1': 'Noah',
#    'article_cost': 55,
#    'publisher': None}],
#  'prev': 1,
#  'next': 3}

