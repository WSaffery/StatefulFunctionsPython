import copy

class stateFunc:
    def __init__(self, body):
        self.body = body
    
    def body_run(self, *args):
        self.body(self, *args)

class stateFuncE(stateFunc):
    def __init__(self, body, kattr):
        self.base_kattr = {}
        self.assign(kattr)
        super().__init__(body)
    
    def assign(self, kattr):
        self.base_kattr.update(copy.deepcopy(kattr))
        for k, v in kattr.items():
            setattr(self, k, v)
            
class stateFuncM(stateFuncE):
    def __init__(self, body, sources):
        self.base_kattr = {}
        for s in sources:
            self.assign(s)
        self.body = body
        
def check_dictlike(dictlike):
    try:
        dictlike.items()
        return True
    except:
        return False
    
class stateFuncI(stateFuncM):
    def __init__(self, body, sources):
        changed_sources = list(sources)
        first_source = sources[0]
        if hasattr(first_source, '__self__'):
            upper = first_source.__self__
            # print(upper)
            if not issubclass(type(upper),stateFunc):
                print("not")
                raise Exception("Invalid inheritence")
            else:
                changed_sources[0] = upper.base_kattr
        super().__init__(body, changed_sources)
            
    
def state_func(function):
    sf = stateFunc(function)
    return sf.body_run

def state_func_e(kattr):
    def decorator(function):
        sf_e = stateFuncE(function, kattr)
        return sf_e.body_run
    return decorator
    
def state_func_i(*sources):
    def decorator(function):
        sf_e = stateFuncI(function, sources)
        return sf_e.body_run
    return decorator
    

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