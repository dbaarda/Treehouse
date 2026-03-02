#!/usr/bin/python3
"""
Convert between metric and imperial standard sizes.

Standard metric sizes are always just a float in mm.

Standard imperial sizes are in one of three different forms; 

* <inch> - the int number of whole inches.
* (<num>,<den>) - the int num/den fraction of an inch.
* (<inch>,<num>,<den>) - the int inches and num/den fraction of inches.

"""
from math import *


# Constant for converting inches to mm.
I2MM=25.4
# tuple of all the imperial standard denominators.
IMPD=tuple(2**i for i in range(7))
# tuple of all the metric standard sizes.
STDM=(1.6,2.0,2.5,3.0,3.5,4.0,5.0,6.0,8.0,10.0,12.0,14.0,16.0,18.0,20.0,22.0,24.0,27.0,30.0)
# tuple of all the imperial standard sizes.
STDI=((1,8),(3,16),(1,4),(5,16),(3,8),(7/16),(1,2),(9,16),(5,8),(3,4),(7,8),1,(1,1,4))

def mm2inch(mm):
  """Convert mm float into float inches."""
  return mm/I2MM

def inch2mm(i):
  """Convert float inches into float mm."""
  return i*I2MM

def _inch2fract(i):
  """ Convert a float inch into an imperial (n, d) fraction."""
  # Note this returns n>=d for values i>=1.
  n0,d0,e0=0,0,inf
  for d in IMPD:
    n = round(i*d)
    e = abs(i - n/d)
    if e < e0:
      n0,d0,e0 = n,d,e
  return n0,d0

def inch2imp(i):
  """Convert float inches into imperial i, (n,d), or (i, n, d)."""
  n,d = _inch2fract(i)
  if d == 1:
    return n
  elif n < d:
    return n,d
  else:
    i,n = divmod(n,d)
    return i,n,d

def imp2inch(imp):
  """Convert float or imp fraction inches into float inches."""
  if isinstance(imp,float):
    return imp
  if isinstance(imp,int):
    return float(imp)
  elif len(imp) == 2:
    n,d = imp
    return n/d
  elif len(imp) == 3:
    i,n,d = imp
    return i + n/d
  else:
    raise TypeError(imp)

def imp2stdi(imp):
  """Convert float or imp fraction inches into closest standard imperial."""
  i = imp2inch(imp)
  imp0,e0 = 0,inf
  for imp in STDI:
    e = abs(i - imp2inch(imp))
    if e < e0:
      imp0,e0 = imp,e
  return imp0

def mm2stdm(mm):
  """Convert float mm into closest standard metric."""
  met0,e0 = 0,inf
  for met in STDM:
    e = abs(mm - met)
    if e < e0:
      met0,e0 = met,e
  return met0

def mm2imp(mm):
  """Convert float mm into imperial."""
  return inch2imp(mm2inch(mm))

def imp2mm(imp):
  """Convert imperial to float mm."""
  return inch2mm(imp2inch(imp))

def fmtmm(mm):
  """Format a float mm into a string."""
  return f'{mm:.1f}mm'

def fmtinch(i):
  """Format a float inch or imp fraction into a decimal inch string."""
  i= imp2inch(i)
  return f'{i:>.3f}"'

def fmtimp(imp):
  """Format either a float inch or imp fraction into a string."""
  if isinstance(imp, float):
    imp = inch2imp(imp)
  if isinstance(imp,int):
    return f'{imp}"'
  elif len(imp) == 2:
    n,d = imp
    return f'{n}/{d}"'
  elif len(imp) == 3:
    i,n,d = imp
    return f'{i}-{n}/{d}"'
  else:
    raise TypeError(imp)

def fmtmet(mm):
  """Format a float mm into the closest metric standard."""
  met=mm2stdm(mm)
  return f'M{met:g}'

def stdm2stdi(mm):
  """Convert metric to imperial standard or None if not closest."""
  stdm = mm2stdm(mm)
  stdi = imp2stdi(mm2inch(stdm))
  if mm2stdm(imp2mm(stdi)) == stdm:
    return stdi
  
def stdi2stdm(imp):
  """Convert imperial to metric standard or None if not closest."""
  stdi = imp2stdi(imp)
  stdm = mm2stdm(imp2mm(stdi))
  if imp2stdi(mm2inch(stdm)) == stdi:
    return stdm

for mm in STDM:
  i = mm2inch(mm)
  stdi=stdm2stdi(mm)
  print(f'{fmtmet(mm):<4} {fmtmm(mm):>6} {fmtinch(i):6} {fmtimp(i):>8} {fmtimp(stdi) if stdi else "":>8}')
  
print()

for imp in STDI:
  mm = imp2mm(imp)
  stdm = stdi2stdm(imp)
  print(f'{fmtimp(imp):8} {fmtinch(imp):6} {fmtmm(mm):>6} {fmtmet(stdm) if stdm else "":4}')
