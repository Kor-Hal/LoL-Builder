# -*-coding:Latin-1 -*
class Mastery(object):
  """Defines a Mastery.
  
  Ref : http://leagueoflegends.wikia.com/wiki/Mastery
  
  """
  
  def __init__(self, tree, name, description, ranks, level, max_points, points_prerequisite, mastery_prerequisite=None, icon=None):
    """ Create a new Mastery.
    
    Named parameters :
    tree -- Mastery's tree
    name -- Mastery's name
    description -- Mastery's description
    ranks -- Values of the different mastery's ranks
    level -- Current number of points spent in the mastery
    max_points -- Max points allowed in this mastery
    points_prerequisite -- Number of points needed in the mastery's tree to be able to spend points in this one
    mastery_prerequisite -- Mastery required to fill before being able to spend points in this one
    icon -- Path to the Mastery's icon
    
    """
    
    self._tree = tree
    self._name = name
    self._description = description
    self._ranks = ranks
    self._level = level
    self._max_points = max_points
    self._points_prerequisite = points_prerequisite
    self._mastery_prerequisite = mastery_prerequisite
    self._icon = icon
  
  @property
  def tree(self):
    """Mastery's tree."""
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
  def max_points(self):
    """Max points allowed in this mastery."""
    return self._max_points
  
  @property
  def points_prerequisite(self):
    """Number of points needed in the mastery's tree to be able to spend points in this one."""
    return self._points_prerequisite
  
  @property
  def mastery_prerequisite(self):
    """Mastery required to fill before being able to spend points in this one."""
    return self._mastery_prerequisite
  
  @property
  def icon(self):
    """Path to the Mastery's icon."""
    return self._icon
  
  # Defining how to access the self._level property
  
  @property
  def level(self):
    """Current number of points spent in the mastery."""
    return self._level
  
  @level.setter
  def level(self, value):
    if self.tree.points_spent >= self.points_prerequisite and \
        self.mastery_prerequisite.level == self.mastery_prerequisite.max_points and \
        value <= self.max_points:
      self._level = value
      self.tree.points_spent += value
  
  def curr_value(self):
    return self.ranks[self.level - 1]

class MasteryTree(object):
  """Defines a Mastery tree.
  
  Ref : http://leagueoflegends.wikia.com/wiki/Mastery
  
  """
    
  def __init__(self, name, masteries):
    """Create a new mastery tree.
    
    Named parameters :
    name -- Mastery page's name
    masteries -- Dict of this tree's masteries
    points_spent -- Points spent in the tree
    
    """
    
    self._name = name
    self._masteries = masteries
    self.points_spent = 0
    
    @property
    def name(self):
      """Mastery tree's name."""
      return self._name
    
    @property
    def masteries(self):
      """Dict of this tree's masteries."""
      return self._masteries

class MasteryPage(object):
  """Defines a Mastery page, with the 3 trees.
  
  Ref : http://leagueoflegends.wikia.com/wiki/Mastery
  
  """
    
  def __init__(self, name):
    """Create a new empty Mastery page.
    
    Named parameters :
    name -- Mastery page's name
    
    """
    
    self._name = name
    
    @property
    def name(self):
      """Mastery page's name."""
      return self._name
    
    # Offense masteries
    offense_masteries = {}
    
    # Tier 1
    summoners_wrath = Mastery("Offense", ("Summoner's Wrath", "Exhaust: Lowers the target's armor and magic resistance by "
    "10.\nIgnite: Grants 5 attack damage and 5 ability power while on cooldown.\nGhost: Bonus movement speed increased to "
    "35% movement speed.\nGarrison: Allied towers gain 50% splash damage."), None, 0, 1, 0)
    fury = Mastery("Offense", "Fury", "Grants {}% attack speed.", (1,2,3,4), 0, 4, 0)
    sorcery = Mastery("Offense", "Sorcery", "Grants {}% cooldown reduction.", (1,2,3,4), 0, 4, 0)
    butcher = Mastery("Offense", "Butcher", "Basic attacks deal {} bonus physical damage to minions and monsters.",
    (2,4), 0, 2, 0)
    
    offense_masteries[(1,1)] = summoners_wrath
    offense_masteries[(1,2)] = fury
    offense_masteries[(1,3)] = sorcery
    offense_masteries[(1,4)] = butcher
    
    # Tier 2
    deadliness = Mastery("Offense", "Deadliness", "Grants {} attack damage per level ({} at level 18).", (0.17,0.33,0.5,0.67),
    0, 4, 4)
    blast = Mastery("Offense", "Blast", "Grants {} ability power per level ({} at level 18).", (0.25,0.5,0.75,1), 0, 4, 4)
    destruction = Mastery("Offense", "Destruction", "Increases damage to turrets by 5%.", None, 0, 1, 4)
    
    offense_masteries[(2,2)] = deadliness
    offense_masteries[(2,3)] = blast
    offense_masteries[(2,4)] = destruction
    
    # Tier 3
    havoc = Mastery("Offense", "Havoc", "Increases damage dealt by {}%.", (0.67,1.33,2), 0, 3, 8)
    weapon_expertise = Mastery("Offense", "Weapon Expertise", "Grants 8% armor penetration.", None, 0, 1, 8, deadliness)
    arcane_knowledge = Mastery("Offense", "Arcane Knowledge", "Grants 8% magic penetration.", None, 0, 1, 8, blast)
    
    offense_masteries[(3,1)] = havoc
    offense_masteries[(3,2)] = weapon_expertise
    offense_masteries[(3,3)] = arcane_knowledge
    
    # Tier 4
    lethality = Mastery("Offense", "Lethality", "Grants {}% critical strike damage (doubled on melee champions).",
    (2.5,5), 0, 2, 12)
    brute_force = Mastery("Offense", "Brute Force", "Grants {} attack damage.", (1.5,3), 0, 2, 12)
    mental_force = Mastery("Offense", "Mental Force", "Grants {} ability power.", (2,4,6), 0, 3, 12)
    spellsword = Mastery("Offense", "Spellsword", ("Your basic attacks deal bonus magic damage equal to 5% of your "
    "ability power."), None, 0, 1, 12)
    
    offense_masteries[(4,1)] = lethality
    offense_masteries[(4,2)] = brute_force
    offense_masteries[(4,3)] = mental_force
    offense_masteries[(4,4)] = spellsword
    
    # Tier 5
    frenzy = Mastery("Offense", "Frenzy", "Grants a 10% attack speed buff for 2 seconds after landing a critical strike.",
    None, 0, 1, 16, lethality)
    sunder = Mastery("Offense", "Sunder", "Grants {} armor penetration.", (2,3.5,5), 0, 3, 16)
    archmage = Mastery("Offense", "Archmage", "Increases ability power by {}%.", (1.25,2.5,3.75,5), 0, 4, 16)
    
    offense_masteries[(5,1)] = frenzy
    offense_masteries[(5,2)] = sunder
    offense_masteries[(5,3)] = archmage
    
    # Tier 6
    executioner = Mastery("Offense", "Executioner", ("Increases damage by 5% against targets below 50% health "
    "(excluding true damage)."), None, 0, 1, 20)
    
    offense_masteries[(6,2)] = executioner
    
    self.offense_tree = MasteryTree("Offense", offense_masteries)
    
    # Defense tree
    defense_masteries = {}
    
    # Tier 1
    summoners_resolve = Mastery("Defense", "Summoner's Resolve", ("Cleanse: Increases the duration of the crowd control "
    "reduction to 4 seconds.\nHeal: Passively grants the champion +5 health per level.\nSmite: Grants 10 gold on use.\nBarrier: "
    "Shield strength increased by 20."), None, 0, 1, 0)
    perseverance = Mastery("Defense", "Perseverance", "Grants up to {} health regen per 5 seconds based on missing health.",
    (2,4,6), 0, 3, 0)
    durability = Mastery("Defense", "Durability", "Grants {} health per level ({} health at level 18).", (1.5,3,4.5,6),
    0, 3, 0)
    tough_skin = Mastery("Defense", "Tough Skin", "Reduces damage from monsters by {}.", (1,2), 0, 2, 0)
    
    defense_masteries[(1,1)] = summoners_resolve
    defense_masteries[(1,2)] = perseverance
    defense_masteries[(1,3)] = durability
    defense_masteries[(1,4)] = tough_skin
    
    # Tier 2
    hardiness = Mastery("Defense", "Hardiness", "Grants {} armor.", (2,3.5,5), 0, 3, 4)
    resistance = Mastery("Defense", "Resistance", "Grants {} magic resistance.", (2,3.5,5), 0, 3, 4)
    bladed_armor = Mastery("Defense", "Bladed Armor", "Deals 6 true damage to any minion or monster that attacks you.",
    None, 0, 1, 4, tough_skin)
    
    defense_masteries[(2,1)] = hardiness
    defense_masteries[(2,2)] = resistance
    defense_masteries[(2,4)] = bladed_armor
    
    # Tier 3
    unyielding = Mastery("Defense", "Unyielding", "Reduces damage from champions by {}.", (1,2), 0, 2, 8)
    relentless = Mastery("Defense", "Relentless", ("Reduces the potency of movement slows by {}% (stacks multiplicatively "
    "with Boots of Swiftness)."), (7.5,15), 0, 2, 8)
    veterans_scars = Mastery("Defense", "Veteran's Scars", "Grants 30 health.", None, 0, 1, 8, durability)
    safeguard = Mastery("Defense", "Safeguard", "Reduces damage taken from turrets by 5%.", None, 0, 1, 8)
    
    defense_masteries[(3,1)] = unyielding
    defense_masteries[(3,2)] = relentless
    defense_masteries[(3,3)] = veterans_scars
    defense_masteries[(3,4)] = safeguard
    
    # Tier 4
    block = Mastery("Defense", "Block", ("Block damage from champion basic attacks by 3. That means it applies before "
    "damage reduction from armor."), None, 0, 1, 12, unyielding)
    tenacious = Mastery("Defense", "Tenacious", ("Reduces the duration of crowd control effects by {}% (stacks "
    "multiplicatively with other sources of crowd control reduction)."), (5,10,15), 0, 3, 12)
    juggernaut = Mastery("Defense", "Juggernaut", "Increases your maximum health by {}%.", (1.5,2.75,4), 0, 3, 12)
    
    defense_masteries[(4,1)] = block
    defense_masteries[(4,2)] = tenacious
    defense_masteries[(4,3)] = juggernaut
    
    # Tier 5
    defender = Mastery("Defense", "Defender", "Grants 1 bonus armor and magic resistance for every nearby enemy champion.",
    None, 0, 1, 16)
    legendary_armor = Mastery("Defense", "Legendary Armor", "Increases bonus armor and magic resistance by {}%.", (2,3.5,5),
    0, 3, 16)
    good_hands = Mastery("Defense", "Good Hands", "Reduces the time spent dead by 10%.", None, 0, 1, 16)
    reinforced_armor = Mastery("Defense", "Reinforced Armor", "Reduces damage taken from critical strikes by 10%.", None,
    0, 1, 16)
    
    defense_masteries[(5,1)] = defender
    defense_masteries[(5,2)] = legendary_armor
    defense_masteries[(5,3)] = good_hands
    defense_masteries[(5,4)] = reinforced_armor
    
    # Tier 6
    honor_guard = Mastery("Defense", "Honor Guard", "Reduces damage taken from all sources by 3%.", None, 0, 1, 20)
    
    defense_masteries[(6,2)] = honor_guard
    
    self.defense_tree = MasteryTree("Defense", defense_masteries)
    
    # Utility tree
    utility_masteries = {}
    
    # Tier 1
    summoners_insight = Mastery("Utility", "Summoner's Insight", ("Clairvoyance: Grants persistent sight of enemies revealed "
    "for 5 seconds.\nClarity: Increases mana restored by 25%.\nFlash: Reduces cooldown by 15 seconds.\nRevive: Grants bonus "
    "health after reviving for 120 seconds.\nTeleport: Reduces cast time by 0.5 seconds."), None, 0, 1, 0)
    wanderer = Mastery("Utility", "Wanderer", "Grants {}% bonus movement speed when out of combat.", (0.66,1.33,2),
    0, 3, 0)
    meditation = Mastery("Utility", "Meditation", "Grants {} mana regeneration per 5 seconds.", (1,2,3), 0, 3, 0)
    improved_recall = Mastery("Utility", "Improved Recall", ("Reduces cast time of Recall by 1 second and Enhanced Recall "
    "by 0.5 seconds."), None, 0, 1, 0)
    
    utility_masteries[(1,1)] = summoners_insight
    utility_masteries[(1,2)] = wanderer
    utility_masteries[(1,3)] = meditation
    utility_masteries[(1,4)] = improved_recall
    
    # Tier 2
    scout = Mastery("Utility", "Scout", "Wards see for 25% further for the first 5 seconds.", None, 0, 1, 4)
    mastermind = Mastery("Utility", "Mastermind", "Reduces the cooldown of Summoner Spells by {}%.", (4,7,10), 0, 3, 4)
    expanded_minds = Mastery("Utility", "Expanded Minds", "Grants {} additional maximum mana per level ({} mana at level 18).", 
    (4,7,10), 0, 3, 4)
    artificer = Mastery("Utility", "Artificer", "Reduces the cooldown of item active effects by {}%.", (7.5,15), 0, 2, 4)
    
    utility_masteries[(2,1)] = scout
    utility_masteries[(2,2)] = mastermind
    utility_masteries[(2,3)] = expanded_minds
    utility_masteries[(2,4)] = artificer
    
    # Tier 3
    greed = Mastery("Utility", "Greed", "Grants {} gold per 10 seconds.", (0.5,1,1.5,2), 0, 4, 8)
    runic_affinity = Mastery("Utility", "Runic Affinity", ("Increases shrine, relic, quest and neutral monster buff durations "
    "by 20%."), None, 0, 1, 8)
    vampirism = Mastery("Utility", "Vampirism", "Grants {}% spell vamp and life steal.", (1,2,3), 0, 3, 8)
    biscuiteer = Mastery("Utility", "Biscuiteer", ("You start the game with a Total Biscuit of Rejuvenation that restores "
    "80 health and 50 mana over 10 seconds."), None, 0, 1, 8)
    
    utility_masteries[(3,1)] = greed
    utility_masteries[(3,2)] = runic_affinity
    utility_masteries[(3,3)] = vampirism
    utility_masteries[(3,4)] = biscuiteer
    
    # Tier 4
    wealth = Mastery("Utility", "Wealth", "You start the game with {} bonus gold.", (25,50), 0, 2, 12, greed)
    awareness = Mastery("Utility", "Awareness", "Increases experienced gained by {}%.", (1.25,2.5,3.75,5), 0, 4, 12)
    strength_of_spirit = Mastery("Utility", "Strength of Spirit", ("Grants {} bonus health regeneration per 5 seconds for "
    "every 400 maximum mana points."), (1,2,3), 0, 3, 12)
    explorer = Mastery("Utility", "Explorer", ("On Summoner's Rift: You start the game with an Explorer's Ward, which "
    "places an invisible ward that lasts 60 seconds.\nOn other maps: You start the game with 25 bonus gold."), None, 0, 1, 12, 
    biscuiteer)
    
    utility_masteries[(4,1)] = wealth
    utility_masteries[(4,2)] = awareness
    utility_masteries[(4,3)] = strength_of_spirit
    utility_masteries[(4,4)] = explorer
    
    # Tier 5
    pickpocket = Mastery("Utility", "Pickpocket", ("Your attacks against enemy champions grant gold (+3 ranged attacks; "
    "+5 melee attacks). 5 seconds cooldown."), None, 0, 1, 16)
    intelligence = Mastery("Utility", "Intelligence", "Grants {}% cooldown reduction.", (2,4,6), 0, 3, 16)
    
    utility_masteries[(5,1)] = pickpocket
    utility_masteries[(5,2)] = intelligence
    
    # Tier 6
    nimble = Mastery("Utility", (6,2), "Nimble", "Grants 3% movement speed.", None, 0, 1, 20)
    
    utility_masteries[(6,2)] = nimble
    
    self.utility_tree = MasteryTree("Utility", utility_masteries)
