# Column we want to exlude duplicate entries
text = '''
aaa
aaa
bbb
'''

# <list> of strings to process them 1 by 1
strings_one_by_one = text[1:-1].split('\n')

# Remove same strings by creating a Set
deduplicated_text = set(strings_one_by_one)

# Print cleaned column
for str in deduplicated_text:
    print(str)
