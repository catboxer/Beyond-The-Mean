# ═══════════════════════════════════════════════════════════════════════════
# GENERATE DATA MANIFEST
# ═══════════════════════════════════════════════════════════════════════════
# PURPOSE: Create manifest.json with full SHA-256 hashes of all data files.
#          Run this ONCE after freezing the dataset. NOTE: as of 2026-09-01,
#          neither notebook actually reads manifest.json back for comparison
#          -- NB1/NB2 compute and print their own live hashes of whatever
#          files they load, but do not check them against this file. This
#          manifest is a standalone provenance record (and a source for the
#          paper's Data Provenance section), not an automated integrity gate.
#
# USAGE:  python generate_manifest.py
#         (run from anywhere -- paths are resolved relative to this file)
# ═══════════════════════════════════════════════════════════════════════════

import hashlib
import json
import os
from datetime import datetime

# ─────────────────────────────────────────────────────────────
# Configuration — list your data files here
# ─────────────────────────────────────────────────────────────
DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data')

DATA_FILES = {
    'participants': 'Frozen_Participants_2026-02-10_195735.csv',
    'sessions':     'Frozen_Sessions_2026-02-10_195735.csv',
    'blocks':       'Frozen_Blocks_2026-02-10_195735.csv',
    'audits':       'Frozen_Audits_2026-02-10_195735.csv',
    'raw_calls':    'Frozen_Exp4_RawBlockBits_2026-07-26.pkl',
    'diagnostic_validation': 'PDP_Diagnostic_Validation_FROZEN.xlsx',
}

# ─────────────────────────────────────────────────────────────
# Compute SHA-256 hashes
# ─────────────────────────────────────────────────────────────
def sha256_file(filepath):
    """Compute full SHA-256 hash of a file."""
    h = hashlib.sha256()
    with open(filepath, 'rb') as f:
        for chunk in iter(lambda: f.read(8192), b''):
            h.update(chunk)
    return h.hexdigest()

manifest = {
    'generated': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    'frozen_date': '2026-02-10',
    'hash_algorithm': 'SHA-256',
    'files': {}
}

print("="*70)
print("Generating Data Manifest")
print("="*70)

for name, filename in DATA_FILES.items():
    filepath = os.path.join(DATA_DIR, filename)
    if not os.path.exists(filepath):
        print(f"  WARNING: {filename} not found!")
        continue

    file_hash = sha256_file(filepath)
    file_size = os.path.getsize(filepath)

    manifest['files'][name] = {
        'filename': filename,
        'sha256': file_hash,
        'size_bytes': file_size,
    }

    print(f"\n  {name}:")
    print(f"    File: {filename}")
    print(f"    SHA-256: {file_hash}")
    print(f"    Size: {file_size:,} bytes")

# ─────────────────────────────────────────────────────────────
# Write manifest.json
# ─────────────────────────────────────────────────────────────
manifest_path = os.path.join(DATA_DIR, 'manifest.json')
with open(manifest_path, 'w') as f:
    json.dump(manifest, f, indent=2)

print(f"\n{'='*70}")
print(f"Manifest written to: {manifest_path}")
print(f"{'='*70}")
print(f"\nPaste these hashes into your paper's Data Provenance section.")
