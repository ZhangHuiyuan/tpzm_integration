"""Python 2 and 3 compatible"""
print('This program calculates the integral of input function from a to b')
print('by cutting it into many parts and calculating each area')
print('Program written by Zhang Huiyuan')
print('from Shanghai Guanghua Cambridge International School')
print('use tpzm_approx(a,b,N,func) to call function')
print('add+ subtract- multiply* divide/ power**')
print('Shortcut: xxxx=tpzm_integration.tpzm_approx')
print('then use xxxx to substitute the long name')
def tpzm_approx(a=1,b=2,N=1,func='1.0/x'):
    try:
        a=float(a)
        b=float(b)
        N=int(N)
        #Function to evaluate
        func
        iterate1=1
        total_area=0
        while iterate1 <= N:
            left_x=a+((b-a)*(iterate1-1)/N)
            right_x=a+((b-a)*iterate1/N)
            #print iterate1
            #print left_x,right_x
            x=left_x
            left_y=eval(func)
            x=right_x
            right_y=eval(func)
            delta_area=(right_x - left_x)*(left_y + right_y)/2
            total_area=total_area+delta_area
            iterate1=iterate1+1
        return total_area
    except ZeroDivisionError:
        return 'Cannot divide things by zero!!'
