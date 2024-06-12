import io
from contextlib import redirect_stdout
import unittest
from unittest.mock import patch
from main import *

class TestMainFunction(unittest.TestCase):
    @patch("builtins.input", side_effect=["P", "M", "T+", "T+", "T-", "P", "P", "M", "T+", "quit"])
    def test_thermostat(self, mock_input):
        expected_output = (
            "Power: Off\n"
            "Power: On\nTemperature: 70°F\nMode: Heating\n"
            "Power: On\nTemperature: 70°F\nMode: Cooling\n"
            "Power: On\nTemperature: 71°F\nMode: Cooling\n"
            "Power: On\nTemperature: 72°F\nMode: Cooling\n"
            "Power: On\nTemperature: 71°F\nMode: Cooling\n"
            "Power: Off\n"
            "Power: On\nTemperature: 71°F\nMode: Cooling\n"
            "Power: On\nTemperature: 71°F\nMode: Fan\n"
            "Power: On\nTemperature: 72°F\nMode: Fan\n"
        )

        f = io.StringIO()
        with redirect_stdout(f):
            main()
        output = f.getvalue()
        self.assertEqual(output, expected_output)

if __name__ == "__main__":
    unittest.main()
