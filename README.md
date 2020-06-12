# Instructions

##### Install Standard Jython on [root]/jython

    java -jar lib/jython-installer-2.7.2.jar

    jython/bin/jython -m pip install PEQNP==2.1.16 --install-option=no-solver --upgrade
    
    Add reference to jython/jython.jar
    

# BLUE
 A Powerful  SAT Solver for Java https://github.com/maxtuno/blue
 
 very simple:
 
 java -jar -Xmx4g blue.jar file.cnf
 
Blue is based on Minisat many thanks to Niklas Een, Niklas Sorensson for this great solver.

MIT License

Copyright (c) 2019 Oscar Riveros [oscar.riveros@peqnp.science]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
