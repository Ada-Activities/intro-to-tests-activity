from main import count_a_letter
import pytest

def test_non_alpha_letter_returns_none():
    test_sentence = "hello world"
    test_letter = "3"

    result = count_a_letter(test_sentence, test_letter)

    assert result is None

def test_empty_string_sentence_returns_none():
    test_sentence = ""
    test_letter = "e"

    result = count_a_letter(test_sentence, test_letter)

    assert result is None

def test_empty_list_sentence_returns_none():
    test_sentence = []
    test_letter = "e"

    result = count_a_letter(test_sentence, test_letter)

    assert result is None

def test_string_with_no_matches_returns_0():
    test_sentence = "hello world"
    test_letter = "q"

    result = count_a_letter(test_sentence, test_letter)

    assert result == 0

def test_list_with_no_matches_returns_0():
    test_sentence = list("hello world")
    test_letter = "q"

    result = count_a_letter(test_sentence, test_letter)

    assert result == 0

def test_string_with_one_match_returns_1():
    test_sentence = "hello world"
    test_letter = "w"

    result = count_a_letter(test_sentence, test_letter)

    assert result == 1

def test_list_with_one_match_returns_1():
    test_sentence = list("hello world")
    test_letter = "w"

    result = count_a_letter(test_sentence, test_letter)

    assert result == 1

def test_string_with_multiple_matches_returns_count():
    test_sentence = "hello world"
    test_letter = "l"

    result = count_a_letter(test_sentence, test_letter)

    assert result == 3

def test_list_with_multiple_matches_returns_count():
    test_sentence = list("hello world")
    test_letter = "l"

    result = count_a_letter(test_sentence, test_letter)

    assert result == 3

def test_string_with_substring_returns_0():
    test_sentence = "hello world"
    test_letter = "ello"

    result = count_a_letter(test_sentence, test_letter)

    assert result == 0

def test_list_with_substring_returns_0():
    test_sentence = list("hello world")
    test_letter = "ello"

    result = count_a_letter(test_sentence, test_letter)

    assert result == 0

# bonus
def test_non_string_letter_reports_error():
    test_sentence = "hello world"
    test_letter = 3

    with pytest.raises(AttributeError):
        count_a_letter(test_sentence, test_letter)

