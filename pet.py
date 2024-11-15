from pet import Pet
import random

def stats(my_pet):
  print(f'Happiness: {my_pet.happy}')
  print(f'Hunger: {my_pet.hunger}')
  print(f'Health: {my_pet.health}')

def menu():
  print('1) Pet')
  print('2) Walk')
  print('3) Feed')
  print('4) Cage')
  print('5) Quit')
  user_choice = int(input('What would you like to do?: '))
  return user_choice


def main():
  new_pet = Pet(input('Give your new pet a name. '))
  print(f'This is your new pet, {new_pet.name}.')
  choice = 0
  while choice != 5 and new_pet.health > 0 and new_pet.hunger > 0 and new_pet.happy > 0:
    stats(new_pet)
    choice = menu()
    print('\n')
    new_pet.health -= random.randint(10,20)
    new_pet.hunger -= random.randint(10,20)
    new_pet.happy -= random.randint(10,20)

    if choice == 1:
      new_pet.pet()
      print(f'You pet {new_pet.name}\n')


    if choice == 2:
      new_pet.walk()
      print(f'You took {new_pet.name} on a walk!\n')

    if choice == 3:
      new_pet.feed()
      print(f'You fed {new_pet.name}\n')

    if choice == 4:
      new_pet.cage()
      print(f"You put {new_pet.name} in it's cage :(\n")

  if new_pet.health <= 0 or new_pet.hunger <= 0 or new_pet.happy <= 0:
    print(f'{new_pet.name} died :( .\n')
  
  else:
    print('Come back later!')

main()


