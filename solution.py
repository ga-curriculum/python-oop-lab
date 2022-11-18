class Vowels:
	def __init__(self, str_input):
		pass

	def check_vowels(self):
		pass


class StringCount:
	def __init__(self, str_input):
		pass

	def find_bob(self):
		pass


class StringReversal:
	def __init__(self, str_input):
		pass

	def reversed_string(self):
		pass


class UpperLower:
	def __init__(self, str_input):
		pass

	def count_upper_lower(self):
		pass


class SortWords:
	def __init__(self, str_input):
		pass

	def split_alpha(self):
		pass


class PalindromeChecker:
	def __init__(self, str_input):
		pass

	def check_palindrome(self):
		pass


question1 = Vowels("Hello World")
question1.check_vowels()
print("==============\n")

question2 = StringCount("HelloWorldbobsureshbosigerabob")
question2.find_bob()
print("==============\n")

question3 = StringReversal("Programming in Python")
question3.reversed_string()
print("==============\n")

question4 = UpperLower("Hello World")
question4.count_upper_lower()
print("==============\n")

question5 = SortWords("without,hello,bag,world")
question5.split_alpha()
print("==============\n")

question6a = PalindromeChecker("Suresh")
question6a.check_palindrome()

print("==============\n")
question6b = PalindromeChecker("pullup")
question6b.check_palindrome()
