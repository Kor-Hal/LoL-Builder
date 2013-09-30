# -*-coding:utf-8 -*
class MasteryTree(object):
  """Defines a Mastery tree.
  
  Ref : http://leagueoflegends.wikia.com/wiki/Mastery
  
  """
    
  def __init__(self, name, masteries, page):
    """Create a new mastery tree.
    
    Named parameters :
    name -- Mastery tree's name
    masteries -- Dict of this tree's masteries
    page -- Mastery tree's page
        
    """
    
    self._name = name
    self._masteries = masteries
    for key in self._masteries.keys():
      self._masteries[key].tree = self
    self._page = page
    self.points_spent = 0
    
  @property
  def name(self):
    """Mastery tree's name."""
    return self._name
  
  @property
  def masteries(self):
    """Dict of this tree's masteries."""
    return self._masteries
  
  @property
  def page(self):
    """Mastery tree's page."""
    return self._page

class MasteryPage(object):
  """Defines a Mastery page, with the 3 trees.
  
  Ref : http://leagueoflegends.wikia.com/wiki/Mastery
  
  """
    
  def __init__(self, name, offense_masteries, defense_masteries,
                     utility_masteries):
    """Create a new empty Mastery page.
    
    Named parameters :
    name -- Mastery page's name
    offense_masteries -- Offense Mastery tree
    defense_masteries -- Defense Mastery tree
    utility_masteries -- Utility Mastery tree
    
    """
    
    self._name = name
    self._offense_tree = MasteryTree("Offense", offense_masteries, self)
    self._defense_tree = MasteryTree("Defense", defense_masteries, self)
    self._utility_tree = MasteryTree("Utility", utility_masteries, self)
    self._statistics = dict(attack_speed=0, cooldown_reduction=0,
                       scaling_attack_damage=0, scaling_ability_power=0,
                       percent_armor_penetration=0,
                       percent_magic_penetration=0, critical_strike_damage=0,
                       attack_damage=0, ability_power=0,
                       flat_armor_penetration=0, percent_ability_power=0,
                       scaling_health=0, armor=0, magic_resistance=0, health=0,
                       percent_health=0, mana_regeneration=0, scaling_mana=0,
                       spell_vamp=0, life_steal=0, movement_speed=0)
    
  @property
  def name(self):
    """Mastery page's name."""
    return self._name
  
  @property
  def offense_tree(self):
    """Mastery page's offense tree."""
    return self._offense_tree
  
  @property
  def defense_tree(self):
    """Mastery page's defense tree."""
    return self._defense_tree
    
  @property
  def utility_tree(self):
    """Mastery page's utility tree."""
    return self._utility_tree
  
  @property
  def statistics(self):
    """Dict of Mastery page's bonus statistics."""
    return self._statistics
  
  @property
  def ability_power(self):
    """Bonus Ability Power of the Mastery page."""
    return self.statistics['ability_power']
  
  @property
  def armor(self):
    """Bonus Armor of the Mastery page."""
    return self.statistics['armor']
  
  @property
  def attack_damage(self):
    """Bonus Attack Damage of the Mastery page."""
    return self.statistics['attack_damage']
  
  @property
  def attack_speed(self):
    """Bonus Attack Speed of the Mastery page."""
    return self.statistics['attack_speed']
  
  @property
  def cooldown_reduction(self):
    """Bonus Cooldown Reduction of the Mastery page."""
    return self.statistics['cooldown_reduction']
  
  @property
  def critical_strike_damage(self):
    """Bonus Critial Strike Damage of the Mastery page."""
    return self.statistics['critical_strike_damage']
  
  @property
  def flat_armor_penetration(self):
    """Bonus Flat Armor Penetration of the Mastery page."""
    return self.statistics['flat_armor_penetration']
  
  @property
  def health(self):
    """Bonus Health of the Mastery page."""
    return self.statistics['health']
  
  @property
  def life_steal(self):
    """Bonus Life Steal of the Mastery page."""
    return self.statistics['life_steal']
  
  @property
  def magic_resistance(self):
    """Bonus Magic Resistance of the Mastery page."""
    return self.statistics['magic_resistance']
  
  @property
  def mana_regeneration(self):
    """Bonus Mana Regeneration of the Mastery page."""
    return self.statistics['mana_regeneration']
  
  @property
  def movement_speed(self):
    """Bonus Movement Speed of the Mastery page."""
    return self.statistics['movement_speed']
  
  @property
  def percent_ability_power(self):
    """Bonus Percentage Ability Power of the Mastery page."""
    return self.statistics['percent_ability_power']
  
  @property
  def percent_armor_penetration(self):
    """Bonus Percentage Armor Penetration of the Mastery page."""
    return self.statistics['percent_armor_penetration']
  
  @property
  def percent_health(self):
    """Bonus Percentage Health of the Mastery page."""
    return self.statistics['percent_health']
  
  @property
  def percent_magic_penetration(self):
    """Bonus Percentage Magic Penetration of the Mastery page."""
    return self.statistics['percent_magic_penetration']
  
  @property
  def scaling_ability_power(self):
    """Bonus Scaling Ability Power of the Mastery page."""
    return self.statistics['scaling_ability_power']
  
  @property
  def scaling_attack_damage(self):
    """Bonus Scaling Attack Damage of the Mastery page."""
    return self.statistics['scaling_attack_damage']
  
  @property
  def scaling_health(self):
    """Bonus Scaling Health of the Mastery page."""
    return self.statistics['scaling_health']
  
  @property
  def scaling_mana(self):
    """Bonus Scaling Mana of the Mastery page."""
    return self.statistics['scaling_mana']
  
  @property
  def spell_vamp(self):
    """Bonus Spell Vamp of the Mastery page."""
    return self.statistics['spell_vamp']
  
  def update_statistics(self):
    for statistic in self.statistics.keys():
      self.statistics[statistic] = 0
    
    self.statistics['ability_power'] = \
                  self.offense_tree.masteries[(4,3)].current_value()
    self.statistics['armor'] = \
                  self.defense_tree.masteries[(2,1)].current_value()
    self.statistics['attack_damage'] = \
                  self.offense_tree.masteries[(4,2)].current_value()
    self.statistics['attack_speed'] = \
                  self.offense_tree.masteries[(1,2)].current_value() / 100
    self.statistics['cooldown_reduction'] = \
                  self.offense_tree.masteries[(1,3)].current_value() / 100 + \
                  self.utility_tree.masteries[(5,2)].current_value()
    self.statistics['critical_strike_damage'] = \
                  self.offense_tree.masteries[(4,1)].current_value() / 100
    self.statistics['flat_armor_penetration'] = \
                  self.offense_tree.masteries[(5,2)].current_value()
    self.statistics['health'] = \
                  self.defense_tree.masteries[(3,3)].current_value()
    self.statistics['life_steal'] = \
                  self.utility_tree.masteries[(3,3)].current_value() / 100
    self.statistics['magic_resistance'] = \
                  self.defense_tree.masteries[(2,2)].current_value()
    self.statistics['mana_regeneration'] = \
                  self.utility_tree.masteries[(1,3)].current_value()
    self.statistics['movement_speed'] = \
                  self.utility_tree.masteries[(6,2)].current_value() / 100
    self.statistics['percent_ability_power'] = \
                  self.offense_tree.masteries[(5,3)].current_value() / 100
    self.statistics['percent_armor_penetration'] = \
                  self.offense_tree.masteries[(3,2)].current_value() / 100
    self.statistics['percent_health'] = \
                  self.defense_tree.masteries[(4,3)].current_value() / 100
    self.statistics['percent_magic_penetration'] = \
                  self.offense_tree.masteries[(3,3)].current_value() / 100
    self.statistics['scaling_ability_power'] = \
                  self.offense_tree.masteries[(2,3)].current_value()
    self.statistics['scaling_attack_damage'] = \
                  self.offense_tree.masteries[(2,2)].current_value()
    self.statistics['scaling_health'] = \
                  self.defense_tree.masteries[(1,3)].current_value()
    self.statistics['scaling_mana'] = \
                  self.utility_tree.masteries[(2,3)].current_value()
    self.statistics['spell_vamp'] = \
                  self.utility_tree.masteries[(3,3)].current_value() / 100
