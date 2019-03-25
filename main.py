# -*-coding:utf-8 -*
import os, pickle

from packages.basics import * # Defining Basics mechanics
from packages.champions import * # Defining all champions' classes

if __name__ == '__main__':
  
  current_champ = Jinx()
  current_champ.currentLevel = 18
  text = ("{}, au niveau {}, possède {} points de vie, {} régénération de vie "
  "toutes les 5 secondes, {} points de mana, {} régénération de mana toutes "
  "les 5 secondes, {} AD, {} en vitesse d'attaque, {} points d'armure, {} "
  "points de résistance magique, {} en vitesse de déplacement et {} range")
  print(text.format(current_champ.__class__.__name__, current_champ.currentLevel, 
  current_champ.current_hp(), current_champ.current_hp5(),
  current_champ.current_resource(), current_champ.current_resource5(),
  current_champ.current_ad(), current_champ.current_as(),
  current_champ.current_ar(), current_champ.current_mr(),
  current_champ.current_ms(), current_champ.current_range()))
  
  current_champ.itemsSet["Slot 1"] = infinity_edge
  print("AD : {}".format(current_champ.current_ad()))
  current_champ.itemsSet["Slot 2"] = phantom_dancer
  print("AD : {}".format(current_champ.current_ad()))
  current_champ.itemsSet["Slot 3"] = last_whisper
  print("AD : {}".format(current_champ.current_ad()))
  current_champ.itemsSet["Slot 4"] = the_black_cleaver
  print("AD : {}".format(current_champ.current_ad()))
  current_champ.itemsSet["Slot 5"] = berserker_s_greaves
  print("AD : {}".format(current_champ.current_ad()))
  current_champ.itemsSet["Slot 6"] = guardian_angel
  print("AD : {}".format(current_champ.current_ad()))
  
  print("Passif : {}".format(current_champ.abilities[0].description[0]))
  print("Ability 1 : {}".format(current_champ.abilities[1].description[0]))
  print("Ability 2 : {}".format(current_champ.abilities[2].description[0]))
  print("Ability 3 : {}".format(current_champ.abilities[3].description[0]))
  print("Ability 4 : {}".format(current_champ.abilities[4].description[0]))
  
  text = ("{}, au niveau {}, possède {} points de vie, {} régénération de vie "
  "toutes les 5 secondes, {} points de mana, {} régénération de mana toutes "
  "les 5 secondes, {} AD, {} en vitesse d'attaque, {} points d'armure, {} "
  "points de résistance magique, {} en vitesse de déplacement et {} range")
  print(text.format(current_champ.__class__.__name__, current_champ.currentLevel,
  current_champ.current_hp(), current_champ.current_hp5(),
  current_champ.current_resource(), current_champ.current_resource5(),
  current_champ.current_ad(), current_champ.current_as(),
  current_champ.current_ar(), current_champ.current_mr(),
  current_champ.current_ms(), current_champ.current_range()))

  os.system("pause")