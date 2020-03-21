import re

PATTERN = r"\[[a-z]*\]"


def is_abba(word):
	for i in range(len(word) - 3):
		sub = word[i:i+4]
		if sub[0] != sub[1] and sub[:2] == sub[-1:1:-1]:
			return True

	return False


def tls(ip):
	matches = re.findall(PATTERN, ip)
	for match in matches:
		if is_abba(match[1:-1]):
			return 0
		ip.replace(match, " ")

	for word in ip.split():
		if is_abba(word):
			return 1

	return 0


def aba(word):
	for i in range(len(word) - 2):
		sub = word[i:i+3]
		if sub[0] != sub[1] and sub == sub[::-1]:
			yield sub


def ssl(ip):
	matches = re.findall(PATTERN, ip)
	all_abas = []
	for match in matches:
		for aba_match in aba(match):
			all_abas.append(aba_match)
		ip = ip.replace(match, " ")

	for aba_word in all_abas:
		bab_word = aba_word[1:] + aba_word[1]
		for word in ip.split():
			if bab_word in word:
				return 1

	return 0


def count_valid(support_type):
	valid_ip_count = 0
	with open("day7.txt", "r") as f:
		for line in map(lambda s: s.strip(), f):
			valid_ip_count += support_type(line)

	return valid_ip_count


print(count_valid(tls))
print(count_valid(ssl))
