
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

from HumanTime import Durations

class DurationsTest(unittest.TestCase):
	"""
	Tests for functions in the HumanTime module.
	"""

	def test_parseDuration_empty(self):
		with self.assertRaises(ValueError):
			Durations.parseDuration('')
		with self.assertRaises(ValueError):
			Durations.parseDuration('     ')

	def test_parseDuration_singleUnit(self):
		self.assertEqual(Durations.parseDuration('sec'), datetime.timedelta(seconds=1))
		self.assertEqual(Durations.parseDuration('kilosecond'), datetime.timedelta(seconds=1000))
		self.assertEqual(Durations.parseDuration('week'), datetime.timedelta(days=7))

	def test_parseDuration_singleUnit_invalid(self):
		with self.assertRaises(ValueError):
			Durations.parseDuration('asdf')

	def test_parseDuration_ordinals(self):
		self.assertEqual(Durations.parseDuration('3 minutes'), datetime.timedelta(seconds=180))
		self.assertEqual(Durations.parseDuration('180 seconds'), datetime.timedelta(seconds=180))

		self.assertEqual(Durations.parseDuration('3 days'), datetime.timedelta(days=3))
		self.assertEqual(Durations.parseDuration('72 hours'), datetime.timedelta(days=3))

		self.assertEqual(Durations.parseDuration('3 megaseconds').total_seconds(), 3000000)

	def test_parseDuration_cardinals(self):
		self.assertEqual(Durations.parseDuration('couple seconds'), datetime.timedelta(seconds=2))
		self.assertEqual(Durations.parseDuration('three seconds'), datetime.timedelta(seconds=3))
		self.assertEqual(Durations.parseDuration('ten days'), datetime.timedelta(days=10))
