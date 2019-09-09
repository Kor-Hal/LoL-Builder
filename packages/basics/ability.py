# -*-coding:utf-8 -*
class Ability(object):
  """ Defines a skill with its name and description.
  
  Ref : http://leagueoflegends.wikia.com/wiki/Champion_ability
  
  """
  
  def __init__(self,
               name,
               description,
               archetype,
               kind,
               cooldown=None,
               cost=None,
               reach=None):
    """Initializing the ability's attributes.
    
    Named parameters :
    name -- Name of the ability (list to handle toggles)
    description -- Description of the ability, as seen in game
                   (list to handle toggles)
    archetype -- Basic, Innate or Ultimate
    kind -- Active, Passive, Toggle or Stance
    cooldown -- Ability's cooldown (default: None)
                (tuple's list to handle toggles)
    cost -- Ability's cost (default: None)
            (tuple's list to handle toggles)
    reach -- Ability's range (default: None) (tuple's list to handle toggles)
    
    """
    
    self.name = name
    self.description = description
    self.archetype = archetype
    self.kind = kind
    self.cooldown = cooldown
    self.cost = cost
    self.reach = reach
