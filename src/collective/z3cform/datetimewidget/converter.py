"""
The standard z3c.form data converters for Date and Datetime widgets result in
a unicode widget value which is the date formatted for the current locale.

The widgets in this package need to do their own handling of the actual
Date/Datetime objects, so for them we'll register a null converter which passes
through the value obtained from the context.
"""

from z3c.form.converter import BaseDataConverter

class NullDataConverter(BaseDataConverter):
    
    def toWidgetValue(self, value):
        return value

    def toFieldValue(self, value):
        return value
