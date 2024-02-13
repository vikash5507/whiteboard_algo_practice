import unittest
from cron_parser import CronParser
from exceptions import InvalidCronString, InvalidRangeValueCronString
from test_cron_element import TestCronElement

class TestCronParser(unittest.TestCase):
    def setUp(self):
        self.parser = CronParser()

    def test_valid_cron_string(self):
        cron_string = "*/15 0 1,15 * 1-5 /usr/bin/find"
        expected_output = """minutes       0 15 30 45
hours         0
day of month  1 15
month         1 2 3 4 5 6 7 8 9 10 11 12
day of week   1 2 3 4 5
command       /usr/bin/find"""
        self.assertEqual(self.parser.parse(cron_string), expected_output)

    def test_valid_range(self):
        cron_string = "1-5 0 1,15 * 1-5 /usr/bin/find"
        expected_output = """minutes       1 2 3 4 5
hours         0
day of month  1 15
month         1 2 3 4 5 6 7 8 9 10 11 12
day of week   1 2 3 4 5
command       /usr/bin/find"""
        self.assertEqual(self.parser.parse(cron_string), expected_output)

    def test_valid_interval(self):
        cron_string = "*/15 0 1,15 * */2 /usr/bin/find"
        expected_output = """minutes       0 15 30 45
hours         0
day of month  1 15
month         1 2 3 4 5 6 7 8 9 10 11 12
day of week   2 4 6
command       /usr/bin/find"""
        self.assertEqual(self.parser.parse(cron_string), expected_output)

    def test_valid_list(self):
        cron_string = "1,15 0 1,15 * 1-5 /usr/bin/find"
        expected_output = """minutes       1 15
hours         0
day of month  1 15
month         1 2 3 4 5 6 7 8 9 10 11 12
day of week   1 2 3 4 5
command       /usr/bin/find"""
        self.assertEqual(self.parser.parse(cron_string), expected_output)

    def test_valid_every_value(self):
        cron_string = "* * * * * /usr/bin/find"
        expected_output = """minutes       0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59
hours         0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
day of month  1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31
month         1 2 3 4 5 6 7 8 9 10 11 12
day of week   1 2 3 4 5 6 7
command       /usr/bin/find"""
        self.assertEqual(self.parser.parse(cron_string), expected_output)

    def test_invalid_cron_string(self):
        cron_string = "*/15 0 1,15 * 1-5"
        with self.assertRaises(InvalidCronString):
            self.parser.parse(cron_string)

    def test_missing_elements(self):
        cron_string = "*/15 0 1,15 * 1-5"
        with self.assertRaises(InvalidCronString):
            self.parser.parse(cron_string)

    def test_invalid_range_value(self):
        cron_string = "*/15 0 1,15 * 1-70 /usr/bin/find"
        with self.assertRaises(InvalidRangeValueCronString):
            self.parser.parse(cron_string)

    def test_invalid_interval_value(self):
        cron_string = "*/15 0 1,15 * 1-/usr/bin/find"
        with self.assertRaises(InvalidCronString):
            self.parser.parse(cron_string)

    def test_invalid_list_value(self):
        cron_string = "*/15 0 1,15 * 1,2,abc /usr/bin/find"
        with self.assertRaises(ValueError):
            self.parser.parse(cron_string)

    def test_invalid_command(self):
        cron_string = "*/15 0 1,15 * 1-5"
        with self.assertRaises(InvalidCronString):
            self.parser.parse(cron_string)


if __name__ == '__main__':
    unittest.main()
    test_cron_element = TestCronElement()
    test_cron_element.run()
