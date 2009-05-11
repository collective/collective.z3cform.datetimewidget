#-*- coding: utf-8 -*- 

#############################################################################
#                                                                           #
#   Copyright (c) 2008 Rok Garbas <rok.garbas@gmail.com>                    #
#                                                                           #
# This program is free software; you can redistribute it and/or modify      #
# it under the terms of the GNU General Public License as published by      #
# the Free Software Foundation; either version 3 of the License, or         #
# (at your option) any later version.                                       #
#                                                                           #
# This program is distributed in the hope that it will be useful,           #
# but WITHOUT ANY WARRANTY; without even the implied warranty of            #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the             #
# GNU General Public License for more details.                              #
#                                                                           #
# You should have received a copy of the GNU General Public License         #
# along with this program.  If not, see <http://www.gnu.org/licenses/>.     #
#                                                                           #
#############################################################################
__docformat__ = "reStructuredText"

import zope.component
import zope.interface
import zope.schema
import z3c.form.widget
import z3c.form.browser.widget

from collective.z3cform.datetimewidget.interfaces import IDateWidget
from collective.z3cform.datetimewidget.interfaces import IDatetimeWidget


class DateWidget(z3c.form.browser.widget.HTMLTextInputWidget,
                 z3c.form.widget.Widget):
    """ Date widget. """

    zope.interface.implementsOnly(IDateWidget)

    klass = u'date-widget'
    value = None

    def update(self):
        super(DateWidget, self).update()
        z3c.form.browser.widget.addFieldClass(self)

    def months(self):
        monthNames = self.request.locale.dates.calendars['gregorian'].getMonthNames()

        try:
            selected = self.value.month
        except AttributeError:
            selected = -1

        for i, month in enumerate(monthNames):
            # TODO :: check if month was selected
            yield dict(
                content  = month,
                value    = i+1,
                selected = (i+1 == selected),
                )
    
    @property
    def formatted_value(self):
        formatter = self.request.locale.dates.getFormatter("date", "short")
        return formatter.format(self.value)

@zope.component.adapter(zope.schema.interfaces.IField, z3c.form.interfaces.IFormLayer)
@zope.interface.implementer(z3c.form.interfaces.IFieldWidget)
def DateFieldWidget(field, request):
    """IFieldWidget factory for DateWidget."""
    return z3c.form.widget.FieldWidget(field, DateWidget(request))


class DatetimeWidget(DateWidget):
    """ DateTime widget """

    zope.interface.implementsOnly(IDatetimeWidget)

    klass = u'datetime-widget'
    value = None

    def update(self):
        super(DatetimeWidget, self).update()
        z3c.form.browser.widget.addFieldClass(self)

    @property
    def formatted_value(self):
        formatter = self.request.locale.dates.getFormatter("dateTime", "short")
        return formatter.format(self.value)

    def _padded_value(self, value):
        value = unicode(value)
        if len(value) == 1:
            value = u'0' + value
        return value
    
    def padded_hour(self):
        try:
            hour = self.value.hour
        except AttributeError:
            hour = 0
        return self._padded_value(hour)

    def padded_minute(self):
        try:
            minute = self.value.minute
        except AttributeError:
            minute = 0
        return self._padded_value(minute)

@zope.component.adapter(zope.schema.interfaces.IField, z3c.form.interfaces.IFormLayer)
@zope.interface.implementer(z3c.form.interfaces.IFieldWidget)
def DatetimeFieldWidget(field, request):
    """IFieldWidget factory for DatetimeWidget."""
    return z3c.form.widget.FieldWidget(field, DatetimeWidget(request))


#class DateDeltaWidget():
#class DatetimeDeltaWidget():


