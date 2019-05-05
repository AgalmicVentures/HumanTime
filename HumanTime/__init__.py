
import datetime

##### Common Helpers #####

def tokenize(s):
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

MICROSECOND = datetime.timedelta(microseconds=1)
MILLISECOND = datetime.timedelta(microseconds=1000)
SECOND = datetime.timedelta(seconds=1)
MINUTE = datetime.timedelta(seconds=60)
HOUR = datetime.timedelta(hours=1)
DAY = datetime.timedelta(days=1)
WEEK = datetime.timedelta(days=7)
FORTNIGHT = datetime.timedelta(days=14)

UNITS = {
	'us': MICROSECOND,
	'micro': MICROSECOND,
	'micros': MICROSECOND,
	'microsecond': MICROSECOND,
	'microseconds': MICROSECOND,

	'ms': MILLISECOND,
	'millis': MILLISECOND,
	'millisecond': MILLISECOND,
	'milliseconds': MILLISECOND,

	's': SECOND,
	'sec': SECOND,
	'second': SECOND,
	'seconds': SECOND,

	'm': MINUTE,
	'min': MINUTE,
	'minute': MINUTE,
	'minutes': MINUTE,

	'h': HOUR,
	'hr': HOUR,
	'hrs': HOUR,
	'hour': HOUR,
	'hours': HOUR,

	'd': DAY,
	'day': DAY,
	'days': DAY,

	'w': WEEK,
	'wk': WEEK,
	'wks': WEEK,
	'week': WEEK,
	'weeks': WEEK,

	'fortnight': FORTNIGHT,
	'fortnights': FORTNIGHT,

	#Months and years require more of a lift than simple deltas
}

def parseDurationTokens(ts):
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
			count = int(ts[0])
			unit = UNITS[ts[1]]
			return count * unit
		except KeyError:
			pass
		except ValueError:
			pass
	raise ValueError('Invalid duration string')

def parseDuration(s):
	ts = tokenize(s)
	return parseDurationTokens(ts)

##### Times #####

def parseTimestamp(s):
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
		except ValueError:
			pass
	return None

def now(t=None):
	return datetime.datetime.now() if t is None else t

def noon(t=None):
	return now(t).replace(hour=12, minute=0, second=0, microsecond=0)

def today(t=None):
	return now(t).replace(hour=0, minute=0, second=0, microsecond=0)

def tomorrow(t=None):
	return today(t) + DAY

def yesterday(t=None):
	return today(t) - DAY

KEYWORDS = {
	'noon': noon,
	'now': now,
	'today': today,
	'tomorrow': tomorrow,
	'yesterday': yesterday,
	#TODO: days of week
	#TODO: week day, weekend
	#TODO: holidays
}

PREPOSITION_SIGNS = {
	'after': 1,
	'before': -1,
	'from': 1,
	'post': 1,
	'pre': -1,
	'until': -1,
}

def parseTimeTokens(ts):
	#TODO: this/next/last
	#TODO: business days
	#TODO: of the month
	n = len(ts)
	if n == 0:
		raise ValueError('Invalid time string - no tokens')
	elif n == 1:
		t = ts[0]
		keyword = KEYWORDS.get(t)
		if keyword is not None:
			return keyword()
		return parseTimestamp(t)
	#D after/etc. T
	for i in [1, 2]:
		sign = PREPOSITION_SIGNS.get(ts[i])
		if sign:
			break
	if sign is not None:
		t0 = parseTimeTokens(ts[i+1:])
		durationTokens = ts[:i]
		count = int(ts[0]) if len(ts) > 1 else 1
		unit = durationTokens[-1]
		if unit in {'mo', 'month', 'months'}:
			yearCount = (t0.month - 1 + count) // 12
			newYear = year=t0.year + sign * yearCount
			newMonth = (t0.month - 1 + count) % 12 + 1
			try:
				return t0.replace(year=newYear, month=newMonth)
			except ValueError:
				#Handle Feb 29 specially
				if newMonth == 2 and t0.day == 29:
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

def parseTime(s):
	ts = tokenize(s)
	return parseTimeTokens(ts)
