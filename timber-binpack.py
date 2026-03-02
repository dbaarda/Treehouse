#!/usr/bin/python3
from math import *
import functools,random,os

def rad(d):
  return d/180*pi

def dsin(d):
  return sin(rad(d))

class Piece(object):
  """A cut piece of timber.
  
  With the piece layed horizontally and flat, the lengths of edges and cut
  angles anticlockwise off perpendicular, are as follows;

    h: front face height.
    w: top face width.
    l1: front top edge length.
    l2: front bottom edge length.
    l3: back bottom edge length.
    l4: back top edge length
    a1: left end across the front face angle.
    a2: right end across the front face angle.
    b1: left end across the top face angle.
    b2: right end across the top face angle.

  The angles are so that positive angles can be cut using a carpenter's square
  set to a[12] and the blade angle set to b[12].
  
  Note pieces can be flipped and rolled, transforming the length and angles,
  or normalized, which flips/rolls them to have longest edge on the top front
  edge.
  """
  def __init__(self, h, w, l1, a1=0, a2=0, b1=0, b2=0):
    self.h, self.w, self.l1, self.a1, self.a2, self.b1, self.b2 = h, w, l1, a1, a2, b1, b2
    assert h >= w, f'height less that width for {self}'
    assert l1 > 0, f'length <= 0 for {self}'
    assert all(-90 < a < 90 for a in (a1,a2,b1,b2)), f'angle <-90 or >90 for {self}'
    
  @property
  def l2(self):
    return self.l1 - self.h*(dsin(self.a1) - dsin(self.a2))
  
  @property
  def l3(self):
    return self.l2 + self.w*(dsin(self.b1) - dsin(self.b2))
  
  @property
  def l4(self):
    return self.l1 + self.w*(dsin(self.b1) - dsin(self.b2))
  
  def roll(self):
    """Roll the piece, turning it over and not swapping ends."""
    self.l1, self.a1, self.a2, self.b1, self.b2 = self.l3, -self.a1, -self.a2, -self.b1, -self.b2
    
  def spin(self):
    """spin the piece, swapping ends and not turning it over."""
    self.l1, self.a1, self.a2, self.b1, self.b2 = self.l2, self.a2, self.a1, -self.b2, -self.b1
  
  def flip(self):
    """Flip the piece, swaping ends and turning it over."""
    self.l1, self.a1, self.a2, self.b1, self.b2 = self.l4, -self.a2, -self.a1, self.b2, self.b1
    
  def norm(self):
    if self.l4 > self.l1:
      self.flip()
    if self.l2 > self.l1:
      self.spin()
  
  def d1(self):
    """How far the left end corners stick out past the middle."""
    dh = -self.h*dsin(self.a1)/2
    dw = self.w*dsin(self.b1)/2
    return -dh-dw, dh-dw, dh+dw, -dh+dw
            
  def d2(self):
    """How far the right end corners stick out past the middle."""
    dh = self.h*dsin(self.a2)/2
    dw = -self.w*dsin(self.b2)/2
    return -dh-dw, dh-dw, dh+dw, -dh+dw
  
  def gapr(self, other):
    """The gap in the middle and top front edge when joining self to the right of other."""
    dl1,dl2,dl3,dl4 = other.d2()
    dr1,dr2,dr3,dr4 = self.d1()
    g1,g2,g3,g4 = -dl1-dr1,-dl2-dr2,-dl3-dr3,-dl4-dr4
    gm = -min(g1,g2,g3,g4)
    return gm, gm+g1

  def fitr(self,other):
    """Spin self to best fit on the right of other, returning the mid and top-front gap."""
    gm,g1 = self.gapr(other)
    self.roll()
    gmn,g1n = self.gapr(other)
    if gmn < gm:
      gm,g1 = gmn,g1n
    else:
      self.roll()
    self.flip()
    gmn,g1n = self.gapr(other)
    if gmn < gm:
      gm,g1 = gmn,g1n
    else:
      self.flip()
    self.spin()
    gmn,g1n = self.gapr(other)
    if gmn < gm:
      gm,g1 = gmn,g1n
    else:
      self.spin()
    return gm,g1

  def __str__(self):
    e1=f'{f"{self.a1}" if self.a1 else ""}{f"/{self.b1}" if self.b1 else ""}'
    e2=f'{f"{self.a2}" if self.a2 else ""}{f"/{self.b2}" if self.b2 else ""}'
    return f'{self.h}x{self.w}x{self.l1:.1f}{f"[{e1}:{e2}]" if e1 or e2 else ""}'

def testPiece():
  p1=Piece(90,45,2000,-45,30,10,20)
  print(p1)
  p1.norm()
  print(p1)
  p2=Piece(90,45,3000,5.8,5.8)
  print(p2)
  gm2,g12 = p2.fitr(p1)
  print(p1, g12, p2)
  p3=Piece(90,45,3000,0,0,5.8,-5.8)
  print(p3)
  gm3,g13 = p3.fitr(p2)
  print(p1, g12, p2, g13, p3)
  os.exit(1)

def fmtlens(lens):
  if not isinstance(lens, dict):
    lens = {l:lens.count(l) for l in lens}
  return ', '.join(f'{lens[l]}x{l}' for l in sorted(lens,reverse=True)) or 'None'


class Lengths(dict):
  """ A dictionary of lengths."""

  def __init__(self, *args,**kwargs):
    """Initialise from a dict of length -> count."""
    super().__init__((k,v) for k,v in dict(*args,**kwargs).items() if v>0)
    assert all(l > 0 for l in self), f'length <= 0 in {self}'
    assert all(self[l] >= 1 for l in self), f'count < 1 in {self}'

  def give(self, l, n=1):
    """Give a length l into the inventory."""
    assert l>0, f'length {l} <= 0'
    assert n>=1, f'count {n} < 1'
    self[l] = self.get(l, 0) + n

  def take(self, l, n=1):
    """Take a length l from the inventory."""
    assert l > 0, f'length {l} <= 0'
    assert n <= self.get(l,0), f'count {n} > available for length {l}'
    self[l] -= n
    if not self[l]:
      del self[l]

  def best(self, need, default=0):
    """ Get the best fit available length."""
    return min((l for l,n in self.items() if l >= need), default=default)

  def swap(self, need, oldlen=0):
    """Try to swap an old length for a new length that is a better fit."""
    if oldlen:
      # give old length back into lens.
      self.give(oldlen)
    if need <= 0:
      # No length needed if nothing used.
      return 0
    # Find, get and return the shortest available length that will fit used.
    newlen = self.best(need, oldlen)
    # It's possible oldlen=0, in which case we might not have anything available.
    if newlen:
      self.take(newlen)
    return newlen

  @property
  def minlen(self):
    return min((l for l,n in self.items() if n > 0), default=0)

  @property
  def maxlen(self):
    return max((l for l,n in self.items() if n > 0), default=0)

  @property
  def avglen(self):
    return sum(l*n for l,n in self.items())/sum(n for n in self.values())

  def __add__(self, other):
    """ Add two lengths collections together. """
    new = self.__class__(self)
    new += other
    return new

  def __iadd__(self, other):
    """ Add two lengths collections together. """
    assert all(l > 0 for l in other), f'length <= 0 in {other}'
    assert all(other[l] >= 1 for l in other), f'count < 1 in {other}'
    for k,v in other.items():
      self.give(k,v)
    return self

  # def __iter__(self):
  #   return (l for l in sorted(self, reverse=True))

  def __str__(self):
    return fmtlens(self)


class Beam(object):

  # The cut width in mm.
  swarf = 2

  def __init__(self, stock):
    self.stock=stock
    self.pieces = []
    self.length = 0
    self.maxlength = 10000

  @property
  def waste(self):
    """The unused timber, including cuts."""
    return self.length - self.used

  @property
  def used(self):
    """The timber used for pieces."""
    return sum(self.pieces)

  @property
  def need(self):
    """Timber length needed for pieces and cuts."""
    # We don't need the last cut.
    return self.used + max(0, len(self.pieces) - 1)*self.swarf

  @property
  def left(self):
    """ The amount of timber left over after cutting all the pieces."""
    # The last cut swarf is truncated at the end of the beam.
    # Lengths from stock are assumed to be cleanly trimmed or have enough
    # excess to cleanly trim the last piece.
    return max(0, self.length - self.used - len(self.pieces)*self.swarf)

  @property
  def dust(self):
    """Amount of beam dusted by cuts."""
    return self.length - self.used - self.left

  def _swapstock(self):
    """ Get the shortest length needed for the pieces. """
    self.length = self.stock.swap(self.need, self.length)


  def _value(self, m):
    """Calculate a scaled value from a metric in the range [0.0,1.0]."""
    # This uses a formula v=1-m^n to adjust the value. Different values of n
    # correspond with different policies;
    #   n=0; first fit.
    #   n=1; least waste, first fit.
    #   n<1; least waste, best fit if decreasing waste, worst fit if increasing waste.
    #   n>1; least waste, worst fit if decreasing waste, best fit if increasing waste.
    return 1.0 - m**(1/16)

  @property
  def value(self):
    """Get the value of a beam in the range [0.0, 1.0]."""
    # Assume waste for a new unused beam is 100.
    waste = self.waste if self.pieces else 100
    #if self.left == 0.0:
    #  # Add a strong bias for perfect fits.
    #  return 2.0
    return self._value(waste/self.maxlength)

  def addcut(self,p):
    """  Cut a new piece. """
    self.pieces.append(p)
    self._swapstock()
    if self.need > self.length:
      self.popcut()
      raise ValueError(f'Cut {p} is too long.')

  def popcut(self):
    """ Remove the last cut piece."""
    self.pieces.pop()
    self._swapstock()

  def __str__(self):
    return f'{self.length}: {self.pieces} {self.left}'

  def __len__(self):
    return len(self.pieces)

  def trycut(self, p):
    """ Get the change in value for cutting a piece. """
    # This must return value in the range [-1.0, 1.0]
    oldvalue = self.value
    try:
      self.addcut(p)
      value = self.value - oldvalue
      self.popcut()
      return value
    except ValueError:
      return -1.0


class Beams(object):

  def __init__(self, stock):
    self.stock = stock
    self.beams = []
    self.missing = []

  def addcut(self, p):
    newb = Beam(self.stock)
    # We put the newb on the end so we favour existing beams.
    bestb,bestw = None, -1.0
    for b in self.beams + [newb]:
      w = b.trycut(p)
      if w > bestw:
        bestb,bestw = b,w
      #print(f'p={p} w={w} bestw={bestw} b=({b})')
    if bestb is None:
      self.missing.append(p)
    else:
      bestb.addcut(p)
      if bestb is newb:
         self.beams.append(bestb)

  @property
  def pieces(self):
    return sum(len(b) for b in self.beams)

  @property
  def length(self):
    return sum(b.length for b in self.beams)

  @property
  def waste(self):
    return sum(b.waste for b in self.beams)

  @property
  def used(self):
    return sum(b.used for b in self.beams)

  @property
  def left(self):
    return sum(p for p in self.missing)

  def __len__(self):
    return len(self.beams)

  def __getitem__(self, index):
    # This makes the beams value iterable.
    return self.beams[index]

  def __str__(self):
    bls = [b.length for b in self.beams]
    fls = functools.reduce(lambda a,b:a+b.pieces, self.beams, [])
    mls = self.missing
    beams = '\n'.join(str(b) for b in self.beams)
    return (f"""\
used: {fmtlens(bls)}
cuts: {fmtlens(fls)}
left: {fmtlens(mls)}
beams={len(self)} length={self.length} pieces={self.pieces} used={self.used} waste={self.waste} left={self.left}
{beams}""")

# Bunnings store prices.
costs = {
  2400:13.8,
  2700:15.53,
  3000:17.25,
  3600:20.7,
  4200:24.15,
  4800:27.60}
cost_mm = costs[4800]/4800


supply = dict((l,1000) for l in costs)

p90x35 = {
    4800: 2,
    1260: 4,
    1410: 1,
    1130: 1}

# Note: these need to be sorted largest first.
parts = (
    + 4 * [415]
    + 4 * [822.5]
    + 2 * [315])
parts.sort(reverse=True)

store = Lengths(supply)
stock = Lengths(p90x35)
print(f'total available stock: {stock}\n')
print(f'parts needed: {fmtlens(parts)}')

# # Do a run using store stock.
# stock=store+stock
bms = Beams(stock)
for p in parts:
  bms.addcut(p)
print(bms)
# cost = sum(b.length*cost_mm for b in bms)
# print(f'cost=${cost:.2f}')
# print()
