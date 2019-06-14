
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

#NOTE: Currently this is US holidays only.

import collections
import datetime

from HumanTime.Weekdays import SATURDAY, dayOfWeekOnOrAfter
from HumanTime.Utility import today

def newYearsDay(year):
	"""
	Returns the date of New Year's Day in a given year.

	:param year: int
	:return: datetime.datetime
	"""
	return datetime.datetime(year, 1, 1)

def martinLutherKingJrDay(year):
	"""
	Returns the date of Martin Luther King Jr. Day in a given year.

	:param year: int
	:return: datetime.datetime or None
	"""
	if year < 1986:
		return None

	#3rd Monday in Jan
	firstMonday = dayOfWeekOnOrAfter(datetime.datetime(year, 1, 1), 0)
	return firstMonday + datetime.timedelta(days=14)

def presidentsDay(year):
	"""
	Returns the date of Presidents' Day in a given year.

	:param year: int
	:return: datetime.datetime or None
	"""
	if year < 1971:
		return None

	#3rd Monday in Feb
	firstMonday = dayOfWeekOnOrAfter(datetime.datetime(year, 2, 1), 0)
	return firstMonday + datetime.timedelta(days=14)

def goodFriday(year):
	"""
	Returns the date of Good Friday in a given year.

	:param year: int
	:return: datetime.datetime or None
	"""
	t0 = easter(year)
	if t0 is None:
		return None

	return t0 - datetime.timedelta(days=2)

def easter(year):
	"""
	Returns the date of Western Easter in a given year.

	:param year: int
	:return: datetime.datetime or None
	"""
	#Implements Butcher's algorithm: https://en.wikipedia.org/wiki/Computus
	a = year % 19 #https://en.wikipedia.org/wiki/Golden_number_(time)
	b = year // 100
	c = year % 100
	d = b // 4
	e = b % 4
	f = (b + 8) // 25
	g = (b - f + 1) // 3
	h = (19 * a + b - d - g + 15) % 30
	i = c // 4
	k = c % 4
	l = (32 + 2 * e + 2 * i - h - k) % 7
	m = (a + 11 * h + 22 * l) // 451

	month = (h + l - 7 * m + 114) // 31
	day = (h + l - 7 * m + 114) % 31 + 1
	return datetime.datetime(year, month, day)

def memorialDay(year):
	"""
	Returns the date of Labor Day in a given year.

	:param year: int
	:return: datetime.datetime or None
	"""
	if year < 1868:
		return None
	elif year < 1971:
		return datetime.datetime(year, 5, 30)
	else:
		#Last Monday in May
		date = datetime.datetime(year, 5, 31)
		while date.weekday() != 0:
			date -= datetime.timedelta(days=1)
		return date

def independenceDay(year):
	"""
	Returns the date of Indepdence Day in a given year.

	:param year: int
	:return: datetime.datetime
	"""
	return datetime.datetime(year, 7, 4)

def laborDay(year):
	"""
	Returns the date of Labor Day in a given year.

	:param year: int
	:return: datetime.datetime
	"""
	#1st Monday in Sep
	return dayOfWeekOnOrAfter(datetime.datetime(year, 9, 1), 0)

def columbusDay(year):
	"""
	Returns the date of Columbus Day in a given year.

	:param year: int
	:return: datetime.datetime or None
	"""
	if year < 1971:
		return None

	#2nd Monday in Oct
	firstMonday = dayOfWeekOnOrAfter(datetime.datetime(year, 10, 1), 0)
	return firstMonday + datetime.timedelta(days=7)

def halloween(year):
	"""
	Returns the date of Halloween in a given year.

	:param year: int
	:return: datetime.datetime or None
	"""
	return datetime.datetime(year, 10, 31)

def veteransDay(year):
	"""
	Returns the date of Veterans' Day in a given year.

	:param year: int
	:return: datetime.datetime or None
	"""
	if year < 1938:
		return None

	return datetime.datetime(year, 11, 11)

def thanksgiving(year):
	"""
	Returns the date of Thanksgiving in a given year.

	:param year: int
	:return: datetime.datetime
	"""
	#4th Thurs in Nov
	firstThursday = dayOfWeekOnOrAfter(datetime.datetime(year, 11, 1), 3)
	return firstThursday + datetime.timedelta(days=21)

def christmas(year):
	"""
	Returns the date of Christmas in a given year.

	:param year: int
	:return: datetime.datetime
	"""
	return datetime.datetime(year, 12, 25)

HOLIDAY_NAME_TO_HOLIDAY = collections.OrderedDict([
	("New Year's Day", newYearsDay),
	('Martin Luther King Jr. Day', martinLutherKingJrDay),
	("Presidents' Day", presidentsDay),
	('Good Friday', goodFriday),
	('Memorial Day', memorialDay),
	('Independence Day', independenceDay),
	('Labor Day', laborDay),
	('Columbus Day', columbusDay),
	("Veterans' Day", veteransDay),
	('Thanksgiving', thanksgiving),
	('Christmas', christmas),
])

def holidayCalendar(fromYear, toYear, holidayNameToHoliday=HOLIDAY_NAME_TO_HOLIDAY):
	"""
	Returns a business holiday calendar from one year to another (inclusive).

	:param fromYear: int
	:param toYear: int
	:param holidayNameToHoliday: collections.OrderedDict of name to holiday function
	:return: datetime.datetime
	"""
	holidays = []
	for year in range(fromYear, toYear + 1):
		for name in holidayNameToHoliday:
			holiday = holidayNameToHoliday[name]
			holidays.append( (holiday(year), name) )

	return [h for h in holidays if h[0] is not None]

#The holidays used to compute business days
HOLIDAY_CALENDAR = holidayCalendar(1900, 2100)
HOLIDAYS = {h[0] for h in HOLIDAY_CALENDAR}

def businessDayOnOrAfter(t, holidays=HOLIDAYS):
	"""
	Returns the first business day on or after a given time.

	:param t: datetime.datetime
	:return: datetime.datetime
	"""
	t = today(t)
	while t.weekday() >= SATURDAY or t in HOLIDAYS:
		t += datetime.timedelta(days=1)
	return t

def businessDayOnOrBefore(t, holidays=HOLIDAYS):
	"""
	Returns the first business day on or before a given time.

	:param t: datetime.datetime
	:return: datetime.datetime
	"""
	t = today(t)
	while t.weekday() >= SATURDAY or t in HOLIDAYS:
		t -= datetime.timedelta(days=1)
	return t
