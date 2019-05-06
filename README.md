
# `HumanTime`
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
