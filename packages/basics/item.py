# -*-coding:utf-8 -*
class Item(object):
  """Defines an item, with its basic characteristics, and the stats it gives.
  
  Ref : http://leagueoflegends.wikia.com/wiki/Item
  """
  
  def __init__(self, name, availability, tier, cost=None, menu=None,
               recipe=None, capacities=None,
               flat_armor_penetration=0, perc_armor_penetration=0,
               attack_damage=0, attack_speed=0, critical_strike_chance=0,
               critical_strike_damage=0, life_steal=0, flat_movement_speed=0,
               perc_movement_speed=0, armor=0, health=0, health_regeneration=0,
               magic_resistance=0, ability_power=0, cooldown_reduction=0,
               flat_magic_penetration=0, perc_magic_penetration=0, mana=0,
               mana_regeneration=0, spell_vamp=0):
    """Initializing the item's stats.
    
    Named parmorameters :
    name -- Item's name
    availability -- Map on which the item may be bought
    tier -- Item's tier (Consumable, Basic, Advanced, Legendary, Mythical)
    cost -- Item's cost
    menu -- Menu(s) to access the item in shop
    recipe -- Item's recipe (List of items)
    capacities -- Dict of capacities (type:description)
    flat_armor_penetration -- Flat Armor Penetration
    perc_armor_penetration -- Percent Armor Penetration
    attack_damage -- Attack Damage
    attack_speed -- Attack Speed
    critical_strike_chance -- Critical Strike Chance
    critical_strike_damage -- Critical Strike Damage
    life_steal -- Life Steal
    flat_movement_speed -- Flat Movement Speed
    perc_movement_speed -- Percent Movement Speed
    armor -- Armor
    health -- Health
    health_regeneration -- Health Regeneration
    magic_resistance -- Magic Resistance
    ability_power -- Ability Power
    cooldown_reduction -- Cooldown Reduction
    flat_magic_penetration -- Flat Magic Penetration
    perc_magic_penetration -- Percent Magic Penetration
    mana -- Mana
    mana_regeneration -- Mana Regeneration
    spell_vamp -- Spell Vamp
        
    """
    
    self._name = name
    self._availability = availability
    self._tier = tier
    self._cost = cost
    self._menu = menu
    self._recipe = recipe
    self._capacities = capacities
    self._flat_armor_penetration = flat_armor_penetration
    self._perc_armor_penetration = perc_armor_penetration
    self._attack_damage = attack_damage
    self._attack_speed = attack_speed
    self._critical_strike_chance = critical_strike_chance
    self._critical_strike_damage = critical_strike_damage
    self._life_steal = life_steal
    self._flat_movement_speed = flat_movement_speed
    self._perc_movement_speed = perc_movement_speed
    self._armor = armor
    self._health = health
    self._health_regeneration = health_regeneration
    self._magic_resistance = magic_resistance
    self._ability_power = ability_power
    self._cooldown_reduction = cooldown_reduction
    self._flat_magic_penetration = flat_magic_penetration
    self._perc_magic_penetration = perc_magic_penetration
    self._mana = mana
    self._mana_regeneration = mana_regeneration
    self._spell_vamp = spell_vamp
  
  @property
  def name(self):
    """Item's name."""
    return self._name

  @property
  def availabilty(self):
  	"""Map on which the item may be bought."""
  	return self._availability
  
  @property
  def tier(self):
  	"""Item's tier (Consumable, Basic, Advanced, Legendary, Mythical)."""
  	return self._tier
  
  @property
  def cost(self):
  	"""Item's cost."""
  	return self._cost
  
  @property
  def menu(self):
  	"""Menu(s) to access the item in shop."""
  	return self._menu
  
  @property
  def recipe(self):
  	"""Item's recipe (List of items)."""
  	return self._recipe
  
  @property
  def capacities(self):
  	"""Dict of capacities (type:description)."""
  	return self._capacities
  
  @property
  def flat_armor_penetration(self):
  	"""Flat Armor Penetration."""
  	return self._flat_armor_penetration
  
  @property
  def perc_armor_penetration(self):
  	"""Percent Armor Penetration."""
  	return self._perc_armor_penetration
  
  @property
  def attack_damage(self):
  	"""Attack Damage."""
  	return self._attack_damage
  
  @property
  def attack_speed(self):
  	"""Attack Speed."""
  	return self._attack_speed
  
  @property
  def critical_strike_chance(self):
  	"""Critical Strike Chance."""
  	return self._critical_strike_chance
  
  @property
  def critical_strike_damage(self):
  	"""Critical Strike Damage."""
  	return self._critical_strike_damage
  
  @property
  def life_steal(self):
  	"""Life Steal."""
  	return self._life_steal
  
  @property
  def flat_movement_speed(self):
  	"""Flat Movement Speed."""
  	return self._flat_movement_speed

  @property
  def perc_movement_speed(self):
  	"""Percent Movement Speed."""
  	return self._perc_movement_speed
  
  @property
  def armor(self):
  	"""Armor."""
  	return self._armor
  
  @property
  def health(self):
  	"""Health."""
  	return self._health
  
  @property
  def health_regeneration(self):
  	"""Health Regeneration."""
  	return self._health_regeneration
  
  @property
  def magic_resistance(self):
  	"""Magic Resistance."""
  	return self._magic_resistance
  
  @property
  def ability_power(self):
  	"""Ability Power."""
  	return self._ability_power
  
  @property
  def cooldown_reduction(self):
  	"""Cooldown Reduction."""
  	return self._cooldown_reduction
  
  @property
  def flat_magic_penetration(self):
  	"""Flat Magic Penetration."""
  	return self._flat_magic_penetration

  @property
  def perc_magic_penetration(self):
  	"""Percent Magic Penetration."""
  	return self._perc_magic_penetration
  
  @property
  def mana(self):
  	"""Mana."""
  	return self._mana
  
  @property
  def mana_regeneration(self):
  	"""Mana Regeneration."""
  	return self._mana_regeneration
  
  @property
  def spell_vamp(self):
  	"""Spell Vamp."""
  	return self._spell_vamp
