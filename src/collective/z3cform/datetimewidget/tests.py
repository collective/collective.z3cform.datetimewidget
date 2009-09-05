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
__docformat__ = "reStructuredText"

import unittest
from zope.app.testing import setup
from zope.testing import doctest
from z3c.form import testing


def setUp(test):
    test.globs = {'root': setup.placefulSetUp(True)}

def tearDown(test):
    setup.placefulTearDown()


def test_suite():
    return unittest.TestSuite((
        doctest.DocFileSuite('widget_date.txt',
            setUp=setUp, tearDown=tearDown,
            optionflags=doctest.REPORT_ONLY_FIRST_FAILURE |
                        doctest.NORMALIZE_WHITESPACE |
                        doctest.ELLIPSIS |
                        doctest.REPORT_UDIFF,
            ),
        doctest.DocFileSuite('widget_datetime.txt',
            setUp=setUp, tearDown=tearDown,
            optionflags=doctest.REPORT_ONLY_FIRST_FAILURE |
                        doctest.NORMALIZE_WHITESPACE |
                        doctest.ELLIPSIS |
                        doctest.REPORT_UDIFF,
            ),
        doctest.DocFileSuite('widget_monthyear.txt',
            setUp=setUp, tearDown=tearDown,
            optionflags=doctest.REPORT_ONLY_FIRST_FAILURE |
                        doctest.NORMALIZE_WHITESPACE |
                        doctest.ELLIPSIS |
                        doctest.REPORT_UDIFF,
            ),
        doctest.DocFileSuite('converter.txt',
            setUp=setUp, tearDown=tearDown,
            optionflags=doctest.REPORT_ONLY_FIRST_FAILURE |
                        doctest.NORMALIZE_WHITESPACE |
                        doctest.ELLIPSIS |
                        doctest.REPORT_UDIFF,
            ),
        doctest.DocFileSuite('issues.txt',
            setUp=testing.setUp, tearDown=testing.tearDown,
            optionflags=doctest.REPORT_ONLY_FIRST_FAILURE |
                        doctest.NORMALIZE_WHITESPACE |
                        doctest.ELLIPSIS |
                        doctest.REPORT_UDIFF,
            ),
        ))

