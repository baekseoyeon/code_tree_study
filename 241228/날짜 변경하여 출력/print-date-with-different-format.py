date = input()
date_split = date.split(".")
date_split[0],date_split[1],date_split[2]=date_split[1],date_split[2],date_split[0]
date_str="-".join(date_split)
print(date_str)