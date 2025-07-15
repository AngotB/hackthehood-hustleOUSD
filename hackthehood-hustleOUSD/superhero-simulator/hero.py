import random
from ability import Ability
from armor import Armor


class Hero:
 
  def __init__(self, name, starting_health=100):
    
    self.name = name
   
    self.starting_health = starting_health
    
    self.current_health = starting_health

    self.armors = []

    self.abilities = []
    

    

  def battle(self, opponent):
    self.opponent = opponent 
    print(f'{self.name} battles {opponent.name}')
    winner = random.choice([opponent.name, self.name])
    print(f'winner is {winner}')

  def add_ability(self, ability):
    self.abilities.append(ability)
    print(f'ability -{ability.name}- has been added to super hero -{self.name}- succesfully')

  def sum_of_attacks(self):
    total_damage = 0
    for ability in self.abilities:
      total_damage += ability.attack()
    return total_damage

  def add_armor(self, armor):
    self.armors.append(armor)
    print(f'armor -{armor.name}- has been added to superhero -{self.name}- succesfully')

  def defend(self):
    total_block = 0
    for armor in self.armors:
      total_block += armor.block()
    return total_block





if __name__ == "__main__":
  my_hero = Hero("Grace Hopper", 200)
  print(my_hero.name)
  print(my_hero.current_health)

  my_hero1 = Hero("Spiderman", 175)
  print(my_hero1.name)
  print(my_hero1.current_health)

  my_hero.add_ability(Ability('fireball', 50))
  my_hero.add_ability(Ability('bomb', 100))
  my_hero.add_ability(Ability('power punch', 125))
  print(my_hero.sum_of_attacks())

  my_hero.add_armor(Armor('shield', 100))
  my_hero.add_armor(Armor('boots', 50))
  my_hero.add_armor(Armor('helmet', 75))
  print(my_hero.defend())
  my_hero.battle(my_hero1)


  
  
