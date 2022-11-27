# 
The repository contains Jupyter notebooks with detailed description of basic quantum protocols and algorithms, the mathematics, circuits and quantum programs using Python. It includes 6 notebooks in total:

 - 01_Quantum_Teleportation
 - 02_Superdense_Coding
 - 03_Quantum_Fourier_Transform
 - 04_Phase_Estimation
 - 05_Period_Finding
 - 06_Shors_Algorithm

The Python environment for these notebooks uses ***Python 3.8.10*** and ***pip 22.3.1*** for installing packages on a Linux machine. The notebooks were composed using Jupyter Notebook. More information on the extra modules and packages needed is provided at the end.

For the purposes of programming, I chose to use two frameworks, ***Qiskit*** from IBM and ***Cirq*** from Google to demonstrate how the two libraries can be used for quantum programming implementations through different syntax and use-cases.

### Note
Whether using Windows, macOS or Linux, it is recommended that you create a virtual environment for Python and install the required packages within it. In this way, you isolate your operating system from the new installations and prevent possible compatibility issues. Also, make sure that you install the Jupyter kernel, which can be used to run Jupyter commands inside the virtual environment.

## *Quantum Teleportation*
The first notebook describes one of the most stunning applications of quantum entanglement, the so-called quantum teleportation protocol. This application sets the pillars for future quantum communication systems, networks and cryptography. With entanglement, quantum information is received by physically sending classical information. Inside the notebook, you can find the math behind the protocol, as well as an implementation using IBM's ***qiskit*** module for quantum programming with circuits and results.

## *Superdense Coding*
Superdense coding is another application of quantum entanglement involving classical information compression and transmission by physically sending a quantum system. It is somehow the opposite of quantum teleportation. ***Qiskit*** is also used here and results are provided along with the cicuits.

## *Quantum Fourier Transform*
The *quantum Fourier transform* is the quantum analogue of the *discrete Fourier transform* used extendedly in modern science. However, the quantum version is not the same at all with the classical case, not even in its application. Τhe quantum Fourier transform is a lame duck by itself, but it serves as a crucial building block for designing other quantum algorithms.  In the notebook, one can find the mathematics behind the algorithm, the circuit and other information regarding complexity and applications. For the purpose of this, as well as for the rest of the notebooks, Google's ***cirq*** open source framework for programming quantum computers is utilized.

## *Phase Estimation*
As the name suggests, this algorithm can be used to estimate the phase (i.e eigenvalue) of an eigenvector of some unitary operator. It demonstrates an application of the *quantum Fourier transform* and accounts for one of the most important subroutines in many quantum algorithms including *period finding* and *Shor's algorithm*. Using ***cirq***, two examples are presented on how the algorithm estimates with high accuracy the phase of two different unitary operators, including *T*-gate.

## *Period Finding*
Period (or order) finding is a procedure to find the order of some integer involving modular arithmetic. It is one of the basic aspects in Number Theory, as well as a mechanism in which the factoring problem can be reduced. Also, a variety of cryptographic protocols rely on the order of some integer. The best classical algorithm for order finding is of exponential time. In quantum computing, the problem can be reduced to estimating the phase of a certain unitary operator and its eigenvector, as well as some classical processing with continued fractions, resulting in a polynomial size quantum circuit. Detailed analysis can be found inside the notebook.

## *Shor's Algorithm*
The last notebook demonstrates the well-known polynomial time quantum algorithm for the factoring problem, developed by Peter Shor in 1994. Starting from  the quantum Fourier transform to construct the phase estimation algorithm and the latter for order finding, Shor's algorithm takes advantage of some theorems of Number Theory and uses the aforementioned to design a process that threatens the future of today's most used cryptographic protocols.

### Packages

| Version Information | Package    | Version |
| ------------------- | ---------- | ------- |
| Qiskit Software     | Qiskit     | 0.39.0  |
|                     | Terra      | 0.22.0  |
|                     | Aer        | 0.11.0  |
|                     | Aqua       | 0.9.5   |
|                     | Ignis      | 0.7.1   |
| Cirq Software       | Cirq       | 1.0.0   |
| Other Software      | Matplotlib | 3.6.1   |
|                     | Numpy      | 1.23.4  |
