## Note: for python older than 3.xx:
#- you need to remove the parentheses for the 'print' command to get the intended effect (e.g. concatenation)
#- Also the input string should come with '', or you should use 'raw_input' as below
# On the other hand, for 3.xx, the print ALWAYS needs parenthesis anytime

print ("test-updated", 11/4)

lines=0

while lines<50 :
 print ("this is a good example")
 print (lines)
 lines = lines +1

#name = raw_input("Enter your name")
name = input("Enter your name")
print (name)
print ("Hello ", name)

if name=="sehoon":
 print ("you are sehoon")
elif name=="yea":
 print ("you are yea")
else: ### this is optional
 print ("who are you")



 
def times_table(how_far, num):
 n=1;
 while n<=how_far:
  n = n + 1
  print("n= %d\n" % n)


times_table(12,17)