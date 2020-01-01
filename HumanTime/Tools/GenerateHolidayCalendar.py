#!/usr/bin/env python3

# Copyright (c) 2015-2020 Agalmic Ventures LLC (www.agalmicventures.com)
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

import argparse
import datetime
import os
import sys

import inspect
_currentFile = os.path.abspath(inspect.getfile(inspect.currentframe()))
_currentDir = os.path.dirname(_currentFile)
_parentDir = os.path.dirname(os.path.dirname(_currentDir))
sys.path.insert(0, _parentDir)

from HumanTime import Holidays

def main():
	parser = argparse.ArgumentParser(description='Holiday Calender Generator')

	now = datetime.datetime.now()
	parser.add_argument('-f', '--from-year', type=int, default=1900,
		help='Year to compute holidays from.')
	parser.add_argument('-t', '--to-year', type=int, default=now.year,
		help='Year to compute holidays to.')
	parser.add_argument('-c', '--country', default='US',
		help='ISO 3166-1 2 digit country code to generate holidays for.')

	parser.add_argument('-n', '--no-headers', action='store_true',
		help='Do not include headers.')
	parser.add_argument('-o', '--observed', action='store_true',
		help='Calculate the day observed for holidays falling on weekends.')

	arguments = parser.parse_args(sys.argv[1:])

	holidays = Holidays.COUNTRY_TO_HOLIDAYS.get(arguments.country)
	if holidays is None:
		print('Country %s not found' % arguments.country)
		return 1

	if not arguments.no_headers:
		print('Date,Country,Name')

	calendar = Holidays.holidayCalendar(arguments.from_year, arguments.to_year,
		holidays=holidays,
		observed=arguments.observed)
	for date, name in calendar:
		print('%s,%s,%s' % (date.strftime('%Y-%m-%d'), arguments.country, name))

	return 0

if __name__ == '__main__':
	sys.exit(main())
