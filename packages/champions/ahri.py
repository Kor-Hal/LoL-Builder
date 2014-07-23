# -*-coding:utf-8 -*
from packages.basics import champion, ability

class Ahri(champion.Champion):
  """ Ahri, the Nine-Tailed Fox
  
  Ref : http://leagueoflegends.wikia.com/wiki/Ahri
  
  """
  
  def __init__(self):
    # Abilities
    # Passive - Essence Theft
    passive = ability.Ability(["Essence Theft"], ["Ahri gains a charge of "
    "Essence Theft with each enemy unit hit by any of her spells, with a cap "
    "of 3 charges gained per spell cast. Upon reaching 9 charges, Ahri's next "
    "spell will have 35% bonus spell vamp."], "Innate", "Passive")
    
    # Q/A - Orb of Deception
    ability1 = ability.Ability(["Orb of Deception"], ["Ahri sends out an orb "
    "in a line in front of her and then pulls it back, dealing magic damage "
    "on the way out and true damage on the way back."], "Basic", "Active",
    [(7,)], [(70,75,80,85,90)], [(880,)])
    
    # W/Z - Fox-Fire
    ability2 = ability.Ability(["Fox-Fire"], ["Ahri releases three fox-fires "
    "to surround her for up to 5 seconds. After a short delay after cast, "
    "each flame will target the closest visible enemy unit to itself, "
    "prioritizing champions, and deal magic damage to the target.\n\n"
    "Additional fox-fires that hit the same target will only deal 50% "
    "damage."], "Basic", "Active", [(9,8,7,6,5)], [(60,)])
    
    # E - Charm
    ability3 = ability.Ability(["Charm"], ["Ahri blows a kiss that travels in "
    "a line in front of her. The first enemy it hits takes magic damage and "
    "is charmed, forcing them to walk harmlessly towards Ahri while being "
    "slowed by 50% for the duration."], "Basic", "Active", [(12,)],
    [(50,65,80,95,110)], [(975,)])
    
    # R (Ultimate) - Spirit Rush
    ability4 = ability.Ability(["Spirit Rush"], ["Ahri dashes towards the "
    "cursor and fires essence bolts, dealing magic damage to up to 3 visible "
    "nearby enemies, prioritizing champions. In the next 10 seconds, Spirit "
    "Rush can be cast two additional times before going on cooldown. Each "
    "enemy can only be hit once per dash."], "Ultimate", "Active",
    [(110, 95, 80)], [(100,)])
    
    champion.Champion.__init__(self,
                               380,         # Base Health
                               80,          # Base Health per level
                               5.5,         # Base Health per 5
                               0.6,         # Base Health per 5 per level
                               230,         # Base Resource
                               50,          # Base Resource per level
                               6.25,        # Base Resource per 5
                               0.6,         # Base Resource per 5 per level
                               50,          # Base Attack Damage
                               3,           # Base Attack Damage per level
                               0.668,       # Base Attack Speed
                               0.02,        # Base Attack Speed per level
                               11,          # Base Armor
                               3.5,         # Base Armor per level
                               30,          # Base Magic Resistance
                               0,           # Base Magic Resistance per level
                               330,         # Base Movement Speed
                               550,         # Base Range
                               "Mana",      # Resource
                               [passive,    # Passive
                                ability1,   # Ability 1 (Q/A)
                                ability2,   # Ability 2 (W/Z)
                                ability3,   # Ability 3 (E)
                                ability4])  # Ability 4 (R)