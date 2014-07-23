# -*-coding:utf-8 -*
from packages.basics import champion, ability

class Jinx(champion.Champion):
  """ Jinx, the Loose Cannon.

  Ref : http://leagueoflegends.wikia.com/wiki/Jinx

  """
  
  def __init__(self):
    # Abilities
    # Passive - Get Excited!
    passive = ability.Ability(["Get Excited!"], ["Whenever a champion or "
    "tower that Jinx has dealt damage to within the last 3 seconds is killed "
    "or destroyed, she gains 175% Movement Speed that decays over 4 seconds."],
    "Innate", "Passive")
    
    # Q/A - Switcheroo!
    ability1 = ability.Ability(["Switcheroo!"], ["TOGGLE OFF - POW-POW, THE "
    "MINIGUN: Jinx's basic attacks grant bonus attack speed for 2.5 seconds, "
    "stacking up to 3 times. The stacks decay one at a time when she stops "
    "attacking with her minigun. Switching to her Rocket Launcher will not "
    "clear any active stacks, but they will not grant attack speed after her "
    "first attack.", "TOGGLE ON - FISHBONES, THE ROCKET LAUNCHER: Jinx gains "
    "bonus attack range and deals 10% AD bonus damage on her attacks, at the "
    "cost of mana per attack. Additionally, her attacks will splash to nearby "
    "enemies - dealing full damage to all enemies within 150 unit radius "
    "(Pending for test). The bonus damage to her target and the splash damage "
    "both scale additively with critical strikes."], "Basic", "Toggle",
    [(1,),(1,)], [(None,),("20 mana per attack",)])
    
    # W/Z - Zap!
    ability2 = ability.Ability(["Zap!"], ["After a short delay, Jinx fires "
    "a shock blast that deals physical damage to the first enemy hit, also "
    "granting true sight and slowing it for 2 seconds."],
    "Basic", "Active", [(10,9,8,7,6)], [("45 Mana","55 Mana","65 Mana","75 "
    "Mana","85 Mana")], [(1500,1500,1500,1500,1500)])
    
    # E - Flame Chompers!
    ability3 = ability.Ability(["Flame Chompers!"], ["Jinx tosses out 3 "
    "chompers that, once armed, explode on contact with enemy champions "
    "dealing magic damage over 1.5 seconds to nearby enemies. The champion "
    "that sets off the chomper is also rooted the same duration. Chompers "
    "explode automatically after 5 seconds."], "Basic", "Active",
    [(24,20,18,16,12)], [("50 Mana","50 Mana","50 Mana","50 Mana","50 Mana",)],
    [(950,950,950,950,950)])
    
    # R (Ultimate) - Super Mega Death Rocket!
    ability4 = ability.Ability(["Super Mega Death Rocket!"], ["Jinx fires a "
    "rocket that gains damage over the first second it travels. It explodes "
    "on the first enemy champion hit, dealing Physical Damage plus a "
    "percentage of the target's missing health. Nearby enemies take 80% "
    "damage."], "Ultimate", "Active", [(90, 75, 60)], [("100 Mana","100 Mana",
    "100 Mana",)], [("Global","Global","Global")])
    
    champion.Champion.__init__(self,
                               420,         # Base Health
                               80,          # Base Health per level
                               5,           # Base Health per 5
                               0.5,         # Base Health per 5 per level
                               170,         # Base Resource
                               45,          # Base Resource per level
                               5,           # Base Resource per 5
                               1,           # Base Resource per 5 per level
                               50,          # Base Attack Damage
                               3,           # Base Attack Damage per level
                               0.625,       # Base Attack Speed
                               0.01,        # Base Attack Speed per level
                               14,          # Base Armor
                               3.5,         # Base Armor per level
                               30,          # Base Magic Resistance
                               0,           # Base Magic Resistance per level
                               325,         # Base Movement Speed
                               525,         # Base Range
                               "Mana",      # Resource
                               [passive,    # Passive
                                ability1,   # Ability 1 (Q/A)
                                ability2,   # Ability 2 (W/Z)
                                ability3,   # Ability 3 (E)
                                ability4])  # Ability 4 (R)
