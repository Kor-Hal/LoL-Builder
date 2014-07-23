# -*-coding:utf-8 -*
import os, pickle

from packages.basics import * # Defining MasteryPage and RunePage
from packages.champions import * # Defining all champions' classes

if __name__ == '__main__':
  # Loading masteries from masteries.pickle file, if it exists.
  # If not, we create a list with one empty mastery page
  try:
    with open('masteries.pickle', 'rb') as masteries_file:
      masteries = pickle.load(masteries_file)
  except IOError:
    temp = MasteryPage("Mastery Page 1", offense_masteries, defense_masteries,
                                         utility_masteries)
    masteries = [temp]
  
  # Loading runes from runes.pickle file, if it exists.
  # If not, we create a list with one empty rune page
  try:
    with open('runes.pickle', 'rb') as runes_file:
      runes = pickle.load(runes_file)
  except IOError:
    temp = RunePage("Rune Page 1")
    runes = [temp]
  
  masteries[0].offense_tree.masteries[(1,3)].level = 4
  masteries[0].offense_tree.masteries[(2,2)].level = 4
  masteries[0].offense_tree.masteries[(3,1)].level = 3
  masteries[0].offense_tree.masteries[(3,2)].level = 1
  masteries[0].offense_tree.masteries[(4,2)].level = 2

  current_champ = Jinx()
  current_champ.masteries = masteries[0]
  current_champ.runes = runes[0]
  current_champ.level = 18
  text = ("{}, au niveau {}, possède {} points de vie, {} régénération de vie "
  "toutes les 5 secondes, {} points de mana, {} régénération de mana toutes "
  "les 5 secondes, {} AD, {} en vitesse d'attaque, {} points d'armure, {} "
  "points de résistance magique, {} en vitesse de déplacement et {} range")
  print(text.format(current_champ.__class__.__name__, current_champ.currentLevel, 
  current_champ.current_hp(), current_champ.current_hp5(),
  current_champ.current_mp(), current_champ.current_mp5(),
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
  current_champ.current_mp(), current_champ.current_mp5(),
  current_champ.current_ad(), current_champ.current_as(),
  current_champ.current_ar(), current_champ.current_mr(),
  current_champ.current_ms(), current_champ.current_range()))

  # Saving masteries to masteries.pickle file
  with open('masteries.pickle', 'wb') as masteries_file:
    pickle.dump(masteries, masteries_file)
  
  # Saving runes to runes.pickle file
  with open('runes.pickle', 'wb') as runes_file:
    pickle.dump(runes, runes_file)
  
  os.system("pause")