print("   _.---.._             _.---...__")
print(".-'   /\   \          .'  /\     /")
print("`.   (  )   \        /   (  )   /")
print("  `.  \/   .'\      /`.   \/  .'")
print("    ``---''   )    (   ``---''")
print("            .';.--.;`.")
print("          .' /_...._\ `.")
print("        .'   `.a  a.'   `.")
print("     \'(        \/       \')")
print("        `.___..-'`-..___.'")
print("           \          /")
print("            `-.____.-'")
print("Welcome to The Cat Game.")
print("You are the Cat. Your mission is to find the fish.Hooman must not see you. Good luck !") 

choice1 = input("You're in the kitchen. Where do you want to go ? Type 'counter' or 'fridge'\n").lower()

if choice1 == ('counter'):
  choice2 = input("On the counter, you see a box. Maybe the fish is in here ! Type 'open' to try to lift the cover. Type 'fall' to throw it on the floor.\n").lower()
  if choice2 == ("open"):
      choice3 = input("Good Choice ! The cover can be lifted. The fish is right here, ready to be eaten. Where can you hide it ? in the garden, the floor, on the couch, or stay on the counter ?\n").lower()
      if choice3 == ("garden"):
        print ("You run outside and go to the garden to bury your precious fish. Well done !")
        print ("|\    \ \ \ \ \ \ \      __")   
        print("|  \    \ \ \ \ \ \ \   | O~-_")
        print("|   >----|-|-|-|-|-|-|--|  __/")
        print("|  /    / / / / / / /   |__\ ")  
        print("|/     / / / / / / /")
      elif choice3 == ("floor"):
        print ("The dog, this horrible monster, was waiting and steal your delicious fish. What a shame ! Game Over.")
      elif choice3 == ("couch"):
        print ("The Hooman saw you dragging your fish on the clean couch. You are grounded AND hungry. Game Over.")
      else:
        print ("You are very much exposed and the Hooman, entering the room, immediatly understands what happened. You are grounded. Game Over.")
  else:
    print ("The Hooman heard the box fell on the floor. You are grounded. Game Over.")
else :
  print ("You do not have hands, you morron ! You cannot open a fridge door. Game Over.")

