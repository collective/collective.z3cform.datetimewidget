#-*- coding: utf-8 -*- 

#############################################################################
#                                                                           #
#   Copyright (c) 2008 Rok Garbas <rok@garbas.si>                           #
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

import zope.i18n
import zope.schema
import zope.interface
import zope.component
import z3c.form
import z3c.form.browser.widget
import z3c.form.widget
from datetime import date, datetime
from interfaces import IDateWidget
from i18n import MessageFactory as _


class DateWidget(z3c.form.browser.widget.HTMLTextInputWidget,
                 z3c.form.widget.Widget):
    """ Date widget. """

    zope.interface.implementsOnly(IDateWidget)

    klass = u'date-widget'
    show_today_link = False
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
                name     = month,
                value    = i+1,
                selected = i+1 == selected)
    
    @property
    def formatted_value(self):
        if self.value == ('', '', ''):
            return ''
        formatter = self.request.locale.dates.getFormatter("date", "short")
        date_value = date(*map(int, self.value))
        if date_value.year > 1900:
            return formatter.format(date_value)
        # due to fantastic datetime.strftime we need this hack
        # for now ctime is default
        return date_value.ctime()

    @property
    def year(self):
        year = self.request.get(self.name+'-year', None)
        if year:
            return year
        return self.value[0]
    
    @property
    def month(self):
        month = self.request.get(self.name+'-month', None)
        if month:
            return month
        return self.value[1]
    
    @property
    def day(self):
        day = self.request.get(self.name+'-day', None)
        if day:
            return day
        return self.value[2]
    
    def extract(self, default=z3c.form.interfaces.NOVALUE):
        # get normal input fields
        day = self.request.get(self.name + '-day', default)
        month = self.request.get(self.name + '-month', default)
        year = self.request.get(self.name + '-year', default)

        if not default in (year, month, day):
            return (year, month, day)

        # get a hidden value
        formatter = self.request.locale.dates.getFormatter("date", "short")
        hidden_date = self.request.get(self.name, '')
        try:
            dateobj = formatter.parse(hidden_date)
            return (str(dateobj.year),
                    str(dateobj.month),
                    str(dateobj.day))
        except zope.i18n.format.DateTimeParseError:
            pass
        
        return default

    def show_today_link_js(self):
        now = datetime.today()
        show_link_func = self.id+'-show-today-link'
        for i in ['-', '_']:
            show_link_func = show_link_func.replace(i, '')
        return '''
            <a href="#" onclick="return %(show_link_func)s()">%(today)s</a>
            <script type="text/javascript">
                var %(show_link_func)s = function() {
                    document.getElementById('%(id)s-day').value = %(day)s;
                    document.getElementById('%(id)s-month').value = %(month)s;
                    document.getElementById('%(id)s-year').value = %(year)s;
                    return false;
                }</script>''' % dict(
                    id = self.id, show_link_func = show_link_func,
                    day = now.day, month = now.month, year = now.year,
                    today = zope.i18n.translate(_(u"Today"), context=self.request))


@zope.component.adapter(zope.schema.interfaces.IField, z3c.form.interfaces.IFormLayer)
@zope.interface.implementer(z3c.form.interfaces.IFieldWidget)
def DateFieldWidget(field, request):
    """IFieldWidget factory for DateWidget."""
    return z3c.form.widget.FieldWidget(field, DateWidget(request))


