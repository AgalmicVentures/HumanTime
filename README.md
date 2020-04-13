
# HumanTime
`HumanTime` is time for humans in Python.

Sidestep tedious and error-prone code in favor of a simple, English-based DSL for specifying absolute and relative times:

    HumanTime.parseTime(Input) | Input
    ---------------------------+------------------------------------------
	2019-05-05 19:32:28.493048 | now
	2019-05-05 00:00:00.000000 | today
	2019-05-05 12:00:00.000000 | noon
	2019-05-04 00:00:00.000000 | yesterday
	2019-05-06 00:00:00.000000 | tomorrow
	2019-05-06 12:00:00.000000 | tomorrow at noon
	2019-05-06 15:30:00.000000 | tomorrow at 3:30PM
	2019-05-08 00:00:00.000000 | Wednesday
	2019-05-05 22:32:28.493048 | 3hrs from now
	2019-05-05 22:31:28.493048 | 1 minute before 3 hours from now
	2019-05-05 13:00:00.000000 | an hour after noon
	2019-05-05 20:00:00.000000 | eight hours after noon
	2019-04-30 00:00:00.000000 | 3 months after 2019-1-31
	2021-02-28 00:00:00.000000 | 1 year after 2020-02-29
	2019-01-01 00:00:02.000000 | second second after 2019-01-01
	2019-06-16 00:00:00.000000 | 1 month after Thurs after 2019-5-9
	2019-07-05 00:00:00.000000 | business day after 2019-7-3
	2019-07-08 00:00:00.000000 | couple bus days after 2019-7-3
	2021-04-04 00:00:00.000000 | Easter 2021

## Installation
To install, simply use `pip`:

	> python3 -m pip install HumanTime

## Usage
Behold the simplicity and elegance of `HumanTime` --

### Times
	>>> import HumanTime
	>>> HumanTime.parseTime('now')
	datetime.datetime(2019, 5, 5, 20, 38, 10, 119936)
	>>> HumanTime.parseTime('3 hours from now')
	datetime.datetime(2019, 5, 5, 23, 38, 13, 120777)
	>>> HumanTime.parseTime('2019-1-3')
	datetime.datetime(2019, 1, 3, 0, 0)
	>>> HumanTime.parseTime('three days before 2019-1-3')
	datetime.datetime(2018, 12, 31, 0, 0)
	>>> HumanTime.parseTime('a month after 20200131')
	datetime.datetime(2020, 2, 29, 0, 0)
	>>> HumanTime.parseTime('Tuesday')
	datetime.datetime(2019, 5, 7, 0, 0)
	>>> HumanTime.parseTime('wed')
	datetime.datetime(2019, 5, 8, 0, 0)
	>>> HumanTime.parseTime('Thurs after 2019-5-9')
	datetime.datetime(2019, 5, 16, 0, 0)
	>>> HumanTime.parseTime('2 business days before 2019-7-8')
	datetime.datetime(2019, 7, 3, 0, 0)

### Durations
Fixed-length durations, representable by a `datetime.timedelta`, may also be parsed:

	>>> HumanTime.parseDuration('3 seconds')
	datetime.timedelta(seconds=3)
	>>> HumanTime.parseDuration('3 minutes')
	datetime.timedelta(seconds=180)
	>>> HumanTime.parseDuration('3 days')
	datetime.timedelta(days=3)
	>>> HumanTime.parseDuration('three weeks')
	datetime.timedelta(days=21)

### Numbers
Simple numbers (those necessary for parsing times) can also be parsed separately:

	>>> HumanTime.parseCardinal('four')
	4
	>>> HumanTime.parseOrdinal('fourth')
	4
	>>> HumanTime.parseNumber('20th')
	20
	>>> HumanTime.parseNumber('45')
	45

### Tools
Common actions are packaged as CLI tools and can be found in the `HumanTime.Tools` module.

#### `GenerateHolidayCalendar`
Generates a holiday calendar CSV with optional from and to years, headers, and observance rules.

	> python3 -m HumanTime.Tools.GenerateHolidayCalendar -f 2020 -t 2021 -o
	Date,Country,Name
	2020-01-01,US,New Year's Day
	2020-01-20,US,Martin Luther King Jr. Day
	2020-02-17,US,Presidents' Day
	2020-04-10,US,Good Friday
	2020-05-25,US,Memorial Day
	2020-07-03,US,Independence Day (Observed)
	2020-09-07,US,Labor Day
	...

## Development

### Unit Tests
Unit tests can be run with the following command:

    > python3 -m unittest discover
	...........................................................................
	----------------------------------------------------------------------
	Ran 75 tests in 0.020s

	OK

### CI
Continuous integration is handled in Gitlab CI via `.gitlab-ci.yml`.
