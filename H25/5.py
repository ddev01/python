import re
teksts = """
Bob said "Nice weather"
John replied "indeed"
"""
fix = re.findall(r'(?<=\")(.*?)(?=\")', teksts)
print(fix)