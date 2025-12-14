# test_esbuildswift.py
"""
Tests for EsbuildSwift module.
"""

import unittest
from esbuildswift import EsbuildSwift

class TestEsbuildSwift(unittest.TestCase):
    """Test cases for EsbuildSwift class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = EsbuildSwift()
        self.assertIsInstance(instance, EsbuildSwift)
        
    def test_run_method(self):
        """Test the run method."""
        instance = EsbuildSwift()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
