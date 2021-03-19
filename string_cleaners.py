from bs4 import BeautifulSoup
import re

def soup_text(text):
	"""
		Args:
			text: html format
		Returns:
			Cleaned and text only. 
			Empyt string if text is None.
	"""
	if text:
		join_text = ''.join(text)
		soup = BeautifulSoup(join_text, 'html.parser')
		clean_text = soup.get_text().strip()

		return clean_text
	return ''


def remove_non_strings(text):
	"""
		Args: 
			List of strings.
		Return:
			Cleaned and removed new lines and tabs from text
	"""
	words = []
	for string in text:
		if string:
			word = string.replace('\n', '').replace('\t', '').replace('\r', '')
			words.append(word)

	return words


def find_string_by_patterns(text, first_pattern, second_pattern):
	"""
		Args:
			first_pattern: string before the desired string
			second_pattern: string after the desired string
		Return
	"""
	form_pattern = first_pattern + "(.*?)" + second_pattern
	find_string = re.findall(form_pattern, text)
	if find_string:
		return ''.join(find_string).strip()
	return ''


def remove_non_alpha_numeric(string):
	"""
		Args:
			Any strings.
		Return:
			Remove and join non alpha numeric characters from string.
	"""
	chars = [char.lower() for char in string if char.isalnum()]
	join_chars = ''.join(chars)
	if join_chars:
		return join_chars
	return string


def find_conclusion_from_last(paragraph):
	for i in range(len(paragraph)):
		indx = -(i+1)
		soup_con = BeautifulSoup(paragraph[indx], 'html.parser')
		text = soup_con.get_text().strip()
		if len(text.split(' ')) > 30:
			return text