from abc import ABC, abstractmethod
import time

"""Sort class: Abstract base class implementation"""
class Sort(ABC):

    def __init__(self, items):
        self._items = items

    @abstractmethod
    def _sort(self):
        """Returns the sorted version of the elements contained
        in the `_items` property.
        Returns:
            List: The sorted elements.
        """
        pass

    def get_items(self):
        return self._items

    def _time(self):
        return self.time


"""Class implementation of the MergeSort algorithm."""
class MergeSort(Sort):

  def _sort(self):
    a = self._items

    self.time = time.time()

    if len(a) == 1:
      return a
    else:
      i = j = 0
      l = MergeSort(a[:len(a)//2])._sort()
      r = MergeSort(a[len(a)//2:])._sort()
      aNew = []

      while i < len(l) and j < len(r):
        if l[i] < r[j]:
          aNew.append(l[i])
          i += 1
        else:
          aNew.append(r[j])
          j += 1

      if i == len(l):
        for i in r[j:]: aNew.append(i)
      else:
        for i in l[i:]: aNew.append(i)

      self.time = time.time() - self.time

      return aNew