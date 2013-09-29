# -*-coding:Latin-1 -*
import os, pickle

from packages.basics import * # Defining MasteryPage and RunePage
from packages.champions import * # Defining all champions' classes

if __name__ == '__main__':
  # Loading masteries from masteries.pickle file, if it exists. If not, we create a list with one empty mastery page
  try:
    with open('masteries.pickle', 'rb') as masteries_file:
      masteries = pickle.load(masteries_file)
  except IOError:
    temp = MasteryPage("Mastery Page 1", offense_masteries, defense_masteries, utility_masteries)
    masteries = [temp]
  
  # Loading runes from runes.pickle file, if it exists. If not, we create a list with one empty rune page
  try:
    with open('runes.pickle', 'rb') as runes_file:
      runes = pickle.load(runes_file)
  except IOError:
    temp = RunePage("Rune Page 1")
    runes = [temp]
  
  current_champ = Aatrox()
  current_champ.masteries = masteries[0]
  current_champ.runes = runes[0]
  level = 18
  text = ("{}, au niveau {}, possède {} points de vie, {} régénération de vie toutes les 5 secondes, "
  "{} points de mana, {} régénération de mana toutes les 5 secondes, {} AD, {} en vitesse d'attaque, "
  "{} points d'armure, {} points de résistance magique, {} en vitesse de déplacement et {} range")
  print(text.format(current_champ.__class__.__name__, level, 
  current_champ.current_hp(level), current_champ.current_hp5(level), current_champ.current_mp(level),
  current_champ.current_mp5(level), current_champ.current_ad(level), current_champ.current_as(level),
  current_champ.current_ar(level), current_champ.current_mr(level), current_champ.current_ms(level),
  current_champ.current_range(level)))
  
  runes[0].add_rune(g_quintessence_attack_damage, 0)
  runes[0].add_rune(g_quintessence_health, 1)
  runes[0].add_rune(g_quintessence_percent_health, 2)
  
  print("AD bonus : {}".format(runes[0].attack_damage))
  print("Flat HP bonus : {}".format(runes[0].health))
  print("Perc HP bonus : {}%".format(runes[0].percent_health * 100))
  
  text = ("{}, au niveau {}, possède {} points de vie, {} régénération de vie toutes les 5 secondes, "
  "{} points de mana, {} régénération de mana toutes les 5 secondes, {} AD, {} en vitesse d'attaque, "
  "{} points d'armure, {} points de résistance magique, {} en vitesse de déplacement et {} range")
  print(text.format(current_champ.__class__.__name__, level, 
  current_champ.current_hp(level), current_champ.current_hp5(level), current_champ.current_mp(level),
  current_champ.current_mp5(level), current_champ.current_ad(level), current_champ.current_as(level),
  current_champ.current_ar(level), current_champ.current_mr(level), current_champ.current_ms(level),
  current_champ.current_range(level)))
  
  runes[0].del_rune("Quintessence", 0)
  runes[0].del_rune("Quintessence", 1)
  runes[0].del_rune("Quintessence", 2)
  
  print("AD bonus : {}".format(runes[0].attack_damage))
  print("HP bonus : {}".format(runes[0].health))
  print("Perc HP bonus : {}%".format(runes[0].percent_health * 100))
  
  text = ("{}, au niveau {}, possède {} points de vie, {} régénération de vie toutes les 5 secondes, "
  "{} points de mana, {} régénération de mana toutes les 5 secondes, {} AD, {} en vitesse d'attaque, "
  "{} points d'armure, {} points de résistance magique, {} en vitesse de déplacement et {} range")
  print(text.format(current_champ.__class__.__name__, level, 
  current_champ.current_hp(level), current_champ.current_hp5(level), current_champ.current_mp(level),
  current_champ.current_mp5(level), current_champ.current_ad(level), current_champ.current_as(level),
  current_champ.current_ar(level), current_champ.current_mr(level), current_champ.current_ms(level),
  current_champ.current_range(level)))
  
  # Saving masteries to masteries.pickle file
  with open('masteries.pickle', 'wb') as masteries_file:
    pickle.dump(masteries, masteries_file)
  
  # Saving runes to runes.pickle file
  with open('runes.pickle', 'wb') as runes_file:
    pickle.dump(runes, runes_file)
  
  os.system("pause")