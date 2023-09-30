import os
import pytest
from qiskit import IBMQ
from dotenv import load_dotenv

load_dotenv()

# Load the IBM Quantum API Token from environment variable.
IBM_QUANTUM_API_TOKEN = os.getenv("IBM_TOKEN")

def test_ibm_quantum_api():
    try:
        # Attempt to connect to IBM Quantum API.
        IBMQ.save_account(IBM_QUANTUM_API_TOKEN, overwrite=True)
        provider = IBMQ.load_account()
        # Check if there are any available backends.
        assert provider.backends()
    except Exception as e:
        pytest.fail(f"Failed to connect to IBM Quantum API: {str(e)}, refer to README.md.")

