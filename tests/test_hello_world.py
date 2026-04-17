import unittest
from hello_world import validate_name


class TestValidateName(unittest.TestCase):
    """Test cases for name validation"""
    
    def test_valid_name_single_letter(self):
        """Test valid single letter name"""
        is_valid, error = validate_name("A")
        self.assertTrue(is_valid)
        self.assertIsNone(error)
    
    def test_valid_name_normal(self):
        """Test valid normal name"""
        is_valid, error = validate_name("Alice")
        self.assertTrue(is_valid)
        self.assertIsNone(error)
    
    def test_valid_name_max_length(self):
        """Test valid name at maximum length (15 chars)"""
        is_valid, error = validate_name("AlexanderSmithB")  # exactly 15 chars, all letters
        self.assertTrue(is_valid)
        self.assertIsNone(error)
    
    def test_invalid_empty_string(self):
        """Test empty string"""
        is_valid, error = validate_name("")
        self.assertFalse(is_valid)
        self.assertIsNotNone(error)
    
    def test_invalid_too_long(self):
        """Test name exceeding 15 characters"""
        is_valid, error = validate_name("AlexanderTheGreatPlus")
        self.assertFalse(is_valid)
        self.assertIn("no more than 15", error)
    
    def test_invalid_with_numbers(self):
        """Test name with numbers"""
        is_valid, error = validate_name("Alice123")
        self.assertFalse(is_valid)
        self.assertIn("only letters", error)
    
    def test_invalid_with_special_chars(self):
        """Test name with special characters"""
        is_valid, error = validate_name("Alice@Smith")
        self.assertFalse(is_valid)
        self.assertIn("only letters", error)
    
    def test_invalid_with_spaces(self):
        """Test name with spaces"""
        is_valid, error = validate_name("Alice Smith")
        self.assertFalse(is_valid)
        self.assertIn("only letters", error)
    
    def test_invalid_not_string(self):
        """Test non-string input"""
        is_valid, error = validate_name(123)
        self.assertFalse(is_valid)
        self.assertIn("string", error)


if __name__ == "__main__":
    unittest.main()
