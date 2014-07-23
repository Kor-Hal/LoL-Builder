# -*-coding:utf-8 -*
class RunePage(object):
  """Defines a Rune page.
  
  Ref : http://leagueoflegends.wikia.com/wiki/Runes
  
  """
  
  def __init__(self,
               name):
    """Create a new empty Rune page.
    
    Named parameters :
    name -- Rune page's name
    
    """
    
    self._name = name
    self._marks = [None,None,None,None,None,None,None,None,None]
    self._seals = [None,None,None,None,None,None,None,None,None]
    self._glyphs = [None,None,None,None,None,None,None,None,None]
    self._quintessences = [None,None,None]
    self._statistics = dict(ability_power=0, armor=0, flat_armor_penetration=0,
                       attack_damage=0, attack_speed=0, cooldown_reduction=0,
                       critical_strike_chance=0, critical_strike_damage=0,
                       energy=0, energy_regeneration=0, experience=0, gold=0,
                       health=0, health_regeneration=0, life_steal=0,
                       flat_magic_penetration=0, magic_resistance=0, mana=0,
                       mana_regeneration=0, percent_movement_speed=0,
                       percent_health=0, revival=0, scaling_ability_power=0,
                       scaling_armor=0, scaling_attack_damage=0,
                       scaling_cooldown_reduction=0, scaling_energy=0,
                       scaling_energy_regeneration=0, scaling_health=0,
                       scaling_health_regeneration=0,
                       scaling_magic_resistance=0, scaling_mana=0,
                       scaling_mana_regeneration=0, spell_vamp=0)
  
  @property
  def name(self):
    """Rune page's name."""
    return self._name
  
  @property
  def marks(self):
    """Marks in the Rune page."""
    return self._marks
  
  @marks.setter
  def marks(self, value):
    self._marks = value
  
  @property
  def seals(self):
    """Seals in the Rune page."""
    return self._seals
  
  @seals.setter
  def seals(self, value):
    self._seals = value
  
  @property
  def glyphs(self):
    """Glyphs in the Rune page."""
    return self._glyphs
  
  @glyphs.setter
  def glyphs(self, value):
    self._glyphs = value
  
  @property
  def quintessences(self):
    """Quintessences in the Rune page."""
    return self._quintessences
  
  @quintessences.setter
  def quintessences(self, value):
    self._quintessences = value
  
  @property
  def statistics(self):
    """Dict of Rune page's bonus statistics."""
    return self._statistics
  
  @property
  def ability_power(self):
    """Bonus Ability Power of the Rune page."""
    return self.statistics['ability_power']
  
  @property
  def armor(self):
    """Bonus Armor of the Rune page."""
    return self.statistics['armor']
  
  @property
  def flat_armor_penetration(self):
    """Bonus Flat Armor Penetration of the Rune page."""
    return self.statistics['flat_armor_penetration']
  
  @property
  def attack_damage(self):
    """Bonus Attack Damage of the Rune page."""
    return self.statistics['attack_damage']
  
  @property
  def attack_speed(self):
    """Bonus Attack Speed of the Rune page."""
    return self.statistics['attack_speed']
  
  @property
  def cooldown_reduction(self):
    """Bonus Cooldown Reduction of the Rune page."""
    return self.statistics['cooldown_reduction']
  
  @property
  def critical_strike_chance(self):
    """Bonus Critical Strike Chance of the Rune page."""
    return self.statistics['critical_strike_chance']
  
  @property
  def critical_strike_damage(self):
    """Bonus Critical Strike Damage of the Rune page."""
    return self.statistics['critical_strike_damage']
  
  @property
  def energy(self):
    """Bonus Energy of the Rune page."""
    return self.statistics['energy']
  
  @property
  def energy_regeneration(self):
    """Bonus Energy Regeneration of the Rune page."""
    return self.statistics['energy_regeneration']
  
  @property
  def experience(self):
    """Bonus Experience of the Rune page."""
    return self.statistics['experience']
  
  @property
  def gold(self):
    """Bonus Gold of the Rune page."""
    return self.statistics['gold']
  
  @property
  def health(self):
    """Bonus Health of the Rune page."""
    return self.statistics['health']
  
  @property
  def health_regeneration(self):
    """Bonus Health Regeneration of the Rune page."""
    return self.statistics['health_regeneration']
  
  @property
  def life_steal(self):
    """Bonus Life Steal of the Rune page."""
    return self.statistics['life_steal']
  
  @property
  def flat_magic_penetration(self):
    """Bonus Flat Magic Penetration of the Rune page."""
    return self.statistics['flat_magic_penetration']
  
  @property
  def magic_resistance(self):
    """Bonus Magic Resistance of the Rune page."""
    return self.statistics['magic_resistance']
  
  @property
  def mana(self):
    """Bonus Mana of the Rune page."""
    return self.statistics['mana']
  
  @property
  def mana_regeneration(self):
    """Bonus Mana Regeneration of the Rune page."""
    return self.statistics['mana_regeneration']
  
  @property
  def percent_movement_speed(self):
    """Bonus Percent Movement Speed of the Rune page."""
    return self.statistics['percent_movement_speed']
  
  @property
  def percent_health(self):
    """Bonus Percent Health of the Rune page."""
    return self.statistics['percent_health']
  
  @property
  def revival(self):
    """Bonus Revival of the Rune page."""
    return self.statistics['revival']
  
  @property
  def scaling_ability_power(self):
    """Bonus Scaling Ability Power of the Rune page."""
    return self.statistics['scaling_ability_power']
      
  @property
  def scaling_armor(self):
    """Bonus Scaling Armor of the Rune page."""
    return self.statistics['scaling_armor']
  
  @property
  def scaling_attack_damage(self):
    """Bonus Scaling Attack Damage of the Rune page."""
    return self.statistics['scaling_attack_damage']
  
  @property
  def scaling_cooldown_reduction(self):
    """Bonus Scaling Cooldown Reduction of the Rune page."""
    return self.statistics['scaling_cooldown_reduction']
  
  @property
  def scaling_energy(self):
    """Bonus Scaling Energy of the Rune page."""
    return self.statistics['scaling_energy']
  
  @property
  def scaling_energy_regeneration(self):
    """Bonus Scaling Energy Regeneration of the Rune page."""
    return self.statistics['scaling_energy_regeneration']
  
  @property
  def scaling_health(self):
    """Bonus Scaling Health of the Rune page."""
    return self.statistics['scaling_health']
  
  @property
  def scaling_health_regeneration(self):
    """Bonus Scaling Health Regeneration of the Rune page."""
    return self.statistics['scaling_health_regeneration']
  
  @property
  def scaling_magic_resistance(self):
    """Bonus Scaling Magic Resistance of the Rune page."""
    return self.statistics['scaling_magic_resistance']
  
  @property
  def scaling_mana(self):
    """Bonus Scaling Mana of the Rune page."""
    return self.statistics['scaling_mana']
  
  @property
  def scaling_mana_regeneration(self):
    """Bonus Scaling Mana Regeneration of the Rune page."""
    return self.statistics['scaling_mana_regeneration']
  
  @property
  def spell_vamp(self):
    """Bonus Spell Vamp of the Rune page."""
    return self.statistics['spell_vamp']
  
  def update_statistics(self):
    for statistic in self.statistics.keys():
      self.statistics[statistic] = 0
      
      for mark in self.marks:
        if mark is not None:
          self.statistics[statistic] += getattr(mark, statistic)
      
      for seal in self.seals:
        if seal is not None:
          self.statistics[statistic] += getattr(seal, statistic)
      
      for glyph in self.glyphs:
        if glyph is not None:
          self.statistics[statistic] += getattr(glyph, statistic)
      
      for quintessence in self.quintessences:
        if quintessence is not None:
          self.statistics[statistic] += getattr(quintessence, statistic)
  
  def add_rune(self, rune, position):
    """Add a Rune to the right part of the Rune page."""
    if rune.kind == "Mark":
      self.marks[position] = rune
    elif rune.kind == "Seal":
      self.seals[position] = rune
    elif rune.kind == "Glyph":
      self.glyphs[position] = rune
    elif rune.kind == "Quintessence":
      self.quintessences[position] = rune
    
    self.update_statistics()
  
  def del_rune(self, kind, position):
    """Delete a Rune from the Rune page."""
    if kind == "Mark":
      self.marks[position] = None
    elif kind == "Seal":
      self.seals[position] = None
    elif kind == "Glyph":
      self.glyphs[position] = None
    elif kind == "Quintessence":
      self.quintessences[position] = None
    
    self.update_statistics()
