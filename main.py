# -*-coding:Latin-1 -*
import os, pickle

from packages.basics import * # Defining MasteryPage
from packages.champions import * # Defining all champions' classes

if __name__ == '__main__':
  # Loading masteries from masteries.pickle file, if it exists. If not, we create a list with one empty mastery page
  try:
    with open('masteries.pickle', 'rb') as masteries_file:
      masteries = pickle.load(masteries_file)
  except IOError:
    temp = MasteryPage("Mastery Page 1")
    masteries = [temp]
  
  # Loading runes from runes.pickle file, if it exists. If not, we create a list with one empty rune page
  try:
    with open('runes.pickle', 'rb') as runes_file:
      runes = pickle.load(runes_file)
  except IOError:
    temp = RunePage("Rune Page 1")
    runes = [temp]
  
  curr_champ = Aatrox()
  level = 18
  text = ("{}, au niveau {}, possède {} points de vie, {} régénération de vie toutes les 5 secondes, "
  "{} points de mana, {} régénération de mana toutes les 5 secondes, {} AD, {} en vitesse d'attaque, "
  "{} points d'armure, {} points de résistance magique, {} en vitesse de déplacement et {} range")
  print(text.format(curr_champ.__class__.__name__, level, 
  curr_champ.curr_hp(level), curr_champ.curr_hp5(level), curr_champ.curr_mp(level),
  curr_champ.curr_mp5(level), curr_champ.curr_ad(level), curr_champ.curr_as(level),
  curr_champ.curr_ar(level), curr_champ.curr_mr(level), curr_champ.curr_ms(level),
  curr_champ.curr_range(level)))
  
  runes[0].add_rune(g_quintessence_attack_damage, 1)
  
  print("AD bonus : {}".format(runes[0].attack_damage))
  
  runes[0].del_rune("Quintessence", 1)
  
  print("AD bonus : {}".format(runes[0].attack_damage))
  
  # Saving masteries to masteries.pickle file
  with open('masteries.pickle', 'wb') as masteries_file:
    pickle.dump(masteries, masteries_file)
  
  # Saving runes to runes.pickle file
  with open('runes.pickle', 'wb') as runes_file:
    pickle.dump(runes, runes_file)
  
  os.system("pause")