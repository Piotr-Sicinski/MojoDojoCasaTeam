from qiskit import QuantumCircuit, Aer, transpile, execute
from qiskit.tools.monitor import job_monitor
from qiskit import IBMQ
from dotenv import load_dotenv
import os

load_dotenv()
API = False
backend = backend = Aer.get_backend('qasm_simulator')

if os.getenv('IBM_TOKEN') is not None:
    IBMQ.save_account(os.getenv('IBM_TOKEN'))
    IBMQ.load_account()
    provider = IBMQ.get_provider('ibm-q')
    backend = provider.get_backend('ibm_brisbane')
    API = True
    print("Using real quantum computer")
else:
    print("Using simulator")

def count_neighbors(board, x, y):
    """Count the number of live neighbors around a cell."""
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            if 0 <= x + i < board.shape[0] and 0 <= y + j < board.shape[1]:
                count += board[x + i, y + j]
    return count

def digital_alive(board, x, y):
    """Returns whether a cell is alive in the next generation."""
    return (board[x, y] and count_neighbors(board, x, y) in [2, 3]) or (
        not board[x, y] and count_neighbors(board, x, y) == 3
    )

def quantum_alive(board, x, y):
    """Returns whether a cell is alive in the next generation."""
    """Returns whether a cell is alive in the next generation."""
    # prepare neighbors list 
    neighbors = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                neighbors.append(0)
                continue
            if 0 <= x + i < board.shape[0] and 0 <= y + j < board.shape[1]:
                neighbors.append(board[x + i, y + j])

    while(len(neighbors) < 8):
        neighbors.append(0)

    qc = QuantumCircuit(11, 1)
    qc.x(0) if board[x][y] else qc.id(0)
    for i in range(1, 9):
        qc.x(i) if neighbors[i - 1] else qc.id(i) 

    qc.h(0)

    for i in range(0, 9):
        qc.cx(i, 9)  

    for i in range(0, 9):
        for j in range(i + 1, min(i +3, 9)):
            qc.ccx(i, j, 10)

    qc.h(7)
    qc.cx(7, 8)

    qc.measure(10, 0)

    if API:
        job = execute(qc, backend, shots=100)
        job_monitor(job)
        result = job.result()
    else:
        result = backend.run(transpile(qc, backend)).result()

    ones = result.get_counts().get('1', 0)
    zeros = result.get_counts().get('0', 0)

    return int(ones / (ones + zeros))

