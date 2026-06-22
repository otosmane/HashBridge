# test_hashbridge.py
"""
Tests for HashBridge module.
"""

import unittest
from hashbridge import HashBridge

class TestHashBridge(unittest.TestCase):
    """Test cases for HashBridge class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = HashBridge()
        self.assertIsInstance(instance, HashBridge)
        
    def test_run_method(self):
        """Test the run method."""
        instance = HashBridge()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
