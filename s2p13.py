g=int(input())

if((g<=10000)and(g>1)):
  for i in range(2,(g//2)+1):
    if((g%i==0)):
      print("no")
      break
      
  else:
    print("yes")
