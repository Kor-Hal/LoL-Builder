# -*-coding:Latin-1 -*
class Item:
  """ Defines an item, with its basic characteristics, and the stats it gives.
  
  Ref : http://leagueoflegends.wikia.com/wiki/Item
  """
  
  def __init__(self, availability, tier, cost, menu, recipe, actives, passives, 
               bonusArPen, bonusAD, bonusAS, bonusCSC, bonusCSD, bonusLS, bonusMS, 
               bonusAR, bonusHP, bonusHP5, bonusMR, 
               bonusAP, bonusCDR, bonusMPen, bonusMP, bonusMP5, bonusSV):
    """ Initializing the item's stats.
    
    Named parameters :
    availability -- Map on which the item may be bought
    tier -- Item's tier (Consumable, Basic, Advanced, Legendary, Mythical)
    cost -- Item's cost
    menu -- Menu(s) to access the item in shop
    recipe -- Item's recipe (List of items)
    actives -- Tuple of actives (descriptions)
    passives -- Tuple of passives (descriptions)
    bonusArPen -- Bonus Armor Penetration
    bonusAD -- Bonus Attack Damage
    bonusAS -- Bonus Attack Speed
    bonusCSC -- Bonus Critical Strike Chance
    bonusCSD -- Bonus Critical Strike Damage
    bonusLS -- Bonus Life Steal
    bonus MS -- Bonus Movement Speed
    bonusAR -- Bonus Armor
    bonusHP -- Bonus Health
    bonusHP5 -- Bonus Health Regeneration
    bonusMR -- Bonus Magic Resistance
    bonusAP -- Bonus Ability Power
    bonusCDR -- Bonus Cooldown Reduction
    bonusMPen -- Bonus Magic Penetration
    bonus MP -- Bonus Mana
    bonusMP5 -- Bonus Mana Regeneration
    bonusSV -- Bonus Spell Vamp
        
    """
    
    self.availability = availability
    self.tier = tier
    self.cost = cost
    self.menu = menu
    self.recipe = recipe
    self.actives = actives
    self.passives = passives
    self.bonusArPen = bonusArPen
    self.bonusAD = bonusAD
    self.bonusAS = bonusAS
    self.bonusCSC = bonusCSC
    self.bonusCSD = bonusCSD
    self.bonusLS = bonusLS
    self.bonusMS = bonusMS
    self.bonusAR = bonusAR
    self.bonusHP = bonusHP
    self.bonusHP5 = bonusHP5
    self.bonusMR = bonusMR
    self.bonusAP = bonusAP
    self.bonusCDR = bonusCDR
    self.bonusMPen = bonusMPen
    self.bonusMP = bonusMP
    self.bonusMP5 = bonusMP5
    self.bonusSV = bonusSV
