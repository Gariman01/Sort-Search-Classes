from abc import ABC, abstractmethod
import time

"""Module with the base implementation of a Search class."""

class Search(ABC):
    """Abstract base class for searching."""

    def __init__(self, items):
        self._items = items

    @abstractmethod
    def _search(self):
        """Returns the index of the `item` contained
        in the `_items` property.
        Returns:
            int: Index of item
        """
        pass

    def get_items(self):
        return self._items

    def _time(self):
        return self.time

class LinearSearch(Search):

  def _search(self, item):
    flag = False
    self.time = time.time()
    for i, j in enumerate(self._items):
      if j == item:
        flag = True
        self.time = time.time() - self.time
        return i
    if flag == False:
      self.time = time.time() - self.time
      return -1