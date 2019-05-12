
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

##### Common Helpers #####

def tokenize(s):
	"""
	Tokenizes a human time string for parsing.

	:param s: str Input
	:return: list String tokens
	"""
	tokens = [
		token
		for token in (
			t.strip()
			for t in s.lower().split(' ')
		)
		if token != ''
	]
	return tokens

##### Durations #####

CARDINALS = {
	'one': 1,
	'two': 2,
	'three': 3,
	'four': 4,
	'five': 5,
	'six': 6,
	'seven': 7,
	'eight': 8,
	'nine': 9,
	'ten': 10,
	'eleven': 11,
	'twelve': 12,
	#Not strictly cardinals, but its helpful
	'a': 1,
	'an': 1,
	'the': 1,
}

ORDINALS = {
	'1st': 1,
	'2nd': 2,
	'3rd': 3,
	'4th': 4,
	'5th': 5,
	'6th': 6,
	'7th': 7,
	'8th': 8,
	'9th': 9,
	'10th': 10,
	'11th': 11,
	'12th': 12,
	'first': 1,
	'second': 2,
	'third': 3,
	'fourth': 4,
	'fifth': 5,
	'sixth': 6,
	'seventh': 7,
	'eighth': 8,
	'ninth': 9,
	'tenth': 10,
	'eleventh': 11,
	'twelfth': 12,
}

def parseCardinal(s):
	"""
	Parses a cardinal number such as "three" or "3".

	:param s: str
	:return: int
	"""
	cardinalValue = CARDINALS.get(s)
	if cardinalValue is not None:
		return cardinalValue

	return int(s)

def parseOrdinal(s):
	"""
	Parses an ordinal number such as "third" or "3rd".

	:param s: str
	:return: int
	"""
	ordinalValue = ORDINALS.get(s)
	if ordinalValue is not None:
		return ordinalValue

	return int(s)

def parseNumber(s):
	"""
	Parses a number such as "three" or "3rd".

	:param s: str
	:return: int
	"""
	cardinalValue = CARDINALS.get(s)
	if cardinalValue is not None:
		return cardinalValue

	ordinalValue = ORDINALS.get(s)
	if ordinalValue is not None:
		return ordinalValue

	return int(s)

MICROSECOND = datetime.timedelta(microseconds=1)
MILLISECOND = datetime.timedelta(microseconds=1000)
SECOND = datetime.timedelta(seconds=1)
MINUTE = datetime.timedelta(seconds=60)
HOUR = datetime.timedelta(hours=1)
DAY = datetime.timedelta(days=1)
WEEK = datetime.timedelta(days=7)
FORTNIGHT = datetime.timedelta(days=14)

UNITS = {}
for unit, names in [
			(MICROSECOND, ['us', 'mic', 'mics', 'micro', 'micros', 'microsecond', 'microseconds']),
			(MILLISECOND, ['ms', 'milli', 'millis', 'millisecond', 'milliseconds']),
			(SECOND, ['s', 'sec', 'secs', 'second', 'seconds']),
			(MINUTE, ['m', 'min', 'mins', 'minute', 'minutes']),
			(HOUR, ['h', 'hr', 'hrs', 'hour', 'hours']),
			(DAY, ['d', 'day', 'days']),
			(WEEK, ['w', 'wk', 'wks', 'week', 'weeks']),
			(FORTNIGHT, ['fortnight', 'fortnights']),
			#Months and years require more of a lift than simple deltas
		]:
	for name in names:
		UNITS[name] = unit

def parseDurationTokens(ts):
	"""
	Parses a duration from some tokens.

	:param ts: list String tokens
	:return: datetime.timedelta
	"""
	n = len(ts)
	if n == 0:
		raise ValueError('Invalid duration string - no tokens')
	elif n == 1:
		try:
			unit = UNITS[ts[0]]
			return unit
		except KeyError:
			pass
	elif n == 2:
		try:
			count = parseNumber(ts[0])
			unit = UNITS[ts[1]]
			return count * unit
		except KeyError:
			pass
		except ValueError:
			pass
	raise ValueError('Invalid duration string')

def parseDuration(s):
	"""
	Parses a duration from a human string.

	:param s: str Input
	:return: datetime.timedelta
	"""
	ts = tokenize(s)
	return parseDurationTokens(ts)

##### Times #####

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
		'%I:%M:%S.%f%p',
		'%I:%M:%S%p',
		'%I:%M%p',
		'%I%p',

		'%H:%M:%S.%f',
		'%H:%M:%S',
		'%H:%M',
		'%H',
	]
	for format in formats:
		try:
			return datetime.datetime.strptime(s, format).time()
		except ValueError as e:
			pass
	raise ValueError('Invalid time: "%s"' % str(s))

def parseTimestamp(s):
	"""
	Parses a timestamp such as 2019-04-29.

	:param s: str Input
	:return: datetime.datetime
	"""
	formats = [
		'%Y',
		'%Y/%m',
		'%Y/%m/%d',
		'%Y-%m',
		'%Y-%m-%d',
		'%Y_%m',
		'%Y_%m_%d',
		'%Y%m',
		'%Y%m%d',
	]
	for format in formats:
		try:
			return datetime.datetime.strptime(s, format)
		except ValueError as e:
			pass
	raise ValueError('Invalid timestamp: "%s"' % str(s))

def now(t=None):
	"""
	Returns now, or the "current" time (allowing relative calls).

	:param t: datetime.datetime Optional current time for relative calls.
	:return: datetime.datetime
	"""
	return datetime.datetime.now() if t is None else t

def noon(t=None):
	"""
	Returns today at 12:00.

	:param t: datetime.datetime Optional current time for relative calls.
	:return: datetime.datetime
	"""
	return now(t).replace(hour=12, minute=0, second=0, microsecond=0)

def today(t=None):
	"""
	Returns today at 0:00.

	:param t: datetime.datetime Optional current time for relative calls.
	:return: datetime.datetime
	"""
	return now(t).replace(hour=0, minute=0, second=0, microsecond=0)

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

DAY_OF_WEEK_ON_OR_AFTER = {}
DAY_OF_WEEK_ON_OR_BEFORE = {}
for dayOfWeek, names in [
			(MONDAY, ['mon', 'monday', 'mondays']),
			(TUESDAY, ['tue', 'tues', 'tuesday', 'tuesdays']),
			(WEDNESDAY, ['wed', 'weds', 'wednesday', 'wednesdays']),
			(THURSDAY, ['thu', 'thur', 'thurs', 'thursday', 'thursdays']),
			(FRIDAY, ['fri', 'friday', 'fridays']),
			(SATURDAY, ['sat', 'saturday', 'saturdays']),
			(SUNDAY, ['sun', 'sunday', 'sundays']),
		]:
	afterFunction = lambda t=None, d=dayOfWeek: dayOfWeekOnOrAfter(t, d)
	beforeFunction = lambda t=None, d=dayOfWeek: dayOfWeekOnOrBefore(t, d)
	for name in names:
		DAY_OF_WEEK_ON_OR_AFTER[name] = afterFunction
		DAY_OF_WEEK_ON_OR_BEFORE[name] = beforeFunction

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
	afterFunction = lambda t=None, m=month: monthOnOrAfter(t, m)
	beforeFunction = lambda t=None, m=month: monthOnOrBefore(t, m)
	for name in names:
		MONTH_ON_OR_AFTER[name] = afterFunction
		MONTH_ON_OR_BEFORE[name] = beforeFunction

KEYWORDS = {
	#Basics
	'noon': noon,
	'now': now,
	'today': today,
	'tomorrow': tomorrow,
	'yesterday': yesterday,

	#Days of the week are added below

	#TODO: holidays
}
KEYWORDS.update(DAY_OF_WEEK_ON_OR_AFTER)
KEYWORDS.update(MONTH_ON_OR_AFTER)

PREPOSITION_SIGNS = {
	'after': 1,
	'before': -1,
	'from': 1,
	'post': 1,
	'pre': -1,
	'until': -1,
}

def parseTimeTokens(ts, t=None):
	"""
	Parses a time from some tokens.

	:param ts: list String tokens
	:param t: datetime.datetime or None Base time
	:return: datetime.datetime
	"""
	#TODO: business days
	#TODO: of the month
	n = len(ts)
	if n == 0:
		raise ValueError('Invalid time string - no tokens')
	elif n == 1:
		token = ts[0]
		keyword = KEYWORDS.get(token)
		if keyword is not None:
			return keyword(t=t)
		return parseTimestamp(token)

	#Articles
	if ts[0] in {'a', 'an', 'the'}:
		return parseTimeTokens(ts[1:], t=t)

	#D ago
	if ts[-1] == 'ago':
		return parseTimeTokens(ts[:-1] + ['before', 'now'], t=t)

	#T at Time
	if len(ts) > 2 and ts[-2] == 'at':
		t0 = parseTimeTokens(ts[:-2], t=t)
		time = parseTimeOfDay(ts[-1])
		return t0.replace(hour=time.hour, minute=time.minute, second=time.second, microsecond=time.microsecond)

	#D after/etc. T
	for i in range(1, min(3, len(ts))):
		sign = PREPOSITION_SIGNS.get(ts[i])
		if sign:
			break

	#If not after/before, maybe next/last?
	if sign is not None:
		t0 = parseTimeTokens(ts[i+1:], t=t)
		durationTokens = ts[:i]
	elif n == 2:
		sign = {
			'last': -1,
			'next': 1,
		}.get(ts[0])
		if sign is not None:
			t0 = now(t)
			durationTokens = ts[1:2]

	if sign is not None:
		unit = durationTokens[-1]
		count = parseNumber(ts[0]) if len(durationTokens) > 1 else 1

		if unit in {'weekday', 'weekdays'}:
			weekday = weekdayOnOrAfter if sign == 1 else weekdayOnOrBefore
			t1 = t0
			for i in range(count):
				t1 = weekday(t=t1 + sign * DAY)
			return t1

		dayOfWeek = (DAY_OF_WEEK_ON_OR_AFTER if sign == 1 else DAY_OF_WEEK_ON_OR_BEFORE).get(unit)
		if dayOfWeek is not None:
			#This is a strict after/before so add/subtract 1 day
			return dayOfWeek(t=t0 + sign * DAY) + ((count - 1) * sign) * WEEK

		month = (MONTH_ON_OR_AFTER if sign == 1 else MONTH_ON_OR_BEFORE).get(unit)
		if month is not None:
			endMonth = 12 if sign == 1 else 1
			t1 = datetime.datetime(t0.year + (sign if t0.month == endMonth else 0), (t0.month + sign) % 12, 1)
			t2 = month(t=t1)
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
