import cirq
from iqft import iqft
from cirq.circuits import InsertStrategy

def qpe(t, control, target, circuit, CU):
    
    # Apply Hadamard to the control qubits
    circuit.append(cirq.H.on_each(control))
    
    # Apply CU gates
    for j in range(t):
        # Obtain the power of CU gate 
        CUj = CU**(2**j)
        # Apply CUj gate where t-j-1 is the control
        circuit.append(CUj(control[t-j-1], *target), strategy = InsertStrategy.NEW)
        
    # Apply IQFT
    iqft(t, control, circuit)
