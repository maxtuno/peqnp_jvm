package com.peqnp;

import org.python.util.PythonInterpreter;

public class FactoringInterop {

    public static void main(String[] args) {
        PythonInterpreter py = new PythonInterpreter();
        py.set("rsa", 3007);
        py.execfile("py/factoring_interop.py");
        System.out.println(py.get("p"));
        System.out.println(py.get("q"));
    }
}
