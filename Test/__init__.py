
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

	def test_paseTimestamp(self):
		self.assertEqual(HumanTime.parseTimestamp('2019-04-02'), datetime.datetime(2019, 4, 2))

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
		sunday = HumanTime.parseTime('Sun')
		self.assertEqual(sunday.weekday(), HumanTime.SUNDAY)

	def test_parseTime_weekdays_monday(self):
		monday = HumanTime.parseTime('Monday')
		self.assertEqual(monday.weekday(), HumanTime.MONDAY)

	def test_parseTime_weekdays_tuesday(self):
		tuesday = HumanTime.parseTime('Tues')
		self.assertEqual(tuesday.weekday(), HumanTime.TUESDAY)

	def test_parseTime_weekdays_friday(self):
		tuesday = HumanTime.parseTime('fri')
		self.assertEqual(tuesday.weekday(), HumanTime.FRIDAY)

	def test_parseTime_weekdayOffsets(self):
		monday = HumanTime.parseTime('Monday after 2019-5-5')
		self.assertEqual(monday, datetime.datetime(2019, 5, 6))

		monday = HumanTime.parseTime('Monday after 2019-5-6')
		self.assertEqual(monday, datetime.datetime(2019, 5, 13))

		monday = HumanTime.parseTime('Monday before 2019-5-5')
		self.assertEqual(monday, datetime.datetime(2019, 4, 29))

		monday = HumanTime.parseTime('Monday before 2019-5-6')
		self.assertEqual(monday, datetime.datetime(2019, 4, 29))

		monday = HumanTime.parseTime('Monday before 2019-5-7')
		self.assertEqual(monday, datetime.datetime(2019, 5, 6))
