# -*-coding:Latin-1 -*
class Mastery:
  """ Defines a Mastery.
  
  Ref : http://leagueoflegends.wikia.com/wiki/Mastery
  
  """
  
  def __init__(self, tree, name, description, ranks, level, maxPoints, pointsPrerequisite, masteryPrerequisite=None):
    """ Create a new Mastery.
    
    Named parameters :
    tree -- Mastery's tree (Offense, Defense or Utility)
    name -- Mastery's name
    description -- Mastery's description
    ranks -- Values of the different mastery's ranks
    level -- Current number of points spent in the mastery
    maxPoints -- Max points allowed in this mastery
    pointsPrerequisite -- Number of points needed in the mastery's tree to be able to spend points in this one
    masteryPrerequisite -- Mastery required to fill before being able to spend points in this one
    
    """
    
    self._tree = tree
    self._name = name
    self._description = description
    self._ranks = ranks
    self._level = level
    self._maxPoints = maxPoints
    self._pointsPrerequisite = pointsPrerequisite
    self._masteryPrerequisite = masteryPrerequisite
  
  # Read-only properties
  
  @property
  def tree(self):
    """Mastery's tree (Offense, Defense or Utility)."""
    return self._tree
  
  @property
  def name(self):
    """Mastery's name."""
    return self._name
  
  @property
  def description(self):
    """Mastery's description."""
    return self._description
  
  @property
  def ranks(self):
    """Values of the different mastery's ranks."""
    return self._ranks
  
  @property
  def maxPoints(self):
    """Max points allowed in this mastery."""
    return self._maxPoints
  
  @property
  def pointsPrerequisite(self):
    """Number of points needed in the mastery's tree to be able to spend points in this one."""
    return self._pointsPrerequisite
  
  @property
  def masteryPrerequisite(self):
    """Mastery required to fill before being able to spend points in this one."""
    return self._masteryPrerequisite
  
  # Defining how to access the self._level property
  
  @property
  def level(self):
    """Current number of points spent in the mastery."""
    return self._level
  
  @level.setter
  def level(self, value, pointsInTree):
    if pointsInTree >= self._pointsPrerequisite and self._masteryPrerequisite.level == self._masteryPrerequisite.maxPoints:
      self._level = value
  
  def curr_value(self):
    return self.ranks[self.level]

class MasteryPage:
  """ Defines a Mastery page, with the 3 trees.
  
  Ref : http://leagueoflegends.wikia.com/wiki/Mastery
  
  """
    
  def __init__(self, name):
    """ Create a new empty Mastery page.
    
    Named parameters :
    name -- Mastery page's name
    
    """
    
    self.name = name
    
    # Offense tree
    self.offenseTree = {}
    
    # Tier 1
    summonersWrath = Mastery("Offense", ("Summoner's Wrath", "Exhaust: Lowers the target's armor and magic resistance by "
    "10.\nIgnite: Grants 5 attack damage and 5 ability power while on cooldown.\nGhost: Bonus movement speed increased to "
    "35% movement speed.\nGarrison: Allied towers gain 50% splash damage."), None, 0, 1, 0)
    fury = Mastery("Offense", "Fury", "Grants {}% attack speed.", (1,2,3,4), 0, 4, 0)
    sorcery = Mastery("Offense", "Sorcery", "Grants {}% cooldown reduction.", (1,2,3,4), 0, 4, 0)
    butcher = Mastery("Offense", "Butcher", "Basic attacks deal {} bonus physical damage to minions and monsters.",
    (2,4), 0, 2, 0)
    
    self.offenseTree[(1,1)] = summonersWrath
    self.offenseTree[(1,2)] = fury
    self.offenseTree[(1,3)] = sorcery
    self.offenseTree[(1,4)] = butcher
    
    # Tier 2
    deadliness = Mastery("Offense", "Deadliness", "Grants {} attack damage per level ({} at level 18).", (0.17,0.33,0.5,0.67),
    0, 4, 4)
    blast = Mastery("Offense", "Blast", "Grants {} ability power per level ({} at level 18).", (0.25,0.5,0.75,1), 0, 4, 4)
    destruction = Mastery("Offense", "Destruction", "Increases damage to turrets by 5%.", None, 0, 1, 4)
    
    self.offenseTree[(2,2)] = deadliness
    self.offenseTree[(2,3)] = blast
    self.offenseTree[(2,4)] = destruction
    
    # Tier 3
    havoc = Mastery("Offense", "Havoc", "Increases damage dealt by {}%.", (0.67,1.33,2), 0, 3, 8)
    weaponExpertise = Mastery("Offense", "Weapon Expertise", "Grants 8% armor penetration.", None, 0, 1, 8, deadliness)
    arcaneKnowledge = Mastery("Offense", "Arcane Knowledge", "Grants 8% magic penetration.", None, 0, 1, 8, blast)
    
    self.offenseTree[(3,1)] = havoc
    self.offenseTree[(3,2)] = weaponExpertise
    self.offenseTree[(3,3)] = arcaneKnowledge
    
    # Tier 4
    lethality = Mastery("Offense", "Lethality", "Grants {}% critical strike damage (doubled on melee champions).",
    (2.5,5), 0, 2, 12)
    bruteForce = Mastery("Offense", "Brute Force", "Grants {} attack damage.", (1.5,3), 0, 2, 12)
    mentalForce = Mastery("Offense", "Mental Force", "Grants {} ability power.", (2,4,6), 0, 3, 12)
    spellsword = Mastery("Offense", "Spellsword", ("Your basic attacks deal bonus magic damage equal to 5% of your "
    "ability power."), None, 0, 1, 12)
    
    self.offenseTree[(4,1)] = lethality
    self.offenseTree[(4,2)] = bruteForce
    self.offenseTree[(4,3)] = mentalForce
    self.offenseTree[(4,4)] = spellsword
    
    # Tier 5
    frenzy = Mastery("Offense", "Frenzy", "Grants a 10% attack speed buff for 2 seconds after landing a critical strike.",
    None, 0, 1, 16, lethality)
    sunder = Mastery("Offense", "Sunder", "Grants {} armor penetration.", (2,3.5,5), 0, 3, 16)
    archmage = Mastery("Offense", "Archmage", "Increases ability power by {}%.", (1.25,2.5,3.75,5), 0, 4, 16)
    
    self.offenseTree[(5,1)] = frenzy
    self.offenseTree[(5,2)] = sunder
    self.offenseTree[(5,3)] = archmage
    
    # Tier 6
    executioner = Mastery("Offense", "Executioner", ("Increases damage by 5% against targets below 50% health "
    "(excluding true damage)."), None, 0, 1, 20)
    
    self.offenseTree[(6,2)] = executioner
    
    # Defense tree
    self.defenseTree = {}
    
    # Tier 1
    summonersResolve = Mastery("Defense", "Summoner's Resolve", ("Cleanse: Increases the duration of the crowd control "
    "reduction to 4 seconds.\nHeal: Passively grants the champion +5 health per level.\nSmite: Grants 10 gold on use.\nBarrier: "
    "Shield strength increased by 20."), None, 0, 1, 0)
    perseverance = Mastery("Defense", "Perseverance", "Grants up to {} health regen per 5 seconds based on missing health.",
    (2,4,6), 0, 3, 0)
    durability = Mastery("Defense", "Durability", "Grants {} health per level ({} health at level 18).", (1.5,3,4.5,6),
    0, 3, 0)
    toughSkin = Mastery("Defense", "Tough Skin", "Reduces damage from monsters by {}.", (1,2), 0, 2, 0)
    
    self.defenseTree[(1,1)] = summonersResolve
    self.defenseTree[(1,2)] = perseverance
    self.defenseTree[(1,3)] = durability
    self.defenseTree[(1,4)] = toughSkin
    
    # Tier 2
    hardiness = Mastery("Defense", "Hardiness", "Grants {} armor.", (2,3.5,5), 0, 3, 4)
    resistance = Mastery("Defense", "Resistance", "Grants {} magic resistance.", (2,3.5,5), 0, 3, 4)
    bladedArmor = Mastery("Defense", "Bladed Armor", "Deals 6 true damage to any minion or monster that attacks you.",
    None, 0, 1, 4, toughSkin)
    
    self.defenseTree[(2,1)] = hardiness
    self.defenseTree[(2,2)] = resistance
    self.defenseTree[(2,4)] = bladedArmor
    
    # Tier 3
    unyielding = Mastery("Defense", "Unyielding", "Reduces damage from champions by {}.", (1,2), 0, 2, 8)
    relentless = Mastery("Defense", "Relentless", ("Reduces the potency of movement slows by {}% (stacks multiplicatively "
    "with Boots of Swiftness)."), (7.5,15), 0, 2, 8)
    veteransScars = Mastery("Defense", "Veteran's Scars", "Grants 30 health.", None, 0, 1, 8, durability)
    safeguard = Mastery("Defense", "Safeguard", "Reduces damage taken from turrets by 5%.", None, 0, 1, 8)
    
    self.defenseTree[(3,1)] = unyielding
    self.defenseTree[(3,2)] = relentless
    self.defenseTree[(3,3)] = veteransScars
    self.defenseTree[(3,4)] = safeguard
    
    # Tier 4
    block = Mastery("Defense", "Block", ("Block damage from champion basic attacks by 3. That means it applies before "
    "damage reduction from armor."), None, 0, 1, 12, unyielding)
    tenacious = Mastery("Defense", "Tenacious", ("Reduces the duration of crowd control effects by {}% (stacks "
    "multiplicatively with other sources of crowd control reduction)."), (5,10,15), 0, 3, 12)
    juggernaut = Mastery("Defense", "Juggernaut", "Increases your maximum health by {}%.", (1.5,2.75,4), 0, 3, 12)
    
    self.defenseTree[(4,1)] = block
    self.defenseTree[(4,2)] = tenacious
    self.defenseTree[(4,3)] = juggernaut
    
    # Tier 5
    defender = Mastery("Defense", "Defender", "Grants 1 bonus armor and magic resistance for every nearby enemy champion.",
    None, 0, 1, 16)
    legendaryArmor = Mastery("Defense", "Legendary Armor", "Increases bonus armor and magic resistance by {}%.", (2,3.5,5),
    0, 3, 16)
    goodHands = Mastery("Defense", "Good Hands", "Reduces the time spent dead by 10%.", None, 0, 1, 16)
    reinforcedArmor = Mastery("Defense", "Reinforced Armor", "Reduces damage taken from critical strikes by 10%.", None,
    0, 1, 16)
    
    self.defenseTree[(5,1)] = defender
    self.defenseTree[(5,2)] = legendaryArmor
    self.defenseTree[(5,3)] = goodHands
    self.defenseTree[(5,4)] = reinforcedArmor
    
    # Tier 6
    honorGuard = Mastery("Defense", "Honor Guard", "Reduces damage taken from all sources by 3%.", None, 0, 1, 20)
    
    self.defenseTree[(6,2)] = honorGuard
    
    # Utility tree
    self.utilityTree = {}
    
    # Tier 1
    summonersInsight = Mastery("Utility", "Summoner's Insight", ("Clairvoyance: Grants persistent sight of enemies revealed "
    "for 5 seconds.\nClarity: Increases mana restored by 25%.\nFlash: Reduces cooldown by 15 seconds.\nRevive: Grants bonus "
    "health after reviving for 120 seconds.\nTeleport: Reduces cast time by 0.5 seconds."), None, 0, 1, 0)
    wanderer = Mastery("Utility", "Wanderer", "Grants {}% bonus movement speed when out of combat.", (0.66,1.33,2),
    0, 3, 0)
    meditation = Mastery("Utility", "Meditation", "Grants {} mana regeneration per 5 seconds.", (1,2,3), 0, 3, 0)
    improvedRecall = Mastery("Utility", "Improved Recall", ("Reduces cast time of Recall by 1 second and Enhanced Recall "
    "by 0.5 seconds."), None, 0, 1, 0)
    
    self.utilityTree[(1,1)] = summonersInsight
    self.utilityTree[(1,2)] = wanderer
    self.utilityTree[(1,3)] = meditation
    self.utilityTree[(1,4)] = improvedRecall
    
    # Tier 2
    scout = Mastery("Utility", "Scout", "Wards see for 25% further for the first 5 seconds.", None, 0, 1, 4)
    mastermind = Mastery("Utility", "Mastermind", "Reduces the cooldown of Summoner Spells by {}%.", (4,7,10), 0, 3, 4)
    expandedMinds = Mastery("Utility", "Expanded Minds", "Grants {} additional maximum mana per level ({} mana at level 18).", 
    (4,7,10), 0, 3, 4)
    artificer = Mastery("Utility", "Artificer", "Reduces the cooldown of item active effects by {}%.", (7.5,15), 0, 2, 4)
    
    self.utilityTree[(2,1)] = scout
    self.utilityTree[(2,2)] = mastermind
    self.utilityTree[(2,3)] = expandedMinds
    self.utilityTree[(2,4)] = artificer
    
    # Tier 3
    greed = Mastery("Utility", "Greed", "Grants {} gold per 10 seconds.", (0.5,1,1.5,2), 0, 4, 8)
    runicAffinity = Mastery("Utility", "Runic Affinity", ("Increases shrine, relic, quest and neutral monster buff durations "
    "by 20%."), None, 0, 1, 8)
    vampirism = Mastery("Utility", "Vampirism", "Grants {}% spell vamp and life steal.", (1,2,3), 0, 3, 8)
    biscuiteer = Mastery("Utility", "Biscuiteer", ("You start the game with a Total Biscuit of Rejuvenation that restores "
    "80 health and 50 mana over 10 seconds."), None, 0, 1, 8)
    
    self.utilityTree[(3,1)] = greed
    self.utilityTree[(3,2)] = runicAffinity
    self.utilityTree[(3,3)] = vampirism
    self.utilityTree[(3,4)] = biscuiteer
    
    # Tier 4
    wealth = Mastery("Utility", "Wealth", "You start the game with {} bonus gold.", (25,50), 0, 2, 12, greed)
    awareness = Mastery("Utility", "Awareness", "Increases experienced gained by {}%.", (1.25,2.5,3.75,5), 0, 4, 12)
    strengthOfSpirit = Mastery("Utility", "Strength of Spirit", ("Grants {} bonus health regeneration per 5 seconds for "
    "every 400 maximum mana points."), (1,2,3), 0, 3, 12)
    explorer = Mastery("Utility", "Explorer", ("On Summoner's Rift: You start the game with an Explorer's Ward, which "
    "places an invisible ward that lasts 60 seconds.\nOn other maps: You start the game with 25 bonus gold."), None, 0, 1, 12, 
    biscuiteer)
    
    self.utilityTree[(4,1)] = wealth
    self.utilityTree[(4,2)] = awareness
    self.utilityTree[(4,3)] = strengthOfSpirit
    self.utilityTree[(4,4)] = explorer
    
    # Tier 5
    pickpocket = Mastery("Utility", "Pickpocket", ("Your attacks against enemy champions grant gold (+3 ranged attacks; "
    "+5 melee attacks). 5 seconds cooldown."), None, 0, 1, 16)
    intelligence = Mastery("Utility", "Intelligence", "Grants {}% cooldown reduction.", (2,4,6), 0, 3, 16)
    
    self.utilityTree[(5,1)] = pickpocket
    self.utilityTree[(5,2)] = intelligence
    
    # Tier 6
    nimble = Mastery("Utility", (6,2), "Nimble", "Grants 3% movement speed.", None, 0, 1, 20)
    
    self.utilityTree[(6,2)] = nimble
