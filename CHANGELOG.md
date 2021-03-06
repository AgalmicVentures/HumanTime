# Change Log

## [0.1.9] - 2020-11-28
### Changed
- Fix name of Remembrance Day in Canada.

## [0.1.8] - 2020-11-28
### Added
- Other Canadian holidays: Victoria Day, Thanksgiving, Remembrance Day.
- Limited UK holiday support.
- More general parsing of holiday names (e.g. 'Easter Sunday', 'Christmas day').
### Changed
- Fix bug in corner case of 'next April' in certain situations.
- Fix name of Labour Day in Canada.
- Improve accuracy of Labor Day (`None` before 1984).

## [0.1.7] - 2020-09-11
### Added
- Helpers for weekdays.
### Changed
- Fix bugs in holiday calendars.

## [0.1.6] - 2020-04-13
### Added
- Support for international holiday calendars, starting with Canada.
- Support for concatenated durations: '3min', '4wks', etc.
### Changed
- Simplify naming of parameters to holiday calendar generation.

## [0.1.5] - 2019-10-16
### Added
- Annual keywords (`May 2010`, `Easter 2021`).
### Changed
- Fix bug in holiday calendar generation when holiday does not occur and observed flag is True.

## [0.1.4] - 2019-08-30
### Added
- More numbers (`thousand`), holiday aliases (`holy day`), and more prepositions.
- More abbreviations (`tmrw`, `yda`, etc.).
- Recurrence rules (`for d in Recurrence('next Thanksgiving', count=10): ...`).
- Optional observance rule for holiday calendar generation.
### Changed
- Correct handling of `this day / hour / minute / second`.

## [0.1.3] - 2019-06-14
### Added
- Support for `hence`, `later`, and `earlier` to complement `ago`.
- Two word named holiday support (`the business day before Labor Day`).
### Changed
- Allow customization for holiday calendar generation.
- Use [Butcher's algorithm](https://en.wikipedia.org/wiki/Computus) to calculate Easter.

## [0.1.2] - 2019-06-08
### Added
- Day of year support (`next 2-28`).
- Single word holiday name support (`last Thanksgiving`).
- Good Friday and Easter holidays from 2010 to 2069.

## [0.1.1] - 2019-06-02
### Changed
- Correct first year for Veterans’ Day.

## [0.1.0] - 2019-06-01
### Added
- All baseline features including...
- Holiday calendar with support for calculating business days.
- NLP date and time parsing with:
	- Numbers: cardinals and ordinals (`two`, `sixth`, `30th`).
	- Absolute durations: `N <UNIT>` (`3 sec`, `15 minutes`, `6 days`).
	- Times with absolute and variable durations (months, business days, etc.):
		- `now` / `today` / `tomorrow` / `yesterday` / etc.
		- `<DURATION> before / after / etc. <TIME>`
		- `<DURATION> ago`
		- `next` / `last` / etc. `<UNIT>` / `<DAY OF WEEK>` / `<MONTH>` / etc.
		- `<TIME> <TIME OF DAY AM / PM>`

[0.1.9]: https://github.com/AgalmicVentures/HumanTime/compare/0.1.8...0.1.9
[0.1.8]: https://github.com/AgalmicVentures/HumanTime/compare/0.1.7...0.1.8
[0.1.7]: https://github.com/AgalmicVentures/HumanTime/compare/0.1.6...0.1.7
[0.1.6]: https://github.com/AgalmicVentures/HumanTime/compare/0.1.5...0.1.6
[0.1.5]: https://github.com/AgalmicVentures/HumanTime/compare/0.1.4...0.1.5
[0.1.4]: https://github.com/AgalmicVentures/HumanTime/compare/0.1.3...0.1.4
[0.1.3]: https://github.com/AgalmicVentures/HumanTime/compare/0.1.2...0.1.3
[0.1.2]: https://github.com/AgalmicVentures/HumanTime/compare/0.1.0...0.1.2
[0.1.1]: https://github.com/AgalmicVentures/HumanTime/compare/0.1.0...0.1.1
[0.1.0]: https://github.com/AgalmicVentures/HumanTime/releases/tag/0.1.0
