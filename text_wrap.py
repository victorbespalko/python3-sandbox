
#Column we want to wrap by Prefix and Postfix
text = '''
asas
aqwqe
sadasd
'''

# <list> of strings to process them 1 by 1
strings_one_by_one = text[1:-1].split('\n')

# Prefix and Postfix
prefix = 'ama mighty prefix!'
postfix = 'ama da postfix11!'

# Print nice processed column
for str in strings_one_by_one:
    print(prefix,str,postfix)