package com.peqnp;

import org.python.util.PythonInterpreter;

public class Factoring {

    public static void main(String[] args) {
        PythonInterpreter py = new PythonInterpreter();
        py.execfile("py/factoring.py");
    }
}
