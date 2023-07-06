# Copyright (c) 2023, Midline International WLL and Contributors
# License: GPL v3. See licence.txt

import frappe
from erpnext.selling.doctype.customer.customer import Customer


class CustomCustomer(Customer):
	def create_primary_address(self):
		from frappe.contacts.doctype.address.address import get_address_display

		if self.flags.is_new_doc and self.get("address_line1"):
			address = make_address(self)
			address_display = get_address_display(address.name)

			self.db_set("customer_primary_address", address.name)
			self.db_set("primary_address", address_display)


def make_address(args, is_primary_address=1):
	reqd_fields = []
	for field in ["city", "country"]:
		if not args.get(field):
			reqd_fields.append("<li>" + field.title() + "</li>")

	if reqd_fields:
		msg = _("Following fields are mandatory to create address:")
		frappe.throw(
			"{0} <br><br> <ul>{1}</ul>".format(msg, "\n".join(reqd_fields)),
			title=_("Missing Values Required"),
		)

	address = frappe.get_doc(
		{
			"doctype": "Address",
			"address_title": args.get("name"),
			"address_line1": args.get("address_line1"),
			"address_line2": args.get("address_line2"),
			"city": args.get("city"),
			"state": args.get("state"),
			"pincode": args.get("pincode"),
			"country": args.get("country"),
			"fax": args.get("fax"),
			"phone": args.get("phone"),
			"links": [{"link_doctype": args.get("doctype"), "link_name": args.get("name")}],
		}
	).insert()

	return address
