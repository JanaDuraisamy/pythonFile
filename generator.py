def fib():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b
for f in fib():
    if f>=1000:
        break
    print(f)

# def yrange(n):
#     i=0
#     while i<n:
#         yield i
#         i+=1
#     print(i)
# yrange(7)
#
