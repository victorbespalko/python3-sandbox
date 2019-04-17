# Column we want to exlude duplicate entries
text = '''
seankane@upwork.com 
scrum-program-management@upwork.com
seankane@upwork.com 
client-experience@upwork.com
iam-eng@upwork.com
reports@upwork.com
reporting-backend@upwork.com
scrum-work-management@upwork.com
wms-agora@upwork.com
sre@upwork.com
dba@upwork.com
infrastructure@upwork.com
dps@upwork.com
Old Team Name Not required
Old Team Name Not required
scrum-api@upwork.com
tnseng@upwork.com
Old Team Name Not required
reporting-backend@upwork.com
marketing-engineering-team@upwork.com
marketing-engineering-team@upwork.com
'''

# <list> of strings to process them 1 by 1
strings_one_by_one = text[1:-1].split('\n')

# Remove same strings by creating a Set
deduplicated_text = set(strings_one_by_one)

# Print cleaned column
for str in deduplicated_text:
    print(str)
