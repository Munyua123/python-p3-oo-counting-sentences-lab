#!/usr/bin/env python3

class MyString:
    
    def __init__(self):
        self._value = None

    def get_value(self):
        return self._value
    
    def set_value(self, value):
        if not isinstance(value, str):
            print("The value must be a string.")
        else:
             self._value = value

    def is_sentence(self):
        return self._value.endswith('.')
    
    def is_question(self):
        return self._value.endswith("?")
    
    def is_exclamation(self):
        return self._value.endswith("!")
    
    def count_sentences(self):
        value_with_periods = self._value.replace('?', '.').replace('!', '.')
        sentences = value_with_periods.split('.')
        return len([sentence for sentence in sentences if sentence.strip()])
    value = property(get_value, set_value)

string = MyString()

string.set_value("This is a sentence. And another one! What about this?")
print(string.is_question())
print(string.count_sentences())




