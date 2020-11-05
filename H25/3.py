import re
names = """
Kardinaal Richelieu 
Charles d’Artagnan
Gilbert duPrez
Joe DiMaggio
Unit X1138
Jan Ronan
Joe
"""
actualnames = re.findall(r'\b[A-Z][a-z]+\b \b[A-Z][a-z]+\b', names)
print(actualnames)