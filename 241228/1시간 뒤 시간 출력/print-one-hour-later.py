time=input()
time_split=time.split(":")
time_split[0] = int(time_split[0])+1
new_time=str(time_split[0])+":"+time_split[1]
print(new_time)