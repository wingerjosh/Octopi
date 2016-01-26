import random
def knockknock():
 joke = random.randint(1,3)
 print('Knock knock')
 input()
 if (joke == 1):
   print('Yo Mama!')
   input()
   print('What did you say about my Mama!?')
 elif joke == 2:
   print('Yoda Lady.')
   input()
   print('I didn\'t know you could yodel!')
 elif joke == 3:
   print('An Owl.')
   input()
   print('Yes.')
 else:
   print('Police! Open the door!')
knockknock()
