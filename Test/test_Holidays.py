
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

from HumanTime import Holidays, Weekdays

YEARS = range(1990, 2030)
GOOD_FRIDAYS = {
	2010: (4,  2),
	2011: (4, 22),
	2012: (4,  6),
	2013: (3, 29),
	2014: (4, 18),
	2015: (4,  3),
	2016: (3, 25),
	2017: (4, 14),
	2018: (3, 30),
	2019: (4, 19),
	2020: (4, 10),
	2021: (4,  2),
	2022: (4, 15),
	2023: (4,  7),
	2024: (3, 29),
	2025: (4, 18),
	2026: (4,  3),
	2027: (3, 26),
	2028: (4, 14),
	2029: (3, 30),
	2030: (4, 19),
	2031: (4, 11),
	2032: (3, 26),
	2033: (4, 15),
	2034: (4,  7),
	2035: (3, 23),
	2036: (4, 11),
	2037: (4,  3),
	2038: (4, 23),
	2039: (4,  8),
	2040: (3, 30),
	2041: (4, 19),
	2042: (4,  4),
	2043: (3, 27),
	2044: (4, 15),
	2045: (4,  7),
	2046: (3, 23),
	2047: (4, 12),
	2048: (4,  3),
	2049: (4, 16),
	2050: (4,  8),
	2051: (3, 31),
	2052: (4, 19),
	2053: (4,  4),
	2054: (3, 27),
	2055: (4, 16),
	2056: (3, 31),
	2057: (4, 20),
	2058: (4, 12),
	2059: (3, 28),
	2060: (4, 16),
	2061: (4,  8),
	2062: (3, 24),
	2063: (4, 13),
	2064: (4,  4),
	2065: (3, 27),
	2066: (4,  9),
	2067: (4,  1),
	2068: (4, 20),
	2069: (4, 12),
}

class HolidaysTest(unittest.TestCase):
	"""
	Tests for functions in the Holidays module.
	"""

	def test_newYearsDay(self):
		for year in YEARS:
			d = Holidays.newYearsDay(year)
			self.assertEqual(d.year, year)
			self.assertEqual(d.month, 1)
			self.assertEqual(d.day, 1)

	def test_martinLutherKingJrDay(self):
		for year in YEARS:
			d = Holidays.martinLutherKingJrDay(year)
			self.assertEqual(d.year, year)
			self.assertEqual(d.month, 1)
			self.assertGreaterEqual(d.day, 15)
			self.assertEqual(d.weekday(), Weekdays.MONDAY)

	def test_presidentsDay(self):
		for year in YEARS:
			d = Holidays.presidentsDay(year)
			self.assertEqual(d.year, year)
			self.assertEqual(d.month, 2)
			self.assertGreaterEqual(d.day, 15)
			self.assertEqual(d.weekday(), Weekdays.MONDAY)

	def test_goodFriday(self):
		for year in range(2010, 2030):
			d = Holidays.goodFriday(year)
			self.assertEqual(d.year, year)
			self.assertTrue(d.month == 3 or d.month == 4)
			self.assertEqual(d.weekday(), Weekdays.FRIDAY)

		for year in GOOD_FRIDAYS:
			d = Holidays.goodFriday(year)
			self.assertEqual(GOOD_FRIDAYS[year], (d.month, d.day))

	def test_easter(self):
		for year in range(2010, 2030):
			d = Holidays.easter(year)
			self.assertEqual(d.year, year)
			self.assertTrue(d.month == 3 or d.month == 4)
			self.assertEqual(d.weekday(), Weekdays.SUNDAY)

	def test_memorialDay(self):
		for year in YEARS:
			d = Holidays.memorialDay(year)
			self.assertEqual(d.year, year)
			self.assertEqual(d.month, 5)
			self.assertGreaterEqual(d.day, 24)
			self.assertEqual(d.weekday(), Weekdays.MONDAY)

	def test_independenceDay(self):
		for year in YEARS:
			d = Holidays.independenceDay(year)
			self.assertEqual(d.year, year)
			self.assertEqual(d.month, 7)
			self.assertEqual(d.day, 4)

	def test_laborDay(self):
		for year in YEARS:
			d = Holidays.laborDay(year)
			self.assertEqual(d.year, year)
			self.assertEqual(d.month, 9)
			self.assertEqual(d.weekday(), Weekdays.MONDAY)

	def test_columbusDay(self):
		for year in YEARS:
			d = Holidays.columbusDay(year)
			self.assertEqual(d.year, year)
			self.assertEqual(d.month, 10)
			self.assertGreaterEqual(d.day, 8)
			self.assertEqual(d.weekday(), Weekdays.MONDAY)

	def test_halloween(self):
		for year in YEARS:
			d = Holidays.halloween(year)
			self.assertEqual(d.year, year)
			self.assertEqual(d.month, 10)
			self.assertEqual(d.day, 31)

	def test_veteransDay(self):
		for year in YEARS:
			d = Holidays.veteransDay(year)
			self.assertEqual(d.year, year)
			self.assertEqual(d.month, 11)
			self.assertEqual(d.day, 11)

	def test_thanksgiving(self):
		for year in YEARS:
			d = Holidays.thanksgiving(year)
			self.assertEqual(d.year, year)
			self.assertEqual(d.month, 11)
			self.assertGreaterEqual(d.day, 22)
			self.assertEqual(d.weekday(), Weekdays.THURSDAY)

	def test_christmas(self):
		for year in YEARS:
			d = Holidays.christmas(year)
			self.assertEqual(d.year, year)
			self.assertEqual(d.month, 12)
			self.assertEqual(d.day, 25)

	def test_holidayCalendar(self):
		hs = Holidays.holidayCalendar(2018, 2020)

		#Spot check
		self.assertGreaterEqual(len(hs), 30)
		self.assertEqual(hs[0][0].year, 2018)
		self.assertEqual(hs[-1][0].year, 2020)

		#Sorted?
		h = None
		for holiday, name in hs:
			if h is not None:
				self.assertGreater(holiday, h)
			h = holiday
