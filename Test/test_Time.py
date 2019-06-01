
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

from HumanTime import Time

class TimeTest(unittest.TestCase):
	"""
	Tests for functions in the Time module.
	"""

	def test_paseTimeOfDay(self):
		self.assertEqual(Time.parseTimeOfDay('1:30'), datetime.time(1, 30))
		self.assertEqual(Time.parseTimeOfDay('1:30PM'), datetime.time(13, 30))
		self.assertEqual(Time.parseTimeOfDay('2:30:13'), datetime.time(2, 30, 13))

	def test_paseTimestamp(self):
		self.assertEqual(Time.parseTimestamp('2019-04-02'), datetime.datetime(2019, 4, 2))
		self.assertEqual(Time.parseTimestamp('2016-06-03'), datetime.datetime(2016, 6, 3))

	def test_noon(self):
		noon = Time.noon()
		self.assertEqual(noon.hour, 12)
		self.assertEqual(noon.minute, 0)
		self.assertEqual(noon.second, 0)
		self.assertEqual(noon.microsecond, 0)

	def test_tomorrow(self):
		tomorrow = Time.tomorrow()
		self.assertEqual(tomorrow.hour, 0)
		self.assertEqual(tomorrow.minute, 0)
		self.assertEqual(tomorrow.second, 0)
		self.assertEqual(tomorrow.microsecond, 0)

	def test_yesterday(self):
		yesterday = Time.yesterday()
		self.assertEqual(yesterday.hour, 0)
		self.assertEqual(yesterday.minute, 0)
		self.assertEqual(yesterday.second, 0)
		self.assertEqual(yesterday.microsecond, 0)

	def test_monthOnOrAfter(self):
		self.assertEqual(Time.monthOnOrAfter(datetime.datetime(2019, 5, 6), 4), datetime.datetime(2020, 4, 1))
		self.assertEqual(Time.monthOnOrAfter(datetime.datetime(2019, 5, 6), 5), datetime.datetime(2019, 5, 1))
		self.assertEqual(Time.monthOnOrAfter(datetime.datetime(2019, 5, 6), 6), datetime.datetime(2019, 6, 1))

	def test_monthOnOrBefore(self):
		self.assertEqual(Time.monthOnOrBefore(datetime.datetime(2019, 5, 6), 4), datetime.datetime(2019, 4, 1))
		self.assertEqual(Time.monthOnOrBefore(datetime.datetime(2019, 5, 6), 5), datetime.datetime(2019, 5, 1))
		self.assertEqual(Time.monthOnOrBefore(datetime.datetime(2019, 5, 6), 6), datetime.datetime(2018, 6, 1))

	def test_parseTime_empty(self):
		with self.assertRaises(ValueError):
			Time.parseTime('')

	def test_parseTime_invalid(self):
		with self.assertRaises(ValueError):
			Time.parseTime('asdf')
		with self.assertRaises(ValueError):
			Time.parseTime('1 year asdf now')
		with self.assertRaises(ValueError):
			Time.parseTime('now now')
		with self.assertRaises(ValueError):
			Time.parseTime('after now')
		with self.assertRaises(ValueError):
			Time.parseTime('1 after now')

	def test_parseTime(self):
		t1 = datetime.datetime.now()
		now = Time.parseTime('now')
		t2 = datetime.datetime.now()

		self.assertLessEqual(t1, now)
		self.assertLessEqual(now, t2)

	def test_parseTime_offsets(self):
		self.assertEqual(Time.parseTime('1 year after 2019-2-1'), datetime.datetime(2020, 2, 1))
		self.assertEqual(Time.parseTime('12 months after 2019-2-1'), datetime.datetime(2020, 2, 1))

		self.assertEqual(Time.parseTime('1 year before 2020-2-28'), datetime.datetime(2019, 2, 28))
		self.assertEqual(Time.parseTime('1 year after 2020-2-28'), datetime.datetime(2021, 2, 28))
		self.assertEqual(Time.parseTime('12 months after 2020-2-28'), datetime.datetime(2021, 2, 28))

	def test_parseTime_offsetsInvalid(self):
		with self.assertRaises(ValueError):
			self.assertEqual(Time.parseTime('1 year after'), datetime.datetime(2020, 2, 1))
		with self.assertRaises(ValueError):
			self.assertEqual(Time.parseTime('12 months before'), datetime.datetime(2020, 2, 1))

	def test_parseTime_cardinalOffsets(self):
		self.assertEqual(Time.parseTime('an hour after 2019-2-1'), datetime.datetime(2019, 2, 1, 1))
		self.assertEqual(Time.parseTime('one year after 2019-2-1'), datetime.datetime(2020, 2, 1))
		self.assertEqual(Time.parseTime('twelve months after 2019-2-1'), datetime.datetime(2020, 2, 1))

		self.assertEqual(Time.parseTime('the year before 2020-2-28'), datetime.datetime(2019, 2, 28))
		self.assertEqual(Time.parseTime('a year after 2020-2-28'), datetime.datetime(2021, 2, 28))
		self.assertEqual(Time.parseTime('twelve months after 2020-2-28'), datetime.datetime(2021, 2, 28))

	def test_parseTime_ordinalOffsets(self):
		self.assertEqual(Time.parseTime('first hour after 2019-2-1'), datetime.datetime(2019, 2, 1, 1))
		self.assertEqual(Time.parseTime('second second after 2019-2-1'), datetime.datetime(2019, 2, 1, 0, 0, 2))
		self.assertEqual(Time.parseTime('3rd month after 2018-1-31'), datetime.datetime(2018, 4, 30))

	def test_parseTime_maxDayOfMonth(self):
		#Max day of month
		self.assertEqual(Time.parseTime('1 month before 2018-1-31'), datetime.datetime(2017, 12, 31))
		self.assertEqual(Time.parseTime('1 month after 2018-1-31'), datetime.datetime(2018, 2, 28))
		self.assertEqual(Time.parseTime('2 months after 2018-1-31'), datetime.datetime(2018, 3, 31))
		self.assertEqual(Time.parseTime('3 months after 2018-1-31'), datetime.datetime(2018, 4, 30))
		self.assertEqual(Time.parseTime('4 months after 2018-1-31'), datetime.datetime(2018, 5, 31))

	def test_parseTime_feb29(self):
		#Special handling for 2-29
		self.assertEqual(Time.parseTime('1 month after 2020-1-31'), datetime.datetime(2020, 2, 29))
		self.assertEqual(Time.parseTime('1 year before 2020-2-29'), datetime.datetime(2019, 2, 28))
		self.assertEqual(Time.parseTime('1 year after 2020-2-29'), datetime.datetime(2021, 2, 28))
		self.assertEqual(Time.parseTime('12 months after 2020-2-29'), datetime.datetime(2021, 2, 28))
		self.assertEqual(Time.parseTime('4 years after 2020-2-29'), datetime.datetime(2024, 2, 29))
		self.assertEqual(Time.parseTime('48 months after 2020-2-29'), datetime.datetime(2024, 2, 29))

	def test_parseTime_weekdays_sunday(self):
		d = Time.parseTime('Sun')
		self.assertEqual(d.weekday(), Time.SUNDAY)

	def test_parseTime_weekdays_monday(self):
		d = Time.parseTime('Monday')
		self.assertEqual(d.weekday(), Time.MONDAY)

	def test_parseTime_weekdays_tuesday(self):
		d = Time.parseTime('Tues')
		self.assertEqual(d.weekday(), Time.TUESDAY)

	def test_parseTime_weekdays_friday(self):
		d = Time.parseTime('fri')
		self.assertEqual(d.weekday(), Time.FRIDAY)

	def test_parseTime_months_january(self):
		d = Time.parseTime('jan')
		self.assertEqual(d.month, 1)

	def test_parseTime_months_february(self):
		d = Time.parseTime('February')
		self.assertEqual(d.month, 2)

	def test_parseTime_months_may(self):
		d = Time.parseTime('may')
		self.assertEqual(d.month, 5)

	def test_parseTime_weekdayOffsets(self):
		self.assertEqual(Time.parseTime('Monday after 2019-5-5'), datetime.datetime(2019, 5, 6))
		self.assertEqual(Time.parseTime('Monday after 2019-5-6'), datetime.datetime(2019, 5, 13))
		self.assertEqual(Time.parseTime('2 Mondays after 2019-5-5'), datetime.datetime(2019, 5, 13))
		self.assertEqual(Time.parseTime('2 Mon after 2019-5-6'), datetime.datetime(2019, 5, 20))
		self.assertEqual(Time.parseTime('Tuesday before 2019-5-5'), datetime.datetime(2019, 4, 30))
		self.assertEqual(Time.parseTime('Monday before 2019-5-6'), datetime.datetime(2019, 4, 29))
		self.assertEqual(Time.parseTime('3 Mondays before 2019-5-6'), datetime.datetime(2019, 4, 15))
		self.assertEqual(Time.parseTime('the third Monday before 2019-5-6'), datetime.datetime(2019, 4, 15))
		self.assertEqual(Time.parseTime('Monday before 2019-5-7'), datetime.datetime(2019, 5, 6))

	def test_parseTime_monthOffsets(self):
		self.assertEqual(Time.parseTime('January after 2019-5-5'), datetime.datetime(2020, 1, 1))
		self.assertEqual(Time.parseTime('May after 2019-5-6'), datetime.datetime(2020, 5, 1))
		self.assertEqual(Time.parseTime('May before 2019-5-6'), datetime.datetime(2018, 5, 1))

	def test_parseTime_weekdayOffsets(self):
		t = datetime.datetime(2019, 5, 11, 13, 30)
		self.assertEqual(Time.parseTime('5th weekday before now', t=t), datetime.datetime(2019, 5, 6))
		self.assertEqual(Time.parseTime('6 weekdays before now', t=t), datetime.datetime(2019, 5, 3))
		self.assertEqual(Time.parseTime('5th weekday after now', t=t), datetime.datetime(2019, 5, 17))
		self.assertEqual(Time.parseTime('6 weekdays after now', t=t), datetime.datetime(2019, 5, 20))

	def test_parseTime_calendarDayOffsets(self):
		self.assertEqual(Time.parseTime('calendar day after 2019-5-5'), datetime.datetime(2019, 5, 6))
		self.assertEqual(Time.parseTime('5 calendar days after 2019-5-5'), datetime.datetime(2019, 5, 10))

	def test_parseTime_businessDayOffsets(self):
		self.assertEqual(Time.parseTime('business day after 2019-7-3'), datetime.datetime(2019, 7, 5))
		self.assertEqual(Time.parseTime('couple business days after 2019-7-2'), datetime.datetime(2019, 7, 5))
		self.assertEqual(Time.parseTime('2 bus days after 2019-7-3'), datetime.datetime(2019, 7, 8))

		self.assertEqual(Time.parseTime('business day before 2019-7-3'), datetime.datetime(2019, 7, 2))
		self.assertEqual(Time.parseTime('business day before 2019-7-5'), datetime.datetime(2019, 7, 3))
		self.assertEqual(Time.parseTime('couple business days before 2019-7-5'), datetime.datetime(2019, 7, 2))
		self.assertEqual(Time.parseTime('2 bus days before 2019-7-8'), datetime.datetime(2019, 7, 3))

	def test_parseTime_ago(self):
		t = datetime.datetime(2019, 5, 6, 13, 30)
		self.assertEqual(Time.parseTime('ten minutes ago', t=t), datetime.datetime(2019, 5, 6, 13, 20))
		self.assertEqual(Time.parseTime('30 minutes ago', t=t), datetime.datetime(2019, 5, 6, 13, 0))
		self.assertEqual(Time.parseTime('a day ago', t=t), datetime.datetime(2019, 5, 5, 13, 30))
		self.assertEqual(Time.parseTime('2 months ago', t=t), datetime.datetime(2019, 3, 6, 13, 30))
		self.assertEqual(Time.parseTime('three years ago', t=t), datetime.datetime(2016, 5, 6, 13, 30))

	def test_parseTime_nextLast_weekday(self):
		t = datetime.datetime(2019, 5, 8, 13, 30)

		#Most days of the week result in only two (2) distinct dates...
		self.assertEqual(Time.parseTime('last Monday', t=t), datetime.datetime(2019, 5, 6))
		self.assertEqual(Time.parseTime('Monday', t=t), datetime.datetime(2019, 5, 13))
		self.assertEqual(Time.parseTime('next Monday', t=t), datetime.datetime(2019, 5, 13))

		#But the current day of the week makes three (3)
		self.assertEqual(Time.parseTime('last Weds', t=t), datetime.datetime(2019, 5, 1))
		self.assertEqual(Time.parseTime('Weds', t=t), datetime.datetime(2019, 5, 8))
		self.assertEqual(Time.parseTime('this Weds', t=t), datetime.datetime(2019, 5, 8))
		self.assertEqual(Time.parseTime('next Weds', t=t), datetime.datetime(2019, 5, 15))

	def test_parseTime_nextLast_weekday_atTime(self):
		t = datetime.datetime(2019, 5, 8, 13, 30)

		#Most days of the week result in only two (2) distinct dates...
		self.assertEqual(Time.parseTime('last Monday at noon', t=t), datetime.datetime(2019, 5, 6, 12))
		self.assertEqual(Time.parseTime('last Monday at 3PM', t=t), datetime.datetime(2019, 5, 6, 15))
		self.assertEqual(Time.parseTime('Monday at 7', t=t), datetime.datetime(2019, 5, 13, 7))
		self.assertEqual(Time.parseTime('this Monday at 7', t=t), datetime.datetime(2019, 5, 13, 7))
		self.assertEqual(Time.parseTime('next Monday at 12:30:01', t=t), datetime.datetime(2019, 5, 13, 12, 30, 1))

	def test_parseTime_nextLast_month(self):
		t = datetime.datetime(2019, 5, 8, 13, 30)

		#Most days of the week result in only two (2) distinct dates...
		self.assertEqual(Time.parseTime('last May', t=t), datetime.datetime(2018, 5, 1))
		self.assertEqual(Time.parseTime('May', t=t), datetime.datetime(2019, 5, 1))
		self.assertEqual(Time.parseTime('this May', t=t), datetime.datetime(2019, 5, 1))
		self.assertEqual(Time.parseTime('next May', t=t), datetime.datetime(2020, 5, 1))

	def test_parseTime_nextLast_weekday(self):
		t = datetime.datetime(2019, 5, 11, 13, 30)
		self.assertEqual(Time.parseTime('last weekday', t=t), datetime.datetime(2019, 5, 10))
		self.assertEqual(Time.parseTime('this weekday', t=t), datetime.datetime(2019, 5, 13))
		self.assertEqual(Time.parseTime('next weekday', t=t), datetime.datetime(2019, 5, 13))
