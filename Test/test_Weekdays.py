
# Copyright (c) 2019 Agalmic Ventures LLC (www.agalmicventures.com)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import datetime
import unittest

from HumanTime import Weekdays

class WeekdaysTest(unittest.TestCase):
	"""
	Tests for functions in the Weekdays module.
	"""

	def test_dayOfWeekOnOrAfter(self):
		self.assertEqual(Weekdays.dayOfWeekOnOrAfter(datetime.datetime(2019, 5, 5), Weekdays.SUNDAY), datetime.datetime(2019, 5, 5))
		self.assertEqual(Weekdays.dayOfWeekOnOrAfter(datetime.datetime(2019, 5, 5), Weekdays.MONDAY), datetime.datetime(2019, 5, 6))

		self.assertEqual(Weekdays.dayOfWeekOnOrAfter(datetime.datetime(2019, 5, 6), Weekdays.SUNDAY), datetime.datetime(2019, 5, 12))
		self.assertEqual(Weekdays.dayOfWeekOnOrAfter(datetime.datetime(2019, 5, 6), Weekdays.MONDAY), datetime.datetime(2019, 5, 6))

	def test_dayOfWeekOnOrBefore(self):
		self.assertEqual(Weekdays.dayOfWeekOnOrBefore(datetime.datetime(2019, 5, 6), Weekdays.SUNDAY), datetime.datetime(2019, 5, 5))
		self.assertEqual(Weekdays.dayOfWeekOnOrBefore(datetime.datetime(2019, 5, 6), Weekdays.MONDAY), datetime.datetime(2019, 5, 6))
