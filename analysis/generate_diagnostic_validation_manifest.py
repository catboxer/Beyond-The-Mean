# ═══════════════════════════════════════════════════════════════════════════
# GENERATE DIAGNOSTIC-VALIDATION MANIFEST
# ═══════════════════════════════════════════════════════════════════════════
# PURPOSE: Create data/diagnostic_validation_manifest.json with the SHA-256
#          hash of PDP_Diagnostic_Validation_FROZEN.xlsx, kept deliberately
#          separate from data/manifest.json (see generate_manifest.py). Two
#          reasons: regenerating one manifest should never touch hashes for
#          the other, and this keeps the pilot's frozen citation-grade
#          dataset untouched by an unrelated validation run.
#
#          preregistration/PDP_Diagnostic_Validation_Prereg.ipynb currently
#          verifies this file against its own hardcoded expected-hash constant
#          rather than reading this manifest -- this file exists as a
#          standalone provenance record matching that same file, not as
#          something that notebook reads back.
#
# USAGE:  python generate_diagnostic_validation_manifest.py
#         (run from anywhere -- paths are resolved relative to this file)
# ═══════════════════════════════════════════════════════════════════════════

import hashlib
import json
import os
from datetime import datetime

DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data')

DATA_FILES = {
    'diagnostic_validation': 'PDP_Diagnostic_Validation_FROZEN.xlsx',
}


def sha256_file(filepath):
    """Compute full SHA-256 hash of a file."""
    h = hashlib.sha256()
    with open(filepath, 'rb') as f:
        for chunk in iter(lambda: f.read(8192), b''):
            h.update(chunk)
    return h.hexdigest()


manifest = {
    'generated': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    'hash_algorithm': 'SHA-256',
    'files': {}
}

print("="*70)
print("Generating Diagnostic-Validation Manifest")
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

manifest_path = os.path.join(DATA_DIR, 'diagnostic_validation_manifest.json')
with open(manifest_path, 'w') as f:
    json.dump(manifest, f, indent=2)

print(f"\n{'='*70}")
print(f"Manifest written to: {manifest_path}")
print(f"{'='*70}")
