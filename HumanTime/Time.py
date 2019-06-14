
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
import re

from HumanTime.Durations import parseDurationTokens, DAY, WEEK
from HumanTime.Numbers import parseNumber
from HumanTime.Utility import tokenize

#Actually bring in these symbols
#XXX: don't use * imports so static analysis can detect unknown symbols
from HumanTime.Holidays import * # @suppress
from HumanTime.Weekdays import * # @suppress
from HumanTime.Utility import now, today

##### Standard Time Format Helpers #####

def parseTimeOfDay(s):
	"""
	Parses a time of day such as 9:30:21 AM.

	:param s: str Input
	:return: datetime.time
	"""
	if s == 'midnight':
		return datetime.time(0, 0, 0)
	elif s == 'noon':
		return datetime.time(12, 0, 0)

	formats = [
		'%I%p',
		'%I:%M%p',
		'%I:%M:%S%p',
		'%I:%M:%S.%f%p',

		'%H',
		'%H:%M',
		'%H:%M:%S',
		'%H:%M:%S.%f',

		'%H%M',
		'%H%M%S',
		'%H%M%S.%f',
	]
	for format in formats:
		try:
			return datetime.datetime.strptime(s, format).time()
		except ValueError as e:
			pass #Try the next one
	raise ValueError('Invalid time: "%s"' % str(s))

def parseTimestamp(s):
	"""
	Parses a timestamp such as 2019-04-29.

	:param s: str Input
	:return: datetime.datetime
	"""
	formats = [
		'%Y',
		#XXX: remove for now, could cause confusion '%Y/%m',
		#XXX: remove for now, could cause confusion '%Y/%m/%d',
		'%Y-%m',
		'%Y-%m-%d',
		'%Y_%m',
		'%Y_%m_%d',
		'%Y%m',
		'%Y%m%d',

		'%Y%m%d_%H%M',
		'%Y%m%d_%H%M%S',
		'%Y%m%d_%H%M%S.%f',
		'%Y%m%dt%H%M%S',
		'%Y%m%dt%H%M%S.%f',
		'%Y%m%dz%H%M%S',
		'%Y%m%dz%H%M%S.%f',
	]
	for format in formats:
		try:
			return datetime.datetime.strptime(s, format)
		except ValueError as e:
			pass #Try the next one
	raise ValueError('Invalid timestamp: "%s"' % str(s))

##### Generators #####

def noon(t=None):
	"""
	Returns today at 12:00.

	:param t: datetime.datetime Optional current time for relative calls.
	:return: datetime.datetime
	"""
	return now(t).replace(hour=12, minute=0, second=0, microsecond=0)

def tomorrow(t=None):
	"""
	Returns tomorrow at 00:00.

	:param t: datetime.datetime Optional current time for relative calls.
	:return: datetime.datetime
	"""
	return today(t) + DAY

def yesterday(t=None):
	"""
	Returns yeseterday at 00:00.

	:param t: datetime.datetime Optional current time for relative calls.
	:return: datetime.datetime
	"""
	return today(t) - DAY

def monthOnOrAfter(t, month):
	"""
	Returns the January/February/etc. on or after the given date.

	:param t: datetime.datetime
	:param month: int 1 - 12
	:return: datetime.datetime
	"""
	if month < 1 or 12 < month:
		raise ValueError('Month must be in [1, 12]')
	t = now(t)
	return datetime.datetime(t.year + 1 if t.month > month else t.year, month, 1)

def monthOnOrBefore(t, month):
	"""
	Returns the January/February/etc. on or before the given date.

	:param t: datetime.datetime
	:param month: int 1 - 12
	:return: datetime.datetime
	"""
	if month < 1 or 12 < month:
		raise ValueError('Month must be in [1, 12]')
	t = now(t)
	return datetime.datetime(t.year - 1 if t.month < month else t.year, month, 1)

def dayOfYearOnOrAfter(t, month, day):
	"""
	Returns the first weekday on or after a given time.

	:param t: datetime.datetime
	:param month: int
	:param day: int
	:return: datetime.datetime
	"""
	t = now(t)
	dayOnOrAfter = month > t.month or (month == t.month and day >= t.day)
	return datetime.datetime(t.year if dayOnOrAfter else t.year + 1, month, day)

def dayOfYearOnOrBefore(t, month, day):
	"""
	Returns the first weekday on or after a given time.

	:param t: datetime.datetime
	:param month: int
	:param day: int
	:return: datetime.datetime
	"""
	t = now(t)
	dayOnOrBefore = month < t.month or (month == t.month and day <= t.day)
	return datetime.datetime(t.year if dayOnOrBefore else t.year - 1, month, day)

def annualOnOrAfter(t, annualEvent):
	"""
	Returns the first annual event on or after this date.

	:param t: datetime.datetime
	:param annualEvent: function from year to datetime
	:return: datetime.datetime
	"""
	t = now(t)
	t0 = annualEvent(t.year)
	dayOnOrAfter = t0.month > t.month or (t0.month == t.month and t0.day >= t.day)
	return t0 if dayOnOrAfter else annualEvent(t.year + 1)

def annualOnOrBefore(t, annualEvent):
	"""
	Returns the first annual event on or before this date.

	:param t: datetime.datetime
	:param annualEvent: function from year to datetime
	:return: datetime.datetime
	"""
	t = now(t)
	t0 = annualEvent(t.year)
	dayOnOrBefore = t0.month < t.month or (t0.month == t.month and t0.day <= t.day)
	return t0 if dayOnOrBefore else annualEvent(t.year - 1)

##### Parsing #####

DAY_OF_WEEK_ON_OR_AFTER = {}
DAY_OF_WEEK_ON_OR_BEFORE = {}
for dayOfWeek, names in [
			(MONDAY, ['mon', 'monday', 'mondays']),
			(TUESDAY, ['tu', 'tue', 'tues', 'tuesday', 'tuesdays']),
			(WEDNESDAY, ['wed', 'weds', 'wednesday', 'wednesdays']),
			(THURSDAY, ['th', 'thu', 'thur', 'thurs', 'thursday', 'thursdays']),
			(FRIDAY, ['fri', 'friday', 'fridays']),
			(SATURDAY, ['sat', 'saturday', 'saturdays']),
			(SUNDAY, ['sun', 'sunday', 'sundays']),
		]:
	afterFunction = lambda t=None, d=dayOfWeek: dayOfWeekOnOrAfter(t, d) # @suppress
	beforeFunction = lambda t=None, d=dayOfWeek: dayOfWeekOnOrBefore(t, d) # @suppress
	for name in names:
		DAY_OF_WEEK_ON_OR_AFTER[name] = afterFunction
		DAY_OF_WEEK_ON_OR_BEFORE[name] = beforeFunction

MONTH_ON_OR_AFTER = {}
MONTH_ON_OR_BEFORE = {}
for month, names in [
			(1, ['jan', 'january']),
			(2, ['feb', 'february']),
			(3, ['mar', 'march']),
			(4, ['apr', 'april']),
			(5, ['may']),
			(6, ['jun', 'june']),
			(7, ['jul', 'july']),
			(8, ['aug', 'august']),
			(9, ['sep', 'sept', 'september']),
			(10, ['oct', 'october']),
			(11, ['nov', 'november']),
			(12, ['dec', 'december']),
		]:
	afterFunction = lambda t=None, m=month: monthOnOrAfter(t, m) # @suppress
	beforeFunction = lambda t=None, m=month: monthOnOrBefore(t, m) # @suppress
	for name in names:
		MONTH_ON_OR_AFTER[name] = afterFunction
		MONTH_ON_OR_BEFORE[name] = beforeFunction

HOLIDAY_ON_OR_AFTER = {}
HOLIDAY_ON_OR_BEFORE = {}
for holiday, names in [
		(easter, ['easter', 'easters']),
		(halloween, ['halloween', 'halloweens']),
		(thanksgiving, ['thanksgiving', 'thanksgivings']),
		(christmas, ['christmas', 'x-mas', 'xmas']),
	]:
	afterFunction = lambda t=None, h=holiday: annualOnOrAfter(t, h) # @suppress
	beforeFunction = lambda t=None, h=holiday: annualOnOrBefore(t, h) # @suppress
	for name in names:
		HOLIDAY_ON_OR_AFTER[name] = afterFunction
		HOLIDAY_ON_OR_BEFORE[name] = beforeFunction

HOLIDAY2_ON_OR_AFTER = {}
HOLIDAY2_ON_OR_BEFORE = {}
for holiday, names0, names1 in [
		(newYearsDay, ['new'], ['year', 'years']),
		(martinLutherKingJrDay, ['mlk'], ['day', 'days']),
		(presidentsDay, ['presidents', "presidents'", "president's"], ['day', 'days']),
		(goodFriday, ['good'], ['friday', 'fridays']),
		(memorialDay, ['memorial'], ['day', 'days']),
		(independenceDay, ['independence'], ['day', 'days']),
		(laborDay, ['labor'], ['day', 'days']),
		(columbusDay, ['columbus'], ['day', 'days']),
		(veteransDay, ['veterans', "veterans'", "veteran's"], ['day', 'days']),
	]:
	afterFunction = lambda t=None, h=holiday: annualOnOrAfter(t, h) # @suppress
	beforeFunction = lambda t=None, h=holiday: annualOnOrBefore(t, h) # @suppress
	for name0 in names0:
		for name1 in names1:
			name = (name0, name1)
			HOLIDAY2_ON_OR_AFTER[name] = afterFunction
			HOLIDAY2_ON_OR_BEFORE[name] = beforeFunction

KEYWORDS = {
	#Basics
	'noon': noon,
	'now': now,
	'today': today,
	'tomorrow': tomorrow,
	'yesterday': yesterday,
}
KEYWORDS.update(DAY_OF_WEEK_ON_OR_AFTER)
KEYWORDS.update(MONTH_ON_OR_AFTER)
KEYWORDS.update(HOLIDAY_ON_OR_AFTER)

KEYWORDS2 = {
	#TODO: Add any 2 token keywords
}
KEYWORDS2.update(HOLIDAY2_ON_OR_AFTER)

PREPOSITION_SIGNS = {
	'after': 1,
	'before': -1,
	'from': 1,
	'post': 1,
	'pre': -1,
	'until': -1,
}

SIGNS = {
	'last': -1,
	'next': 1,
	'prev': -1,
	'previous': -1,
	'prior': -1,
	'this': 0,
}

def parseTimeTokens(ts, t=None):
	"""
	Parses a time from some tokens.

	:param ts: list String tokens
	:param t: datetime.datetime or None Base time
	:return: datetime.datetime
	"""
	n = len(ts)
	if n == 0:
		raise ValueError('Invalid time string - no tokens')
	elif n == 1:
		token = ts[0]
		keyword = KEYWORDS.get(token)
		if keyword is not None:
			return keyword(t=t)
		return parseTimestamp(token)
	elif n == 2:
		token = (ts[0], ts[1])
		keyword = KEYWORDS2.get(token)
		if keyword is not None:
			return keyword(t=t)

	#Articles
	if ts[0] in {'a', 'an', 'the'}:
		return parseTimeTokens(ts[1:], t=t)

	#D ago / hence
	if ts[-1] in {'ago', 'earlier'}:
		return parseTimeTokens(ts[:-1] + ['before', 'now'], t=t)
	elif ts[-1] in {'hence', 'later'}:
		return parseTimeTokens(ts[:-1] + ['after', 'now'], t=t)

	#T at Time
	if len(ts) > 2 and ts[-2] == 'at':
		t0 = parseTimeTokens(ts[:-2], t=t)
		time = parseTimeOfDay(ts[-1])
		return t0.replace(hour=time.hour, minute=time.minute, second=time.second, microsecond=time.microsecond)

	#D after/etc. T
	for i in range(1, min(4, len(ts))):
		sign = PREPOSITION_SIGNS.get(ts[i])
		if sign:
			break

	#If not after/before, maybe next/last?
	if sign is not None:
		t0 = parseTimeTokens(ts[i+1:], t=t)
		durationTokens = ts[:i]
	elif n == 2:
		sign = SIGNS.get(ts[0])
		if sign is not None:
			t0 = now(t)
			durationTokens = ts[1:2]

	if sign is not None:
		#Try two token units first
		if len(durationTokens) > 1:
			unit0 = durationTokens[-2]
			unit1 = durationTokens[-1]
			count = parseNumber(ts[0]) if len(durationTokens) > 2 else 1

			if unit1 in {'d', 'day', 'days'}:
				if unit0 in {'cal', 'calendar'}:
					return t0 + sign * count * DAY

				if unit0 in {'b', 'bus', 'business'}:
					businessDay = businessDayOnOrBefore if sign == -1 else businessDayOnOrAfter
					t1 = t0
					for _ in range(count):
						t1 = businessDay(t=t1 + sign * DAY)
					return t1

			#Two word holidays
			unit = (unit0, unit1)
			holiday = (HOLIDAY2_ON_OR_BEFORE if sign == -1 else HOLIDAY2_ON_OR_AFTER).get(unit)
			if holiday is not None:
				t1 = t0
				for _ in range(count):
					t1 = holiday(t=t1 + sign * DAY)
				return t1

		#Otherwise, single token units
		unit = durationTokens[-1]
		count = parseNumber(ts[0]) if len(durationTokens) > 1 else 1

		#First, handle special units that require more than simple addition --
		#weekdays, days of the week, months, years.

		if unit in {'wkdy', 'weekday', 'weekdays'}:
			weekday = weekdayOnOrBefore if sign == -1 else weekdayOnOrAfter
			t1 = t0
			for _ in range(count):
				t1 = weekday(t=t1 + sign * DAY)
			return t1

		dayOfWeek = (DAY_OF_WEEK_ON_OR_BEFORE if sign == -1 else DAY_OF_WEEK_ON_OR_AFTER).get(unit)
		if dayOfWeek is not None:
			#This is a strict after/before so add/subtract 1 day
			return dayOfWeek(t=t0 + sign * DAY) + ((count - 1) * sign) * WEEK

		month = (MONTH_ON_OR_BEFORE if sign == -1 else MONTH_ON_OR_AFTER).get(unit)
		if month is not None:
			endMonth = 12 if sign == 1 else 1
			t1 = datetime.datetime(t0.year + (sign if t0.month == endMonth else 0), (t0.month + sign) % 12, 1)
			t2 = month(t=t1)
			return t2.replace(year=t2.year + sign * (count - 1))

		holiday = (HOLIDAY_ON_OR_BEFORE if sign == -1 else HOLIDAY_ON_OR_AFTER).get(unit)
		if holiday is not None:
			t1 = t0
			for _ in range(count):
				t1 = holiday(t=t1 + sign * DAY)
			return t1

		monthDay = re.match('^([0-9]+)[-/._]([0-9]+)$', unit)
		if monthDay:
			month = int(monthDay.group(1))
			day = int(monthDay.group(2))
			dayOfYear = dayOfYearOnOrBefore if sign == -1 else dayOfYearOnOrAfter
			t1 = t0 + sign * DAY
			t2 = dayOfYear(t1, month, day)
			return t2.replace(year=t2.year + sign * (count - 1))

		if unit in {'mo', 'month', 'months'}:
			deltaMonth = t0.month - 1 + sign * count
			yearCount = deltaMonth // 12
			newYear = t0.year + yearCount
			newMonth = deltaMonth % 12 + 1
			newDay = min(t0.day, [31, 29, 31, 30, 31, 30, 31, 30, 30, 31, 30, 31][newMonth - 1])
			try:
				return t0.replace(year=newYear, month=newMonth, day=newDay)
			except ValueError:
				#Handle Feb 29 specially
				if newMonth == 2 and newDay == 29:
					return t0.replace(year=newYear, month=newMonth, day=28)
				raise

		elif unit in {'y', 'yr', 'yrs', 'year', 'years'}:
			newYear = t0.year + sign * count
			try:
				return t0.replace(year=newYear)
			except ValueError:
				#Handle Feb 29 specially
				if t0.month == 2 and t0.day == 29:
					return t0.replace(year=newYear, day=28)
				raise

		duration = parseDurationTokens(durationTokens)
		return t0 + sign * duration
	raise ValueError('Invalid time string')

def parseTime(s, t=None):
	"""
	Parses a time from a human string.

	:param s: str Input
	:param t: datetime.datetime or None Base time
	:return: datetime.timedelta
	"""
	ts = tokenize(s)
	return parseTimeTokens(ts, t=t)
