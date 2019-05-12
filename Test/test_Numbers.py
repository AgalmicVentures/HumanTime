
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

from HumanTime import Numbers

class NumbersTest(unittest.TestCase):
	"""
	Tests for functions in the Numbers module.
	"""

	def test_parseCardinal_zero(self):
		self.assertEqual(Numbers.parseCardinal('zero'), 0)

	def test_parseCardinal_small(self):
		self.assertEqual(Numbers.parseCardinal('one'), 1)
		self.assertEqual(Numbers.parseCardinal('two'), 2)
		self.assertEqual(Numbers.parseCardinal('three'), 3)
		self.assertEqual(Numbers.parseCardinal('four'), 4)
		self.assertEqual(Numbers.parseCardinal('five'), 5)
		self.assertEqual(Numbers.parseCardinal('six'), 6)
		self.assertEqual(Numbers.parseCardinal('seven'), 7)
		self.assertEqual(Numbers.parseCardinal('eight'), 8)
		self.assertEqual(Numbers.parseCardinal('nine'), 9)
		self.assertEqual(Numbers.parseCardinal('ten'), 10)
		self.assertEqual(Numbers.parseCardinal('eleven'), 11)
		self.assertEqual(Numbers.parseCardinal('twelve'), 12)

	def test_parseCardinal_large(self):
		self.assertEqual(Numbers.parseCardinal('twenty'), 20)
		self.assertEqual(Numbers.parseCardinal('fifty'), 50)
		self.assertEqual(Numbers.parseCardinal('ninety'), 90)

	def test_parseOrdinal_small(self):
		self.assertEqual(Numbers.parseOrdinal('1st'), 1)
		self.assertEqual(Numbers.parseOrdinal('second'), 2)
		self.assertEqual(Numbers.parseOrdinal('3rd'), 3)
		self.assertEqual(Numbers.parseOrdinal('fourth'), 4)
		self.assertEqual(Numbers.parseOrdinal('5th'), 5)
		self.assertEqual(Numbers.parseOrdinal('6th'), 6)
		self.assertEqual(Numbers.parseOrdinal('seventh'), 7)
		self.assertEqual(Numbers.parseOrdinal('eighth'), 8)
		self.assertEqual(Numbers.parseOrdinal('ninth'), 9)
		self.assertEqual(Numbers.parseOrdinal('10th'), 10)
		self.assertEqual(Numbers.parseOrdinal('11th'), 11)
		self.assertEqual(Numbers.parseOrdinal('12th'), 12)

	def test_parseOrdinal_large(self):
		self.assertEqual(Numbers.parseOrdinal('29th'), 29)
		self.assertEqual(Numbers.parseOrdinal('30th'), 30)
		self.assertEqual(Numbers.parseOrdinal('31st'), 31)

	def test_parseNumber_small(self):
		self.assertEqual(Numbers.parseNumber('one'), 1)
		self.assertEqual(Numbers.parseNumber('two'), 2)
		self.assertEqual(Numbers.parseNumber('three'), 3)
		self.assertEqual(Numbers.parseNumber('four'), 4)
		self.assertEqual(Numbers.parseNumber('5th'), 5)
		self.assertEqual(Numbers.parseNumber('6th'), 6)
		self.assertEqual(Numbers.parseNumber('seventh'), 7)
		self.assertEqual(Numbers.parseNumber('eighth'), 8)
		self.assertEqual(Numbers.parseNumber('ninth'), 9)
		self.assertEqual(Numbers.parseNumber('10'), 10)
		self.assertEqual(Numbers.parseNumber('11'), 11)
		self.assertEqual(Numbers.parseNumber('12'), 12)
