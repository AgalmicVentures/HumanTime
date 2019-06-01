
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

from HumanTime.Utility import today

#Values returned by .weekday()
MONDAY = 0
TUESDAY = 1
WEDNESDAY = 2
THURSDAY = 3
FRIDAY = 4
SATURDAY = 5
SUNDAY = 6

def dayOfWeekOnOrAfter(t, dayOfWeek):
	"""
	Returns the Monday/Tuesday/etc. on or after the given date.

	:param t: datetime.datetime
	:param dayOfWeek: int returned by .weekday()
	:return: datetime.datetime
	"""
	if dayOfWeek < 0 or 7 <= dayOfWeek:
		raise ValueError('Day of week must be in [0, 6] (MONDAY-SUNDAY)')
	t = today(t)
	while t.weekday() != dayOfWeek:
		t += datetime.timedelta(days=1)
	return t

def dayOfWeekOnOrBefore(t, dayOfWeek):
	"""
	Returns the Monday/Tuesday/etc. on or before the given date.

	:param t: datetime.datetime
	:param dayOfWeek: int returned by .weekday()
	:return: datetime.datetime
	"""
	if dayOfWeek < 0 or 7 <= dayOfWeek:
		raise ValueError('Day of week must be in [0, 6] (MONDAY-SUNDAY)')
	t = today(t)
	while t.weekday() != dayOfWeek:
		t -= datetime.timedelta(days=1)
	return t

def weekdayOnOrAfter(t):
	"""
	Returns the first weekday on or after a given time.

	:param t: datetime.datetime
	:return: datetime.datetime
	"""
	t = today(t)
	while t.weekday() >= SATURDAY:
		t += datetime.timedelta(days=1)
	return t

def weekdayOnOrBefore(t):
	"""
	Returns the first weekday on or before a given time.

	:param t: datetime.datetime
	:return: datetime.datetime
	"""
	t = today(t)
	while t.weekday() >= SATURDAY:
		t -= datetime.timedelta(days=1)
	return t
