
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

from HumanTime.Numbers import parseNumber
from HumanTime.Utility import tokenize

MICROSECOND = datetime.timedelta(microseconds=1)
MILLISECOND = datetime.timedelta(microseconds=1000)
SECOND = datetime.timedelta(seconds=1)
KILOSECOND = datetime.timedelta(seconds=1000)
MEGASECOND = datetime.timedelta(seconds=1000000)

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
			(KILOSECOND, ['ks', 'ksec', 'ksecs', 'kilosecond', 'kiloseconds']),
			(MEGASECOND, ['megasecond', 'megaseconds']),

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
			pass #Try the next one
	elif n == 2:
		try:
			count = parseNumber(ts[0])
			unit = UNITS[ts[1]]
			return count * unit
		except KeyError:
			pass #Try the next one
		except ValueError:
			pass #Try the next one
	raise ValueError('Invalid duration string')

def parseDuration(s):
	"""
	Parses a duration from a human string.

	:param s: str Input
	:return: datetime.timedelta
	"""
	ts = tokenize(s)
	return parseDurationTokens(ts)
