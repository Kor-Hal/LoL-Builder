# -*-coding:utf-8 -*
class Item(object):
  """Defines an item, with its basic characteristics, and the stats it gives.
  
  Ref : http://leagueoflegends.wikia.com/wiki/Item
  """
  
  def __init__(self, availability, tier, cost, menu, recipe, actives, passives, 
               armor_penetration, attack_damage, attack_speed,
               critical_strike_chance, critical_strike_damage, life_steal,
               movement_speed, armor, health, health_regeneration,
               magic_resistance, ability_power, cooldown_reduction,
               magic_penetration, mana, mana_regeneration, spell_vamp):
<<<<<<< HEAD
=======
               flat_armor_penetration, perc_armor_penetrationattack_damage, attack_speed, 
               critical_strike_chance, critical_strike_damage, life_steal, movement_speed, 
               armor, health, health_regeneration, magic_resistance, ability_power, 
               cooldown_reduction, magic_penetration, mana, mana_regeneration, spell_vamp):
>>>>>>> 9462e49... Adding properties to items
=======
>>>>>>> baec904... Still resolving conflicts
    """Initializing the item's stats.
    
    Named parmorameters :
    availability -- Map on which the item may be bought
    tier -- Item's tier (Consumable, Basic, Advanced, Legendary, Mythical)
    cost -- Item's cost
    menu -- Menu(s) to access the item in shop
    recipe -- Item's recipe (List of items)
    actives -- Tuple of actives (descriptions)
    passives -- Tuple of passives (descriptions)
    flat_armor_penetration -- Flat Armor Penetration
    perc_armor_penetration -- Percent Armor Penetration
    attack_damage -- Attack Damage
    attack_speed -- Attack Speed
    critical_strike_chance -- Critical Strike Chance
    critical_strike_damage -- Critical Strike Damage
    life_steal -- Life Steal
    movement_speed -- Movement Speed
    armor -- Armor
    health -- Health
    health_regeneration -- Health Regeneration
    magic_resistance -- Magic Resistance
    ability_power -- Ability Power
    cooldown_reduction -- Cooldown Reduction
    magic_penetration -- Magic Penetration
    mana -- Mana
    mana_regeneration -- Mana Regeneration
    spell_vamp -- Spell Vamp
        
    """
    
    self._availability = availability
    self._tier = tier
    self._cost = cost
    self._menu = menu
    self._recipe = recipe
    self._actives = actives
    self._passives = passives
    self._flat_armor_penetration = flat_armor_penetration
    self._perc_armor_penetration = perc_armor_penetration
    self._attack_damage = attack_damage
    self._attack_speed = attack_speed
    self._critical_strike_chance = critical_strike_chance
    self._critical_strike_damage = critical_strike_damage
    self._life_steal = life_steal
    self._movement_speed = movement_speed
    self._armor = armor
    self._health = health
    self._health_regeneration = health_regeneration
    self._magic_resistance = magic_resistance
    self._ability_power = ability_power
    self._cooldown_reduction = cooldown_reduction
    self._magic_penetration = magic_penetration
    self._mana = mana
    self._mana_regeneration = mana_regeneration
    self._spell_vamp = spell_vamp
  
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
  def actives(self):
  	"""Tuple of actives (descriptions)."""
  	return self._actives
  
  @property
  def passives(self):
  	"""Tuple of passives (descriptions)."""
  	return self._passives
  
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
  def movement_speed(self):
  	"""Movement Speed."""
  	return self._movement_speed
  
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
  def magic_penetration(self):
  	"""Magic Penetration."""
  	return self._magic_penetration
  
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
