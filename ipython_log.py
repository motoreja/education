# IPython log file

bin(1234567)
#[Out]# '0b100101101011010000111'
0b00110011 | 0b01000000
#[Out]# 115
bin(115)
#[Out]# '0b1110011'
a = 99
-10 < a < 100
#[Out]# True
42 << 34
#[Out]# 721554505728
int(13.8)
#[Out]# 13
a = 13.888
a.__ceil__()
#[Out]# 14
a.__floor__()
#[Out]# 13
a.round(2)
dir(a)
#[Out]# ['__abs__',
#[Out]#  '__add__',
#[Out]#  '__bool__',
#[Out]#  '__ceil__',
#[Out]#  '__class__',
#[Out]#  '__delattr__',
#[Out]#  '__dir__',
#[Out]#  '__divmod__',
#[Out]#  '__doc__',
#[Out]#  '__eq__',
#[Out]#  '__float__',
#[Out]#  '__floor__',
#[Out]#  '__floordiv__',
#[Out]#  '__format__',
#[Out]#  '__ge__',
#[Out]#  '__getattribute__',
#[Out]#  '__getformat__',
#[Out]#  '__getnewargs__',
#[Out]#  '__getstate__',
#[Out]#  '__gt__',
#[Out]#  '__hash__',
#[Out]#  '__init__',
#[Out]#  '__init_subclass__',
#[Out]#  '__int__',
#[Out]#  '__le__',
#[Out]#  '__lt__',
#[Out]#  '__mod__',
#[Out]#  '__mul__',
#[Out]#  '__ne__',
#[Out]#  '__neg__',
#[Out]#  '__new__',
#[Out]#  '__pos__',
#[Out]#  '__pow__',
#[Out]#  '__radd__',
#[Out]#  '__rdivmod__',
#[Out]#  '__reduce__',
#[Out]#  '__reduce_ex__',
#[Out]#  '__repr__',
#[Out]#  '__rfloordiv__',
#[Out]#  '__rmod__',
#[Out]#  '__rmul__',
#[Out]#  '__round__',
#[Out]#  '__rpow__',
#[Out]#  '__rsub__',
#[Out]#  '__rtruediv__',
#[Out]#  '__setattr__',
#[Out]#  '__sizeof__',
#[Out]#  '__str__',
#[Out]#  '__sub__',
#[Out]#  '__subclasshook__',
#[Out]#  '__truediv__',
#[Out]#  '__trunc__',
#[Out]#  'as_integer_ratio',
#[Out]#  'conjugate',
#[Out]#  'fromhex',
#[Out]#  'hex',
#[Out]#  'imag',
#[Out]#  'is_integer',
#[Out]#  'real']
round(a,2)
#[Out]# 13.89
13.444 % 1
#[Out]# 0.44400000000000084
a = 13.444
a - a % 1
#[Out]# 13.0
int(a)
#[Out]# 13
a = 13.888
int(0.888)
#[Out]# 0
a + (1 - a % 1)
#[Out]# 14.0
int(a) + (a % 1)/(1 - a % 1)
#[Out]# 20.92857142857142
int(a) + int((a % 1)/(1 - a % 1))
#[Out]# 20
int(a) + int(((a % 1)/(1 - a % 1))>1)
#[Out]# 14
a = 13.444
int(a) + int(((a % 1)/(1 - a % 1))>1)
#[Out]# 13
int(a) + int((a % 1) >= 0.5)
#[Out]# 13
a = 13.888
int(a) + int((a % 1) >= 0.5)
#[Out]# 14
