import math, sys, time
import pp

def isprime(n):
    if not isinstance(n, int):
        raise TypeError("argument is not int")
    if n < 2:
        return False
    if n == 2:
        return True
    max = int(math.ceil(math.sqrt(n)))
    i = 2
    while i <= max:
        if n % i == 0:
            return False
        i += 1
    return True

def sumprime(n):
    return sum([x for x in xrange(2, n) if isprime(x)])

ppservers = ('*',)

if len(sys.argv) > 1:
    ncpus = int(sys.argv[1])
    job_server = pp.Server(ncpus, ppservers=ppservers)
else:
    job_server =pp.Server(ppservers=ppservers)

print("Start ", job_server.get_ncpus(), " work")

job1 = job_server.submit(sumprime, (100, ), (isprime,), ("math",))

result = job1()

print("Sum below 100 is ", result)

start_time = time.time()

inputs = (100000, 100100, 100200, 100300, 100400, 100500, 100600, 100700)
jobs = [(input, job_server.submit(sum_primes,(input,), (isprime,), ("math",))) for input in inputs]
for input, job in jobs:
    print("Sum of primes below", input, "is", job())
 
print("Time elapsed: ", time.time() - start_time, "s")
job_server.print_stats()