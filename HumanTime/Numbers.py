
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