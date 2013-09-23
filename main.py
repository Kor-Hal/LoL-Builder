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
  
  currChamp = Aatrox()
  for level in range(1, 19):
    text = ("{}, au niveau {}, possède {} points de vie, {} régénération de vie toutes les 5 secondes, "
    "{} points de mana, {} régénération de mana toutes les 5 secondes, {} AD, {} en vitesse d'attaque, "
    "{} points d'armure, {} points de résistance magique, {} en vitesse de déplacement et {} range")
    print(text.format(currChamp.__class__.__name__, level, 
    currChamp.curr_hp(level), currChamp.curr_hp5(level), currChamp.curr_mp(level),
    currChamp.curr_mp5(level), currChamp.curr_ad(level), currChamp.curr_as(level),
    currChamp.curr_ar(level), currChamp.curr_mr(level), currChamp.curr_ms(level),
    currChamp.curr_range(level)))
  
  # Saving masteries to masteries.pickle file
  with open('masteries.pickle', 'wb') as f:
    pickle.dump(masteries, f)
  
  os.system("pause")