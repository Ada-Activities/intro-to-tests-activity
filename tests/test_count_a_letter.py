from main import count_a_letter
import pytest

def test_check_correct_count():
    sentence = "This is a sentence"
    letter = "a"
    count = count_a_letter(sentence,letter)
    assert count == 1

def test_non_alphabetic_input_in_string():
    sentence = "This is a sentence"
    letter = "10"
    count = count_a_letter(sentence,letter)
    assert count is None

def test_input_empty_strings():
    sentence = ""
    letter = ""
    count = count_a_letter(sentence,letter)
    assert count is None
    

# Delete the demo tests and add your tests here 

# def count_a_letter(sentence, letter):
#     if not letter.isalpha():
#         return None
#     if not sentence:
#         return None
    
#     count = 0
#     for char in sentence:
#         if char == letter:
#             count +=1
    
#     return count