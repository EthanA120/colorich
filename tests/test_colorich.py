import unittest
from colorich import enrich, dye, printr, printd


class TestColorich(unittest.TestCase):
    def test_enrich_named_color(self):
        output = enrich("Hello", fore="red")
        self.assertIn("\x1b[38;2;255;0;0mHello\x1b[0m", output)

    def test_enrich_case_insensitive_and_spaces(self):
        output1 = enrich("Sea", fore="SeaGreen")
        output2 = enrich("Sea", fore="sea green")
        self.assertEqual(output1, output2)

    def test_enrich_hex_6_chars(self):
        output_with_hash = enrich("Test", fore="#FF0000")
        output_no_hash = enrich("Test", fore="FF0000")
        self.assertEqual(output_with_hash, output_no_hash)
        self.assertIn("38;2;255;0;0", output_with_hash)

    def test_enrich_hex_3_chars(self):
        output_short = enrich("Test", fore="#F00")
        output_full = enrich("Test", fore="#FF0000")
        self.assertEqual(output_short, output_full)

    def test_enrich_rgb_tuple(self):
        output = enrich("RGB", fore=(10, 20, 30), back=(40, 50, 60))
        self.assertIn("38;2;10;20;30", output)
        self.assertIn("48;2;40;50;60", output)

    def test_enrich_decorations(self):
        output_bold = enrich("Bold", decor="bold")
        output_b = enrich("Bold", decor="b")
        self.assertEqual(output_bold, output_b)
        self.assertIn("\x1b[1mBold\x1b[0m", output_bold)

    def test_dye_dictionary(self):
        res = dye({"One": "red", "Two": "blue"})
        self.assertIn("One", res)
        self.assertIn("Two", res)
        self.assertIn("38;2;255;0;0", res)
        self.assertIn("38;2;0;0;255", res)

    def test_invalid_color_graceful(self):
        # Should not crash on invalid color name
        output = enrich("Safe", fore="NonExistentColor123")
        self.assertIn("Safe", output)


if __name__ == "__main__":
    unittest.main()
