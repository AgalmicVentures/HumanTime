
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
	2019-05-05 22:32:28.493048 | 3 hours from now
	2019-05-05 22:31:28.493048 | 1 minute before 3 hours from now
	2019-04-30 00:00:00.000000 | 3 months after 2019-1-31
	2021-02-28 00:00:00.000000 | 1 year after 2020-02-29

## Installation
To install, simply use `pip`:

	> python3 -m pip install HumanTime

## Usage
Behold the simplicity and elegance of `HumanTime`:

	> python3
	Python 3.7.2 (default, Feb 12 2019, 08:15:36)
	[Clang 10.0.0 (clang-1000.11.45.5)] on darwin
	Type "help", "copyright", "credits" or "license" for more information.
	>>> import HumanTime
	>>> HumanTime.parseTime('now')
	datetime.datetime(2019, 5, 5, 20, 38, 10, 119936)
	>>> HumanTime.parseTime('3 hours from now')
	datetime.datetime(2019, 5, 5, 23, 38, 13, 120777)
	>>> HumanTime.parseTime('2019-1-3')
	datetime.datetime(2019, 1, 3, 0, 0)
	>>> HumanTime.parseTime('3 days before 2019-1-3')
	datetime.datetime(2018, 12, 31, 0, 0)
	>>> HumanTime.parseTime('1 month after 20200131')
	datetime.datetime(2020, 2, 29, 0, 0)

## Development

### Unit Tests
Unit tests can be run with the following command:

    > python3 -m unittest discover
    ..............
	----------------------------------------------------------------------
	Ran 14 tests in 0.006s

	OK

### CI
Continuous integration is handled in Gitlab CI via `.gitlab-ci.yml`.
