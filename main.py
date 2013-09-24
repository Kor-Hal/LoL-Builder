# -*-coding:Latin-1 -*
import os, pickle

from packages.basics import * # Defining MasteryPage
from packages.champions import * # Defining all champions' classes

if __name__ == '__main__':
  # Loading masteries from masteries.pickle file, if it exists. If not, we create a list with one empty mastery page
  try:
    with open('masteries.pickle', 'rb') as f:
      masteries = pickle.load(f)
  except IOError:
    temp = MasteryPage("Mastery Page 1")
    masteries = [temp]
  
  curr_champ = Aatrox()
  for level in range(1, 19):
    text = ("{}, au niveau {}, possède {} points de vie, {} régénération de vie toutes les 5 secondes, "
    "{} points de mana, {} régénération de mana toutes les 5 secondes, {} AD, {} en vitesse d'attaque, "
    "{} points d'armure, {} points de résistance magique, {} en vitesse de déplacement et {} range")
    print(text.format(curr_champ.__class__.__name__, level, 
    curr_champ.curr_hp(level), curr_champ.curr_hp5(level), curr_champ.curr_mp(level),
    curr_champ.curr_mp5(level), curr_champ.curr_ad(level), curr_champ.curr_as(level),
    curr_champ.curr_ar(level), curr_champ.curr_mr(level), curr_champ.curr_ms(level),
    curr_champ.curr_range(level)))
  
  # Saving masteries to masteries.pickle file
  with open('masteries.pickle', 'wb') as f:
    pickle.dump(masteries, f)
  
  os.system("pause")