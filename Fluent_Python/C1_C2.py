import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])
ranks = [str(n) for n in range(2,11) + list('JQKA')]
print ranks