def my_generator():
    for i in range(3500):
        yield i
        
gen = my_generator()
for j in gen:
    print(j)
            