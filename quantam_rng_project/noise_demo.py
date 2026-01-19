from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit_aer.noise import NoiseModel, depolarizing_error
import math
import matplotlib.pyplot as plt


def run_circuit(simulator, shots=1000):
    qc = QuantumCircuit(1, 1)
    qc.h(0)
    qc.measure(0, 0)

    job = simulator.run(qc, shots=shots)
    result = job.result()
    return result.get_counts()


def frequency_from_counts(counts):
    zeros = counts.get("0", 0)
    ones = counts.get("1", 0)
    return zeros, ones


def entropy_from_counts(counts):
    total = sum(counts.values())
    entropy = 0.0

    for count in counts.values():
        if count == 0:
            continue
        p = count / total
        entropy -= p * math.log2(p)

    return entropy


def main():
    shots = 1000

    # -----------------------
    # Ideal simulator
    # -----------------------
    ideal_simulator = AerSimulator()
    ideal_counts = run_circuit(ideal_simulator, shots)

    # -----------------------
    # Noisy simulator
    # -----------------------
    noise_model = NoiseModel()
    error = depolarizing_error(0.1, 1)  # 10% noise
    noise_model.add_all_qubit_quantum_error(error, ["h"])

    noisy_simulator = AerSimulator(noise_model=noise_model)
    noisy_counts = run_circuit(noisy_simulator, shots)

    # -----------------------
    # Frequency comparison
    # -----------------------
    ideal_zeros, ideal_ones = frequency_from_counts(ideal_counts)
    noisy_zeros, noisy_ones = frequency_from_counts(noisy_counts)

    print("Frequency Comparison:")
    print(f"Ideal -> 0s: {ideal_zeros}, 1s: {ideal_ones}")
    print(f"Noisy -> 0s: {noisy_zeros}, 1s: {noisy_ones}")

    # -----------------------
    # Entropy comparison
    # -----------------------
    ideal_entropy = entropy_from_counts(ideal_counts)
    noisy_entropy = entropy_from_counts(noisy_counts)

    print("\nEntropy Comparison:")
    print(f"Ideal entropy : {ideal_entropy:.4f}")
    print(f"Noisy entropy : {noisy_entropy:.4f}")

    # -----------------------
    # Plot distributions
    # -----------------------
    labels = ["0", "1"]
    ideal_values = [ideal_zeros, ideal_ones]
    noisy_values = [noisy_zeros, noisy_ones]

    x = range(len(labels))

    plt.figure()
    plt.bar(x, ideal_values)
    plt.bar(x, noisy_values, bottom=ideal_values)
    plt.xticks(x, labels)
    plt.xlabel("Measurement Outcome")
    plt.ylabel("Counts")
    plt.title("Ideal vs Noisy Quantum Measurement Distribution")
    plt.show()


if __name__ == "__main__":
    main()
