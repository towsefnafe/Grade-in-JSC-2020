num = input("Give your number:")
numint = int(num)

if numint > 100:
  print('Something Wrong')
elif numint >= 90 and numint <= 100:
  print('Your grade is A+')
elif numint >= 80 and numint <= 89:
  print('Your grade point is A')
elif numint >= 70 and numint <= 79:
  print('Your grade point is B+')
elif numint >= 60 and numint <= 69:
  print('Your grade point is B')
elif numint >= 50 and numint <= 59:
  print('Your grade point is C+')
elif numint >= 40 and numint <= 49:
  print('Your grade point is C')
elif numint >= 33 and numint <= 39:
  print('Your grade point is D')
else:
  print('Your grade is F')