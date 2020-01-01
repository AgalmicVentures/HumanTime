
# Copyright (c) 2019-2020 Agalmic Ventures LLC (www.agalmicventures.com)
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
import re

def now(t=None):
	"""
	Returns now, or the "current" time (allowing relative calls).

	:param t: datetime.datetime Optional current time for relative calls.
	:return: datetime.datetime
	"""
	return datetime.datetime.now() if t is None else t

def thisYear(t=None):
	"""
	Returns this year.

	:param t: datetime.datetime Optional current time for relative calls.
	:return: datetime.datetime
	"""
	return now(t).replace(month=1, day=1, hour=0, minute=0, second=0, microsecond=0)

def thisMonth(t=None):
	"""
	Returns this month.

	:param t: datetime.datetime Optional current time for relative calls.
	:return: datetime.datetime
	"""
	return now(t).replace(day=1, hour=0, minute=0, second=0, microsecond=0)

def today(t=None):
	"""
	Returns today at 0:00.

	:param t: datetime.datetime Optional current time for relative calls.
	:return: datetime.datetime
	"""
	return now(t).replace(hour=0, minute=0, second=0, microsecond=0)

def thisHour(t=None):
	"""
	Returns today at 0:00.

	:param t: datetime.datetime Optional current time for relative calls.
	:return: datetime.datetime
	"""
	return now(t).replace(minute=0, second=0, microsecond=0)

def thisMinute(t=None):
	"""
	Returns today at 0:00.

	:param t: datetime.datetime Optional current time for relative calls.
	:return: datetime.datetime
	"""
	return now(t).replace(second=0, microsecond=0)

def thisSecond(t=None):
	"""
	Returns today at 0:00.

	:param t: datetime.datetime Optional current time for relative calls.
	:return: datetime.datetime
	"""
	return now(t).replace(microsecond=0)

def tokenize(s):
	"""
	Tokenizes a human string for parsing.

	:param s: str Input
	:return: list String tokens
	"""
	tokens = [
		token
		for token in re.split(r'\s+', s.lower())
		if token != ''
	]
	return tokens
