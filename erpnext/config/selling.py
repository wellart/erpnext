from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Sales"),
			"icon": "fa fa-star",
			"items": [
				{
					"type": "doctype",
					"name": "Quotation",
					"description": _("Quotes to Leads or Customers."),
				},
				{
					"type": "doctype",
					"name": "Sales Order",
					"description": _("Confirmed orders from Customers."),
				},
			]
		},
		{
			"label": _("Customers"),
			"items": [
				{
					"type": "doctype",
					"name": "Customer",
					"description": _("Customer database."),
				},
				{
					"type": "doctype",
					"name": "Contact",
					"description": _("All Contacts."),
				},
				{
					"type": "doctype",
					"name": "Address",
					"description": _("All Addresses."),
				},
				{
					"type": "doctype",
					"label": _("Customer Group"),
					"name": "Customer Group",
					"icon": "fa fa-sitemap",
					"link": "Tree/Customer Group",
					"description": _("Manage Customer Group Tree."),
				},
			]
		},
# 		{
# 			"label": _("Items and Pricing"),
# 			"items": [
# 				{
# 					"type": "doctype",
# 					"name": "Item",
# 					"description": _("All Products or Services."),
# 				},
# 				{
# 					"type": "doctype",
# 					"name": "Product Bundle",
# 					"description": _("Bundle items at time of sale."),
# 				},
# 				{
# 					"type": "doctype",
# 					"name": "Item Group",
# 					"icon": "fa fa-sitemap",
# 					"label": _("Item Group"),
# 					"link": "Tree/Item Group",
# 					"description": _("Tree of Item Groups."),
# 				},
# 				{
# 					"type": "doctype",
# 					"name": "Item Price",
# 					"description": _("Multiple Item prices."),
# 					"route": "Report/Item Price"
# 				},
# 				{
# 					"type": "doctype",
# 					"name": "Price List",
# 					"description": _("Price List master.")
# 				},
# 				{
# 					"type": "doctype",
# 					"name": "Pricing Rule",
# 					"description": _("Rules for applying pricing and discount.")
# 				},
# 				{
# 					"type": "doctype",
# 					"name": "Shipping Rule",
# 					"description": _("Rules for adding shipping costs.")
# 				},
#
# 			]
# 		},
		{
			"label": _("POS"),
			"icon": "fa fa-credit-card",
			"items": [
				{
					"type": "page",
					"name": "pos",
					"label": _("Point-of-Sale (POS)"),
					"description": _("Point of Sale")
				},
				{
					"type": "doctype",
					"name": "POS Profile",
					"label": _("POS Profile"),
					"description": _("Setup default values for POS Invoices")
				},
				{
					"type": "doctype",
					"name": "POS Settings",
					"description": _("Setup mode of POS (Online / Offline)")
				},
			]
		},
		{
			"label": _("Fulfilment"),
			"items": [
				{
					"type": "doctype",
					"name": "Delivery Trip",
					"description": _("Delivery Trip service tours to customers.")
				},
				{
					"type": "doctype",
					"name": "Shipping Rule",
				},
			]
		},
		{
			"label": _("Sales Partners and Territory"),
			"items": [
				{
					"type": "doctype",
					"label": _("Sales Person"),
					"name": "Sales Person",
					"icon": "fa fa-sitemap",
					"link": "Tree/Sales Person",
					"description": _("Manage Sales Person Tree."),
				},
				{
					"type": "doctype",
					"label": _("Sales Partner"),
					"name": "Sales Partner",
					"description": _("Manage Sales Partners."),
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Addresses And Contacts",
					"label": _("Sales Partner Contacts"),
					"doctype": "Address",
					"route_options": {
						"party_type": "Sales Partner"
					}
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Sales Person Target Variance (Item Group-Wise)",
					"route": "query-report/Sales Person Target Variance Item Group-Wise",
					"doctype": "Sales Person",
				},
				{
					"type": "doctype",
					"label": _("Territory"),
					"name": "Territory",
					"icon": "fa fa-sitemap",
					"link": "Tree/Territory",
					"description": _("Manage Territory Tree."),
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Territory Target Variance (Item Group-Wise)",
					"route": "query-report/Territory Target Variance Item Group-Wise",
					"doctype": "Territory"
				},
			]
		},
		{
			"label": _(""),
			"items": [
				{
					"type": "help",
					"label": _(""),
					"kolom kosong": "",
				}
			]
		},
		{
			"label": _("Analytics"),
			"icon": "fa fa-table",
			"items": [
				{
					"type": "page",
					"name": "sales-analytics",
					"label": _("Sales Analytics"),
					"icon": "fa fa-bar-chart",
				},
				{
					"type": "page",
					"name": "sales-funnel",
					"label": _("Sales Funnel"),
					"icon": "fa fa-bar-chart",
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Customer Acquisition and Loyalty",
					"doctype": "Customer",
					"icon": "fa fa-bar-chart",
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Quotation Trends",
					"doctype": "Quotation"
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Sales Order Trends",
					"doctype": "Sales Order"
				},
			]
		},
		{
			"label": _("Reports"),
			"icon": "fa fa-list",
			"items": [
				{
					"type": "report",
					"is_query_report": True,
					"name": "Lead Details",
					"doctype": "Lead"
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Addresses And Contacts",
					"label": _("Customer Addresses Book"),
					"doctype": "Address",
					"route_options": {
						"party_type": "Customer"
					}
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Inactive Customers",
					"doctype": "Sales Order"
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Customer Credit Balance",
					"doctype": "Customer"
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Ordered Items To Be Delivered",
					"doctype": "Sales Order"
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Item-wise Sales History",
					"doctype": "Item"
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Sales Person-wise Transaction Summary",
					"doctype": "Sales Order"
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Available Stock for Packing Items",
					"doctype": "Item",
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Pending SO Items For Purchase Request",
					"doctype": "Sales Order"
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "BOM Search",
					"doctype": "BOM"
				},
			]
		},
		{
			"label": _("Setup"),
			"icon": "fa fa-cog",
			"items": [
				{
					"type": "doctype",
					"name": "Selling Settings",
					"description": _("Default settings for selling transactions.")
				},
				{
					"type": "doctype",
					"name": "Campaign",
					"description": _("Sales campaigns."),
				},
				{
					"type": "doctype",
					"name":"Terms and Conditions",
					"label": _("Terms and Conditions Template"),
					"description": _("Template of terms or contract.")
				},
				{
					"type": "doctype",
					"name": "Sales Taxes and Charges Template",
					"description": _("Tax template for selling transactions.")
				},
				{
					"type": "doctype",
					"name": "Industry Type",
					"description": _("Track Leads by Industry Type.")
				},
			]
		},
# 		{
# 			"label": _("Help"),
# 			"items": [
# 				{
# 					"type": "help",
# 					"help_type": "helpdesk",
# 					"label": _("help desk"),
# 				},
# 				{
# 					"type": "help",
# 					"label": _("Customer and Supplier"),
# 					"youtube_id": "anoGi_RpQ20"
# 				},
# 				{
# 					"type": "help",
# 					"label": _("Sales Order to Payment"),
# 					"youtube_id": "7AMq4lqkN4A"
# 				},
# 				{
# 					"type": "help",
# 					"label": _("Point-of-Sale"),
# 					"youtube_id": "4WkelWkbP_c"
# 				},
# 			]
# 		}
	]
