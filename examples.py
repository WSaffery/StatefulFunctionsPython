from state_func import *

@state_func
def test(this, a, b,c):
    try:
        this.count += 1
    except:
        this.count = 0
    print(a,b,c, this.count)
    
test("hi", "hello", "goodbye") # hi hello goodbye 0
test("hi", "hello", "goodbye") # hi hello goodbye 1
test("hi", "hello", "goodbye") # hi hello goodbye 2

@state_func_e({"count":0})
def test2(this, a, b,c):
    print(a,b,c, this.count)
    this.count += 1 
    
test2("hi", "hello", "goodbye") # hi hello goodbye 0
test2("hi", "hello", "goodbye") # hi hello goodbye 1
test2("hi", "hello", "goodbye") # hi hello goodbye 2

@state_func_i(test2)
def test3(this, a, b,c):
    print(a,b,c, this.count)
    this.count += 1 
    
test3("hi", "hello", "goodbye") # hi hello goodbye 0
test3("hi", "hello", "goodbye") # hi hello goodbye 1
test3("hi", "hello", "goodbye") # hi hello goodbye 2