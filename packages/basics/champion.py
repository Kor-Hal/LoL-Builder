# -*-coding:Latin-1 -*
class Champion(object):
  """Defines a champion, with its most basic stats.
  
  Ref : http://leagueoflegends.wikia.com/wiki/Base_champion_statistics
  
  """
  
  def __init__(self, base_hp, base_hp_plus, base_hp5, base_hp5_plus, base_mp, base_mp_plus, 
              base_mp5, base_mp5_plus, base_ad, base_ad_plus, base_as, base_as_plus, base_ar, base_ar_plus, 
              base_mr, base_mr_plus, base_ms, base_range,
              abilities,
              masteries=None,
              runes=None,
              itemsSet={'Slot 1': None, 'Slot 2': None, 'Slot 3': None, 'Slot 4': None, 'Slot 5': None, 'Slot 6': None}):
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
    self.masteries = masteries
    self.runes = runes
    self.itemSet = itemsSet
  
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
    """Base Health Points regeneration augmentation per level of the champion."""
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
  
  # Defining current stats functions. They'll be implemented in every subclass that needs specific calculations
  def current_hp(self, level):
    return round(self.base_hp + self.base_hp_plus * level, 2)
  def current_hp5(self, level):
    return round(self.base_hp5 + self.base_hp5_plus * level, 2)
  def current_mp(self, level):
    return round(self.base_mp + self.base_mp_plus * level, 2)
  def current_mp5(self, level):
    return round(self.base_mp5 + self.base_mp5_plus * level, 2)
  def current_ad(self, level):
    return round(self.base_ad + self.base_ad_plus * level, 2)
  def current_as(self, level):
    return round(self.base_as * (1 + self.base_as_plus * (level - 1)), 3)
  def current_ar(self, level):
    return round(self.base_ar + self.base_ar_plus * level, 2)
  def current_mr(self, level):
    return round(self.base_mr + self.base_mr_plus * level, 2)
  def current_ms(self, level):
    return self.base_ms
  def current_range(self, level):
    return self.base_range
