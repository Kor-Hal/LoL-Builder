# -*-coding:utf-8 -*
class Rune(object):
  """Defines a Rune.
  
  Ref : http://leagueoflegends.wikia.com/wiki/List_of_runes
  
  """
  
  def __init__(self, tier, kind, name, rank, cost, icon, 
               ability_power=0, armor=0, flat_armor_penetration=0,
               attack_damage=0, attack_speed=0, cooldown_reduction=0, 
               critical_strike_chance=0, critical_strike_damage=0, energy=0,
               energy_regeneration=0, experience=0, gold=0, health=0,
               health_regeneration=0, life_steal=0, flat_magic_penetration=0,
               magic_resistance=0, mana=0, mana_regeneration=0,
               percent_movement_speed=0, percent_health=0, revival=0,
               scaling_ability_power=0, scaling_armor=0,
               scaling_attack_damage=0, scaling_cooldown_reduction=0,
               scaling_energy=0, scaling_energy_regeneration=0,
               scaling_health=0, scaling_health_regeneration=0,
               scaling_magic_resistance=0, scaling_mana=0,
               scaling_mana_regeneration=0, spell_vamp=0):
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
    flat_armor_penetration -- Bonus flat ArPen
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
    flat_magic_penetration -- Bonus flat MPen
    magic_resistance -- Bonus MR
    mana -- Bonus MP
    mana_regeneration -- Bonus MP5
    percent_movement_speed -- Bonus Percent MS
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
    self._flat_armor_penetration = flat_armor_penetration
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
    self._flat_magic_penetration = flat_magic_penetration
    self._magic_resistance = magic_resistance
    self._mana = mana
    self._mana_regeneration = mana_regeneration
    self._percent_movement_speed = percent_movement_speed
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
  def flat_armor_penetration(self):
    """Rune's armor penetration bonus."""
    return self._flat_armor_penetration
  
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
  def flat_magic_penetration(self):
    """Rune's magic penetration bonus."""
    return self._flat_magic_penetration
  
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
  def percent_movement_speed(self):
    """Rune's percent movement speed bonus."""
    return self._percent_movement_speed
  
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
