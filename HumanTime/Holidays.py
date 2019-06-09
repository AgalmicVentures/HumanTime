
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

import datetime

from HumanTime.Weekdays import SATURDAY, dayOfWeekOnOrAfter
from HumanTime.Utility import today

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
	monthDay = GOOD_FRIDAYS.get(year)
	if monthDay is None:
		return None

	return datetime.datetime(year, monthDay[0], monthDay[1])

def easter(year):
	"""
	Returns the date of Easter in a given year.

	:param year: int
	:return: datetime.datetime or None
	"""
	t0 = goodFriday(year)
	if t0 is None:
		return None

	return t0 + datetime.timedelta(days=2)

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

def holidayCalendar(fromYear, toYear):
	"""
	Returns a business holiday calendar from one year to another (inclusive).

	:param fromYear: int
	:param toYear: int
	:return: datetime.datetime
	"""
	holidays = []
	for year in range(fromYear, toYear + 1):
		#Jan
		holidays.append( (newYearsDay(year), 'New Year\'s Day') )

		holidays.append( (martinLutherKingJrDay(year), 'Martin Luther King Jr. Day') )

		#Feb
		holidays.append( (presidentsDay(year), 'Presidents\' Day') )

		#Mar/Apr
		holidays.append( (goodFriday(year), 'Good Friday') )

		#May
		holidays.append( (memorialDay(year), 'Memorial Day') )

		#Jul
		holidays.append( (independenceDay(year), 'Independence Day') )

		#Sep
		holidays.append( (laborDay(year), 'Labor Day') )

		#Oct
		holidays.append( (columbusDay(year), 'Columbus Day') )

		#Nov
		holidays.append( (veteransDay(year), 'Veterans\' Day') )

		holidays.append( (thanksgiving(year), 'Thanksgiving') )

		#Dec
		holidays.append( (christmas(year), 'Christmas') )

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
