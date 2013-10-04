# -*-coding:utf-8 -*
class Champion(object):
  """Defines a champion, with its most basic stats.
  
  Ref : http://leagueoflegends.wikia.com/wiki/Base_champion_statistics
  
  """
  
  def __init__(self, base_hp, base_hp_plus, base_hp5, base_hp5_plus, base_mp,
                     base_mp_plus, base_mp5, base_mp5_plus, base_ad,
                     base_ad_plus, base_as, base_as_plus, base_ar,
                     base_ar_plus, base_mr, base_mr_plus, base_ms, base_range,
                     abilities,
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
    
    self._base_hp = base_hp
    self._base_hp_plus = base_hp_plus
    self._base_hp5 = base_hp5
    self._base_hp5_plus = base_hp5_plus
    self._base_mp = base_mp
    self._base_mp_plus = base_mp_plus
    self._base_mp5 = base_mp5
    self._base_mp5_plus = base_mp5_plus
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
    self._abilities = abilities
    self._masteries = masteries
    self._runes = runes
    self._itemsSet = itemsSet
  
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
  def base_mp(self):
    """Base Mana Points of the champion."""
    return self._base_mp
  
  @property
  def base_mp_plus(self):
    """Base Mana Points augmentation per level of the champion."""
    return self._base_mp_plus
  
  @property
  def base_mp5(self):
    """Base Mana Points regeneration of the champion."""
    return self._base_mp5
  
  @property
  def base_mp5_plus(self):
    """Base Mana Points regeneration augmentation per level of the champion."""
    return self._base_mp5_plus
    
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
  
  # Defining current stats functions. They'll be implemented in every subclass
  # that needs specific calculations

  def current_hp(self, level):
    total = 0
    total += self.base_hp + self.base_hp_plus * level
    if self.runes is not None:
      total += self.runes.health + self.runes.scaling_health * level
    if self.masteries is not None:
      total += self.masteries.health + self.masteries.scaling_health * level
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
  def current_hp5(self, level):
    total = 0
    total += self.base_hp5 + self.base_hp5_plus * level
    if self.runes is not None:
      total += (self.runes.health_regeneration +
                self.runes.scaling_health_regeneration * level)
    for key in self.itemsSet.keys():
      if self.itemsSet[key] is not None:
        total += self.itemsSet[key].health_regeneration

    return round(total, 2)
  def current_mp(self, level):
    total = 0
    total += self.base_mp + self.base_mp_plus * level
    if self.runes is not None:
      total += self.runes.mana + self.runes.scaling_mana * level
    if self.masteries is not None:
      total += self.masteries.scaling_mana * level
    for key in self.itemsSet.keys():
      if self.itemsSet[key] is not None:
        total += self.itemsSet[key].mana

    return round(total, 2)
  def current_mp5(self, level):
    total = 0
    total += self.base_mp5 + self.base_mp5_plus * level
    if self.runes is not None:
      total += (self.runes.mana_regeneration +
                self.runes.scaling_mana_regeneration * level)
    for key in self.itemsSet.keys():
      if self.itemsSet[key] is not None:
        total += self.itemsSet[key].mana_regeneration

    return round(total, 2)
  def current_ad(self, level):
    total = 0
    total += self.base_ad + self.base_ad_plus * level
    if self.runes is not None:
      total += (self.runes.attack_damage + self.runes.scaling_attack_damage *
                                            level)
    if self.masteries is not None:
      total += (self.masteries.attack_damage +
                self.masteries.scaling_attack_damage * level)
    for key in self.itemsSet.keys():
      if self.itemsSet[key] is not None:
        total += self.itemsSet[key].attack_damage

    return round(total, 2)
  def current_as(self, level):
    perc_as = 0
    perc_as += self.base_as_plus * (level - 1)
    if self.runes is not None:
      perc_as += self.runes.attack_speed
    if self.masteries is not None:
      perc_as += self.masteries.attack_speed
    for key in self.itemsSet.keys():
      if self.itemsSet[key] is not None:
        perc_as += self.itemsSet[key].attack_speed

    total = self.base_as * (1 + perc_as)

    return round(total, 3)
  def current_ar(self, level):
    total = 0
    total += self.base_ar + self.base_ar_plus * level
    if self.runes is not None:
      total += self.runes.armor + self.runes.scaling_armor * level
    if self.masteries is not None:
      total += self.masteries.armor
    for key in self.itemsSet.keys():
      if self.itemsSet[key] is not None:
        total += self.itemsSet[key].armor

    return round(total, 2)
  def current_mr(self, level):
    total = 0
    total += self.base_mr + self.base_mr_plus * level
    if self.runes is not None:
      total += (self.runes.magic_resistance +
                self.runes.scaling_magic_resistance * level)
    if self.masteries is not None:
      total += self.masteries.magic_resistance
    for key in self.itemsSet.keys():
      if self.itemsSet[key] is not None:
        total += self.itemsSet[key].magic_resistance

    return round(total, 2)
  def current_ms(self, level):
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
  def current_range(self, level):
    return self.base_range
