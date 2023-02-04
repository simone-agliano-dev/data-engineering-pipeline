import unittest

from src.app.utilities.utils import validate_fields


class TestValidateFields(unittest.TestCase):
    def test_validate_fields(self):
        test_data = {"mock_field1": "mock_field1", "mock_field2": "mock_value2"}
        fields = ["mock_field1", "mock_field2"]
        self.assertTrue(validate_fields(test_data, fields))

    def test_validate_fields_missing(self):
        test_data = {"mock_field1": "mock_field1"}
        fields = ["mock_field1", "mock_field2"]
        self.assertRaises(AssertionError, validate_fields, test_data, fields)
