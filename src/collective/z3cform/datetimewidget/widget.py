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

from datetime import date, datetime

import zope.component
import zope.interface
import zope.schema
import z3c.form.widget
import z3c.form.browser.widget
from z3c.form import interfaces
from collective.z3cform.datetimewidget.interfaces import IDateWidget, IDatetimeWidget

class DateWidget(z3c.form.browser.widget.HTMLTextInputWidget,
                 z3c.form.widget.Widget):
    """ Date widget. """

    zope.interface.implementsOnly(IDateWidget)

    klass = u'date-widget'
    value = ('', '', '')

    def update(self):
        super(DateWidget, self).update()
        z3c.form.browser.widget.addFieldClass(self)

    def months(self):
        monthNames = self.request.locale.dates.calendars['gregorian'].getMonthNames()

        try:
            selected = int(self.month)
        except:
            selected = -1

        for i, month in enumerate(monthNames):
            yield dict(
                content  = month,
                value    = i+1,
                selected = (i+1 == selected),
                )
    
    @property
    def formatted_value(self):
        if self.value == ('', '', ''):
            return ''
        formatter = self.request.locale.dates.getFormatter("date", "short")
        return formatter.format(date(*self.value))
    
    @property
    def year(self):
        return self.value[0]
    
    @property
    def month(self):
        return self.value[1]
    
    @property
    def day(self):
        return self.value[2]
    
    def extract(self, default=interfaces.NOVALUE):
        day = self.request.get(self.name + '-day', default)
        month = self.request.get(self.name + '-month', default)
        year = self.request.get(self.name + '-year', default)
        if default in (year, month, day):
            return default
        return (year, month, day)

@zope.component.adapter(zope.schema.interfaces.IField, z3c.form.interfaces.IFormLayer)
@zope.interface.implementer(z3c.form.interfaces.IFieldWidget)
def DateFieldWidget(field, request):
    """IFieldWidget factory for DateWidget."""
    return z3c.form.widget.FieldWidget(field, DateWidget(request))


class DatetimeWidget(DateWidget):
    """ DateTime widget """

    zope.interface.implementsOnly(IDatetimeWidget)

    klass = u'datetime-widget'
    value = ('', '', '', '00', '00')
    ampm  = False

    @property
    def formatted_value(self):
        if self.value == ('', '', '', '00', '00'):
            return ''
        formatter = self.request.locale.dates.getFormatter("dateTime", "short")
        return formatter.format(datetime(*self.value))

    @property
    def hour(self):
        return self.value[3]

    @property
    def minute(self):
        return self.value[4]

    def _padded_value(self, value):
        value = unicode(value)
        if value and len(value) == 1:
            value = u'0' + value
        return value

    def is_pm(self):
        if int(self.hour) >= 12:
            return True
        return False

    def padded_hour(self):
        hour = self.hour
        if self.ampm is True and self.is_pm() and int(hour)!=12:
            hour = str(int(hour)-12)
        return self._padded_value(hour)

    def padded_minute(self):
        return self._padded_value(self.minute)

    def extract(self, default=interfaces.NOVALUE):
        day = self.request.get(self.name + '-day', default)
        month = self.request.get(self.name + '-month', default)
        year = self.request.get(self.name + '-year', default)
        hour = self.request.get(self.name + '-hour', default)
        minute = self.request.get(self.name + '-min', default)

        if default in (year, month, day, hour, minute):
            return default

        if self.ampm is True and int(hour)!=12:
            ampm = self.request.get(self.name + '-ampm', default)
            if ampm == 'PM':
                hour = str(12+int(hour))
            # something strange happened since we either
            # should have 'PM' or 'AM', return default
            elif ampm != 'AM':
                return default

        return (year, month, day, hour, minute)

@zope.component.adapter(zope.schema.interfaces.IField, z3c.form.interfaces.IFormLayer)
@zope.interface.implementer(z3c.form.interfaces.IFieldWidget)
def DatetimeFieldWidget(field, request):
    """IFieldWidget factory for DatetimeWidget."""
    return z3c.form.widget.FieldWidget(field, DatetimeWidget(request))


#class DateDeltaWidget():
#class DatetimeDeltaWidget():


