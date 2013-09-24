# -*-coding:Latin-1 -*
class Rune:
  """ Defines a Rune.
  
  Ref : http://leagueoflegends.wikia.com/wiki/List_of_runes
  
  """
  
  def __init__(self, tier, kind, name, rank, value, cost, icon, 
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
  
  # Read-only properties
  
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

# Ability Power
l_mark_of_ap = Rune("Lesser", "Mark", "Ability Power", "Secondary", 30, None, ability_power=0.33)
n_mark_of_ap = Rune("Normal", "Mark", "Ability Power", "Secondary", 165, None, ability_power=0.46)
g_mark_of_ap = Rune("Greater", "Mark", "Ability Power", "Secondary", 410, None, ability_power=0.59)
l_seal_of_ap = Rune("Lesser", "Seal", "Ability Power", "Secondary", 30, None, ability_power=0.33)
n_seal_of_ap = Rune("Normal", "Seal", "Ability Power", "Secondary", 165, None, ability_power=0.46)
g_seal_of_ap = Rune("Greater", "Seal", "Ability Power", "Secondary", 410, None, ability_power=0.59)
l_glyph_of_ap = Rune("Lesser", "Glyph", "Ability Power", "Primary", 30, None, ability_power=0.66)
n_glyph_of_ap = Rune("Normal", "Glyph", "Ability Power", "Primary", 165, None, ability_power=0.92)
g_glyph_of_ap = Rune("Greater", "Glyph", "Ability Power", "Primary", 410, None, ability_power=1.19)
l_quintessence_of_ap = Rune("Lesser", "Quintessence", "Ability Power", "Primary", 80, None, ability_power=2.75)
n_quintessence_of_ap = Rune("Normal", "Quintessence", "Ability Power", "Primary", 410, None, ability_power=3.85)
g_quintessence_of_ap = Rune("Greater", "Quintessence", "Ability Power", "Primary", 1025, None, ability_power=4.95)

# Armor
l_mark_of_armor = Rune("Lesser", "Mark", "Armor", "Secondary", 15, None, armor=0.51)
n_mark_of_armor = Rune("Normal", "Mark", "Armor", "Secondary", 80, None, armor=0.71)
g_mark_of_armor = Rune("Greater", "Mark", "Armor", "Secondary", 205, None, armor=0.91)
l_seal_of_armor = Rune("Lesser", "Seal", "Armor", "Primary", 15, None, armor=0.78)
n_seal_of_armor = Rune("Normal", "Seal", "Armor", "Primary", 80, None, armor=1.09)
g_seal_of_armor = Rune("Greater", "Seal", "Armor", "Primary", 205, None, armor=1.41)
l_glyph_of_armor = Rune("Lesser", "Glyph", "Armor", "Secondary", 15, None, armor=0.39)
n_glyph_of_armor = Rune("Normal", "Glyph", "Armor", "Secondary", 80, None, armor=0.55)
g_glyph_of_armor = Rune("Greater", "Glyph", "Armor", "Secondary", 205, None, armor=0.7)
l_quintessence_of_armor = Rune("Lesser", "Quintessence", "Armor", "Primary", 80, None, armor=2.37)
n_quintessence_of_armor = Rune("Normal", "Quintessence", "Armor", "Primary", 410, None, armor=3.32)
g_quintessence_of_armor = Rune("Greater", "Quintessence", "Armor", "Primary", 1025, None, armor=4.26)

# Armor Penetration
l_mark_of_armor_penetration = Rune("Lesser", "Mark", "Armor Penetration", "Primary", 30, None, armor_penetration=0.72)
n_mark_of_armor_penetration = Rune("Normal", "Mark", "Armor Penetration", "Primary", 165, None, armor_penetration=1)
g_mark_of_armor_penetration = Rune("Greater", "Mark", "Armor Penetration", "Primary", 410, None, armor_penetration=1.28)
l_quintessence_of_armor_penetration = Rune("Lesser", "Quintessence", "Armor Penetration", "Secondary", 80, None, armor_penetration=1.42)
n_quintessence_of_armor_penetration = Rune("Normal", "Quintessence", "Armor Penetration", "Secondary", 410, None, armor_penetration=1.99)
g_quintessence_of_armor_penetration = Rune("Greater", "Quintessence", "Armor Penetration", "Secondary", 1025, None, armor_penetration=2.56)

# Attack Damage
l_mark_of_attack_damage = Rune("Lesser", "Mark", "Attack Damage", "Primary", 15, None, attack_damage=0.53)
n_mark_of_attack_damage = Rune("Normal", "Mark", "Attack Damage", "Primary", 80, None, attack_damage=0.74)
g_mark_of_attack_damage = Rune("Greater", "Mark", "Attack Damage", "Primary", 205, None, attack_damage=0.95)
l_seal_of_attack_damage = Rune("Lesser", "Seal", "Attack Damage", "Secondary", 15, None, attack_damage=0.24)
n_seal_of_attack_damage = Rune("Normal", "Seal", "Attack Damage", "Secondary", 80, None, attack_damage=0.33)
g_seal_of_attack_damage = Rune("Greater", "Seal", "Attack Damage", "Secondary", 205, None, attack_damage=0.43)
l_glyph_of_attack_damage = Rune("Lesser", "Glyph", "Attack Damage", "Secondary", 15, None, attack_damage=0.16)
n_glyph_of_attack_damage = Rune("Normal", "Glyph", "Attack Damage", "Secondary", 80, None, attack_damage=0.22)
g_glyph_of_attack_damage = Rune("Greater", "Glyph", "Attack Damage", "Secondary", 205, None, attack_damage=0.28)
l_quintessence_of_attack_damage = Rune("Lesser", "Quintessence", "Attack Damage", "Secondary", 80, None, attack_damage=1.25)
n_quintessence_of_attack_damage = Rune("Normal", "Quintessence", "Attack Damage", "Secondary", 410, None, attack_damage=1.75)
g_quintessence_of_attack_damage = Rune("Greater", "Quintessence", "Attack Damage", "Secondary", 1025, None, attack_damage=2.25)

# Attack Speed
l_mark_of_attack_speed = Rune("Lesser", "Mark", "Attack Speed", "Primary", 30, None, attack_speed=0.0094)
n_mark_of_attack_speed = Rune("Normal", "Mark", "Attack Speed", "Primary", 165, None, attack_speed=0.0132)
g_mark_of_attack_speed = Rune("Greater", "Mark", "Attack Speed", "Primary", 410, None, attack_speed=0.017)
l_seal_of_attack_speed = Rune("Lesser", "Seal", "Attack Speed", "Secondary", 30, None, attack_speed=0.0042)
n_seal_of_attack_speed = Rune("Normal", "Seal", "Attack Speed", "Secondary", 165, None, attack_speed=0.0059)
g_seal_of_attack_speed = Rune("Greater", "Seal", "Attack Speed", "Secondary", 410, None, attack_speed=0.0076)
l_glyph_of_attack_speed = Rune("Lesser", "Glyph", "Attack Speed", "Secondary", 30, None, attack_speed=0.0035)
n_glyph_of_attack_speed = Rune("Normal", "Glyph", "Attack Speed", "Secondary", 165, None, attack_speed=0.005)
g_glyph_of_attack_speed = Rune("Greater", "Glyph", "Attack Speed", "Secondary", 410, None, attack_speed=0.0064)
l_quintessence_of_attack_speed = Rune("Lesser", "Quintessence", "Attack Speed", "Secondary", 80, None, attack_speed=0.0189)
n_quintessence_of_attack_speed = Rune("Normal", "Quintessence", "Attack Speed", "Secondary", 410, None, attack_speed=0.0264)
g_quintessence_of_attack_speed = Rune("Greater", "Quintessence", "Attack Speed", "Secondary", 1025, None, attack_speed=0.034)

# Cooldown Reduction
l_mark_of_cooldown_reduction = Rune("Lesser", "Mark", "Cooldown Reduction", "Secondary", 30, None, cooldown_reduction=0.0011)
n_mark_of_cooldown_reduction = Rune("Normal", "Mark", "Cooldown Reduction", "Secondary", 165, None, cooldown_reduction=0.0016)
g_mark_of_cooldown_reduction = Rune("Greater", "Mark", "Cooldown Reduction", "Secondary", 410, None, cooldown_reduction=0.002)
l_seal_of_cooldown_reduction = Rune("Lesser", "Seal", "Cooldown Reduction", "Secondary", 30, None, cooldown_reduction=0.002)
n_seal_of_cooldown_reduction = Rune("Normal", "Seal", "Cooldown Reduction", "Secondary", 165, None, cooldown_reduction=0.0029)
g_seal_of_cooldown_reduction = Rune("Greater", "Seal", "Cooldown Reduction", "Secondary", 410, None, cooldown_reduction=0.0036)
l_glyph_of_cooldown_reduction = Rune("Lesser", "Glyph", "Cooldown Reduction", "Primary", 65, None, cooldown_reduction=0.0047)
n_glyph_of_cooldown_reduction = Rune("Normal", "Glyph", "Cooldown Reduction", "Primary", 330, None, cooldown_reduction=0.0067)
g_glyph_of_cooldown_reduction = Rune("Greater", "Glyph", "Cooldown Reduction", "Primary", 820, None, cooldown_reduction=0.0083)
l_quintessence_of_cooldown_reduction = Rune("Lesser", "Quintessence", "Cooldown Reduction", "Secondary", 165, None, cooldown_reduction=0.0093)
n_quintessence_of_cooldown_reduction = Rune("Normal", "Quintessence", "Cooldown Reduction", "Secondary", 820, None, cooldown_reduction=0.0133)
g_quintessence_of_cooldown_reduction = Rune("Greater", "Quintessence", "Cooldown Reduction", "Secondary", 2050, None, cooldown_reduction=0.0167)

# Critical Chance
l_mark_of_critical_chance = Rune("Lesser", "Mark", "Critical Chance", "Primary", 30, None, critical_chance=0.0052)
n_mark_of_critical_chance = Rune("Normal", "Mark", "Critical Chance", "Primary", 165, None, critical_chance=0.0072)
g_mark_of_critical_chance = Rune("Greater", "Mark", "Critical Chance", "Primary", 410, None, critical_chance=0.0093)
l_seal_of_critical_chance = Rune("Lesser", "Seal", "Critical Chance", "Secondary", 30, None, critical_chance=0.0023)
n_seal_of_critical_chance = Rune("Normal", "Seal", "Critical Chance", "Secondary", 165, None, critical_chance=0.0032)
g_seal_of_critical_chance = Rune("Greater", "Seal", "Critical Chance", "Secondary", 410, None, critical_chance=0.0042)
l_glyph_of_critical_chance = Rune("Lesser", "Glyph", "Critical Chance", "Secondary", 30, None, critical_chance=0.0015)
n_glyph_of_critical_chance = Rune("Normal", "Glyph", "Critical Chance", "Secondary", 165, None, critical_chance=0.0022)
g_glyph_of_critical_chance = Rune("Greater", "Glyph", "Critical Chance", "Secondary", 410, None, critical_chance=0.0028)
l_quintessence_of_critical_chance = Rune("Lesser", "Quintessence", "Critical Chance", "Secondary", 80, None, critical_chance=0.0103)
n_quintessence_of_critical_chance = Rune("Normal", "Quintessence", "Critical Chance", "Secondary", 410, None, critical_chance=0.0144)
g_quintessence_of_critical_chance = Rune("Greater", "Quintessence", "Critical Chance", "Secondary", 1025, None, critical_chance=0.0186)

# Critical Damage
l_mark_of_critical_damage = Rune("Lesser", "Mark", "Critical Damage", "Primary", 65, None, critical_damage=0.0124)
n_mark_of_critical_damage = Rune("Normal", "Mark", "Critical Damage", "Primary", 330, None, critical_damage=0.0174)
g_mark_of_critical_damage = Rune("Greater", "Mark", "Critical Damage", "Primary", 820, None, critical_damage=0.0223)
l_seal_of_critical_damage = Rune("Lesser", "Seal", "Critical Damage", "Secondary", 65, None, critical_damage=0.0043)
n_seal_of_critical_damage = Rune("Normal", "Seal", "Critical Damage", "Secondary", 330, None, critical_damage=0.0061)
g_seal_of_critical_damage = Rune("Greater", "Seal", "Critical Damage", "Secondary", 820, None, critical_damage=0.0078)
l_glyph_of_critical_damage = Rune("Lesser", "Glyph", "Critical Damage", "Secondary", 65, None, critical_damage=0.0031)
n_glyph_of_critical_damage = Rune("Normal", "Glyph", "Critical Damage", "Secondary", 330, None, critical_damage=0.0043)
g_glyph_of_critical_damage = Rune("Greater", "Glyph", "Critical Damage", "Secondary", 820, None, critical_damage=0.0056)
l_quintessence_of_critical_damage = Rune("Lesser", "Quintessence", "Critical Damage", "Secondary", 80, None, critical_damage=0.0248)
n_quintessence_of_critical_damage = Rune("Normal", "Quintessence", "Critical Damage", "Secondary", 410, None, critical_damage=0.0347)
g_quintessence_of_critical_damage = Rune("Greater", "Quintessence", "Critical Damage", "Secondary", 1025, None, critical_damage=0.0446)

# Energy
g_glyph_of_energy = Rune("Greater", "Glyph", "Energy", "Primary", 820, None, energy=2.2)
g_quintessence_of_energy = Rune("Greater", "Quintessence", "Energy", "Primary", 1025, None, energy=5.4)

# Energy Regeneration
g_seal_of_energy_regeneration = Rune("Greater", "Seal", "Energy Regeneration", "Primary", 820, None, energy_regeneration=0.63)
g_quintessence_of_energy_regeneration = Rune("Greater", "Quintessence", "Energy Regeneration", "Primary", 2050, None, energy_regeneration=1.575)

# Experience
g_quintessence_of_experience = Rune("Greater", "Quintessence", "Experience", "Primary", 2050, None, experience=0.02)

# Gold (Gold / 10 sec)
g_seal_of_gold = Rune("Greater", "Seal", "Gold", "Primary", 410, None, gold=0.25)
g_quintessence_of_gold = Rune("Greater", "Quintessence", "Gold", "Primary", 515, None, gold=1)

# Health
l_mark_of_health = Rune("Lesser", "Mark", "Health", "Secondary", 30, None, health=1.93)
n_mark_of_health = Rune("Normal", "Mark", "Health", "Secondary", 165, None, health=2.7)
g_mark_of_health = Rune("Greater", "Mark", "Health", "Secondary", 410, None, health=3.47)
l_seal_of_health = Rune("Lesser", "Seal", "Health", "Primary", 65, None, health=2.97)
n_seal_of_health = Rune("Normal", "Seal", "Health", "Primary", 330, None, health=4.16)
g_seal_of_health = Rune("Greater", "Seal", "Health", "Primary", 820, None, health=5.35)
l_glyph_of_health = Rune("Lesser", "Glyph", "Health", "Secondary", 30, None, health=1.49)
n_glyph_of_health = Rune("Normal", "Glyph", "Health", "Secondary", 165, None, health=2.08)
g_glyph_of_health = Rune("Greater", "Glyph", "Health", "Secondary", 410, None, health=2.67)
l_quintessence_of_health = Rune("Lesser", "Quintessence", "Health", "Primary", 165, None, health=14.5)
n_quintessence_of_health = Rune("Normal", "Quintessence", "Health", "Primary", 820, None, health=20)
g_quintessence_of_health = Rune("Greater", "Quintessence", "Health", "Primary", 2050, None, health=26)

# Health Regeneration (Health Regen / 5 sec)
l_seal_of_health_regeneration = Rune("Lesser", "Seal", "Health Regeneration", "Primary", 65, None, health_regeneration=0.24)
n_seal_of_health_regeneration = Rune("Normal", "Seal", "Health Regeneration", "Primary", 330, None, health_regeneration=0.34)
g_seal_of_health_regeneration = Rune("Greater", "Seal", "Health Regeneration", "Primary", 820, None, health_regeneration=0.43)
l_glyph_of_health_regeneration = Rune("Lesser", "Glyph", "Health Regeneration", "Secondary", 65, None, health_regeneration=0.15)
n_glyph_of_health_regeneration = Rune("Normal", "Glyph", "Health Regeneration", "Secondary", 330, None, health_regeneration=0.21)
g_glyph_of_health_regeneration = Rune("Greater", "Glyph", "Health Regeneration", "Secondary", 820, None, health_regeneration=0.27)
l_quintessence_of_health_regeneration = Rune("Lesser", "Quintessence", "Health Regeneration", "Primary", 165, None, health_regeneration=1.5)
n_quintessence_of_health_regeneration = Rune("Normal", "Quintessence", "Health Regeneration", "Primary", 820, None, health_regeneration=2.1)
g_quintessence_of_health_regeneration = Rune("Greater", "Quintessence", "Health Regeneration", "Primary", 2050, None, health_regeneration=2.7)

# Hybrid Penetration (Armor Penetration / Magic Penetration)
l_mark_of_hybrid_penetration = Rune("Lesser", "Mark", "Hybrid Penetration", "Primary", 65, None, armor_penetration=0.5, magic_penetration=0.34)
n_mark_of_hybrid_penetration = Rune("Normal", "Mark", "Hybrid Penetration", "Primary", 330, None, armor_penetration=0.7, magic_penetration=0.48)
g_mark_of_hybrid_penetration = Rune("Greater", "Mark", "Hybrid Penetration", "Primary", 820, None, armor_penetration=0.9, magic_penetration=0.62)
l_quintessence_of_hybrid_penetration = Rune("Lesser", "Quintessence", "Hybrid Penetration", "Secondary", 165, None, armor_penetration=0.99, magic_penetration=0.78)
n_quintessence_of_hybrid_penetration = Rune("Normal", "Quintessence", "Hybrid Penetration", "Secondary", 820, None, armor_penetration=1.39, magic_penetration=1.09)
g_quintessence_of_hybrid_penetration = Rune("Greater", "Quintessence", "Hybrid Penetration", "Secondary", 2050, None, armor_penetration=1.79, magic_penetration=1.4)

# Life Steal
l_quintessence_of_life_steal = Rune("Lesser", "Quintessence", "Life Steal", "Primary", 165, None, life_steal=0.0112)
n_quintessence_of_life_steal = Rune("Normal", "Quintessence", "Life Steal", "Primary", 820, None, life_steal=0.0156)
g_quintessence_of_life_steal = Rune("Greater", "Quintessence", "Life Steal", "Primary", 2050, None, life_steal=0.02)

# Magic Penetration
l_mark_of_magic_penetration = Rune("Lesser", "Mark", "Magic Penetration", "Primary", 30, None, magic_penetration=0.49)
n_mark_of_magic_penetration = Rune("Normal", "Mark", "Magic Penetration", "Primary", 165, None, magic_penetration=0.68)
g_mark_of_magic_penetration = Rune("Greater", "Mark", "Magic Penetration", "Primary", 410, None, magic_penetration=0.87)
l_glyph_of_magic_penetration = Rune("Lesser", "Glyph", "Magic Penetration", "Secondary", 30, None, magic_penetration=0.35)
n_glyph_of_magic_penetration = Rune("Normal", "Glyph", "Magic Penetration", "Secondary", 165, None, magic_penetration=0.49)
g_glyph_of_magic_penetration = Rune("Greater", "Glyph", "Magic Penetration", "Secondary", 410, None, magic_penetration=0.63)
l_quintessence_of_magic_penetration = Rune("Lesser", "Quintessence", "Magic Penetration", "Secondary", 80, None, magic_penetration=1.11)
n_quintessence_of_magic_penetration = Rune("Normal", "Quintessence", "Magic Penetration", "Secondary", 410, None, magic_penetration=1.56)
g_quintessence_of_magic_penetration = Rune("Greater", "Quintessence", "Magic Penetration", "Secondary", 1025, None, magic_penetration=2.01)

# Magic Resist
l_mark_of_magic_resist = Rune("Lesser", "Mark", "Magic Resist", "Secondary", 15, None, magic_resist=0.43)
n_mark_of_magic_resist = Rune("Normal", "Mark", "Magic Resist", "Secondary", 80, None, magic_resist=0.6)
g_mark_of_magic_resist = Rune("Greater", "Mark", "Magic Resist", "Secondary", 205, None, magic_resist=0.77)
l_seal_of_magic_resist = Rune("Lesser", "Seal", "Magic Resist", "Secondary", 15, None, magic_resist=0.41)
n_seal_of_magic_resist = Rune("Normal", "Seal", "Magic Resist", "Secondary", 80, None, magic_resist=0.58)
g_seal_of_magic_resist = Rune("Greater", "Seal", "Magic Resist", "Secondary", 205, None, magic_resist=0.74)
l_glyph_of_magic_resist = Rune("Lesser", "Glyph", "Magic Resist", "Primary", 15, None, magic_resist=0.74)
n_glyph_of_magic_resist = Rune("Normal", "Glyph", "Magic Resist", "Primary", 80, None, magic_resist=1.04)
g_glyph_of_magic_resist = Rune("Greater", "Glyph", "Magic Resist", "Primary", 205, None, magic_resist=1.34)
l_quintessence_of_magic_resist = Rune("Lesser", "Quintessence", "Magic Resist", "Secondary", 80, None, magic_resist=2.22)
n_quintessence_of_magic_resist = Rune("Normal", "Quintessence", "Magic Resist", "Secondary", 410, None, magic_resist=3.11)
g_quintessence_of_magic_resist = Rune("Greater", "Quintessence", "Magic Resist", "Secondary", 1025, None, magic_resist=4)

# Mana
l_mark_of_mana = Rune("Lesser", "Mark", "Mana", "Secondary", 30, None, mana=3.28)
n_mark_of_mana = Rune("Normal", "Mark", "Mana", "Secondary", 165, None, mana=4.59)
g_mark_of_mana = Rune("Greater", "Mark", "Mana", "Secondary", 410, None, mana=5.91)
l_seal_of_mana = Rune("Lesser", "Seal", "Mana", "Secondary", 30, None, mana=3.83)
n_seal_of_mana = Rune("Normal", "Seal", "Mana", "Secondary", 165, None, mana=5.36)
g_seal_of_mana = Rune("Greater", "Seal", "Mana", "Secondary", 410, None, mana=6.89)
l_glyph_of_mana = Rune("Lesser", "Glyph", "Mana", "Primary", 30, None, mana=6.25)
n_glyph_of_mana = Rune("Normal", "Glyph", "Mana", "Primary", 165, None, mana=8.75)
g_glyph_of_mana = Rune("Greater", "Glyph", "Mana", "Primary", 410, None, mana=11.25)
l_quintessence_of_mana = Rune("Lesser", "Quintessence", "Mana", "Primary", 80, None, mana=20.83)
n_quintessence_of_mana = Rune("Normal", "Quintessence", "Mana", "Primary", 410, None, mana=29.17)
g_quintessence_of_mana = Rune("Greater", "Quintessence", "Mana", "Primary", 1025, None, mana=37.5)

# Mana Regeneration (Mana regen / 5 sec)
l_mark_of_mana_regeneration = Rune("Lesser", "Mark", "Mana Regeneration", "Secondary", 15, None, mana_regeneration=0.15)
n_mark_of_mana_regeneration = Rune("Normal", "Mark", "Mana Regeneration", "Secondary", 80, None, mana_regeneration=0.2)
g_mark_of_mana_regeneration = Rune("Greater", "Mark", "Mana Regeneration", "Secondary", 205, None, mana_regeneration=0.26)
l_seal_of_mana_regeneration = Rune("Lesser", "Seal", "Mana Regeneration", "Primary", 15, None, mana_regeneration=0.23)
n_seal_of_mana_regeneration = Rune("Normal", "Seal", "Mana Regeneration", "Primary", 80, None, mana_regeneration=0.32)
g_seal_of_mana_regeneration = Rune("Greater", "Seal", "Mana Regeneration", "Primary", 205, None, mana_regeneration=0.41)
l_glyph_of_mana_regeneration = Rune("Lesser", "Glyph", "Mana Regeneration", "Secondary", 30, None, mana_regeneration=0.17)
n_glyph_of_mana_regeneration = Rune("Normal", "Glyph", "Mana Regeneration", "Secondary", 165, None, mana_regeneration=0.24)
g_glyph_of_mana_regeneration = Rune("Greater", "Glyph", "Mana Regeneration", "Secondary", 410, None, mana_regeneration=0.31)
l_quintessence_of_mana_regeneration = Rune("Lesser", "Quintessence", "Mana Regeneration", "Primary", 80, None, mana_regeneration=0.69)
n_quintessence_of_mana_regeneration = Rune("Normal", "Quintessence", "Mana Regeneration", "Primary", 410, None, mana_regeneration=0.97)
g_quintessence_of_mana_regeneration = Rune("Greater", "Quintessence", "Mana Regeneration", "Primary", 1025, None, mana_regeneration=1.25)

# Movement Speed
l_quintessence_of_movement_speed = Rune("Lesser", "Quintessence", "Movement Speed", "Primary", 165, None, movement_speed=0.0083)
n_quintessence_of_movement_speed = Rune("Normal", "Quintessence", "Movement Speed", "Primary", 820, None, movement_speed=0.0117)
g_quintessence_of_movement_speed = Rune("Greater", "Quintessence", "Movement Speed", "Primary", 2050, None, movement_speed=0.015)

# Percent Health
l_mark_of_attack_damage = Rune("Lesser", "Mark", "Attack Damage", "Primary", 15, None, attack_damage=0.53)
n_mark_of_attack_damage = Rune("Normal", "Mark", "Attack Damage", "Primary", 80, None, attack_damage=0.74)
g_mark_of_attack_damage = Rune("Greater", "Mark", "Attack Damage", "Primary", 205, None, attack_damage=0.95)
l_seal_of_attack_damage = Rune("Lesser", "Seal", "Attack Damage", "Secondary", 15, None, attack_damage=0.24)
n_seal_of_attack_damage = Rune("Normal", "Seal", "Attack Damage", "Secondary", 80, None, attack_damage=0.33)
g_seal_of_attack_damage = Rune("Greater", "Seal", "Attack Damage", "Secondary", 205, None, attack_damage=0.43)
l_glyph_of_attack_damage = Rune("Lesser", "Glyph", "Attack Damage", "Secondary", 15, None, attack_damage=0.16)
n_glyph_of_attack_damage = Rune("Normal", "Glyph", "Attack Damage", "Secondary", 80, None, attack_damage=0.22)
g_glyph_of_attack_damage = Rune("Greater", "Glyph", "Attack Damage", "Secondary", 205, None, attack_damage=0.28)
l_quintessence_of_attack_damage = Rune("Lesser", "Quintessence", "Attack Damage", "Secondary", 80, None, attack_damage=1.25)
n_quintessence_of_attack_damage = Rune("Normal", "Quintessence", "Attack Damage", "Secondary", 410, None, attack_damage=1.75)
g_quintessence_of_attack_damage = Rune("Greater", "Quintessence", "Attack Damage", "Secondary", 1025, None, attack_damage=2.25)

# Revival (Reduction of time dead)
l_mark_of_attack_damage = Rune("Lesser", "Mark", "Attack Damage", "Primary", 15, None, attack_damage=0.53)
n_mark_of_attack_damage = Rune("Normal", "Mark", "Attack Damage", "Primary", 80, None, attack_damage=0.74)
g_mark_of_attack_damage = Rune("Greater", "Mark", "Attack Damage", "Primary", 205, None, attack_damage=0.95)
l_seal_of_attack_damage = Rune("Lesser", "Seal", "Attack Damage", "Secondary", 15, None, attack_damage=0.24)
n_seal_of_attack_damage = Rune("Normal", "Seal", "Attack Damage", "Secondary", 80, None, attack_damage=0.33)
g_seal_of_attack_damage = Rune("Greater", "Seal", "Attack Damage", "Secondary", 205, None, attack_damage=0.43)
l_glyph_of_attack_damage = Rune("Lesser", "Glyph", "Attack Damage", "Secondary", 15, None, attack_damage=0.16)
n_glyph_of_attack_damage = Rune("Normal", "Glyph", "Attack Damage", "Secondary", 80, None, attack_damage=0.22)
g_glyph_of_attack_damage = Rune("Greater", "Glyph", "Attack Damage", "Secondary", 205, None, attack_damage=0.28)
l_quintessence_of_attack_damage = Rune("Lesser", "Quintessence", "Attack Damage", "Secondary", 80, None, attack_damage=1.25)
n_quintessence_of_attack_damage = Rune("Normal", "Quintessence", "Attack Damage", "Secondary", 410, None, attack_damage=1.75)
g_quintessence_of_attack_damage = Rune("Greater", "Quintessence", "Attack Damage", "Secondary", 1025, None, attack_damage=2.25)

# Scaling Ability Power (Ability Power per level)
l_mark_of_attack_damage = Rune("Lesser", "Mark", "Attack Damage", "Primary", 15, None, attack_damage=0.53)
n_mark_of_attack_damage = Rune("Normal", "Mark", "Attack Damage", "Primary", 80, None, attack_damage=0.74)
g_mark_of_attack_damage = Rune("Greater", "Mark", "Attack Damage", "Primary", 205, None, attack_damage=0.95)
l_seal_of_attack_damage = Rune("Lesser", "Seal", "Attack Damage", "Secondary", 15, None, attack_damage=0.24)
n_seal_of_attack_damage = Rune("Normal", "Seal", "Attack Damage", "Secondary", 80, None, attack_damage=0.33)
g_seal_of_attack_damage = Rune("Greater", "Seal", "Attack Damage", "Secondary", 205, None, attack_damage=0.43)
l_glyph_of_attack_damage = Rune("Lesser", "Glyph", "Attack Damage", "Secondary", 15, None, attack_damage=0.16)
n_glyph_of_attack_damage = Rune("Normal", "Glyph", "Attack Damage", "Secondary", 80, None, attack_damage=0.22)
g_glyph_of_attack_damage = Rune("Greater", "Glyph", "Attack Damage", "Secondary", 205, None, attack_damage=0.28)
l_quintessence_of_attack_damage = Rune("Lesser", "Quintessence", "Attack Damage", "Secondary", 80, None, attack_damage=1.25)
n_quintessence_of_attack_damage = Rune("Normal", "Quintessence", "Attack Damage", "Secondary", 410, None, attack_damage=1.75)
g_quintessence_of_attack_damage = Rune("Greater", "Quintessence", "Attack Damage", "Secondary", 1025, None, attack_damage=2.25)

# Scaling Armor (Armor per level)
l_mark_of_attack_damage = Rune("Lesser", "Mark", "Attack Damage", "Primary", 15, None, attack_damage=0.53)
n_mark_of_attack_damage = Rune("Normal", "Mark", "Attack Damage", "Primary", 80, None, attack_damage=0.74)
g_mark_of_attack_damage = Rune("Greater", "Mark", "Attack Damage", "Primary", 205, None, attack_damage=0.95)
l_seal_of_attack_damage = Rune("Lesser", "Seal", "Attack Damage", "Secondary", 15, None, attack_damage=0.24)
n_seal_of_attack_damage = Rune("Normal", "Seal", "Attack Damage", "Secondary", 80, None, attack_damage=0.33)
g_seal_of_attack_damage = Rune("Greater", "Seal", "Attack Damage", "Secondary", 205, None, attack_damage=0.43)
l_glyph_of_attack_damage = Rune("Lesser", "Glyph", "Attack Damage", "Secondary", 15, None, attack_damage=0.16)
n_glyph_of_attack_damage = Rune("Normal", "Glyph", "Attack Damage", "Secondary", 80, None, attack_damage=0.22)
g_glyph_of_attack_damage = Rune("Greater", "Glyph", "Attack Damage", "Secondary", 205, None, attack_damage=0.28)
l_quintessence_of_attack_damage = Rune("Lesser", "Quintessence", "Attack Damage", "Secondary", 80, None, attack_damage=1.25)
n_quintessence_of_attack_damage = Rune("Normal", "Quintessence", "Attack Damage", "Secondary", 410, None, attack_damage=1.75)
g_quintessence_of_attack_damage = Rune("Greater", "Quintessence", "Attack Damage", "Secondary", 1025, None, attack_damage=2.25)

# Scaling Attack Damage (Attack Damage per level)
l_mark_of_attack_damage = Rune("Lesser", "Mark", "Attack Damage", "Primary", 15, None, attack_damage=0.53)
n_mark_of_attack_damage = Rune("Normal", "Mark", "Attack Damage", "Primary", 80, None, attack_damage=0.74)
g_mark_of_attack_damage = Rune("Greater", "Mark", "Attack Damage", "Primary", 205, None, attack_damage=0.95)
l_seal_of_attack_damage = Rune("Lesser", "Seal", "Attack Damage", "Secondary", 15, None, attack_damage=0.24)
n_seal_of_attack_damage = Rune("Normal", "Seal", "Attack Damage", "Secondary", 80, None, attack_damage=0.33)
g_seal_of_attack_damage = Rune("Greater", "Seal", "Attack Damage", "Secondary", 205, None, attack_damage=0.43)
l_glyph_of_attack_damage = Rune("Lesser", "Glyph", "Attack Damage", "Secondary", 15, None, attack_damage=0.16)
n_glyph_of_attack_damage = Rune("Normal", "Glyph", "Attack Damage", "Secondary", 80, None, attack_damage=0.22)
g_glyph_of_attack_damage = Rune("Greater", "Glyph", "Attack Damage", "Secondary", 205, None, attack_damage=0.28)
l_quintessence_of_attack_damage = Rune("Lesser", "Quintessence", "Attack Damage", "Secondary", 80, None, attack_damage=1.25)
n_quintessence_of_attack_damage = Rune("Normal", "Quintessence", "Attack Damage", "Secondary", 410, None, attack_damage=1.75)
g_quintessence_of_attack_damage = Rune("Greater", "Quintessence", "Attack Damage", "Secondary", 1025, None, attack_damage=2.25)

# Scaling Cooldown Reduction (Cooldown Reduction per level)
l_mark_of_attack_damage = Rune("Lesser", "Mark", "Attack Damage", "Primary", 15, None, attack_damage=0.53)
n_mark_of_attack_damage = Rune("Normal", "Mark", "Attack Damage", "Primary", 80, None, attack_damage=0.74)
g_mark_of_attack_damage = Rune("Greater", "Mark", "Attack Damage", "Primary", 205, None, attack_damage=0.95)
l_seal_of_attack_damage = Rune("Lesser", "Seal", "Attack Damage", "Secondary", 15, None, attack_damage=0.24)
n_seal_of_attack_damage = Rune("Normal", "Seal", "Attack Damage", "Secondary", 80, None, attack_damage=0.33)
g_seal_of_attack_damage = Rune("Greater", "Seal", "Attack Damage", "Secondary", 205, None, attack_damage=0.43)
l_glyph_of_attack_damage = Rune("Lesser", "Glyph", "Attack Damage", "Secondary", 15, None, attack_damage=0.16)
n_glyph_of_attack_damage = Rune("Normal", "Glyph", "Attack Damage", "Secondary", 80, None, attack_damage=0.22)
g_glyph_of_attack_damage = Rune("Greater", "Glyph", "Attack Damage", "Secondary", 205, None, attack_damage=0.28)
l_quintessence_of_attack_damage = Rune("Lesser", "Quintessence", "Attack Damage", "Secondary", 80, None, attack_damage=1.25)
n_quintessence_of_attack_damage = Rune("Normal", "Quintessence", "Attack Damage", "Secondary", 410, None, attack_damage=1.75)
g_quintessence_of_attack_damage = Rune("Greater", "Quintessence", "Attack Damage", "Secondary", 1025, None, attack_damage=2.25)

# Scaling Energy (Energy per level)
l_mark_of_attack_damage = Rune("Lesser", "Mark", "Attack Damage", "Primary", 15, None, attack_damage=0.53)
n_mark_of_attack_damage = Rune("Normal", "Mark", "Attack Damage", "Primary", 80, None, attack_damage=0.74)
g_mark_of_attack_damage = Rune("Greater", "Mark", "Attack Damage", "Primary", 205, None, attack_damage=0.95)
l_seal_of_attack_damage = Rune("Lesser", "Seal", "Attack Damage", "Secondary", 15, None, attack_damage=0.24)
n_seal_of_attack_damage = Rune("Normal", "Seal", "Attack Damage", "Secondary", 80, None, attack_damage=0.33)
g_seal_of_attack_damage = Rune("Greater", "Seal", "Attack Damage", "Secondary", 205, None, attack_damage=0.43)
l_glyph_of_attack_damage = Rune("Lesser", "Glyph", "Attack Damage", "Secondary", 15, None, attack_damage=0.16)
n_glyph_of_attack_damage = Rune("Normal", "Glyph", "Attack Damage", "Secondary", 80, None, attack_damage=0.22)
g_glyph_of_attack_damage = Rune("Greater", "Glyph", "Attack Damage", "Secondary", 205, None, attack_damage=0.28)
l_quintessence_of_attack_damage = Rune("Lesser", "Quintessence", "Attack Damage", "Secondary", 80, None, attack_damage=1.25)
n_quintessence_of_attack_damage = Rune("Normal", "Quintessence", "Attack Damage", "Secondary", 410, None, attack_damage=1.75)
g_quintessence_of_attack_damage = Rune("Greater", "Quintessence", "Attack Damage", "Secondary", 1025, None, attack_damage=2.25)

# Scaling Energy Regeneration (Energy Regen / 5 sec per level)
l_mark_of_attack_damage = Rune("Lesser", "Mark", "Attack Damage", "Primary", 15, None, attack_damage=0.53)
n_mark_of_attack_damage = Rune("Normal", "Mark", "Attack Damage", "Primary", 80, None, attack_damage=0.74)
g_mark_of_attack_damage = Rune("Greater", "Mark", "Attack Damage", "Primary", 205, None, attack_damage=0.95)
l_seal_of_attack_damage = Rune("Lesser", "Seal", "Attack Damage", "Secondary", 15, None, attack_damage=0.24)
n_seal_of_attack_damage = Rune("Normal", "Seal", "Attack Damage", "Secondary", 80, None, attack_damage=0.33)
g_seal_of_attack_damage = Rune("Greater", "Seal", "Attack Damage", "Secondary", 205, None, attack_damage=0.43)
l_glyph_of_attack_damage = Rune("Lesser", "Glyph", "Attack Damage", "Secondary", 15, None, attack_damage=0.16)
n_glyph_of_attack_damage = Rune("Normal", "Glyph", "Attack Damage", "Secondary", 80, None, attack_damage=0.22)
g_glyph_of_attack_damage = Rune("Greater", "Glyph", "Attack Damage", "Secondary", 205, None, attack_damage=0.28)
l_quintessence_of_attack_damage = Rune("Lesser", "Quintessence", "Attack Damage", "Secondary", 80, None, attack_damage=1.25)
n_quintessence_of_attack_damage = Rune("Normal", "Quintessence", "Attack Damage", "Secondary", 410, None, attack_damage=1.75)
g_quintessence_of_attack_damage = Rune("Greater", "Quintessence", "Attack Damage", "Secondary", 1025, None, attack_damage=2.25)

# Scaling Health (Health per level)
l_mark_of_attack_damage = Rune("Lesser", "Mark", "Attack Damage", "Primary", 15, None, attack_damage=0.53)
n_mark_of_attack_damage = Rune("Normal", "Mark", "Attack Damage", "Primary", 80, None, attack_damage=0.74)
g_mark_of_attack_damage = Rune("Greater", "Mark", "Attack Damage", "Primary", 205, None, attack_damage=0.95)
l_seal_of_attack_damage = Rune("Lesser", "Seal", "Attack Damage", "Secondary", 15, None, attack_damage=0.24)
n_seal_of_attack_damage = Rune("Normal", "Seal", "Attack Damage", "Secondary", 80, None, attack_damage=0.33)
g_seal_of_attack_damage = Rune("Greater", "Seal", "Attack Damage", "Secondary", 205, None, attack_damage=0.43)
l_glyph_of_attack_damage = Rune("Lesser", "Glyph", "Attack Damage", "Secondary", 15, None, attack_damage=0.16)
n_glyph_of_attack_damage = Rune("Normal", "Glyph", "Attack Damage", "Secondary", 80, None, attack_damage=0.22)
g_glyph_of_attack_damage = Rune("Greater", "Glyph", "Attack Damage", "Secondary", 205, None, attack_damage=0.28)
l_quintessence_of_attack_damage = Rune("Lesser", "Quintessence", "Attack Damage", "Secondary", 80, None, attack_damage=1.25)
n_quintessence_of_attack_damage = Rune("Normal", "Quintessence", "Attack Damage", "Secondary", 410, None, attack_damage=1.75)
g_quintessence_of_attack_damage = Rune("Greater", "Quintessence", "Attack Damage", "Secondary", 1025, None, attack_damage=2.25)

# Scaling Health Regeneration (Health Regen / 5 sec per level)
l_mark_of_attack_damage = Rune("Lesser", "Mark", "Attack Damage", "Primary", 15, None, attack_damage=0.53)
n_mark_of_attack_damage = Rune("Normal", "Mark", "Attack Damage", "Primary", 80, None, attack_damage=0.74)
g_mark_of_attack_damage = Rune("Greater", "Mark", "Attack Damage", "Primary", 205, None, attack_damage=0.95)
l_seal_of_attack_damage = Rune("Lesser", "Seal", "Attack Damage", "Secondary", 15, None, attack_damage=0.24)
n_seal_of_attack_damage = Rune("Normal", "Seal", "Attack Damage", "Secondary", 80, None, attack_damage=0.33)
g_seal_of_attack_damage = Rune("Greater", "Seal", "Attack Damage", "Secondary", 205, None, attack_damage=0.43)
l_glyph_of_attack_damage = Rune("Lesser", "Glyph", "Attack Damage", "Secondary", 15, None, attack_damage=0.16)
n_glyph_of_attack_damage = Rune("Normal", "Glyph", "Attack Damage", "Secondary", 80, None, attack_damage=0.22)
g_glyph_of_attack_damage = Rune("Greater", "Glyph", "Attack Damage", "Secondary", 205, None, attack_damage=0.28)
l_quintessence_of_attack_damage = Rune("Lesser", "Quintessence", "Attack Damage", "Secondary", 80, None, attack_damage=1.25)
n_quintessence_of_attack_damage = Rune("Normal", "Quintessence", "Attack Damage", "Secondary", 410, None, attack_damage=1.75)
g_quintessence_of_attack_damage = Rune("Greater", "Quintessence", "Attack Damage", "Secondary", 1025, None, attack_damage=2.25)

# Scaling Magic Resist (Magic Resist per level)
l_mark_of_attack_damage = Rune("Lesser", "Mark", "Attack Damage", "Primary", 15, None, attack_damage=0.53)
n_mark_of_attack_damage = Rune("Normal", "Mark", "Attack Damage", "Primary", 80, None, attack_damage=0.74)
g_mark_of_attack_damage = Rune("Greater", "Mark", "Attack Damage", "Primary", 205, None, attack_damage=0.95)
l_seal_of_attack_damage = Rune("Lesser", "Seal", "Attack Damage", "Secondary", 15, None, attack_damage=0.24)
n_seal_of_attack_damage = Rune("Normal", "Seal", "Attack Damage", "Secondary", 80, None, attack_damage=0.33)
g_seal_of_attack_damage = Rune("Greater", "Seal", "Attack Damage", "Secondary", 205, None, attack_damage=0.43)
l_glyph_of_attack_damage = Rune("Lesser", "Glyph", "Attack Damage", "Secondary", 15, None, attack_damage=0.16)
n_glyph_of_attack_damage = Rune("Normal", "Glyph", "Attack Damage", "Secondary", 80, None, attack_damage=0.22)
g_glyph_of_attack_damage = Rune("Greater", "Glyph", "Attack Damage", "Secondary", 205, None, attack_damage=0.28)
l_quintessence_of_attack_damage = Rune("Lesser", "Quintessence", "Attack Damage", "Secondary", 80, None, attack_damage=1.25)
n_quintessence_of_attack_damage = Rune("Normal", "Quintessence", "Attack Damage", "Secondary", 410, None, attack_damage=1.75)
g_quintessence_of_attack_damage = Rune("Greater", "Quintessence", "Attack Damage", "Secondary", 1025, None, attack_damage=2.25)

# Scaling Mana (Mana per level)
l_mark_of_attack_damage = Rune("Lesser", "Mark", "Attack Damage", "Primary", 15, None, attack_damage=0.53)
n_mark_of_attack_damage = Rune("Normal", "Mark", "Attack Damage", "Primary", 80, None, attack_damage=0.74)
g_mark_of_attack_damage = Rune("Greater", "Mark", "Attack Damage", "Primary", 205, None, attack_damage=0.95)
l_seal_of_attack_damage = Rune("Lesser", "Seal", "Attack Damage", "Secondary", 15, None, attack_damage=0.24)
n_seal_of_attack_damage = Rune("Normal", "Seal", "Attack Damage", "Secondary", 80, None, attack_damage=0.33)
g_seal_of_attack_damage = Rune("Greater", "Seal", "Attack Damage", "Secondary", 205, None, attack_damage=0.43)
l_glyph_of_attack_damage = Rune("Lesser", "Glyph", "Attack Damage", "Secondary", 15, None, attack_damage=0.16)
n_glyph_of_attack_damage = Rune("Normal", "Glyph", "Attack Damage", "Secondary", 80, None, attack_damage=0.22)
g_glyph_of_attack_damage = Rune("Greater", "Glyph", "Attack Damage", "Secondary", 205, None, attack_damage=0.28)
l_quintessence_of_attack_damage = Rune("Lesser", "Quintessence", "Attack Damage", "Secondary", 80, None, attack_damage=1.25)
n_quintessence_of_attack_damage = Rune("Normal", "Quintessence", "Attack Damage", "Secondary", 410, None, attack_damage=1.75)
g_quintessence_of_attack_damage = Rune("Greater", "Quintessence", "Attack Damage", "Secondary", 1025, None, attack_damage=2.25)

# Scaling Mana Regeneration (Mana regen / 5 sec per level)
l_mark_of_attack_damage = Rune("Lesser", "Mark", "Attack Damage", "Primary", 15, None, attack_damage=0.53)
n_mark_of_attack_damage = Rune("Normal", "Mark", "Attack Damage", "Primary", 80, None, attack_damage=0.74)
g_mark_of_attack_damage = Rune("Greater", "Mark", "Attack Damage", "Primary", 205, None, attack_damage=0.95)
l_seal_of_attack_damage = Rune("Lesser", "Seal", "Attack Damage", "Secondary", 15, None, attack_damage=0.24)
n_seal_of_attack_damage = Rune("Normal", "Seal", "Attack Damage", "Secondary", 80, None, attack_damage=0.33)
g_seal_of_attack_damage = Rune("Greater", "Seal", "Attack Damage", "Secondary", 205, None, attack_damage=0.43)
l_glyph_of_attack_damage = Rune("Lesser", "Glyph", "Attack Damage", "Secondary", 15, None, attack_damage=0.16)
n_glyph_of_attack_damage = Rune("Normal", "Glyph", "Attack Damage", "Secondary", 80, None, attack_damage=0.22)
g_glyph_of_attack_damage = Rune("Greater", "Glyph", "Attack Damage", "Secondary", 205, None, attack_damage=0.28)
l_quintessence_of_attack_damage = Rune("Lesser", "Quintessence", "Attack Damage", "Secondary", 80, None, attack_damage=1.25)
n_quintessence_of_attack_damage = Rune("Normal", "Quintessence", "Attack Damage", "Secondary", 410, None, attack_damage=1.75)
g_quintessence_of_attack_damage = Rune("Greater", "Quintessence", "Attack Damage", "Secondary", 1025, None, attack_damage=2.25)

# Spell Vamp
l_mark_of_attack_damage = Rune("Lesser", "Mark", "Attack Damage", "Primary", 15, None, attack_damage=0.53)
n_mark_of_attack_damage = Rune("Normal", "Mark", "Attack Damage", "Primary", 80, None, attack_damage=0.74)
g_mark_of_attack_damage = Rune("Greater", "Mark", "Attack Damage", "Primary", 205, None, attack_damage=0.95)
l_seal_of_attack_damage = Rune("Lesser", "Seal", "Attack Damage", "Secondary", 15, None, attack_damage=0.24)
n_seal_of_attack_damage = Rune("Normal", "Seal", "Attack Damage", "Secondary", 80, None, attack_damage=0.33)
g_seal_of_attack_damage = Rune("Greater", "Seal", "Attack Damage", "Secondary", 205, None, attack_damage=0.43)
l_glyph_of_attack_damage = Rune("Lesser", "Glyph", "Attack Damage", "Secondary", 15, None, attack_damage=0.16)
n_glyph_of_attack_damage = Rune("Normal", "Glyph", "Attack Damage", "Secondary", 80, None, attack_damage=0.22)
g_glyph_of_attack_damage = Rune("Greater", "Glyph", "Attack Damage", "Secondary", 205, None, attack_damage=0.28)
l_quintessence_of_attack_damage = Rune("Lesser", "Quintessence", "Attack Damage", "Secondary", 80, None, attack_damage=1.25)
n_quintessence_of_attack_damage = Rune("Normal", "Quintessence", "Attack Damage", "Secondary", 410, None, attack_damage=1.75)
g_quintessence_of_attack_damage = Rune("Greater", "Quintessence", "Attack Damage", "Secondary", 1025, None, attack_damage=2.25)