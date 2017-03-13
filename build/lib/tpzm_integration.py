"""Python 2 and 3 compatible"""
print('This program calculates the integral of input function from a to b')
print('by cutting it into many parts and calculating each area')
print('Program written by Zhang Huiyuan')
print('from Shanghai Guanghua Cambridge International School')
print('use integral_approx(a,b,N,func) to call function')
print('add+ subtract- multiply* divide/ power**')
print('Shortcut: xxxx=tpzm_integration.integral_approx')
print('then use xxxx to substitute the long name')
def integral_approx(a=1,b=2,N=1,func='1.0/x'):
    try:
        a=float(a)
        b=float(b)
        N=int(N)
        #Function to evaluate
        func
        iterate1=1
        total_area_1=0
        total_area_2=0
        while iterate1 <= N:
            #the trapezium way
            left_x=a+((b-a)*(iterate1-1)/N)
            right_x=a+((b-a)*iterate1/N)
            #print iterate1
            #print left_x,right_x
            x=left_x
            left_y=eval(func)
            x=right_x
            right_y=eval(func)
            delta_area_1=(right_x - left_x)*(left_y + right_y)/2
            total_area_1=total_area_1+delta_area_1
            #the rectangle way
            x=(left_x+right_x)/2
            y=eval(func)
            delta_area_2=(right_x - left_x)*y
            total_area_2=total_area_2+delta_area_2
            iterate1=iterate1+1
        return 'Trapezium way ',total_area_1,' Rectangle way ',total_area_2
    except ZeroDivisionError:
        return "ErrorM1 Division by Zero ERROR!"
    except NameError:
        return "ErrorM2 Don't use undefined variables!"
    except ValueError:
        return "ErrorM3 Don't use strings in first 3 inputs!"
