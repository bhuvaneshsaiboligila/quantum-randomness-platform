from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit_aer.noise import NoiseModel, depolarizing_error
import random


def generate_quantum_bits(num_bits):
    """
    Generate ideal (noiseless) quantum random bits.
    """
    simulator = AerSimulator()
    bits = []

    for _ in range(num_bits):
        qc = QuantumCircuit(1, 1)
        qc.h(0)
        qc.measure(0, 0)

        job = simulator.run(qc, shots=1)
        result = job.result()
        counts = result.get_counts()

        bit = list(counts.keys())[0]
        bits.append(bit)

    return bits


def generate_noisy_quantum_bits(num_bits, noise_strength=0.1):
    """
    Generate quantum random bits using a noisy simulator.
    noise_strength controls the depolarizing noise level (0.0 to 1.0).
    """
    noise_model = NoiseModel()
    error = depolarizing_error(noise_strength, 1)
    noise_model.add_all_qubit_quantum_error(error, ["h"])

    simulator = AerSimulator(noise_model=noise_model)
    bits = []

    for _ in range(num_bits):
        qc = QuantumCircuit(1, 1)
        qc.h(0)
        qc.measure(0, 0)

        job = simulator.run(qc, shots=1)
        result = job.result()
        counts = result.get_counts()

        bit = list(counts.keys())[0]
        bits.append(bit)

    return bits


def generate_classical_bits(num_bits):
    """
    Generate classical random bits using Python's random module.
    """
    bits = []
    for _ in range(num_bits):
        bit = random.choice(["0", "1"])
        bits.append(bit)
    return bits
