
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

import HumanTime

class HumanTimeTest(unittest.TestCase):
	"""
	Tests for functions in the HumanTime module.
	"""

	def test_tokenize_empty(self):
		self.assertEqual(HumanTime.tokenize(''), [])
		self.assertEqual(HumanTime.tokenize('     '), [])

	def test_tokenize_single(self):
		self.assertEqual(HumanTime.tokenize('now'), ['now'])
		self.assertEqual(HumanTime.tokenize('now   '), ['now'])
		self.assertEqual(HumanTime.tokenize('    now'), ['now'])
		self.assertEqual(HumanTime.tokenize('  now  '), ['now'])

	def test_tokenize(self):
		self.assertEqual(HumanTime.tokenize('3 hours from now'), ['3', 'hours', 'from', 'now'])

	def test_parseCardinal(self):
		self.assertEqual(HumanTime.parseCardinal('one'), 1)
		self.assertEqual(HumanTime.parseCardinal('two'), 2)
		self.assertEqual(HumanTime.parseCardinal('three'), 3)
		self.assertEqual(HumanTime.parseCardinal('four'), 4)
		self.assertEqual(HumanTime.parseCardinal('five'), 5)
		self.assertEqual(HumanTime.parseCardinal('six'), 6)
		self.assertEqual(HumanTime.parseCardinal('seven'), 7)
		self.assertEqual(HumanTime.parseCardinal('eight'), 8)
		self.assertEqual(HumanTime.parseCardinal('nine'), 9)
		self.assertEqual(HumanTime.parseCardinal('ten'), 10)
		self.assertEqual(HumanTime.parseCardinal('eleven'), 11)
		self.assertEqual(HumanTime.parseCardinal('twelve'), 12)

	def test_parseOrdinal(self):
		self.assertEqual(HumanTime.parseOrdinal('1st'), 1)
		self.assertEqual(HumanTime.parseOrdinal('second'), 2)
		self.assertEqual(HumanTime.parseOrdinal('3rd'), 3)
		self.assertEqual(HumanTime.parseOrdinal('fourth'), 4)
		self.assertEqual(HumanTime.parseOrdinal('5th'), 5)
		self.assertEqual(HumanTime.parseOrdinal('6th'), 6)
		self.assertEqual(HumanTime.parseOrdinal('seventh'), 7)
		self.assertEqual(HumanTime.parseOrdinal('eighth'), 8)
		self.assertEqual(HumanTime.parseOrdinal('ninth'), 9)
		self.assertEqual(HumanTime.parseOrdinal('10th'), 10)
		self.assertEqual(HumanTime.parseOrdinal('11th'), 11)
		self.assertEqual(HumanTime.parseOrdinal('12th'), 12)

	def test_parseNumber(self):
		self.assertEqual(HumanTime.parseNumber('one'), 1)
		self.assertEqual(HumanTime.parseNumber('two'), 2)
		self.assertEqual(HumanTime.parseNumber('three'), 3)
		self.assertEqual(HumanTime.parseNumber('four'), 4)
		self.assertEqual(HumanTime.parseNumber('5th'), 5)
		self.assertEqual(HumanTime.parseNumber('6th'), 6)
		self.assertEqual(HumanTime.parseNumber('seventh'), 7)
		self.assertEqual(HumanTime.parseNumber('eighth'), 8)
		self.assertEqual(HumanTime.parseNumber('ninth'), 9)
		self.assertEqual(HumanTime.parseNumber('10'), 10)
		self.assertEqual(HumanTime.parseNumber('11'), 11)
		self.assertEqual(HumanTime.parseNumber('12'), 12)

	def test_parseDuration_empty(self):
		with self.assertRaises(ValueError):
			HumanTime.parseDuration('')

	def test_parseDuration(self):
		self.assertEqual(HumanTime.parseDuration('second'), datetime.timedelta(seconds=1))
		self.assertEqual(HumanTime.parseDuration('week'), datetime.timedelta(days=7))

		self.assertEqual(HumanTime.parseDuration('3 minutes'), datetime.timedelta(seconds=180))
		self.assertEqual(HumanTime.parseDuration('180 seconds'), datetime.timedelta(seconds=180))

		self.assertEqual(HumanTime.parseDuration('3 days'), datetime.timedelta(days=3))
		self.assertEqual(HumanTime.parseDuration('72 hours'), datetime.timedelta(days=3))

	def test_parseDuration_cardinals(self):
		self.assertEqual(HumanTime.parseDuration('three seconds'), datetime.timedelta(seconds=3))
		self.assertEqual(HumanTime.parseDuration('ten days'), datetime.timedelta(days=10))

	def test_paseTimeOfDay(self):
		self.assertEqual(HumanTime.parseTimeOfDay('1:30'), datetime.time(1, 30))
		self.assertEqual(HumanTime.parseTimeOfDay('1:30PM'), datetime.time(13, 30))
		self.assertEqual(HumanTime.parseTimeOfDay('2:30:13'), datetime.time(2, 30, 13))

	def test_paseTimestamp(self):
		self.assertEqual(HumanTime.parseTimestamp('2019-04-02'), datetime.datetime(2019, 4, 2))
		self.assertEqual(HumanTime.parseTimestamp('2016-06-03'), datetime.datetime(2016, 6, 3))

	def test_now(self):
		t1 = datetime.datetime.now()
		now = HumanTime.now()
		t2 = datetime.datetime.now()

		self.assertLessEqual(t1, now)
		self.assertLessEqual(now, t2)

		nowT2 = HumanTime.now(t=t2)
		nowT1 = HumanTime.now(t=t1)
		self.assertEqual(t1, nowT1)
		self.assertEqual(t2, nowT2)

	def test_noon(self):
		noon = HumanTime.noon()
		self.assertEqual(noon.hour, 12)
		self.assertEqual(noon.minute, 0)
		self.assertEqual(noon.second, 0)
		self.assertEqual(noon.microsecond, 0)

	def test_today(self):
		today = HumanTime.today()
		self.assertEqual(today.hour, 0)
		self.assertEqual(today.minute, 0)
		self.assertEqual(today.second, 0)
		self.assertEqual(today.microsecond, 0)

	def test_tomorrow(self):
		tomorrow = HumanTime.tomorrow()
		self.assertEqual(tomorrow.hour, 0)
		self.assertEqual(tomorrow.minute, 0)
		self.assertEqual(tomorrow.second, 0)
		self.assertEqual(tomorrow.microsecond, 0)

	def test_yesterday(self):
		yesterday = HumanTime.yesterday()
		self.assertEqual(yesterday.hour, 0)
		self.assertEqual(yesterday.minute, 0)
		self.assertEqual(yesterday.second, 0)
		self.assertEqual(yesterday.microsecond, 0)

	def test_dayOfWeekOnOrAfter(self):
		self.assertEqual(HumanTime.dayOfWeekOnOrAfter(datetime.datetime(2019, 5, 5), HumanTime.SUNDAY), datetime.datetime(2019, 5, 5))
		self.assertEqual(HumanTime.dayOfWeekOnOrAfter(datetime.datetime(2019, 5, 5), HumanTime.MONDAY), datetime.datetime(2019, 5, 6))

		self.assertEqual(HumanTime.dayOfWeekOnOrAfter(datetime.datetime(2019, 5, 6), HumanTime.SUNDAY), datetime.datetime(2019, 5, 12))
		self.assertEqual(HumanTime.dayOfWeekOnOrAfter(datetime.datetime(2019, 5, 6), HumanTime.MONDAY), datetime.datetime(2019, 5, 6))

	def test_dayOfWeekOnOrBefore(self):
		self.assertEqual(HumanTime.dayOfWeekOnOrBefore(datetime.datetime(2019, 5, 6), HumanTime.SUNDAY), datetime.datetime(2019, 5, 5))
		self.assertEqual(HumanTime.dayOfWeekOnOrBefore(datetime.datetime(2019, 5, 6), HumanTime.MONDAY), datetime.datetime(2019, 5, 6))

	def test_monthOnOrAfter(self):
		self.assertEqual(HumanTime.monthOnOrAfter(datetime.datetime(2019, 5, 6), 4), datetime.datetime(2020, 4, 1))
		self.assertEqual(HumanTime.monthOnOrAfter(datetime.datetime(2019, 5, 6), 5), datetime.datetime(2019, 5, 1))
		self.assertEqual(HumanTime.monthOnOrAfter(datetime.datetime(2019, 5, 6), 6), datetime.datetime(2019, 6, 1))

	def test_monthOnOrBefore(self):
		self.assertEqual(HumanTime.monthOnOrBefore(datetime.datetime(2019, 5, 6), 4), datetime.datetime(2019, 4, 1))
		self.assertEqual(HumanTime.monthOnOrBefore(datetime.datetime(2019, 5, 6), 5), datetime.datetime(2019, 5, 1))
		self.assertEqual(HumanTime.monthOnOrBefore(datetime.datetime(2019, 5, 6), 6), datetime.datetime(2018, 6, 1))

	def test_parseTime_empty(self):
		with self.assertRaises(ValueError):
			HumanTime.parseTime('')

	def test_parseTime_invalid(self):
		with self.assertRaises(ValueError):
			HumanTime.parseTime('asdf')
		with self.assertRaises(ValueError):
			HumanTime.parseTime('1 year asdf now')
		with self.assertRaises(ValueError):
			HumanTime.parseTime('now now')
		with self.assertRaises(ValueError):
			HumanTime.parseTime('after now')
		with self.assertRaises(ValueError):
			HumanTime.parseTime('1 after now')

	def test_parseTime(self):
		t1 = datetime.datetime.now()
		now = HumanTime.parseTime('now')
		t2 = datetime.datetime.now()

		self.assertLessEqual(t1, now)
		self.assertLessEqual(now, t2)

	def test_parseTime_offsets(self):
		#Basic month, year offsets
		self.assertEqual(HumanTime.parseTime('1 year after 2019-2-1'), datetime.datetime(2020, 2, 1))
		self.assertEqual(HumanTime.parseTime('12 months after 2019-2-1'), datetime.datetime(2020, 2, 1))

		self.assertEqual(HumanTime.parseTime('1 year before 2020-2-28'), datetime.datetime(2019, 2, 28))
		self.assertEqual(HumanTime.parseTime('1 year after 2020-2-28'), datetime.datetime(2021, 2, 28))
		self.assertEqual(HumanTime.parseTime('12 months after 2020-2-28'), datetime.datetime(2021, 2, 28))

	def test_parseTime_cardinalOffsets(self):
		#Basic month, year offsets
		self.assertEqual(HumanTime.parseTime('an hour after 2019-2-1'), datetime.datetime(2019, 2, 1, 1))
		self.assertEqual(HumanTime.parseTime('one year after 2019-2-1'), datetime.datetime(2020, 2, 1))
		self.assertEqual(HumanTime.parseTime('twelve months after 2019-2-1'), datetime.datetime(2020, 2, 1))

		self.assertEqual(HumanTime.parseTime('the year before 2020-2-28'), datetime.datetime(2019, 2, 28))
		self.assertEqual(HumanTime.parseTime('a year after 2020-2-28'), datetime.datetime(2021, 2, 28))
		self.assertEqual(HumanTime.parseTime('twelve months after 2020-2-28'), datetime.datetime(2021, 2, 28))

	def test_parseTime_ordinalOffsets(self):
		self.assertEqual(HumanTime.parseTime('first hour after 2019-2-1'), datetime.datetime(2019, 2, 1, 1))
		self.assertEqual(HumanTime.parseTime('second second after 2019-2-1'), datetime.datetime(2019, 2, 1, 0, 0, 2))
		self.assertEqual(HumanTime.parseTime('3rd month after 2018-1-31'), datetime.datetime(2018, 4, 30))

	def test_parseTime_maxDayOfMonth(self):
		#Max day of month
		self.assertEqual(HumanTime.parseTime('1 month before 2018-1-31'), datetime.datetime(2017, 12, 31))
		self.assertEqual(HumanTime.parseTime('1 month after 2018-1-31'), datetime.datetime(2018, 2, 28))
		self.assertEqual(HumanTime.parseTime('2 months after 2018-1-31'), datetime.datetime(2018, 3, 31))
		self.assertEqual(HumanTime.parseTime('3 months after 2018-1-31'), datetime.datetime(2018, 4, 30))
		self.assertEqual(HumanTime.parseTime('4 months after 2018-1-31'), datetime.datetime(2018, 5, 31))

	def test_parseTime_feb29(self):
		#Special handling for 2-29
		self.assertEqual(HumanTime.parseTime('1 month after 2020-1-31'), datetime.datetime(2020, 2, 29))
		self.assertEqual(HumanTime.parseTime('1 year before 2020-2-29'), datetime.datetime(2019, 2, 28))
		self.assertEqual(HumanTime.parseTime('1 year after 2020-2-29'), datetime.datetime(2021, 2, 28))
		self.assertEqual(HumanTime.parseTime('12 months after 2020-2-29'), datetime.datetime(2021, 2, 28))
		self.assertEqual(HumanTime.parseTime('4 years after 2020-2-29'), datetime.datetime(2024, 2, 29))
		self.assertEqual(HumanTime.parseTime('48 months after 2020-2-29'), datetime.datetime(2024, 2, 29))

	def test_parseTime_weekdays_sunday(self):
		d = HumanTime.parseTime('Sun')
		self.assertEqual(d.weekday(), HumanTime.SUNDAY)

	def test_parseTime_weekdays_monday(self):
		d = HumanTime.parseTime('Monday')
		self.assertEqual(d.weekday(), HumanTime.MONDAY)

	def test_parseTime_weekdays_tuesday(self):
		d = HumanTime.parseTime('Tues')
		self.assertEqual(d.weekday(), HumanTime.TUESDAY)

	def test_parseTime_weekdays_friday(self):
		d = HumanTime.parseTime('fri')
		self.assertEqual(d.weekday(), HumanTime.FRIDAY)

	def test_parseTime_months_january(self):
		d = HumanTime.parseTime('jan')
		self.assertEqual(d.month, 1)

	def test_parseTime_months_february(self):
		d = HumanTime.parseTime('February')
		self.assertEqual(d.month, 2)

	def test_parseTime_months_may(self):
		d = HumanTime.parseTime('may')
		self.assertEqual(d.month, 5)

	def test_parseTime_weekdayOffsets(self):
		monday = HumanTime.parseTime('Monday after 2019-5-5')
		self.assertEqual(monday, datetime.datetime(2019, 5, 6))

		monday = HumanTime.parseTime('Monday after 2019-5-6')
		self.assertEqual(monday, datetime.datetime(2019, 5, 13))

		monday = HumanTime.parseTime('2 Mondays after 2019-5-5')
		self.assertEqual(monday, datetime.datetime(2019, 5, 13))

		monday = HumanTime.parseTime('2 Mon after 2019-5-6')
		self.assertEqual(monday, datetime.datetime(2019, 5, 20))

		tuesday = HumanTime.parseTime('Tuesday before 2019-5-5')
		self.assertEqual(tuesday, datetime.datetime(2019, 4, 30))

		monday = HumanTime.parseTime('Monday before 2019-5-6')
		self.assertEqual(monday, datetime.datetime(2019, 4, 29))

		monday = HumanTime.parseTime('3 Mondays before 2019-5-6')
		self.assertEqual(monday, datetime.datetime(2019, 4, 15))

		monday = HumanTime.parseTime('the third Monday before 2019-5-6')
		self.assertEqual(monday, datetime.datetime(2019, 4, 15))

		monday = HumanTime.parseTime('Monday before 2019-5-7')
		self.assertEqual(monday, datetime.datetime(2019, 5, 6))

	def test_parseTime_monthOffsets(self):
		self.assertEqual(HumanTime.parseTime('January after 2019-5-5'), datetime.datetime(2020, 1, 1))
		self.assertEqual(HumanTime.parseTime('May after 2019-5-6'), datetime.datetime(2020, 5, 1))
		self.assertEqual(HumanTime.parseTime('May before 2019-5-6'), datetime.datetime(2018, 5, 1))

	def test_parseTime_weekdayOffsets(self):
		t = datetime.datetime(2019, 5, 11, 13, 30)
		self.assertEqual(HumanTime.parseTime('5th weekday before now', t=t), datetime.datetime(2019, 5, 6))
		self.assertEqual(HumanTime.parseTime('6 weekdays before now', t=t), datetime.datetime(2019, 5, 3))
		self.assertEqual(HumanTime.parseTime('5th weekday after now', t=t), datetime.datetime(2019, 5, 17))
		self.assertEqual(HumanTime.parseTime('6 weekdays after now', t=t), datetime.datetime(2019, 5, 20))

	def test_parseTime_ago(self):
		t = datetime.datetime(2019, 5, 6, 13, 30)
		self.assertEqual(HumanTime.parseTime('ten minutes ago', t=t), datetime.datetime(2019, 5, 6, 13, 20))
		self.assertEqual(HumanTime.parseTime('30 minutes ago', t=t), datetime.datetime(2019, 5, 6, 13, 0))
		self.assertEqual(HumanTime.parseTime('a day ago', t=t), datetime.datetime(2019, 5, 5, 13, 30))
		self.assertEqual(HumanTime.parseTime('2 months ago', t=t), datetime.datetime(2019, 3, 6, 13, 30))
		self.assertEqual(HumanTime.parseTime('three years ago', t=t), datetime.datetime(2016, 5, 6, 13, 30))

	def test_parseTime_nextLast_weekday(self):
		t = datetime.datetime(2019, 5, 8, 13, 30)

		#Most days of the week result in only two (2) distinct dates...
		self.assertEqual(HumanTime.parseTime('last Monday', t=t), datetime.datetime(2019, 5, 6))
		self.assertEqual(HumanTime.parseTime('Monday', t=t), datetime.datetime(2019, 5, 13))
		self.assertEqual(HumanTime.parseTime('next Monday', t=t), datetime.datetime(2019, 5, 13))

		#But the current day of the week makes three (3)
		self.assertEqual(HumanTime.parseTime('last Weds', t=t), datetime.datetime(2019, 5, 1))
		self.assertEqual(HumanTime.parseTime('Weds', t=t), datetime.datetime(2019, 5, 8))
		self.assertEqual(HumanTime.parseTime('next Weds', t=t), datetime.datetime(2019, 5, 15))

	def test_parseTime_nextLast_weekday_atTime(self):
		t = datetime.datetime(2019, 5, 8, 13, 30)

		#Most days of the week result in only two (2) distinct dates...
		self.assertEqual(HumanTime.parseTime('last Monday at noon', t=t), datetime.datetime(2019, 5, 6, 12))
		self.assertEqual(HumanTime.parseTime('last Monday at 3PM', t=t), datetime.datetime(2019, 5, 6, 15))
		self.assertEqual(HumanTime.parseTime('Monday at 7', t=t), datetime.datetime(2019, 5, 13, 7))
		self.assertEqual(HumanTime.parseTime('next Monday at 12:30:01', t=t), datetime.datetime(2019, 5, 13, 12, 30, 1))

	def test_parseTime_nextLast_month(self):
		t = datetime.datetime(2019, 5, 8, 13, 30)

		#Most days of the week result in only two (2) distinct dates...
		self.assertEqual(HumanTime.parseTime('last May', t=t), datetime.datetime(2018, 5, 1))
		self.assertEqual(HumanTime.parseTime('May', t=t), datetime.datetime(2019, 5, 1))
		self.assertEqual(HumanTime.parseTime('next May', t=t), datetime.datetime(2020, 5, 1))

	def test_parseTime_nextLast_weekday(self):
		t = datetime.datetime(2019, 5, 11, 13, 30)
		self.assertEqual(HumanTime.parseTime('last weekday', t=t), datetime.datetime(2019, 5, 10))
		self.assertEqual(HumanTime.parseTime('next weekday', t=t), datetime.datetime(2019, 5, 13))
