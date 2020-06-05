import peqnp.cnf as cnf

# rsa set from java

cnf.begin(bits=rsa.bit_length(), key='factoring_interop')
p = cnf.integer()
q = cnf.integer()
assert p * q == rsa
cnf.end({'p': p, 'q': q})

cnf.satisfy(solver='java -jar -Xmx4g blue.jar')

print(p, q)