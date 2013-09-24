# -*-coding:Latin-1 -*
class Rune(object):
  """Defines a Rune.
  
  Ref : http://leagueoflegends.wikia.com/wiki/List_of_runes
  
  """
  
  def __init__(self, tier, kind, name, rank, cost, icon, 
               ability_power=0, armor=0, armor_penetration=0, attack_damage=0, attack_speed=0, cooldown_reduction=0, 
               critical_strike_chance=0, critical_strike_damage=0, energy=0, energy_regeneration=0, experience=0, 
               gold=0, health=0, health_regeneration=0, life_steal=0, magic_penetration=0, magic_resistance=0, mana=0, 
               mana_regeneration=0, movement_speed=0, percent_health=0, revival=0, scaling_ability_power=0, 
               scaling_armor=0, scaling_attack_damage=0, scaling_cooldown_reduction=0, scaling_energy=0, 
               scaling_energy_regeneration=0, scaling_health=0, scaling_health_regeneration=0, 
               scaling_magic_resistance=0, scaling_mana=0, scaling_mana_regeneration=0, spell_vamp=0):
    """ Create a new Rune.
    
    Named parameters :
    tier -- Rune's tier (Lesser, Normal or Greater)
    kind -- Rune's type (Mark, Seal, Glyph or Quintessence)
    name -- Rune's name
    rank -- Rune's rank (Primary or Secondary)
    cost -- IP cost
    icon -- Path to the Rune's icon
    ability_power -- Bonus AP
    armor -- Bonus Armor
    armor_penetration -- Bonus ArPen
    attack_damage -- Bonus AD
    attack_speed -- Bonus AS
    cooldown_reduction -- Bonus CDR
    critical_strike_chance -- Bonus CSC
    critical_strike_damage -- Bonus CSD
    energy -- Bonus Energy
    energy_regeneration -- Bonus Energy per 5
    experience -- Bonus Experience
    gold -- Bonus Gold per 5
    health -- Bonus HP
    health_regeneration -- Bonus HP5
    life_steal -- Bonus LS
    magic_penetration -- Bonus MPen
    magic_resistance -- Bonus MR
    mana -- Bonus MP
    mana_regeneration -- Bonus MP5
    movement_speed -- Bonus MS
    percent_health -- Bonus Percent HP
    revival -- Reduction of time dead
    scaling_ability_power -- Bonus AP per level
    scaling_armor -- Bonus Armor per level
    scaling_attack_damage -- Bonus AD per level
    scaling_cooldown_reduction -- Bonus CDR per level
    scaling_energy -- Bonus Energy per level
    scaling_energy_regeneration -- Bonus Energy per 5 per level
    scaling_health -- Bonus HP per level
    scaling_health_regeneration -- Bonus HP5 per level
    scaling_magic_resistance -- Bonus MR per level
    scaling_mana -- Bonus MP per level
    scaling_mana_regeneration -- Bonus MP5 per level
    spell_vamp -- Bonus SV
    
    """
    
    self._name = name
    self._kind = kind
    self._rank = rank
    self._cost = cost
    self._icon = icon
    self._ability_power = ability_power
    self._armor = armor
    self._armor_penetration = armor_penetration
    self._attack_damage = attack_damage
    self._attack_speed = attack_speed
    self._cooldown_reduction = cooldown_reduction
    self._critical_strike_chance = critical_strike_chance
    self._critical_strike_damage = critical_strike_damage
    self._energy = energy
    self._energy_regeneration = energy_regeneration
    self._experience = experience
    self._gold = gold
    self._health = health
    self._health_regeneration = health_regeneration
    self._life_steal = life_steal
    self._magic_penetration = magic_penetration
    self._magic_resistance = magic_resistance
    self._mana = mana
    self._mana_regeneration = mana_regeneration
    self._movement_speed = movement_speed
    self._percent_health = percent_health
    self._revival = revival
    self._scaling_ability_power = scaling_ability_power
    self._scaling_armor = scaling_armor
    self._scaling_attack_damage = scaling_attack_damage
    self._scaling_cooldown_reduction = scaling_cooldown_reduction
    self._scaling_energy = scaling_energy
    self._scaling_energy_regeneration = scaling_energy_regeneration
    self._scaling_health = scaling_health
    self._scaling_health_regeneration = scaling_health_regeneration
    self._scaling_magic_resistance = scaling_magic_resistance
    self._scaling_mana = scaling_mana
    self._scaling_mana_regeneration = scaling_mana_regeneration
    self._spell_vamp = spell_vamp
  
  @property
  def name(self):
    """Rune's name."""
    return self._name
  
  @property
  def kind(self):
    """Rune's type (Mark, Seal, Glyph or Quitenssence)."""
    return self._kind
  
  @property
  def rank(self):
    """Rune's rank (Primary or Secondary)."""
    return self._rank
  
  @property
  def cost(self):
    """Rune's IP cost."""
    return self._cost
  
  @property
  def icon(self):
    """Rune's icon."""
    return self._icon
  
  @property
  def ability_power(self):
    """Rune's ability power bonus."""
    return self._ability_power
  
  @property
  def armor(self):
    """Rune's armor bonus."""
    return self._armor
  
  @property
  def armor_penetration(self):
    """Rune's armor penetration bonus."""
    return self._armor_penetration
  
  @property
  def attack_damage(self):
    """Rune's attack damage bonus."""
    return self._attack_damage
  
  @property
  def attack_speed(self):
    """Rune's attack speed bonus."""
    return self._attack_speed
  
  @property
  def cooldown_reduction(self):
    """Rune's cooldown reduction bonus."""
    return self._cooldown_reduction
  
  @property
  def critical_strike_chance(self):
    """Rune's critical strike chance bonus."""
    return self._critical_strike_chance
  
  @property
  def critical_strike_damage(self):
    """Rune's critical strike damage bonus."""
    return self._critical_strike_damage
  
  @property
  def energy(self):
    """Rune's energy bonus."""
    return self._energy
  
  @property
  def energy_regeneration(self):
    """Rune's energy regeneration bonus."""
    return self._energy_regeneration
  
  @property
  def experience(self):
    """Rune's experience bonus."""
    return self._experience
  
  @property
  def gold(self):
    """Rune's gold bonus."""
    return self._gold
  
  @property
  def health(self):
    """Rune's health bonus."""
    return self._health
  
  @property
  def health_regeneration(self):
    """Rune's health regeneration bonus."""
    return self._health_regeneration
  
  @property
  def life_steal(self):
    """Rune's life steal bonus."""
    return self._life_steal
  
  @property
  def magic_penetration(self):
    """Rune's magic penetration bonus."""
    return self._magic_penetration
  
  @property
  def magic_resistance(self):
    """Rune's magic resistance bonus."""
    return self._magic_resistance
  
  @property
  def mana(self):
    """Rune's mana bonus."""
    return self._mana
  
  @property
  def mana_regeneration(self):
    """Rune's mana regeneration bonus."""
    return self._mana_regeneration
  
  @property
  def movement_speed(self):
    """Rune's movement speed bonus."""
    return self._movement_speed
  
  @property
  def percent_health(self):
    """Rune's percent health bonus."""
    return self._percent_health
  
  @property
  def revival(self):
    """Rune's revival bonus."""
    return self._revival
  
  @property
  def scaling_ability_power(self):
    """Rune's scaling ability power bonus."""
    return self._scaling_ability_power
  
  @property
  def scaling_armor(self):
    """Rune's scaling armor bonus."""
    return self._scaling_armor
  
  @property
  def scaling_attack_damage(self):
    """Rune's scaling attack damage bonus."""
    return self._scaling_attack_damage
  
  @property
  def scaling_cooldown_reduction(self):
    """Rune's scaling cooldown reduction bonus."""
    return self._scaling_cooldown_reduction
  
  @property
  def scaling_energy(self):
    """Rune's scaling energy bonus."""
    return self._scaling_energy
  
  @property
  def scaling_energy_regeneration(self):
    """Rune's scaling energy regeneration bonus."""
    return self._scaling_energy_regeneration
  
  @property
  def scaling_health(self):
    """Rune's scaling health bonus."""
    return self._scaling_health
  
  @property
  def scaling_health_regeneration(self):
    """Rune's scaling health regeneration bonus."""
    return self._scaling_health_regeneration
  
  @property
  def scaling_magic_resistance(self):
    """Rune's scaling magic resistance bonus."""
    return self._scaling_magic_resistance
  
  @property
  def scaling_mana(self):
    """Rune's scaling mana bonus."""
    return self._scaling_mana
  
  @property
  def scaling_mana_regeneration(self):
    """Rune's scaling mana regeneration bonus."""
    return self._scaling_mana_regeneration
  
  @property
  def spell_vamp(self):
    """Rune's spell vamp bonus."""
    return self._spell_vamp

class RunePage(object):
  """Defines a Rune page.
  
  Ref : http://leagueoflegends.wikia.com/wiki/Runes
  
  """
  
  def __init__(self, name):
    """Create a new empty Rune page.
    
    Named parameters :
    name -- Rune page's name
    
    """
    
    self._name = name
    self._marks = [None,None,None,None,None,None,None,None,None]
    self._seals = [None,None,None,None,None,None,None,None,None]
    self._glyphs = [None,None,None,None,None,None,None,None,None]
    self._quintessences = [None,None,None]
    self._statistics = dict(ability_power=0, armor=0, armor_penetration=0, attack_damage=0, attack_speed=0, 
    cooldown_reduction=0, critical_strike_chance=0, critical_strike_damage=0, energy=0, energy_regeneration=0, 
    experience=0, gold=0, health=0, health_regeneration=0, life_steal=0, magic_penetration=0, magic_resistance=0, 
    mana=0, mana_regeneration=0, movement_speed=0, percent_health=0, revival=0, scaling_ability_power=0, scaling_armor=0, 
    scaling_attack_damage=0, scaling_cooldown_reduction=0, scaling_energy=0, scaling_energy_regeneration=0, scaling_health=0, 
    scaling_health_regeneration=0, scaling_magic_resistance=0, scaling_mana=0, scaling_mana_regeneration=0, spell_vamp=0)
  
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
  def armor_penetration(self):
    """Bonus Armor Penetration of the Rune page."""
    return self.statistics['armor_penetration']
  
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
  def magic_penetration(self):
    """Bonus Magic Penetration of the Rune page."""
    return self.statistics['magic_penetration']
  
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
  def movement_speed(self):
    """Bonus Movement Speed of the Rune page."""
    return self.statistics['movement_speed']
  
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
