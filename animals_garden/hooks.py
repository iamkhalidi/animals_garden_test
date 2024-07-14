app_name = "animals_garden"
app_title = "Animals Garden"
app_publisher = "khalid"
app_description = "this app is for managing animals garden add them anhem"
app_email = "iq2lfl@gmail.com"
app_license = "mit"
# required_apps = []

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/animals_garden/css/animals_garden.css"
# app_include_js = "/assets/animals_garden/js/animals_garden.js"

# include js, css files in header of web template
# web_include_css = "/assets/animals_garden/css/animals_garden.css"
# web_include_js = "/assets/animals_garden/js/animals_garden.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "animals_garden/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "animals_garden/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "animals_garden.utils.jinja_methods",
# 	"filters": "animals_garden.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "animals_garden.install.before_install"
# after_install = "animals_garden.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "animals_garden.uninstall.before_uninstall"
# after_uninstall = "animals_garden.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "animals_garden.utils.before_app_install"
# after_app_install = "animals_garden.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "animals_garden.utils.before_app_uninstall"
# after_app_uninstall = "animals_garden.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "animals_garden.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

 
 
doc_events = {
	# "*": {
	# 	"on_update": "method",
	# 	"on_cancel": "method",
	# 	"on_trash": "method"
	# },
    "Article_Garden": {
		"validate": "animals_garden.utils.test_hook",
	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {  

#     "cron": {
#         "* * * * *": [
#             "animals_garden.tasks.cron"
#         ],
#         "* * * * *": [
#             "animals_garden.tasks.cron2"
#         ]
#     },

# 	"all": [
# 		"animals_garden.tasks.all"
# 	],
# 	"daily": [
# 		"anim als_garden.tasks.daily"
# 	],
# 	"hourly": [
# 		"animals_garden.tasks.hourly"
# 	],
# 	"weekly": [
# 		"animals_garden.tasks.weekly"
# 	],
# 	"monthly": [
# 		"animals_garden.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "animals_garden.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "animals_garden.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "animals_garden.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["animals_garden.utils.before_request"]
# after_request = ["animals_garden.utils.after_request"]

# Job Events
# ----------
# before_job = ["animals_garden.utils.before_job"]
# after_job = ["animals_garden.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"animals_garden.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

