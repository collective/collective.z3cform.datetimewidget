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

from z3c.form.interfaces import IWidget
from zope.schema import interfaces
from zope.schema import ValidationError
from collective.z3cform.datetimewidget.i18n import MessageFactory as _

class IDateField(interfaces.IDate):
    """ Special marker for date fields that use our widget """

class IDatetimeField(interfaces.IDatetime):
    """ Special marker for datetime fields that use our widget """

class IDateWidget(IWidget):
    """ Date widget marker for z3c.form """

class IDatetimeWidget(IWidget):
    """ Datetime widget marker for z3c.form """

class DateValidationError(ValidationError):
    __doc__ = _(u'Please enter a valid date.')

class DatetimeValidationError(ValidationError):
    __doc__ = _(u'Please enter a valid date and time.')
