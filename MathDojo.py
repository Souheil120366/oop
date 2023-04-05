class MathDojo:
    def __init__(self):
        self.result =0
    def add(self, num, *args):
        self.result+=num
        for x in args:
            self.result+=x
        return self    
    def subtract(self, num, *args):
        self.result-=num
        for x in args:
            self.result-=x
        return self   
# create an instance:
md = MathDojo()
print(md.add(1).result)
print(md.add(1,2,3).result)
print(md.add(10,11,12,13).result)

print(md.subtract(1).result)
print(md.subtract(1,2,3).result)
print(md.subtract(10,11,12,13).result)
# to test:
x = md.add(2).add(2,5,1).subtract(3,2).result

print(x)	# should print 5
# run each of the methods a few more times and check the result!

