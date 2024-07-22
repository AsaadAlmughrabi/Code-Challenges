import pytest
from challenge02 import first_repeated_word  # Adjust the import based on your file name

def test_first_repeated_word():
    # Test cases
    assert first_repeated_word("ASAC is a department at LTUC. ASAC teaches programming in LTUC.") == "ASAC"
    assert first_repeated_word("I am learning programming at ASAC.") == "No Repetition"
    assert first_repeated_word("Hello world, Hello again!") == "Hello"
    assert first_repeated_word("Python is great. Python is fun!") == "Python"
    assert first_repeated_word("Unique words only here!") == "No Repetition"
    assert first_repeated_word("This test is a test for a basic test case.") == "test"

if __name__ == "__main__":
    pytest.main()
