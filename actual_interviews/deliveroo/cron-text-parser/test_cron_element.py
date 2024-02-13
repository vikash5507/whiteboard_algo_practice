import unittest
from cron_element import CronElement
from cron_element_type import CronElementType
from exceptions import InvalidRangeValueCronString, InvalidIntervalValueCronString, InvalidListValueCronString, InvalidCronString

class TestCronElement(unittest.TestCase):
    def test_decode_all_values(self):
        cron_elem = CronElement("*", CronElementType.MINUTES)
        self.assertEqual(cron_elem.decode(), "0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 "
                                             "27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 "
                                             "50 51 52 53 54 55 56 57 58 59")

    def test_decode_range(self):
        cron_elem = CronElement("10-15", CronElementType.MINUTES)
        self.assertEqual(cron_elem.decode(), "10 11 12 13 14 15")

    def test_decode_intervals(self):
        cron_elem = CronElement("*/10", CronElementType.MINUTES)
        self.assertEqual(cron_elem.decode(), "0 10 20 30 40 50")

    def test_decode_list_values(self):
        cron_elem = CronElement("1,3,5", CronElementType.MINUTES)
        self.assertEqual(cron_elem.decode(), "1 3 5")

    def test_decode_single_value(self):
        cron_elem = CronElement("30", CronElementType.MINUTES)
        self.assertEqual(cron_elem.decode(), "30")

    def test_invalid_range_value(self):
        cron_elem = CronElement("30-20", CronElementType.MINUTES)
        self.assertRaises(InvalidRangeValueCronString, cron_elem.decode)

    def test_invalid_interval_value(self):
        cron_elem = CronElement("*/0", CronElementType.MINUTES)
        self.assertRaises(InvalidIntervalValueCronString, cron_elem.decode)

    def test_invalid_list_value(self):
        cron_elem = CronElement("1,a,5", CronElementType.MINUTES)
        self.assertRaises(InvalidListValueCronString, cron_elem.decode)

    def test_invalid_cron_string(self):
        cron_elem = CronElement("abc", CronElementType.MINUTES)
        self.assertRaises(InvalidCronString, cron_elem.decode)

    def test_out_of_bound_single_value(self):
        cron_elem = CronElement("70", CronElementType.MINUTES)
        self.assertRaises(InvalidCronString, cron_elem.decode)

    def test_out_of_bound_range_value(self):
        cron_elem = CronElement("10-70", CronElementType.MINUTES)
        self.assertRaises(InvalidRangeValueCronString, cron_elem.decode)

    def test_invalid_interval_value_with_range(self):
        cron_elem = CronElement("10-20/0", CronElementType.MINUTES)
        self.assertRaises(ValueError, cron_elem.decode)

    def test_invalid_interval_value_with_single_value(self):
        cron_elem = CronElement("10/0", CronElementType.MINUTES)
        self.assertRaises(ValueError, cron_elem.decode)

    def test_range_with_single_value(self):
        cron_elem = CronElement("10-20,25", CronElementType.MINUTES)
        self.assertRaises(ValueError, cron_elem.decode)

    def test_invalid_cron_string_with_valid_range(self):
        cron_elem = CronElement("10-20-30", CronElementType.MINUTES)
        self.assertRaises(ValueError, cron_elem.decode)

    def test_invalid_cron_string_with_valid_interval(self):
        cron_elem = CronElement("*/10-20", CronElementType.MINUTES)
        self.assertRaises(ValueError, cron_elem.decode)


if __name__ == '__main__':
    unittest.main()
