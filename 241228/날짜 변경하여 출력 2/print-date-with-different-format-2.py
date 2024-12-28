date = input()

date_split=date.split('-')
date_split[0],date_split[1],date_split[2]=date_split[2],date_split[0],date_split[1]
result = '.'.join(date_split)
print(result)