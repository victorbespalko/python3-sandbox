
# Column we want to wrap by Prefix and Postfix
text = '''
aaa1
bbb2
vvv3
'''

# <list> of strings to process them 1 by 1
strings_one_by_one = text[1:-1].split('\n')

# Prefix and Postfix
prefix = r"INSERT INTO tags_approved_values VALUES ('"
postfix = r"', 'contact');"

# Print nice processed column
for str in strings_one_by_one:
    print(prefix+str+postfix)