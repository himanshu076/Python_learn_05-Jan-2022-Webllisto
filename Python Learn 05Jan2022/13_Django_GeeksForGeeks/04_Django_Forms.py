'''*************Django Forms - Diff from HTML Forms****************'''

'''Django maps the fields defined in Django forms into HTML input fields. Django handles three distinct parts of the work involved in forms:

1. preparing and restructuring data to make it ready for rendering
2. creating HTML forms for the data
3. receiving and processing submitted forms and data from the client

Syntax :  Django Fields work like Django Model Fields and have the syntax:
          field_name = forms.FieldType(**options)
'''

from django import forms