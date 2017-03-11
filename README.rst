This program is Python 2 and 3 friendly. Link to PyPi site:

https://pypi.python.org/pypi/tpzm_integration

You can install it with Pip, or with setup.py install.

The program defines a function. Use from tpzm_integration import tpzm_approx

After the chevron >>> prompt pops up after the blue words, after importing the function,

call function by tpzm_approx(a,b,N,func)

(a,b,N are values, func is the text of your function).

"a" is the lower boundary while "b" is the upper boundary. 

They can both be Floating Point numbers and should be both positive or both negative.

"N" is the number of sections. Must be a positive integer.

"func" is the text of the function. For example '(x*x+2*x+1)/(x-1)' or '1/x'

The program returns the value obtained. 

If there is a division by zero error, it will return 'Cannot divide things by zero!!'

If you have any problems or suggestions please email to zhanghuiyuanses@126.com
