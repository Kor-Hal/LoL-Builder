# -*-coding:Latin-1 -*
class Champion:
  """ Defines a champion, with its most basic stats.
  
  Ref : http://leagueoflegends.wikia.com/wiki/Base_champion_statistics
  
  """
  
  def __init__(self, baseHP, baseHPPlus, baseHP5, baseHP5Plus, baseMP, baseMPPlus, 
              baseMP5, baseMP5Plus, baseAD, baseADPlus, baseAS, baseASPlus, baseAR, baseARPlus, 
              baseMR, baseMRPlus, baseMS, baseRange,
              abilities,
              masteries,
              runes,
              itemsSet):
    """ Initializing the basic stats.
    
    Named parameters :
    baseHP -- Base health
    baseHPPlus -- Base health per level
    baseHP5 -- Base health regeneration
    baseHP5Plus -- Base health regeneration per level
    baseMP -- Base mana/energy
    baseMPPlus -- Base mana/energy per level
    baseMP5 -- Base mana/energy regeneration
    baseMP5Plus -- Base mana/energy regeneration per level
    baseAD -- Base attack damage
    baseADPlus -- Base attack damage per level
    baseAS -- Base attack speed
    baseASPlus -- Base attack speed per level
    baseAR -- Base armor
    baseARPlus -- Base armor per level
    baseMR -- Base magic resistance
    baseMRPlus -- Base magic resistance per level
    baseMS -- Base movement speed
    baseRange -- Base range
    abilities -- Champion's abilities
    masteries -- Champion's masteries
    runes -- Champion's runes
    itemsSet -- Champion's items
    
    """
    
    self.baseHP = baseHP
    self.baseHPPlus = baseHPPlus
    self.baseHP5 = baseHP5
    self.baseHP5Plus = baseHP5Plus
    self.baseMP = baseMP
    self.baseMPPlus = baseMPPlus
    self.baseMP5 = baseMP5
    self.baseMP5Plus = baseMP5Plus
    self.baseAD = baseAD
    self.baseADPlus = baseADPlus
    self.baseAS = baseAS
    self.baseASPlus = baseASPlus
    self.baseAR = baseAR
    self.baseARPlus = baseARPlus
    self.baseMR = baseMR
    self.baseMRPlus = baseMRPlus
    self.baseMS = baseMS
    self.baseRange = baseRange
    self.abilities = abilities
    self.masteries = masteries
    self.runes = runes
    self.itemSet = itemsSet
  
  # Functions calculating basic stats. Attack Speed is special, because it's not an addition
  def curr_base_hp(self, level):
    return self.baseHP + self.baseHPPlus * (level + 1)
  def curr_base_hp5(self, level):
    return self.baseHP5 + self.baseHP5 * (level + 1)
  def curr_base_mp(self, level):
    return self.baseMP + self.baseMP * (level + 1)
  def curr_base_mp5(self, level):
    return self.baseMP5 + self.baseMP5 * (level + 1)
  def curr_base_ad(self, level):
    return self.baseAD + self.baseAD * (level + 1)
  def curr_base_ar(self, level):
    return self.baseAR + self.baseAR * (level + 1)
  def curr_base_mr(self, level):
    return self.baseMR + self.baseMR * (level + 1)
  
  # Defining current stats functions. They'll be implemented in every subclass that needs specific calculations
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
