# -*-coding:Latin-1 -*
class Item:
  """ Defines an item, with its basic characteristics, and the stats it gives.
  
  Ref : http://leagueoflegends.wikia.com/wiki/Item
  """
  
  def __init__(self, availability, tier, cost, menu, recipe, actives, passives, 
               armor_penetration, attack_damage, attack_speed, critical_strike_chance, critical_strike_damage, 
               life_steal, movement_speed, armor, health, health_regeneration, magic_resistance, 
               ability_power, cooldown_reduction, magic_penetration, mana, mana_regeneration, spell_vamp):
    """ Initializing the item's stats.
    
    Named parmorameters :
    availability -- Map on which the item may be bought
    tier -- Item's tier (Consumable, Basic, Advanced, Legendary, Mythical)
    cost -- Item's cost
    menu -- Menu(s) to access the item in shop
    recipe -- Item's recipe (List of items)
    actives -- Tuple of actives (descriptions)
    passives -- Tuple of passives (descriptions)
    armor_penetration -- Bonus Armor Penetration
    attack_damage -- Bonus Attack Damage
    attack_speed -- Bonus Attack Speed
    critical_strike_chance -- Bonus Critical Strike Chance
    critical_strike_damage -- Bonus Critical Strike Damage
    life_steal -- Bonus Life Steal
    movement_speed -- Bonus Movement Speed
    armor -- Bonus Armor
    health -- Bonus Health
    health_regeneration -- Bonus Health Regeneration
    magic_resistance -- Bonus Magic Resistance
    ability_power -- Bonus Ability Power
    cooldown_reduction -- Bonus Cooldown Reduction
    magic_penetration -- Bonus Magic Penetration
    mana -- Bonus Mana
    mana_regeneration -- Bonus Mana Regeneration
    spell_vamp -- Bonus Spell Vamp
        
    """
    
    self.availability = availability
    self.tier = tier
    self.cost = cost
    self.menu = menu
    self.recipe = recipe
    self.actives = actives
    self.passives = passives
    self.armor_penetration = armor_penetration
    self.attack_damage = attack_damage
    self.attack_speed = attack_speed
    self.critical_strike_chance = critical_strike_chance
    self.critical_strike_damage = critical_strike_damage
    self.life_steal = life_steal
    self.movement_speed = movement_speed
    self.armor = armor
    self.health = health
    self.health_regeneration = health_regeneration
    self.magic_resistance = magic_resistance
    self.ability_power = ability_power
    self.cooldown_reduction = cooldown_reduction
    self.magic_penetration = magic_penetration
    self.mana = mana
    self.mana_regeneration = mana_regeneration
    self.spell_vamp = spell_vamp
