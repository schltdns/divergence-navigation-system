#!/usr/bin/env python3
"""
calc_delta_div.py

Calculate pairwise divergence (Δdiv) between model responses.
Δdiv = 0.5 * (1 - Jaccard) + 0.5 * (1 - Cosine)

Usage:
    python calc_delta_div.py

Expects a file '03_outputs/raw_responses.json' with the following structure:
{
  "prompt": "...",
  "responses": [
    {"model": "ModelName", "text": "response text"},
    ...
  ]
}
"""

import json
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

def jaccard_similarity(text1: str, text2: str) -> float:
    """Compute Jaccard similarity between two texts (token overlap)."""
    set1 = set(text1.lower().split())
    set2 = set(text2.lower().split())
    if not set1 or not set2:
        return 0.0
    return len(set1 & set2) / len(set1 | set2)

def calculate_delta_div(responses: list) -> float:
    """
    Calculate average pairwise Δdiv across all responses.
    
    Args:
        responses: List of text strings (each from a different model)
    
    Returns:
        Average Δdiv (float)
    """
    if len(responses) < 2:
        return 0.0
    
    # Load embedding model
    model = SentenceTransformer('all-MiniLM-L6-v2')
    embeddings = model.encode(responses)
    
    n = len(responses)
    total_div = 0.0
    pairs = 0
    
    for i in range(n):
        for j in range(i + 1, n):
            # Cosine similarity
            cos_sim = cosine_similarity([embeddings[i]], [embeddings[j]])[0][0]
            # Jaccard similarity
            jac_sim = jaccard_similarity(responses[i], responses[j])
            # Pairwise divergence
            delta_pair = 0.5 * (1 - jac_sim) + 0.5 * (1 - cos_sim)
            total_div += delta_pair
            pairs += 1
    
    return total_div / pairs if pairs > 0 else 0.0

def main():
    # Load response data
    try:
        with open("03_outputs/raw_responses.json", "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        print("Error: 03_outputs/raw_responses.json not found.")
        return
    
    responses = [item["text"] for item in data.get("responses", [])]
    if not responses:
        print("Error: No responses found in JSON.")
        return
    
    delta = calculate_delta_div(responses)
    
    print(f"Δdiv = {delta:.4f}")
    
    # Classification
    if delta < 0.2:
        print("Classification: Convergence – generalization allowed")
    elif delta < 0.5:
        print("Classification: Structured divergence – qualification needed")
    elif delta < 0.7:
        print("Classification: High divergence – narrative risk, do not generalize")
    else:
        print("Classification: Contested – claim likely hallucination")
    
    # Optional: Print pair table
    print("\nPairwise Δdiv matrix:")
    model_names = [item["model"] for item in data["responses"]]
    n = len(model_names)
    print(" " * 12, end="")
    for name in model_names:
        print(f"{name:>10}", end="")
    print()
    
    for i in range(n):
        print(f"{model_names[i]:<10}", end="")
        for j in range(n):
            if i == j:
                print(f"{0.000:>10.3f}", end="")
            elif j < i:
                print(" " * 10, end="")
            else:
                cos_sim = cosine_similarity(
                    [SentenceTransformer('all-MiniLM-L6-v2').encode([responses[i]])[0]],
                    [SentenceTransformer('all-MiniLM-L6-v2').encode([responses[j]])[0]]
                )[0][0]
                jac_sim = jaccard_similarity(responses[i], responses[j])
                delta_pair = 0.5 * (1 - jac_sim) + 0.5 * (1 - cos_sim)
                print(f"{delta_pair:>10.3f}", end="")
        print()

if __name__ == "__main__":
    main()
