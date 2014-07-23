# -*-coding:utf-8 -*
from abc import ABCMeta

class Champion(metaclass=ABCMeta):
  """Defines a champion, with its most basic stats.
  This class should never be implemented. It's only here to be inherited and provide useful generic functions.
  
  Ref : http://leagueoflegends.wikia.com/wiki/Base_champion_statistics
  
  """
  
  def __init__(self,
               base_hp=None,
               base_hp_plus=None,
               base_hp5=None,
               base_hp5_plus=None,
               base_resource=None,
               base_resource_plus=None,
               base_resourceper5=None,
               base_resourceper5_plus=None,
               base_ad=None,
               base_ad_plus=None,
               base_as=None,
               base_as_plus=None,
               base_ar=None,
               base_ar_plus=None,
               base_mr=None,
               base_mr_plus=None,
               base_ms=None,
               base_range=None,
               resource=None,
               abilities=None,
               masteries=None,
               runes=None,
               itemsSet={"Slot 1":None, "Slot 2":None, "Slot 3":None,
                         "Slot 4":None, "Slot 5":None, "Slot 6":None}):
    """Initializing the basic stats.
    
    Named parameters :
    base_hp -- Base health
    base_hp_plus -- Base health per level
    base_hp5 -- Base health regeneration
    base_hp5_plus -- Base health regeneration per level
    base_resource -- Base mana/energy
    base_resource_plus -- Base mana/energy per level
    base_resourceper5 -- Base mana/energy regeneration
    base_resourceper5_plus -- Base mana/energy regeneration per level
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
    resource -- Champion's Resource (Mana, Energy, Health, None)
    abilities -- Champion's abilities
    masteries -- Champion's masteries
    runes -- Champion's runes
    itemsSet -- Champion's items
    
    """
    
    self._base_hp = base_hp
    self._base_hp_plus = base_hp_plus
    self._base_hp5 = base_hp5
    self._base_hp5_plus = base_hp5_plus
    self._base_resource = base_resource
    self._base_resource_plus = base_resource_plus
    self._base_resourceper5 = base_resourceper5
    self._base_resourceper5_plus = base_resourceper5_plus
    self._base_ad = base_ad
    self._base_ad_plus = base_ad_plus
    self._base_as = base_as
    self._base_as_plus = base_as_plus
    self._base_ar = base_ar
    self._base_ar_plus = base_ar_plus
    self._base_mr = base_mr
    self._base_mr_plus = base_mr_plus
    self._base_ms = base_ms
    self._base_range = base_range
    self._resource = resource
    self._abilities = abilities
    self._masteries = masteries
    self._runes = runes
    self._itemsSet = itemsSet
    
    self._currentLevel = 0
  
  @property
  def currentLevel(self):
    """Current level of the Champion"""
    return self._currentLevel
  
  @currentLevel.setter
  def currentLevel(self, value):
    if value < 1 or value > 18: # The level must be between 1 and 18
      raise ValueError
    else :
      self._currentLevel = value
  
  @property
  def base_hp(self):
    """Base Health Points of the champion."""
    return self._base_hp
  
  @property
  def base_hp_plus(self):
    """Base Health Points augmentation per level of the champion."""
    return self._base_hp_plus
  
  @property
  def base_hp5(self):
    """Base Health Points regeneration of the champion."""
    return self._base_hp5
  
  @property
  def base_hp5_plus(self):
    """Base Health Points regeneration augmentation per level of the
    champion."""
    return self._base_hp5_plus
  
  @property
  def base_resource(self):
    """Base Resource Points of the champion."""
    return self._base_resource
  
  @property
  def base_resource_plus(self):
    """Base Resource Points augmentation per level of the champion."""
    return self._base_resource_plus
  
  @property
  def base_resourceper5(self):
    """Base Resource Points regeneration of the champion."""
    return self._base_resourceper5
  
  @property
  def base_resourceper5_plus(self):
    """Base Resource Points regeneration augmentation per level of the champion."""
    return self._base_resourceper5_plus
    
  @property
  def base_ad(self):
    """Base Attack Damage of the champion."""
    return self._base_ad
  
  @property
  def base_ad_plus(self):
    """Base Attack Damage augmentation per level of the champion."""
    return self._base_ad_plus
  
  @property
  def base_as(self):
    """Base Attack Speed of the champion."""
    return self._base_as
  
  @property
  def base_as_plus(self):
    """Base Attack Speed augmentation per level of the champion."""
    return self._base_as_plus
  
  @property
  def base_ar(self):
    """Base Armor of the champion."""
    return self._base_ar
  
  @property
  def base_ar_plus(self):
    """Base Armor augmentation per level of the champion."""
    return self._base_ar_plus
  
  @property
  def base_mr(self):
    """Base Magic Resistance of the champion."""
    return self._base_mr
  
  @property
  def base_mr_plus(self):
    """Base Magic Resistance augmentation per level of the champion."""
    return self._base_mr_plus
  
  @property
  def base_ms(self):
    """Base Movement Speed of the champion."""
    return self._base_ms
  
  @property
  def base_range(self):
    """Base Range of the champion."""
    return self._base_range
  
  @property
  def resource(self):
    """Champion's Resource."""
    return self._resource

  @property
  def abilities(self):
    """Abilities of the champion."""
    return self._abilities
  
  @property
  def masteries(self):
   """Champion's masteries."""
   return self._masteries
  
  @masteries.setter
  def masteries(self, value):
    self._masteries = value
  
  @property
  def runes(self):
   """Champion's runes"""
   return self._runes
  
  @runes.setter
  def runes(self, value):
    self._runes = value
  
  @property
  def itemsSet(self):
   """Champion's items"""
   return self._itemsSet
  
  @property
  def level(self):
    """Current level of the champion. Goes from 1 to 18."""
    return self._currentLevel
  
  @level.setter
  def level(self, value):
    if value < 1 or value > 18: # Level must be between 1 and 18
      raise ValueError
    else:
      self._currentLevel = value
  
  # Defining current stats functions. They'll be implemented in every subclass
  # that needs specific calculations

  def current_hp(self):
    total = 0
    total += self.base_hp + self.base_hp_plus * self.currentLevel
    if self.runes is not None:
      total += self.runes.health + self.runes.scaling_health * self.currentLevel
    if self.masteries is not None:
      total += self.masteries.health + self.masteries.scaling_health * self.currentLevel
    
    for key in self.itemsSet.keys():
      if self.itemsSet[key] is not None:
        total += self.itemsSet[key].health
    
    perc_hp = 0
    if self.runes is not None:
      perc_hp += self.runes.percent_health
    if self.masteries is not None:
      perc_hp += self.masteries.percent_health

    total *= 1 + perc_hp

    return round(total, 2)
    
  def current_hp5(self):
    total = 0
    total += self.base_hp5 + self.base_hp5_plus * self.currentLevel
    if self.runes is not None:
      total += (self.runes.health_regeneration +
                self.runes.scaling_health_regeneration * self.currentLevel)
    
    for key in self.itemsSet.keys():
      if self.itemsSet[key] is not None:
        total += self.itemsSet[key].health_regeneration

    return round(total, 2)
    
  def current_mp(self):
    total = 0
    total += self.base_resource + self.base_resource_plus * self.currentLevel
    if self.runes is not None:
      total += self.runes.mana + self.runes.scaling_mana * self.currentLevel
    if self.masteries is not None:
      total += self.masteries.scaling_mana * self.currentLevel
    
    for key in self.itemsSet.keys():
      if self.itemsSet[key] is not None:
        total += self.itemsSet[key].mana

    return round(total, 2)
    
  def current_mp5(self):
    total = 0
    total += self.base_resourceper5 + self.base_resourceper5_plus * self.currentLevel
    if self.runes is not None:
      total += (self.runes.mana_regeneration +
                self.runes.scaling_mana_regeneration * self.currentLevel)
    
    for key in self.itemsSet.keys():
      if self.itemsSet[key] is not None:
        total += self.itemsSet[key].mana_regeneration

    return round(total, 2)
    
  def current_ad(self):
    total = 0
    total += self.base_ad + self.base_ad_plus * self.currentLevel
    if self.runes is not None:
      total += (self.runes.attack_damage + self.runes.scaling_attack_damage *
                                            self.currentLevel)
    if self.masteries is not None:
      total += (self.masteries.attack_damage +
                self.masteries.scaling_attack_damage * self.currentLevel)
    
    for key in self.itemsSet.keys():
      if self.itemsSet[key] is not None:
        total += self.itemsSet[key].attack_damage

    return round(total, 2)
    
  def current_as(self):
    perc_as = 0
    perc_as += self.base_as_plus * (self.currentLevel - 1)
    
    if self.runes is not None:
      perc_as += self.runes.attack_speed
    if self.masteries is not None:
      perc_as += self.masteries.attack_speed
    for key in self.itemsSet.keys():
      if self.itemsSet[key] is not None:
        perc_as += self.itemsSet[key].attack_speed

    total = self.base_as * (1 + perc_as)
    total = min(total, 2.5) # AS is caped at 2.5

    return round(total, 3)
    
  def current_ar(self):
    total = 0
    total += self.base_ar + self.base_ar_plus * self.currentLevel
    if self.runes is not None:
      total += self.runes.armor + self.runes.scaling_armor * self.currentLevel
    
    if self.masteries is not None:
      total += self.masteries.armor
    for key in self.itemsSet.keys():
      if self.itemsSet[key] is not None:
        total += self.itemsSet[key].armor

    return round(total, 2)
    
  def current_mr(self):
    total = 0
    total += self.base_mr + self.base_mr_plus * self.currentLevel
    if self.runes is not None:
      total += (self.runes.magic_resistance +
                self.runes.scaling_magic_resistance * self.currentLevel)
    
    if self.masteries is not None:
      total += self.masteries.magic_resistance
    for key in self.itemsSet.keys():
      if self.itemsSet[key] is not None:
        total += self.itemsSet[key].magic_resistance

    return round(total, 2)
    
  def current_ms(self):
    total = 0
    total += self.base_ms
    if self.masteries is not None:
      total += self.masteries.movement_speed
    for key in self.itemsSet.keys():
      if self.itemsSet[key] is not None:
        total += self.itemsSet[key].flat_movement_speed

    perc_ms = 0
    if self.runes is not None:
      perc_ms += self.runes.percent_movement_speed
    for key in self.itemsSet.keys():
      if self.itemsSet[key] is not None:
        perc_ms += self.itemsSet[key].perc_movement_speed

    total *= 1 + perc_ms

    return round(total, 2)
    
  def current_range(self):
    return self.base_range
