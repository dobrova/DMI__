Python 2.7.6 (default, Jun 22 2015, 17:58:13) 
[GCC 4.8.2] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> vars ()
{'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__doc__': None, '__package__': None}
>>> type(vars())
<type 'dict'>
>>> __builtins__
<module '__builtin__' (built-in)>
>>> help
Type help() for interactive help, or help(object) for help about object.
>>> help()

Welcome to Python 2.7!  This is the online help utility.

If this is your first time using Python, you should definitely check out
the tutorial on the Internet at http://docs.python.org/2.7/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, or topics, type "modules",
"keywords", or "topics".  Each module also comes with a one-line summary
of what it does; to list the modules whose summaries contain a given word
such as "spam", type "modules spam".

help> help(__builtin__)
no Python documentation found for 'help(__builtin__)'

help> __builtins__
no Python documentation found for '__builtins__'

help> 

You are now leaving help and returning to the Python interpreter.
If you want to ask for help on a particular object directly from the
interpreter, you can type "help(object)".  Executing "help('string')"
has the same effect as typing a particular string at the help> prompt.
>>> __builtins__.inpuit

Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    __builtins__.inpuit
AttributeError: 'module' object has no attribute 'inpuit'
>>> __builtins__.input
<built-in function input>
>>> print __builtins__.input.__doc__
input([prompt]) -> value

Equivalent to eval(raw_input(prompt)).
>>> sin(2)

Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    sin(2)
NameError: name 'sin' is not defined
>>> math.sin(2)

Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    math.sin(2)
NameError: name 'math' is not defined
>>> help(sin)

Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    help(sin)
NameError: name 'sin' is not defined
>>> import math
>>> math.sin(x)

Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    math.sin(x)
NameError: name 'x' is not defined
>>> math.sin(2)
0.9092974268256817
>>> math.cos(4)
-0.6536436208636119
>>> math.cosh(15)
1634508.6862362083
>>> math.atan(2)
1.1071487177940904
>>> math.degrees(math.sin(2))
52.098904879217365
>>> import cmath
>>> cmath.sin(2)
(0.9092974268256817-0j)
>>> cmath.cos(4)
(-0.6536436208636119+0j)
>>> cmath.cosh(15)
(1634508.6862362083+0j)
>>> cmath.atan(2)
(1.1071487177940904+0j)
>>> cmath.degrees(cmath.sin(2))

Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    cmath.degrees(cmath.sin(2))
AttributeError: 'module' object has no attribute 'degrees'
>>> help(cmath)
Help on built-in module cmath:

NAME
    cmath

FILE
    (built-in)

DESCRIPTION
    This module is always available. It provides access to mathematical
    functions for complex numbers.

FUNCTIONS
    acos(...)
        acos(x)
        
        Return the arc cosine of x.
    
    acosh(...)
        acosh(x)
        
        Return the hyperbolic arccosine of x.
    
    asin(...)
        asin(x)
        
        Return the arc sine of x.
    
    asinh(...)
        asinh(x)
        
        Return the hyperbolic arc sine of x.
    
    atan(...)
        atan(x)
        
        Return the arc tangent of x.
    
    atanh(...)
        atanh(x)
        
        Return the hyperbolic arc tangent of x.
    
    cos(...)
        cos(x)
        
        Return the cosine of x.
    
    cosh(...)
        cosh(x)
        
        Return the hyperbolic cosine of x.
    
    exp(...)
        exp(x)
        
        Return the exponential value e**x.
    
    isinf(...)
        isinf(z) -> bool
        Checks if the real or imaginary part of z is infinite.
    
    isnan(...)
        isnan(z) -> bool
        Checks if the real or imaginary part of z not a number (NaN)
    
    log(...)
        log(x[, base]) -> the logarithm of x to the given base.
        If the base not specified, returns the natural logarithm (base e) of x.
    
    log10(...)
        log10(x)
        
        Return the base-10 logarithm of x.
    
    phase(...)
        phase(z) -> float
        
        Return argument, also known as the phase angle, of a complex.
    
    polar(...)
        polar(z) -> r: float, phi: float
        
        Convert a complex from rectangular coordinates to polar coordinates. r is
        the distance from 0 and phi the phase angle.
    
    rect(...)
        rect(r, phi) -> z: complex
        
        Convert from polar coordinates to rectangular coordinates.
    
    sin(...)
        sin(x)
        
        Return the sine of x.
    
    sinh(...)
        sinh(x)
        
        Return the hyperbolic sine of x.
    
    sqrt(...)
        sqrt(x)
        
        Return the square root of x.
    
    tan(...)
        tan(x)
        
        Return the tangent of x.
    
    tanh(...)
        tanh(x)
        
        Return the hyperbolic tangent of x.

DATA
    e = 2.718281828459045
    pi = 3.141592653589793


>>> math.acos.__class__
<type 'builtin_function_or_method'>
>>> 
