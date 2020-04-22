seconds = int(input("Enter seconds: "))

minutes = seconds // 60
hours = minutes // 60
sec = seconds % 60
min = minutes % 60

print("{:02d}:{:02d}:{:02d}".format(hours,min, sec))
