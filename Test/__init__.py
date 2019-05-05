
import datetime
import unittest

import HumanTime

class HumanTimeTest(unittest.TestCase):
	"""
	Tests for functions in the HumanTime module.
	"""

	def test_tokenize_empty(self):
		self.assertEqual(HumanTime.tokenize(''), [])
		self.assertEqual(HumanTime.tokenize('     '), [])

	def test_tokenize_single(self):
		self.assertEqual(HumanTime.tokenize('now'), ['now'])
		self.assertEqual(HumanTime.tokenize('now   '), ['now'])
		self.assertEqual(HumanTime.tokenize('    now'), ['now'])
		self.assertEqual(HumanTime.tokenize('  now  '), ['now'])

	def test_tokenize(self):
		self.assertEqual(HumanTime.tokenize('3 hours from now'), ['3', 'hours', 'from', 'now'])

	def test_parseDuration_empty(self):
		with self.assertRaises(ValueError):
			HumanTime.parseDuration('')

	def test_parseDuration(self):
		self.assertEqual(HumanTime.parseDuration('second'), datetime.timedelta(seconds=1))
		self.assertEqual(HumanTime.parseDuration('week'), datetime.timedelta(days=7))

		self.assertEqual(HumanTime.parseDuration('3 minutes'), datetime.timedelta(seconds=180))
		self.assertEqual(HumanTime.parseDuration('180 seconds'), datetime.timedelta(seconds=180))

		self.assertEqual(HumanTime.parseDuration('3 days'), datetime.timedelta(days=3))
		self.assertEqual(HumanTime.parseDuration('72 hours'), datetime.timedelta(days=3))

	def test_paseTimestamp(self):
		self.assertEqual(HumanTime.parseTimestamp('2019-04-02'), datetime.datetime(2019, 4, 2))

	def test_now(self):
		t1 = datetime.datetime.now()
		now = HumanTime.now()
		t2 = datetime.datetime.now()

		self.assertLessEqual(t1, now)
		self.assertLessEqual(now, t2)

		nowT2 = HumanTime.now(t=t2)
		nowT1 = HumanTime.now(t=t1)
		self.assertEqual(t1, nowT1)
		self.assertEqual(t2, nowT2)

	def test_noon(self):
		noon = HumanTime.noon()
		self.assertEqual(noon.hour, 12)
		self.assertEqual(noon.minute, 0)
		self.assertEqual(noon.second, 0)
		self.assertEqual(noon.microsecond, 0)

	def test_today(self):
		today = HumanTime.today()
		self.assertEqual(today.hour, 0)
		self.assertEqual(today.minute, 0)
		self.assertEqual(today.second, 0)
		self.assertEqual(today.microsecond, 0)

	def test_tomorrow(self):
		tomorrow = HumanTime.tomorrow()
		self.assertEqual(tomorrow.hour, 0)
		self.assertEqual(tomorrow.minute, 0)
		self.assertEqual(tomorrow.second, 0)
		self.assertEqual(tomorrow.microsecond, 0)

	def test_yesterday(self):
		yesterday = HumanTime.yesterday()
		self.assertEqual(yesterday.hour, 0)
		self.assertEqual(yesterday.minute, 0)
		self.assertEqual(yesterday.second, 0)
		self.assertEqual(yesterday.microsecond, 0)

	def test_parseTime_empty(self):
		with self.assertRaises(ValueError):
			HumanTime.parseTime('')

	def test_parseTime_invalid(self):
		with self.assertRaises(ValueError):
			HumanTime.parseTime('asdf')
		with self.assertRaises(ValueError):
			HumanTime.parseTime('1 year asdf now')
		with self.assertRaises(ValueError):
			HumanTime.parseTime('now now')
		with self.assertRaises(ValueError):
			HumanTime.parseTime('after now')
		with self.assertRaises(ValueError):
			HumanTime.parseTime('1 after now')

	def test_parseTime(self):
		t1 = datetime.datetime.now()
		now = HumanTime.parseTime('now')
		t2 = datetime.datetime.now()

		self.assertLessEqual(t1, now)
		self.assertLessEqual(now, t2)

		self.assertEqual(HumanTime.parseTime('1 year after 2019-2-1'), datetime.datetime(2020, 2, 1))
		self.assertEqual(HumanTime.parseTime('12 months after 2019-2-1'), datetime.datetime(2020, 2, 1))

		self.assertEqual(HumanTime.parseTime('1 year after 2020-2-28'), datetime.datetime(2021, 2, 28))
		self.assertEqual(HumanTime.parseTime('12 months after 2020-2-28'), datetime.datetime(2021, 2, 28))

		self.assertEqual(HumanTime.parseTime('1 year after 2020-2-29'), datetime.datetime(2021, 2, 28))
		self.assertEqual(HumanTime.parseTime('12 months after 2020-2-29'), datetime.datetime(2021, 2, 28))
