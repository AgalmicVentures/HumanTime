
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
