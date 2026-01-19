# Quantum Randomness Platform (QRNG)

## Overview
This project implements a **Quantum Random Number Generator (QRNG)** using **Qiskit** and Python.
It demonstrates how quantum mechanics can be used to generate randomness and compares:

- Ideal (noiseless) quantum randomness
- Noisy (hardware-like) quantum randomness
- Classical pseudo-randomness

The project also evaluates randomness quality using statistical tests and visualizations.

---

## Key Features
- Quantum random bit generation using superposition
- Classical random number generation for comparison
- Noisy quantum simulator using depolarizing noise models
- Statistical analysis of randomness:
  - Frequency test
  - Shannon entropy
  - Runs test
- Visual comparison using plots
- Clean, modular, and professional project structure

---

## Technologies Used
- Python 3.11
- Qiskit
- Qiskit Aer Simulator
- Matplotlib
- PyCharm
- Virtual Environment (venv)

---

## Project Structure

quantum_rng_project/
│
├── quantum_rng.py # Main pipeline (ideal vs noisy vs classical)
├── qrng.py # Random bit generators
├── analysis.py # Statistical analysis functions
├── noise_demo.py # Noise simulator experiments
├── quantum_bits.txt # Generated quantum bits
├── analysis_results.txt # Classical vs quantum analysis
├── ideal_vs_noisy_analysis.txt # Ideal vs noisy quantum comparison
└── README.md # Project documentation


---

## How It Works
1. A single qubit is placed into superposition using a Hadamard gate
2. The qubit is measured to produce a random bit
3. This process is repeated to generate bitstreams
4. A noisy simulator introduces realistic quantum errors
5. Statistical tests evaluate randomness quality
6. Results are saved and visualized

---

## How to Run the Project
1. Open the project in **PyCharm**
2. Activate the virtual environment
3. Run the main file:
4. Optional: run noise experiments using:

---

## Example Analysis
- Ideal quantum entropy ≈ 1.0
- Noisy quantum entropy is lower due to hardware-like errors
- Classical randomness varies depending on algorithm behavior
- Noise introduces measurable bias and pattern degradation

---

## Why This Project Matters
This project demonstrates:
- Practical quantum computing using Qiskit
- Understanding of quantum noise and hardware limitations
- Realistic comparison between quantum and classical randomness
- Clean engineering practices and reproducible results

---

## Future Improvements
- Run experiments on real IBM Quantum hardware
- Add additional randomness tests (NIST suite)
- Scale experiments to 100,000+ bits
- Save plots automatically as image files
- Convert analysis into a formal report or paper

---
## QRNG Service (API)

This project also provides a Quantum Random Number Generator as a REST API using FastAPI.

Available endpoints:
- `/random/ideal` – Ideal quantum randomness
- `/random/noisy` – Hardware-like noisy quantum randomness
- `/random/classical` – Classical randomness
- `/analyze` – Randomness quality analysis (entropy, frequency)

Interactive API documentation is available at `/docs` when the service is running.

## Author
Boligila Bhuvanesh sai
Quantum Computing Project


