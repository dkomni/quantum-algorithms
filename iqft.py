import cirq
from cirq import H, SWAP, CZPowGate
from cirq.circuits import InsertStrategy

def iqft(n, qubits, circuit):
    
    # swap the qubits
    for q in range(n//2):
        circuit.append(SWAP(qubits[q], qubits[n-q-1]), strategy=InsertStrategy.NEW)
        
    # follow inverse procedure of QFT
    for q in range(n-1, -1, -1):
        k = n-q
        for i in range(n-1, q, -1):
            CRk = CZPowGate(exponent=-2/(2**k))
            circuit.append(CRk(qubits[i], qubits[q]), strategy = InsertStrategy.NEW)
            k -= 1
            
        #Apply Hadamard to the qubit
        circuit.append(H(qubits[q]),strategy=InsertStrategy.NEW)
