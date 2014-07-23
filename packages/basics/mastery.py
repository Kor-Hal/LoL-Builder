# -*-coding:utf-8 -*
class Mastery(object):
  """Defines a Mastery.
  
  Ref : http://leagueoflegends.wikia.com/wiki/Mastery
  
  """
  
  def __init__(self,
               tree,
               name,
               description,
               ranks,
               level,
               max_points,
               points_prerequisite,
               mastery_prerequisite=None,
               icon=None):
    """ Create a new Mastery.
    
    Named parameters :
    tree -- Mastery's tree
    name -- Mastery's name
    description -- Mastery's description
    ranks -- Values of the different mastery's ranks
    level -- Current number of points spent in the mastery
    max_points -- Max points allowed in this mastery
    points_prerequisite -- Number of points needed in the mastery's tree to be
                           able to spend points in this one
    mastery_prerequisite -- Mastery required to fill before being able to spend
                            points in this one
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
  
  @tree.setter
  def tree(self, value):
    self._tree = value
  
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
    """Number of points needed in the mastery's tree to be able to spend points
    in this one."""
    return self._points_prerequisite
  
  @property
  def mastery_prerequisite(self):
    """Mastery required to fill before being able to spend points in this
    one."""
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
    if self.mastery_prerequisite is not None:
      if (self.tree.points_spent >= self.points_prerequisite and
         self.mastery_prerequisite.level ==
          self.mastery_prerequisite.max_points and value <= self.max_points):
        self._level = value
        self.tree.points_spent += value
        self.tree.page.update_statistics()
    else:
      if (self.tree.points_spent >= self.points_prerequisite and
          value <= self.max_points):
        self._level = value
        self.tree.points_spent += value
        self.tree.page.update_statistics()

  def current_value(self):
    if self.level > 0 and self.ranks is not None:
      return self.ranks[self.level - 1]
    else:
      return 0
