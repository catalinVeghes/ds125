#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 11:06:54 2019

@author: DataScience 125
"""

from hangman import *

#
# Test code
#

def test_is_word_guessed():
    """
    Unit test for is_word_guessed
    """
    failure = False
    word1 = "apple"
    letters_guessed1 = ['a', 'b', 'c']
    letters_guessed2 = ['a', 'p', 'l', 'e']

    if is_word_guessed(word1, letters_guessed1):
        print("FAILURE: is_word_guessed()")
        print("\tExpected return was true but", word1, "for guessed letters", letters_guessed1, "should be false.")
        failure = True
    if not is_word_guessed(word1, letters_guessed2):
        print("FAILURE: is_word_guessed()")
        print("\tExpected return was false but", word1, "for guessed letters", letters_guessed2, "should be true.")
        failure = True
    
    if not failure:
        print("SUCCESS: test_get_word_score()")
        
def test_get_available_letters():
    """
    Unit test for get_available_letters
    """    
    failure = False
    letters_guessed1 = ['a', 'b', 'c']
    
    if get_available_letters(letters_guessed1) != "d e f g h i j k l m n o p q r s t u v w x y z ":
        print("FAILURE: get_available_letters()")
        print("\tThe alphabet was not updated and returned properly.")
        failure = True
    
    if not failure:
        print("SUCCESS: get_available_letters()")
        


print("----------------------------------------------------------------------")
print("Testing is_word_guessed...")
test_is_word_guessed()
print("----------------------------------------------------------------------")
print("Testing get_available_letters...")
test_get_available_letters()
print("All done!")
