# -*-coding:Latin-1 -*
from packages.basics import champion, ability

class Gragas(champion.Champion):
  """ Gragas, the Rabble Rouser
  
  Ref : http://leagueoflegends.wikia.com/wiki/Gragas
  
  """
  
  def __init__(self):
    # Basic stats
    baseHP = 434
    baseHPPlus = 89
    baseHP5 = 7.25
    baseHP5Plus = 0.85
    baseMP = 221
    baseMPPlus = 47
    baseMP5 = 6.45
    baseMP5Plus = 0.45
    baseAD = 55.78
    baseADPlus = 3.375
    baseAS = 0.651
    baseASPlus = 0.0205
    baseAR = 16
    baseARPlus = 3.6
    baseMR = 30
    baseMRPlus = 0
    baseMS = 340
    baseRange = 125
        
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
    
    champion.Champion.__init__(self, baseHP, baseHPPlus, baseHP5, baseHP5Plus, baseMP, baseMPPlus, 
                              baseMP5, baseMP5Plus, baseAD, baseADPlus, baseAS, baseASPlus, baseAR, baseARPlus, 
                              baseMR, baseMRPlus, baseMS, baseRange,
                              [passive, ability1, ability2, ability3, ability4],
                              {},
                              {},
                              {'Slot 1': None, 'Slot 2': None, 'Slot 3': None, 'Slot 4': None, 'Slot 5': None, 'Slot 6': None})
  
  # Defining current stats functions.
  def curr_hp(self, level):
    return round(self.baseHP + self.baseHPPlus * level, 2)
  def curr_hp5(self, level):
    return round(self.baseHP5 + self.baseHP5Plus * level, 2)
  def curr_mp(self, level):
    return round(self.baseMP + self.baseMPPlus * level, 2)
  def curr_mp5(self, level):
    return round(self.baseMP5 + self.baseMP5Plus * level, 2)
  def curr_ad(self, level):
    return round(self.baseAD + self.baseADPlus * level, 2)
  def curr_as(self, level):
    return round(self.baseAS * (1 + self.baseASPlus * (level - 1)), 3)
  def curr_ar(self, level):
    return round(self.baseAR + self.baseARPlus * level, 2)
  def curr_mr(self, level):
    return round(self.baseMR + self.baseMRPlus * level, 2)
  def curr_ms(self, level):
    return self.baseMS
  def curr_range(self, level):
    return self.baseRange
