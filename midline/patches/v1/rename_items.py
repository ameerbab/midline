# Copyright (c) 2015, Midline International WLL and Contributors
# License: GPL v3. See licence.txt

import frappe


def execute():
    to_rename = frappe.db.get_all('Item', filters={'new_code': ['!=', '']}, fields=['name', 'new_code'])
    for item in to_rename:
        try:
            frappe.rename_doc('Item', item.name, item.new_code)
        except Exception as e:
            frappe.log_error(str(e), "Error in rename")
            continue
