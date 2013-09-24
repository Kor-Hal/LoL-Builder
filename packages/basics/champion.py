# -*-coding:Latin-1 -*
class Champion:
  """ Defines a champion, with its most basic stats.
  
  Ref : http://leagueoflegends.wikia.com/wiki/Base_champion_statistics
  
  """
  
  def __init__(self, base_hp, base_hp_plus, base_hp5, base_hp5_plus, base_mp, base_mp_plus, 
              base_mp5, base_mp5_plus, base_ad, base_ad_plus, base_as, base_as_plus, base_ar, base_ar_plus, 
              base_mr, base_mr_plus, base_ms, base_range,
              abilities,
              masteries,
              runes,
              itemsSet):
    """ Initializing the basic stats.
    
    Named parameters :
    base_hp -- Base health
    base_hp_plus -- Base health per level
    base_hp5 -- Base health regeneration
    base_hp5_plus -- Base health regeneration per level
    base_mp -- Base mana/energy
    base_mp_plus -- Base mana/energy per level
    base_mp5 -- Base mana/energy regeneration
    base_mp5_plus -- Base mana/energy regeneration per level
    base_ad -- Base attack damage
    base_ad_plus -- Base attack damage per level
    base_as -- Base attack speed
    base_as_plus -- Base attack speed per level
    base_ar -- Base armor
    base_ar_plus -- Base armor per level
    base_mr -- Base magic resistance
    base_mr_plus -- Base magic resistance per level
    base_ms -- Base movement speed
    base_range -- Base range
    abilities -- Champion's abilities
    masteries -- Champion's masteries
    runes -- Champion's runes
    itemsSet -- Champion's items
    
    """
    
    self.base_hp = base_hp
    self.base_hp_plus = base_hp_plus
    self.base_hp5 = base_hp5
    self.base_hp5_plus = base_hp5_plus
    self.base_mp = base_mp
    self.base_mp_plus = base_mp_plus
    self.base_mp5 = base_mp5
    self.base_mp5_plus = base_mp5_plus
    self.base_ad = base_ad
    self.base_ad_plus = base_ad_plus
    self.base_as = base_as
    self.base_as_plus = base_as_plus
    self.base_ar = base_ar
    self.base_ar_plus = base_ar_plus
    self.base_mr = base_mr
    self.base_mr_plus = base_mr_plus
    self.base_ms = base_ms
    self.base_range = base_range
    self.abilities = abilities
    self.masteries = masteries
    self.runes = runes
    self.itemSet = itemsSet
  
  # Functions calculating basic stats. Attack Speed is special, because it's not an addition
  def curr_base_hp(self, level):
    return self.base_hp + self.base_hp_plus * (level + 1)
  def curr_base_hp5(self, level):
    return self.base_hp5 + self.base_hp5 * (level + 1)
  def curr_base_mp(self, level):
    return self.base_mp + self.base_mp * (level + 1)
  def curr_base_mp5(self, level):
    return self.base_mp5 + self.base_mp5 * (level + 1)
  def curr_base_ad(self, level):
    return self.base_ad + self.base_ad * (level + 1)
  def curr_base_ar(self, level):
    return self.base_ar + self.base_ar * (level + 1)
  def curr_base_mr(self, level):
    return self.base_mr + self.base_mr * (level + 1)
  
  # Defining current stats functions. They'll be implemented in every subclass that needs specific calculations
  def curr_hp(self, level):
    return round(self.base_hp + self.base_hp_plus * level, 2)
  def curr_hp5(self, level):
    return round(self.base_hp5 + self.base_hp5_plus * level, 2)
  def curr_mp(self, level):
    return round(self.base_mp + self.base_mp_plus * level, 2)
  def curr_mp5(self, level):
    return round(self.base_mp5 + self.base_mp5_plus * level, 2)
  def curr_ad(self, level):
    return round(self.base_ad + self.base_ad_plus * level, 2)
  def curr_as(self, level):
    return round(self.base_as * (1 + self.base_as_plus * (level - 1)), 3)
  def curr_ar(self, level):
    return round(self.base_ar + self.base_ar_plus * level, 2)
  def curr_mr(self, level):
    return round(self.base_mr + self.base_mr_plus * level, 2)
  def curr_ms(self, level):
    return self.base_ms
  def curr_range(self, level):
    return self.base_range
