import unittest
from ProductCode.staircase import staircase # Import ฟังก์ชันมาทดสอบ [cite: 51]

class StaircaseTest(unittest.TestCase): # สร้าง Class สำหรับทดสอบ [cite: 53]
    def test_give_n_2_should_be_staircase_2_layers(self):
        # Arrange
        n = 2
        pattern = '#'
        expected_output = " #\n##"
        
        # Act
        result = staircase(n, pattern)
        
        # Assert
        self.assertEqual(result, expected_output) # ตรวจสอบค่า [cite: 31, 121]