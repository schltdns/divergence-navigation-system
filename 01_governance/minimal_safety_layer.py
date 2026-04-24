#!/usr/bin/env python3
"""
minimal_safety_layer.py
Demonstrates DNS Safety Layer: Four questions → AI Act mapping → hash chain.
"""

import hashlib
import json
import uuid
from datetime import datetime, timezone

def create_log_entry(prognose_id, answers, dissent=None):
    """Create a log entry with AI Act mapping."""
    entry = {
        "prognose_id": prognose_id,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "session_hash": hashlib.sha256(b"session_salt").hexdigest()[:16],
        "fragen": answers,
        "ai_act_mapping": {
            "art_13_transparenz": not answers.get("thema_getroffen", True),
            "art_14_human_oversight": dissent is not None,
            "art_9_risikomanagement": answers.get("ueberpruefbar", False)
        }
    }
    if dissent:
        entry["dissent_log"] = dissent
    return entry

def hash_entry(entry):
    """Create SHA256 hash of the JSON entry."""
    entry_str = json.dumps(entry, sort_keys=True)
    return hashlib.sha256(entry_str.encode()).hexdigest()

def build_merkle_root(hashes):
    """Build Merkle root from list of hashes (simplified)."""
    if not hashes:
        return None
    while len(hashes) > 1:
        if len(hashes) % 2:
            hashes.append(hashes[-1])
        hashes = [hashlib.sha256((h1 + h2).encode()).hexdigest() 
                  for h1, h2 in zip(hashes[::2], hashes[1::2])]
    return hashes[0]

# Example usage
if __name__ == "__main__":
    # Simulate a decision
    answers = {
        "thema_getroffen": True,
        "neue_idee": "voll",
        "ueberpruefbar": True,
        "verstaendlich": True
    }
    dissent = {
        "kategorie": "fehlender_kontext",
        "begruendung": "Die KI kennt die lokalen Schulschließungen nicht. Der Rat hat deshalb die Prognose angepasst." * 3  # >140 chars
    }
    entry = create_log_entry("nrw-20250421-3F2A", answers, dissent)
    print("Log Entry:", json.dumps(entry, indent=2))
    h = hash_entry(entry)
    print("SHA256 Hash:", h)
    
    # Simulate daily batch
    daily_hashes = [h, "abc123", "def456"]  # other entries
    merkle_root = build_merkle_root(daily_hashes)
    print("Merkle Root (daily batch):", merkle_root)
