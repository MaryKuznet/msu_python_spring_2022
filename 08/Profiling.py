import cProfile
import pstats
import io
import weakref
from memory_profiler import profile
from LRUCache import LRUCache


class Ordinal:
    def __init__(self, x):
        self.x = x
        self.y = "Python"
        self.z = [1, 'a', {'a': 1}]


class Slot:
    __slots__ = ("x", "y", "z")

    def __init__(self, x):
        self.x = x
        self.y = "Python"
        self.z = [1, 'a', {'a': 1}]


@profile
def for_memory_ordinal(size):
    cache = LRUCache(size)
    for i in range(size):
        cache.set(i, Ordinal(i))


@profile
def for_memory_slot(size):
    cache = LRUCache(size)
    for i in range(size):
        cache.set(i, Slot(i))


@profile
def for_memory_ref(size):
    cache = LRUCache(size)
    a = Ordinal(1)
    ref = weakref.ref(a)
    for i in range(size):
        cache.set(i, ref())


pr = cProfile.Profile()
pr.enable()

for_memory_ordinal(1000)
for_memory_slot(1000)
for_memory_ref(1000)

for_memory_ordinal(10000)
for_memory_slot(10000)
for_memory_ref(10000)

pr.disable()

s = io.StringIO()
sort_by = "cumulative"
ps = pstats.Stats(pr, stream=s).sort_stats(sort_by)
ps.print_stats()
print(s.getvalue())
