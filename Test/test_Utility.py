
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

from HumanTime import Utility

class UtilityTest(unittest.TestCase):
	"""
	Tests for functions in the Utility module.
	"""

	def test_now(self):
		t1 = datetime.datetime.now()
		now = Utility.now()
		t2 = datetime.datetime.now()

		self.assertLessEqual(t1, now)
		self.assertLessEqual(now, t2)

		nowT2 = Utility.now(t=t2)
		nowT1 = Utility.now(t=t1)
		self.assertEqual(t1, nowT1)
		self.assertEqual(t2, nowT2)

	def test_today(self):
		today = Utility.today()
		self.assertEqual(today.hour, 0)
		self.assertEqual(today.minute, 0)
		self.assertEqual(today.second, 0)
		self.assertEqual(today.microsecond, 0)

	def test_tokenize_empty(self):
		self.assertEqual(Utility.tokenize(''), [])

	def test_tokenize_blank(self):
		self.assertEqual(Utility.tokenize(' '), [])
		self.assertEqual(Utility.tokenize('\t'), [])
		self.assertEqual(Utility.tokenize('     '), [])
		self.assertEqual(Utility.tokenize(' \t  \t  '), [])

	def test_tokenize_single(self):
		self.assertEqual(Utility.tokenize('now'), ['now'])
		self.assertEqual(Utility.tokenize('now\n'), ['now'])
		self.assertEqual(Utility.tokenize('now   '), ['now'])
		self.assertEqual(Utility.tokenize('    now'), ['now'])
		self.assertEqual(Utility.tokenize('  now  \n'), ['now'])

	def test_tokenize(self):
		self.assertEqual(Utility.tokenize('3 hours from now'), ['3', 'hours', 'from', 'now'])

	def test_tokenize_whitespace(self):
		self.assertEqual(Utility.tokenize('  3     hours  from   now   '), ['3', 'hours', 'from', 'now'])
		self.assertEqual(Utility.tokenize('3 hours\nfrom\tnow'), ['3', 'hours', 'from', 'now'])
