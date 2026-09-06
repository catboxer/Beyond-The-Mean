# ═══════════════════════════════════════════════════════════════════════════
# GENERATE PROVIDER-VALIDATION MANIFEST
# ═══════════════════════════════════════════════════════════════════════════
# PURPOSE: Create data/provider_validation_manifest.json with the SHA-256 hash
#          of Frozen_ProviderValidation_Blocks_2026-09-06.csv, kept deliberately
#          separate from data/manifest.json (see generate_manifest.py) for the
#          same reason as generate_diagnostic_validation_manifest.py: regenerating
#          one manifest should never touch hashes for the other, and this keeps
#          the pilot's frozen citation-grade dataset untouched by an unrelated
#          validation run's own data.
#
#          Exp4_ProviderValidation_ResolutionFloor_and_Section5.ipynb has the
#          expected hash hardcoded as EXPECTED_SHA256 and fails loudly if the
#          downloaded/local CSV doesn't match it -- this file exists as a
#          standalone provenance record matching that same value, not as
#          something that notebook reads back.
#
# USAGE:  python generate_provider_validation_manifest.py
#         (run from anywhere -- paths are resolved relative to this file)
# ═══════════════════════════════════════════════════════════════════════════

import hashlib
import json
import os
from datetime import datetime

DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data')

DATA_FILES = {
    'provider_validation_blocks': 'Frozen_ProviderValidation_Blocks_2026-09-06.csv',
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
    'source': 'PROVIDER_VALIDATION_PRESPEC.md Section 9 (qart-experiment repo, experiments/exp4/)',
    'hash_algorithm': 'SHA-256',
    'files': {}
}

print("=" * 70)
print("Generating Provider-Validation Manifest")
print("=" * 70)

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

manifest_path = os.path.join(DATA_DIR, 'provider_validation_manifest.json')
with open(manifest_path, 'w') as f:
    json.dump(manifest, f, indent=2)

print(f"\n{'=' * 70}")
print(f"Manifest written to: {manifest_path}")
print(f"{'=' * 70}")
