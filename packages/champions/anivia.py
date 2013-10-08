# -*-coding:utf-8 -*
from packages.basics import champion, ability

class Anivia(champion.Champion):
  """ Anivia, the Cryophoenix
  
  Ref : http://leagueoflegends.wikia.com/wiki/Anivia
  
  """
  
  def __init__(self):
    # Basic stats
    base_hp = 350
    base_hp_plus = 70
    base_hp5 = 4.65
    base_hp5_plus = 0.55
    base_mp = 257
    base_mp_plus = 53
    base_mp5 = 7
    base_mp5_plus = 0.6
    base_ad = 48
    base_ad_plus = 3.2
    base_as = 0.625
    base_as_plus = 0.0168
    base_ar = 10.5
    base_ar_plus = 4
    base_mr = 30
    base_mr_plus = 0
    base_ms = 325
    base_range = 600
        
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
    
    champion.Champion.__init__(self, base_hp, base_hp_plus, base_hp5,
                               base_hp5_plus, base_mp, base_mp_plus, base_mp5,
                               base_mp5_plus, base_ad, base_ad_plus, base_as,
                               base_as_plus, base_ar, base_ar_plus, base_mr,
                               base_mr_plus, base_ms, base_range, [passive,
                               ability1, ability2, ability3, ability4])