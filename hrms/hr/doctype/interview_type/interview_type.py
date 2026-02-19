# Copyright (c) 2021, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt


import json

import frappe
from frappe.model.document import Document


class InterviewType(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		description: DF.Text | None
	# end: auto-generated types

	pass


@frappe.whitelist()
def create_interview(doc):
	if isinstance(doc, str):
		doc = json.loads(doc)
		doc = frappe.get_doc(doc)

	interview = frappe.new_doc("Interview")
	interview.interview_type = doc.name
	interview.designation = doc.designation

	if doc.interviewers:
		interview.interview_details = []
		for d in doc.interviewers:
			interview.append("interview_details", {"interviewer": d.user})

	return interview
