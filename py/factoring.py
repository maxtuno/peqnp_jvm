import peqnp.cnf as cnf

rsa = 3007

cnf.begin(bits=rsa.bit_length(), key='factoring')
p = cnf.integer()
q = cnf.integer()
assert p * q == rsa
cnf.end({'p': p, 'q': q})

while cnf.satisfy(solver='java -jar blue.jar'):
    print(p, q)
