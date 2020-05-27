cars = ["Dodge", "Chevy", "Toyota"]
for x in cars:
  print(x)

for y in "Studebaker":
    print(y)

for x in cars:
  if x == "Chevy":
    break
  print(x)
  
for x in cars:
  if x == "Chevy":
    continue
  print(x)

for x in range(5, 10):
    print(x)
else:
    print("Finally Finished")
