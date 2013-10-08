# -*-coding:utf-8 -*
from packages.basics import champion, ability

class Akali(champion.Champion):
  """ Akali, the Fist of Shadow
  
  Ref : http://leagueoflegends.wikia.com/wiki/Akali
  
  """
  
  def __init__(self):
    # Basic stats
    base_hp = 445
    base_hp_plus = 85
    base_hp5 = 7.25
    base_hp5_plus = 0.65
    base_mp = 200
    base_mp_plus = 0
    base_mp5 = 50
    base_mp5_plus = 0
    base_ad = 53
    base_ad_plus = 3.2
    base_as = 0.694
    base_as_plus = 0.031
    base_ar = 16.5
    base_ar_plus = 3.5
    base_mr = 30
    base_mr_plus = 1.25
    base_ms = 350
    base_range = 125
        
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
    
    champion.Champion.__init__(self, base_hp, base_hp_plus, base_hp5,
                               base_hp5_plus, base_mp, base_mp_plus, base_mp5,
                               base_mp5_plus, base_ad, base_ad_plus, base_as,
                               base_as_plus, base_ar, base_ar_plus, base_mr,
                               base_mr_plus, base_ms, base_range, "Energy",
                               [passive,ability1,ability2,ability3,ability4])