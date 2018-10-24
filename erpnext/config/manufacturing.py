from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Bill of Materials"),
			"items": [
				{
					"type": "doctype",
					"name": "BOM",
					"description": _("Bill of Materials (BOM)"),
					"label": _("Bill of Materials")
				},
				{
					"type": "doctype",
					"name": "BOM",
					"icon": "fa fa-sitemap",
					"label": _("BOM Browser"),
					"description": _("Tree of Bill of Materials"),
					"link": "Tree/BOM",
				},
				{
					"type": "doctype",
					"name": "BOM Update Tool",
					"description": _("Replace BOM and update latest price in all BOMs"),
				}
			]
		},
		{
			"label": _("Production"),
			"icon": "fa fa-industry",
			"items": [
				{
					"type": "doctype",
					"name": "Production Order",
					"description": _("Orders released for production."),
				},
				{
					"type": "doctype",
					"name": "Production Planning Tool",
					"description": _("Generate Material Requests (MRP) and Production Orders."),
				},
				{
					"type": "doctype",
					"name": "Stock Entry",
				},
				{
					"type": "doctype",
					"name": "Timesheet",
					"description": _("Time Sheet for manufacturing."),
				},

			]
		},
		{
			"label": _("Analytics"),
			"icon": "fa fa-list",
			"items": [
				{
					"type": "page",
					"name": "production-analytics",
					"label": _("Production Analytics"),
					"icon": "fa fa-bar-chart",
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
					"name": "Open Production Orders",
					"doctype": "Production Order"
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Production Orders in Progress",
					"doctype": "Production Order"
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Issued Items Against Production Order",
					"doctype": "Production Order"
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Completed Production Orders",
					"doctype": "Production Order"
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "BOM Search",
					"doctype": "BOM"
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "BOM Stock Report",
					"doctype": "BOM"
				}
			]
		},
		{
			"label": _("Setup"),
			"items": [
				{
					"type": "doctype",
					"name": "Workstation",
					"description": _("Where manufacturing operations are carried."),
				},
				{
					"type": "doctype",
					"name": "Operation",
					"description": _("Details of the operations carried out."),
				},
				{
					"type": "doctype",
					"name": "Manufacturing Settings",
					"description": _("Global settings for all manufacturing processes."),
				}
			]
		},
# 		{
# 			"label": _("Help"),
# 			"icon": "fa fa-facetime-video",
# 			"items": [
# 				{
# 					"type": "help",
# 					"label": _("Bill of Materials"),
# 					"youtube_id": ""
# 				},
# 				{
# 					"type": "help",
# 					"label": _("Production Planning Tool"),
# 					"youtube_id": ""
# 				},
# 				{
# 					"type": "help",
# 					"label": _("Production Order"),
# 					"youtube_id": ""
# 				},
# 			]
# 		}
	]
