# • The ? matches zero or one of the preceding group.
# • The * matches zero or more of the preceding group.
# • The + matches one or more of the preceding group.
# • The {n} matches exactly n of the preceding group.
# • The {n,} matches n or more of the preceding group.
# • The {,m} matches 0 to m of the preceding group.
# • The {n,m} matches at least n and at most m of the preceding group.
# • {n,m}? or *? or +? performs a nongreedy match of the preceding group.
# • ^spam means the string must begin with spam.
# • spam$ means the string must end with spam.
# • The . matches any character, except newline characters.
# • \d, \w, and \s match a digit, word, or space character, respectively.
# • \D, \W, and \S match anything except a digit, word, or space character, respectively.
# • [abc] matches any character between the brackets (such as a, b, or c).
# • [^abc] matches any character that isn’t between the brackets.

# *** #
# *** #
# *** #

# def isPhoneNumber(text):
# 	if len(text) != 12:
# 		return False
# 	for i in range(0, 3):
# 		if not text[i].isdecimal():
# 			return False
# 	if text[3] != '-':
# 		return False
# 	for i in range(4, 7):
# 		if not text[i].isdecimal():
# 			return False
# 	if text[7] != '-':
# 		return False
# 	for i in range(8, 12):
# 		if not text[i].isdecimal():
# 			return False
# 	return True

# print('415-555-4242 is a phone number:')
# print(isPhoneNumber('415-555-4242'))
# print('Moshi moshi is a phone number:')
# print(isPhoneNumber('Moshi moshi'))

# *** #
# *** #
# *** #

# módulo que contém métodos para tratar com regex
import re

# r antes da regex (raw string) indica que não deve escapar o texto em frente
# .compile cria uma regex
	# phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
	# phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
	# mo = phoneNumRegex.search('My number is 415-555-4242.')
	# print('Phone number found: ' + mo.group(1))
	# print('Phone number found: ' + mo.group(2))
	# print('Phone number found: ' + mo.group(0))
	# print('Phone number found: ' + mo.group())

# multiple-assignment trick
	# areaCode, mainNumber = mo.groups()
	# print(areaCode)
	# print(mainNumber)

# ferramenta para testar regex online http://regexpal.com

# *** #
# *** #
# *** #

# encontra um ou outro
	# heroRegex = re.compile(r'Batman|Tina Fey') 
	# mo1 = heroRegex.search('Batman and Tina Fey.') 
	# print(mo1.group())
	# mo2 = heroRegex.search('Tina Fey and Batman.') 
	# print(mo2.group())

	# batRegex = re.compile(r'Bat(man|mobile|copter|bat)') 
	# mo = batRegex.search('Batmobile lost a wheel')
	# print(mo.group())
	# print(mo.group(1))

# encontra se tiver ou não o que está dentro dos ()
	# batRegex = re.compile(r'Bat(wo)?man')
	# mo1 = batRegex.search('The Adventures of Batman') 
	# print(mo1.group())
	# mo2 = batRegex.search('The Adventures of Batwoman') 
	# print(mo2.group())

# encontra se tiver 0 ou mais ocorrências da string entre ()
	# batRegex = re.compile(r'Bat(wo)*man')
	# mo1 = batRegex.search('The Adventures of Batman') 
	# print(mo1.group())
	# mo2 = batRegex.search('The Adventures of Batwoman') 
	# print(mo2.group())
	# mo3 = batRegex.search('The Adventures of Batwowowowoman') 
	# print(mo3.group())
	# 'Batwowowowoman'

# encontra um ou mais com sinal +
	# batRegex = re.compile(r'Bat(wo)+man')
	# mo1 = batRegex.search('The Adventures of Batwoman') 
	# print(mo1.group())
	# mo2 = batRegex.search('The Adventures of Batwowowowoman') 
	# print(mo2.group())
	# mo3 = batRegex.search('The Adventures of Batman') 
	# print(mo3 == None)

# curly brackets
    # haRegex = re.compile(r'(Ha){3}')
    # mo1 = haRegex.search('HaHaHa') #cuidado com o case-sensitive
    # print(mo1.group())
    # mo2 = haRegex.search('Ha')
    # print(mo2 == None)

# greedy & nongreedy matching
    # greedyHaRegex = re.compile(r'(Ha){3,5}')
    # mo1 = greedyHaRegex.search('HaHaHaHaHa') # match a versão mais longa da string
    # print(mo1.group())
    # nongreedyHaRegex = re.compile(r'(Ha){3,5}?') # match a versão mais curta da string
    # mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
    # print(mo2.group())

# findall method
    # phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
    # mo1 = phoneNumRegex.search('Cell: 415-555-9999 Work: 212-555-0000') 
    # print(mo1.group())
    # mo2 = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000') # não retorno dentro de um grupo
    # print(mo2)
    # xmasRegex = re.compile(r'\d+\s\w+')
    # mo3 = xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')
    # print(mo3)

# character class
    # vowelRegex = re.compile(r'[aeiouAEIOU]')
    # mo4 = vowelRegex.findall('RoboCop eats baby food. BABY FOOD.')
    # print(mo4)
    # consonantRegex = re.compile(r'[^aeiouAEIOU]')
    # mo5 = consonantRegex.findall('RoboCop eats baby food. BABY FOOD.')
    # print(mo5)

# começa com xxx
    # beginsWithHello = re.compile(r'^Hello')
# termina com xxx
    # endsWithNumber = re.compile(r'\d$')
# começa e termina com xxx
    # wholeStringIsNum = re.compile(r'^\d+$')

# match nova linha
    # noNewlineRegex = re.compile('.*')
    # print(noNewlineRegex.search('Serve the public trust.\nProtect the innocent. \nUphold the law.').group())
    # newlineRegex = re.compile('.*', re.DOTALL)
    # print(newlineRegex.search('Serve the public trust.\nProtect the innocent. \nUphold the law.').group())

# case-insensitive
    # robocop = re.compile(r'robocop', re.I)
    # print(robocop.search('RoboCop is part man, part machine, all cop.').group())
    # print(robocop.search('ROBOCOP protects the innocent.').group())
    # print(robocop.search('Al, why does your programming book talk about robocop so much?').group())

    # namesRegex = re.compile(r'Agent \w+')
    # print(namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.'))

    # agentNamesRegex = re.compile(r'Agent (\w)\w*')
    # print(agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent'))

# re.VERBOSE = ignore whitespace and comments inside the regular expression string
# (''') to create a multiline string so that you can spread the regular expression definition over many lines
    # phoneRegex = re.compile(r'''(
    #     (\d{3}|\(\d{3}\))?              # area code
    #     (\s|-|\.)?                      # separator
    #     \d{3}                           # first 3 digits
    #     (\s|-|\.)                       # separator
    #     \d{4}                           # last 4 digits
    #     (\s*(ext|x|ext.)\s*\d{2,5})?    # extension
    #     )''', re.VERBOSE)

# combining re.ignorecASe, re.dotAll, and re.VerBoSe
    # someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)

# ********************************** #
# REALIZAR EXERCICIOS PRÁTICOS - 166 #
# ********************************** #