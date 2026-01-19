from fastapi import FastAPI, Query
from pydantic import BaseModel

from qrng import (
    generate_quantum_bits,
    generate_noisy_quantum_bits,
    generate_classical_bits,
)

from analysis import frequency_test, calculate_entropy

app = FastAPI(title="Quantum Randomness Service")


# =========================
# Health check
# =========================
@app.get("/health")
def health_check():
    return {"status": "QRNG service is running"}


# =========================
# Ideal quantum randomness
# =========================
@app.get("/random/ideal")
def get_ideal_quantum_randomness(bits: int = Query(8, ge=1, le=1024)):
    quantum_bits = generate_quantum_bits(bits)
    bit_string = "".join(quantum_bits)

    return {
        "type": "quantum",
        "mode": "ideal",
        "bits_requested": bits,
        "random_bits": bit_string
    }


# =========================
# Noisy quantum randomness
# =========================
@app.get("/random/noisy")
def get_noisy_quantum_randomness(
    bits: int = Query(8, ge=1, le=1024),
    noise: float = Query(0.1, ge=0.0, le=1.0)
):
    noisy_bits = generate_noisy_quantum_bits(bits, noise_strength=noise)
    bit_string = "".join(noisy_bits)

    return {
        "type": "quantum",
        "mode": "noisy",
        "noise_strength": noise,
        "bits_requested": bits,
        "random_bits": bit_string
    }


# =========================
# Classical randomness
# =========================
@app.get("/random/classical")
def get_classical_randomness(bits: int = Query(8, ge=1, le=1024)):
    classical_bits = generate_classical_bits(bits)
    bit_string = "".join(classical_bits)

    return {
        "type": "classical",
        "bits_requested": bits,
        "random_bits": bit_string
    }


# =========================
# Analysis endpoint
# =========================
class AnalyzeRequest(BaseModel):
    bit_string: str


@app.post("/analyze")
def analyze_randomness(request: AnalyzeRequest):
    bits = list(request.bit_string)

    zeros, ones = frequency_test(bits)
    entropy = calculate_entropy(bits)

    return {
        "length": len(bits),
        "zeros": zeros,
        "ones": ones,
        "entropy": round(entropy, 4)
    }
