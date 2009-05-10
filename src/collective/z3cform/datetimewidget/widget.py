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
    value = u''

    def update(self):
        super(DateWidget, self).update()
        z3c.form.browser.widget.addFieldClass(self)

    def months(self):
        # TODO :: check that months names are locales awared
        monthNames = ['January', 'February', 'March', 'April', 'May',
                      'June', 'July', 'August', 'September',
                      'October', 'November', 'December']

        for i in monthNames:
            # TODO :: check if month was selected
            yield dict(
                content  = i,
                value    = monthNames.index(i)+1,
                selected = False,)

@zope.component.adapter(zope.schema.interfaces.IField, z3c.form.interfaces.IFormLayer)
@zope.interface.implementer(z3c.form.interfaces.IFieldWidget)
def DateFieldWidget(field, request):
    """IFieldWidget factory for DateWidget."""
    return z3c.form.widget.FieldWidget(field, DateWidget(request))


class DatetimeWidget(DateWidget):
    """ DateTime widget """

    zope.interface.implementsOnly(IDatetimeWidget)

    klass = u'datetime-widget'
    value = u''

    def update(self):
        super(DatetimeWidget, self).update()
        z3c.form.browser.widget.addFieldClass(self)

@zope.component.adapter(zope.schema.interfaces.IField, z3c.form.interfaces.IFormLayer)
@zope.interface.implementer(z3c.form.interfaces.IFieldWidget)
def DatetimeFieldWidget(field, request):
    """IFieldWidget factory for DatetimeWidget."""
    return z3c.form.widget.FieldWidget(field, DatetimeWidget(request))


#class DateDeltaWidget():
#class DatetimeDeltaWidget():


