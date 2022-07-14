# 一个关于+=的谜题

"""
>>> t = (1, 2, [30, 40])
>>> t[2] += [50, 60]
Traceback (most recent call last):
...
TypeError: 'tuple' object does not support item assignment
>>> t
(1, 2, [30, 40, 50, 60])
"""

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
