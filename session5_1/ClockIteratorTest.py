from ClockIterator import ClockIterator
import unittest


class MyTestCase(unittest.TestCase):
    def first_test(self):
        self.assertEqual(ClockIterator().user_iter(1), "00:00")

    def first_test(self):
        self.assertEqual(ClockIterator().user_iter(60), "00:59")
    def second_test(self):
        self.assertEqual(ClockIterator().user_iter(61), "01:00")
    def third_test(self):
        self.assertEqual(ClockIterator().user_iter(1440), "23:59")


if __name__ == '__main__':
    unittest.main()
