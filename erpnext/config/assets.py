from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Assets"),
			"items": [
				{
					"type": "doctype",
					"name": "Asset",
				},
				{
					"type": "doctype",
					"name": "Asset Movement",
					"description": _("Transfer an asset from one warehouse to another")
				},
				{
					"type": "doctype",
					"name": "Asset Category",
				}
			]
		},
		{
			"label": _("Maintenance"),
			"items": [
				{
					"type": "doctype",
					"name": "Asset Maintenance Team",
				},
				{
					"type": "doctype",
					"name": "Asset Maintenance",
				},
				{
					"type": "doctype",
					"name": "Asset Maintenance Tasks",
				},
				{
					"type": "doctype",
					"name": "Asset Maintenance Log",
				},
				{
					"type": "doctype",
					"name": "Asset Repair",
				},
			]
		},
		{
			"label": _("Fleet Management"),
			"items": [
				{
					"type": "doctype",
					"name": "Vehicle"
				},
				{
					"type": "doctype",
					"name": "Vehicle Log"
				},
				{
					"type": "doctype",
					"name": "Vehicle Assignment"
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
			"label": _("Reports"),
			"icon": "fa fa-table",
			"items": [
				{
					"type": "report",
					"name": "Asset Depreciation Ledger",
					"doctype": "Asset",
					"is_query_report": True,
				},
				{
					"type": "report",
					"name": "Asset Depreciations and Balances",
					"doctype": "Asset",
					"is_query_report": True,
				},
				{
					"type": "report",
					"name": "Asset Maintenance",
					"doctype": "Asset Maintenance"
				}
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
# 					"label": _("Asset Management"),
# 					"youtube_id": ""
# 				},
# 				{
# 					"type": "help",
# 					"label": _("Asset Maintenance"),
# 					"youtube_id": ""
# 				},
# 				{
# 					"type": "help",
# 					"label": _("Fleet Management"),
# 					"youtube_id": ""
# 				}
# 			]
# 		}
	]
