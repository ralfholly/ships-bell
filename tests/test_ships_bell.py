import unittest

from ships_bell import ShipsBell

class TestShipsBell(unittest.TestCase):
    def test_strike_computation(self):
        sb = ShipsBell()
        # Full hours.
        self.assertEqual((1, 0), sb.compute_strikes(1, 0))
        self.assertEqual((2, 0), sb.compute_strikes(2, 0))
        self.assertEqual((3, 0), sb.compute_strikes(3, 0))
        self.assertEqual((4, 0), sb.compute_strikes(4, 0))
        self.assertEqual((1, 0), sb.compute_strikes(5, 0))
        self.assertEqual((2, 0), sb.compute_strikes(6, 0))

        # Half hours.
        self.assertEqual((1, 1), sb.compute_strikes(1, 30))
        self.assertEqual((1, 0), sb.compute_strikes(1, 31))
        self.assertEqual((1, 0), sb.compute_strikes(1, 29))

        self.assertEqual((4, 0), sb.compute_strikes(0, 0))
        self.assertEqual((0, 1), sb.compute_strikes(0, 30))
        self.assertEqual((3, 1), sb.compute_strikes(23, 30))
        self.assertEqual((4, 0), sb.compute_strikes(24, 0))
        self.assertEqual((4, 0), sb.compute_strikes(0, 0))
        self.assertEqual((0, 1), sb.compute_strikes(0, 30))

    def test_sleep_time_computation(self):
        sb = ShipsBell()
        self.assertAlmostEqual(30.0 / 2.0 * 60.0, sb.compute_sleep_time(30))
        self.assertAlmostEqual(30.0 / 2.0 * 60.0, sb.compute_sleep_time(0))
        self.assertAlmostEqual((30.0 - 22.0) / 2.0 * 60.0, sb.compute_sleep_time(22))
        self.assertAlmostEqual((30.0 - 28.0) / 2.0 * 60.0, sb.compute_sleep_time(28))
        self.assertAlmostEqual(1.0, sb.compute_sleep_time(29))
        self.assertAlmostEqual(1.0, sb.compute_sleep_time(59))
        self.assertAlmostEqual(60.0, sb.compute_sleep_time(28))
        self.assertAlmostEqual(60.0, sb.compute_sleep_time(58))

