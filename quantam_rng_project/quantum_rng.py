import os

from qrng import (
    generate_quantum_bits,
    generate_noisy_quantum_bits,
    generate_classical_bits,
)

from analysis import (
    frequency_test,
    calculate_entropy,
    runs_test,
)


def main():
    num_bits = 100

    # =========================
    # Generate random bits
    # =========================
    quantum_bits = generate_quantum_bits(num_bits)
    noisy_quantum_bits = generate_noisy_quantum_bits(num_bits, noise_strength=0.1)
    classical_bits = generate_classical_bits(num_bits)

    # =========================
    # Save ideal quantum bits
    # =========================
    quantum_bits_file = os.path.join(os.getcwd(), "quantum_bits.txt")
    with open(quantum_bits_file, "w") as f:
        for bit in quantum_bits:
            f.write(bit + "\n")

    print(f"Generated {num_bits} ideal quantum random bits.")
    print(f"Ideal quantum bits saved to: {quantum_bits_file}")

    # =========================
    # Preview bits
    # =========================
    print("\nFirst 20 Ideal Quantum bits:")
    print(quantum_bits[:20])

    print("\nFirst 20 Noisy Quantum bits:")
    print(noisy_quantum_bits[:20])

    print("\nFirst 20 Classical bits:")
    print(classical_bits[:20])

    # =========================
    # Frequency test
    # =========================
    q_zeros, q_ones = frequency_test(quantum_bits)
    nq_zeros, nq_ones = frequency_test(noisy_quantum_bits)
    c_zeros, c_ones = frequency_test(classical_bits)

    print("\nFrequency Test Results:")
    print(f"Ideal Quantum   -> 0s: {q_zeros}, 1s: {q_ones}")
    print(f"Noisy Quantum   -> 0s: {nq_zeros}, 1s: {nq_ones}")
    print(f"Classical       -> 0s: {c_zeros}, 1s: {c_ones}")

    # =========================
    # Entropy calculation
    # =========================
    q_entropy = calculate_entropy(quantum_bits)
    nq_entropy = calculate_entropy(noisy_quantum_bits)
    c_entropy = calculate_entropy(classical_bits)

    print("\nEntropy Results:")
    print(f"Ideal Quantum entropy   : {q_entropy:.4f}")
    print(f"Noisy Quantum entropy   : {nq_entropy:.4f}")
    print(f"Classical entropy       : {c_entropy:.4f}")

    # =========================
    # Runs test
    # =========================
    q_runs = runs_test(quantum_bits)
    nq_runs = runs_test(noisy_quantum_bits)
    c_runs = runs_test(classical_bits)

    print("\nRuns Test Results:")
    print(f"Ideal Quantum runs   : {q_runs}")
    print(f"Noisy Quantum runs   : {nq_runs}")
    print(f"Classical runs       : {c_runs}")

    # =========================
    # Save ideal vs noisy analysis
    # =========================
    analysis_file = os.path.join(os.getcwd(), "ideal_vs_noisy_analysis.txt")

    with open(analysis_file, "w") as f:
        f.write("Ideal vs Noisy Quantum Randomness Analysis\n")
        f.write("=========================================\n\n")

        f.write(f"Number of bits: {num_bits}\n\n")

        f.write("Frequency Test:\n")
        f.write(f"Ideal Quantum   -> 0s: {q_zeros}, 1s: {q_ones}\n")
        f.write(f"Noisy Quantum   -> 0s: {nq_zeros}, 1s: {nq_ones}\n")
        f.write(f"Classical       -> 0s: {c_zeros}, 1s: {c_ones}\n\n")

        f.write("Entropy:\n")
        f.write(f"Ideal Quantum entropy   : {q_entropy:.4f}\n")
        f.write(f"Noisy Quantum entropy   : {nq_entropy:.4f}\n")
        f.write(f"Classical entropy       : {c_entropy:.4f}\n\n")

        f.write("Runs Test:\n")
        f.write(f"Ideal Quantum runs   : {q_runs}\n")
        f.write(f"Noisy Quantum runs   : {nq_runs}\n")
        f.write(f"Classical runs       : {c_runs}\n")

    print(f"\nIdeal vs noisy analysis saved to: {analysis_file}")


if __name__ == "__main__":
    main()
