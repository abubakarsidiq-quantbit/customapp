// Copyright (c) 2023, Quantbit and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Manufacturing Stock"] = {
	"filters": [
		{
			"fieldname": "Stock Entry",
    		"label": __("Stock Entry"),
    		"fieldtype": "Link",
    		"options": "Stock Entry",
    		"width": 100,
			"reqd" : 0,
		},
		{
			"fieldname": "from",
    		"label": __("From Date"),
    		"fieldtype": "Date",
    	    "width": 0,
			"reqd" : 1,
			"default" : dateutil.year_start()
		},
		{
			"fieldname": "to",
    		"label": __("To Date"),
    		"fieldtype": "Date",
    	    "width": 80,
			"reqd" : 1,
			"default" : dateutil.year_end()
		}
	]
};
