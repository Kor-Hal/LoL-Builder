# -*-coding:utf-8 -*
from packages.basics import champion, ability

class Ahri(champion.Champion):
  """ Ahri, the Nine-Tailed Fox
  
  Ref : http://leagueoflegends.wikia.com/wiki/Ahri
  
  """
  
  def __init__(self):
    # Basic stats
    base_hp = 380
    base_hp_plus = 80
    base_hp5 = 5.5
    base_hp5_plus = 0.6
    base_mp = 230
    base_mp_plus = 50
    base_mp5 = 6.25
    base_mp5_plus = 0.6
    base_ad = 50
    base_ad_plus = 3
    base_as = 0.668
    base_as_plus = 0.02
    base_ar = 11
    base_ar_plus = 3.5
    base_mr = 30
    base_mr_plus = 0
    base_ms = 330
    base_range = 550
        
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
    
    champion.Champion.__init__(self, base_hp, base_hp_plus, base_hp5,
                               base_hp5_plus, base_mp, base_mp_plus, base_mp5,
                               base_mp5_plus, base_ad, base_ad_plus, base_as,
                               base_as_plus, base_ar, base_ar_plus, base_mr,
                               base_mr_plus, base_ms, base_range, "Mana",
                               [passive,ability1,ability2,ability3,ability4])