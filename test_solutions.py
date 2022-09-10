from tabnanny import check
from interview_mock import *
import pytest

class TestIsUnique:
    def test_1(self):
        assert isUnique("hello") == False

    def test_2(self):
        assert isUnique("Daniel") == True
    
    def test_3(self):
        assert isUnique("Brian") == True
    
    def test_4(self):
        assert isUnique("onomonopia") == False


class Test_check_permuatation:
    def test_1(self):
        assert checkPermutation("god", "dog") == True
    
    def test_2(self):
        assert checkPermutation("cat", "mat") == False
    
    def test_3(self):
        assert checkPermutation("ABCDEFG", "GEFABCD") == True


class Test_URLify:
    def test_1(self):
        str = "Mr Daniel Hwang    "
        assert URLify(str, len(str)) == "Mr%20Daniel%20Hwang"
    
    def test_2(self):
        str = "Mr D  "
        assert URLify(str, len(str)) == "Mr%20D"

class Test_isPalindromePerm:
    def test_1(self):
        assert isPalindromePerm("taco cat")
    
    def test_2(self):
        assert isPalindromePerm("tcao act")