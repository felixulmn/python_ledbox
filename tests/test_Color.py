import unittest

from python_ledbox import Color


class TestColor(unittest.TestCase):
    def test_rgb_setter_and_getter(self):
        """Test that setter and getter convert colors as intended."""

        test_colors = [
            {"input": (242, 154, 111), "value": 15899247},
            {"input": (8, 102, 99), "value": 550499},
            {"input": (255, 255, 255), "value": 16777215},
            {"input": (0, 0, 0), "value": 0},
        ]

        for c in test_colors:
            intColor = Color.from_rgb(*c["input"])
            self.assertEqual(Color.to_rgb(intColor), c["input"])
