# Copyright (c) 2023, Quantbit and contributors
# For license information, please see license.txt

from frappe import _
import frappe
from datetime import datetime


def execute(filters=None):
	return get_columns(), get_data(filters)

def get_data(filters):
	print("f\n\n\n{filters}\n\n\n")
	return[['test']]
		

def get_columns():
	return[
		"Stock Entry:Link/Stock Entry:70"
		
	]
