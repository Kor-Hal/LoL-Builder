# -*-coding:utf-8 -*
from packages.basics import champion, ability

class Akali(champion.Champion):
  """ Akali, the Fist of Shadow
  
  Ref : http://leagueoflegends.wikia.com/wiki/Akali
  
  """
  
  def __init__(self):
    # Abilities
    # Passive - Twin Disciplines
    passive = ability.Ability(["Twin Disciplines"], ["Discipline of Force : "
    "Akali's auto attacks deal {}% bonus magic damage.\nDiscipline of Might : "
    "Akali gains {}% spell vamp."], "Innate", "Passive")
    
    # Q/A - Mark of the Assassin
    ability1 = ability.Ability(["Mark of the Assassin"], ["Akali throws her "
    "kama at a target enemy, dealing magic damage and marking the target for "
    "6 seconds.\n\nAkali's basic attacks or Crescent Slashes against a marked "
    "target will consume the mark, dealing additional magic damage again and "
    "restoring energy."], "Basic", "Active", [(6,5.5,5,4.5,4)], [(60,)],
    [(600,)])
    
    # W/Z - Twilight Shroud
    ability2 = ability.Ability(["Twilight Shroud"], ["Akali creates a "
    "vision-granting smoke cloud in a 300-radius area for 8 seconds. While "
    "within the cloud, Akali is stealthed and gains bonus armor and magic "
    "resistance. Attacking or using abilities reveals her for 0.65 seconds. "
    "Enemies inside the smoke are slowed."], "Basic", "Active", [(20,)],
    [(80,75,70,65,60)], [(700,)])
    
    # E - Crescent Slash
    ability3 = ability.Ability(["Crescent Slash"], ["Akali flourishes her "
    "kamas, dealing physical damage and triggering any Marks of the Assassin "
    "on nearby enemies."], "Basic", "Active", [(7,6,5,4,3)],
    [(60,55,50,45,40)], [(325,)])
    
    # R (Ultimate) - Shadow Dance
    ability4 = ability.Ability(["Shadow Dance"], ["Akali uses an Essence of "
    "Shadow, dashing to and dealing magic damage to a target enemy. Akali "
    "gains an Essence of Shadow periodically, affected by cooldown reduction, "
    "up to a maximum of 3. Additionally, gaining a kill or assist will "
    "restore an Essence of Shadow."], "Ultimate", "Active", [(2,1.5,1)],
    [("1 Essence of Shadow",)], [(800,)])

    champion.Champion.__init__(self,
                               445,         # Base Health
                               85,          # Base Health per level
                               7.25,        # Base Health per 5
                               0.65,        # Base Health per 5 per level
                               200,         # Base Resource
                               0,           # Base Resource per level
                               50,          # Base Resource per 5
                               0,           # Base Resource per 5 per level
                               53,          # Base Attack Damage
                               3.2,         # Base Attack Damage per level
                               0.694,       # Base Attack Speed
                               0.031,       # Base Attack Speed per level
                               16.5,        # Base Armor
                               3.5,         # Base Armor per level
                               30,          # Base Magic Resistance
                               1.25,        # Base Magic Resistance per level
                               350,         # Base Movement Speed
                               125,         # Base Range
                               "Energy",    # Resource
                               [passive,    # Passive
                                ability1,   # Ability 1 (Q/A)
                                ability2,   # Ability 2 (W/Z)
                                ability3,   # Ability 3 (E)
                                ability4])  # Ability 4 (R)