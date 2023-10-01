from qiskit import QuantumCircuit, Aer, transpile


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

    ## init circuit
    qc = QuantumCircuit(14, 1)
    qc.x(0) if board[x][y] else qc.id(0)
    for i in range(1, 9):
        qc.x(i) if board[x][y] else qc.id(i)

    """ 
        TODO:
        1. Do the addition of the neighbors
        2. Make a decision based on the result of the addition
        3. Measure the output qubit
    """

    # Random stuff for the time begin
    for i in range(1, 9):
        qc.ccx(0, i, 9)

    qc.measure(9, 0)
    result = (
        Aer.get_backend("qasm_simulator")
        .run(transpile(qc, Aer.get_backend("qasm_simulator")))
        .result()
    )

    ones = result.get_counts().get("1", 0)
    zeros = result.get_counts().get("0", 0)

    return ones > zeros

