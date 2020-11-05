import re
verhaal = "Dit is een tekst en d1t word niet geprint omdat er een cijfer in zit"
search = re.compile(r'\b[a-zA-Z]+\b')
matches = search.finditer(verhaal)
wordlist = []
for match in matches:
    print(match)
    wordlist.append(match.group(0))

print(wordlist)