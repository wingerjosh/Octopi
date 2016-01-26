import random
def knockknock():
 Joke = ['Mama','Yoda','Owl']
 eggs = random.choice(Joke)
 print('Knock knock')
 input()
 if (eggs == 'Mama'):
   print('Yo Mama!')
   input()
   print('What did you say about my Mama!?')
 elif eggs == 'Yoda':
   print('Yoda Lady.')
   input()
   print('I didn\'t know you could yodel!')
 elif eggs == 'Owl':
   print('An Owl.')
   input()
   print('Yes.')
 else:
   print('Police! Open the door!')
knockknock()
