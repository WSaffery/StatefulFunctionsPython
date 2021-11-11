class stateFunc:
    def __init__(self, body):
        self.body = body
    
    def body_run(self, *args):
        self.body(self, *args)

class stateFuncE(stateFunc):
    def __init__(self, kattr, body):
        self.assign(kattr)
        super().__init__(body)
    
    def assign(self, kattr):
        for k, v in kattr.items():
            setattr(self, k, v)
            
    
def state_func(function):
        sf = stateFunc(function)
        return sf.body_run

def state_func_e(kattr):
    def decorator(function):
        sf_e = stateFuncE(kattr, function)
        return sf_e.body_run
    return decorator
    

@state_func
def test(this, a, b,c):
    try:
        this.count += 1
    except:
        this.count = 0
    print(a,b,c, this.count)
    
test("hi", "hello", "goodbye")
test("hi", "hello", "goodbye")
test("hi", "hello", "goodbye")

@state_func_e({"count":0})
def test2(this, a, b,c):
    this.count += 1 
    print(a,b,c, this.count)
    
test2("hi", "hello", "goodbye")
test2("hi", "hello", "goodbye")
test2("hi", "hello", "goodbye")