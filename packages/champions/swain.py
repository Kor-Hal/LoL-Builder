# -*-coding:utf-8 -*
from packages.basics import champion, ability

class Swain(champion.Champion):
  """ Swain, the Master Tactician
  
  Ref : http://leagueoflegends.wikia.com/wiki/Swain
  
  """
  
  def __init__(self):
    # Abilities
    # Passive - Blood Well
    #passive = ability.Ability(["Blood Well"], ["""Whenever Aatrox uses an ability that costs health, he stores 100% of the health 
    #cost into his Blood Well. The maximum amount of health the Blood Well can store is 30 + {}. If Aatrox has not dealt or received
    #damage in the last 5 seconds, his Blood Well will deplete at a rate of 2% per second.\n\nUpon taking fatal damage, 
    #Blood Well activates and places Aatrox in stasis for 3 seconds. Over the stasis duration the Blood Well is emptied and 
    #Aatrox restores health equal to its contents plus 10.5 + {}. Blood Well's activation has a static cooldown and is unaffected by 
    #cooldown reduction.\n\nAlso, Aatrox passively increases his attack speed by 1% for every 2% in the Blood Well."""], 
    #"Innate", "Passive", [(225,)])
    
    # Q/A - Dark Flight
    #ability1 = ability.Ability(["Dark Flight"], ["""Aatrox takes flight and slams down at a targeted area, dealing physical damage 
    #to nearby enemies upon landing. Enemies in the center of the area are also knocked up for 1 second."""],
    #"Basic", "Active", [(16,15,14,13,12)], [("10% of current health",)], [(650,)])
    
    # W/Z - Blood Thirst / Blood Price
    #ability2 = ability.Ability(["Blood Thirst", "Blood Price"], ["""Aatrox heals himself on every third attack. If Aatrox is 
    #below 50% health he will heal for three times as much.""", """Aatrox deals bonus physical damage on every third attack 
    #at the cost of health."""], 
    #"Basic", "Toggle", [(0.5,)], [("","See below")])
    
    # E - Blades of Torment
    #ability3 = ability.Ability(["Blades of Torment"], ["""Aatrox unleashes and sends forward the power of his blade, 
    #dealing magic damage to enemies in a line and slowing them by 40% for a few seconds."""],
    #"Basic", "Active", [(12, 11, 10, 9, 8)], [("5% of current health",)], [(1000,)])
    
    # R (Ultimate) - Massacre
    #ability4 = ability.Ability(["Massacre"], ["""Aatrox draws in the blood of his foes, dealing magic damage to nearby enemy 
    #champions.\n\nFor the next 12 seconds, Aatrox gains bonus attack speed and 175 bonus attack range (325 total range). His 
    #attacks are still considered melee."""],
    #"Ultimate", "Active", [(100, 85, 70)], [("No cost",)])

    champion.Champion.__init__(self,
                               385,         # Base Health
                               78,          # Base Health per level
                               6.75,        # Base Health per 5
                               0.65,        # Base Health per 5 per level
                               240,         # Base Resource
                               50,          # Base Resource per level
                               6.8,         # Base Resource per 5
                               0.65,        # Base Resource per 5 per level
                               49,          # Base Attack Damage
                               3,           # Base Attack Damage per level
                               0.625,       # Base Attack Speed
                               0.0211,      # Base Attack Speed per level
                               12,          # Base Armor
                               4,           # Base Armor per level
                               30,          # Base Magic Resistance
                               0,           # Base Magic Resistance per level
                               335,         # Base Movement Speed
                               500,         # Base Range
                               "Mana",      # Resource
                               [passive,    # Passive
                                ability1,   # Ability 1 (Q/A)
                                ability2,   # Ability 2 (W/Z)
                                ability3,   # Ability 3 (E)
                                ability4])  # Ability 4 (R)