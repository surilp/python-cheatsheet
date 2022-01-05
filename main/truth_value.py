'''
False
- None
- False
- 0
- 0.0
- 0j
- Decimal(0)
- Fraction(0,x)
- ''
- ()
- []
- {}
- set()
- range(0)
- Custom object by default true unless they overrride __bool__ --> return false or __len__ --> return 0
'''


print(bool([]))