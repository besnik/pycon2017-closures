# average closure - variant with list
def create_avg():
    items = []
    def add(num):
        items.append(num)
        print(sum(items)/len(items))
    return add

avg = create_avg()
avg(4) # 4.0
avg(5) # 4.5
avg(6) # 5.0

# counter closure - nonlocal
def counter():
    count = 0
    def inc_count():
        nonlocal count
        count += 1
        print("Called", count, "times")
    return inc_count

inc = counter()
inc() # Called 1 times
inc() # Called 2 times
inc() # Called 3 times

# average closure - nonlocal
def create_avg2():
    sum = 0
    count = 0
    def add(num):
        nonlocal sum
        nonlocal count
        sum += num
        count += 1
        print(sum/count)
    return add

avg = create_avg2()
avg(4)
avg(5)
avg(6)

# closure - lambda
l = [x for x in range(1,20)]

def filter1(l):
    limit = 5
    return list(filter(lambda item: item > limit, l))

def filter2(l):
    limit = 5
    return [y for y in l if y > limit]    

import dis

dis.dis(filter1)
print("-------")
dis.dis(filter2)

print("CODE INFO")
print(dis.code_info(filter2))

# more closures

def create_filter(threshold):
    def filter_it(iterable):
        return [x for x in iterable if x > threshold]
    return filter_it

t = (1,2,3,4,5,6,7)
f = create_filter(2)
print(f(t))
f = create_filter(5)
print(f(t))

def create_filter2(threshold):
    return lambda iterable: [x for x in iterable if x > threshold]

f = create_filter2(2)
print(f(t))
f = create_filter2(5)
print(f(t))

class Filter:
    
    def __init__(self, threshold):
        self.threshold = threshold
    
    def __call__(self, iterable):
        return [x for x in iterable if x > self.threshold]
        #print(list(filter(lambda x: x>self.treshold, iterable)))

    
fi = Filter(2)
print(fi(t))


