#!/usr/bin/env python3

class MyString:
    def __init__(self, value=""):
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if isinstance(value, str):
            self._value = value
        else:
            print("The value must be a string.")
    def is_sentence(self):
        return self.value.endswith(".")

    def is_question(self):
        return self.value.endswith("?")

    def is_exclamation(self):
        if self.value[-1] == "!":
            return True
        else:
            return False

    def count_sentences(self):
        if self.value == "":
            return 0
        else:
            import re
            return len(re.split(r"[.?!] ", self.value))
  