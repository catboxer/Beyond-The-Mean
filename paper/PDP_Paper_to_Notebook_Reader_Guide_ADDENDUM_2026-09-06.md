# Reader Guide addendum — 2026-09-06

**Not yet merged into `PDP_Paper_to_Notebook_Reader_Guide.pdf` / the live Google Doc.**
I have no write access to that Doc from here — this addendum exists so the entry isn't
lost; fold it into the guide (and re-export the PDF) by hand, in the same table format as
the guide's other entries.

---

## QRNG provider-identity validation (real perturbation)

| | |
|---|---|
| Notebook and header | `Exp4_ProviderValidation_ResolutionFloor_and_Section5.ipynb` — "Part 1: Resolution floor (delta)" / "Part 2: Section 5 Step 1" / "Part 3: Section 5 Step 2" |
| What it does | Derives this study's own equivalence bound (delta) from real collected data, then tests whether QRNG provider identity (Outshift vs. LFDR) produces a detectable hit-rate/H_RS difference, unpaired and paired-by-provider |
| How it was done | Whole-sitting cluster bootstrap (3,000 draws) on 269 completed machine-only sittings (8,042 blocks), loaded from the frozen `Frozen_ProviderValidation_Blocks_2026-09-06.csv` (self-downloads from this repo's `data/` folder if not present locally; SHA-256 verified against `data/provider_validation_manifest.json`) |
| Result shown | delta ≈ 0.0014; no significant provider difference detected (both unpaired and paired-by-provider, both metrics), but none of the four CIs fall entirely within ±delta — indeterminate, not a clean equivalence pass |
| Population / data | 269 sittings / 8,042 blocks, machine-only (no Human or AI condition involved) — a separate follow-up study, not part of the four Study 1 / Pilot 4 notebooks (NB1/NB2/Interleaving/Exp4-vs-Exp5) |
| Source role | Primary result source for this claim |

**Files added to this repo:**
- `analysis/Exp4_ProviderValidation_ResolutionFloor_and_Section5.ipynb` (already executed — real outputs baked in; reruns standalone, no credentials needed)
- `data/Frozen_ProviderValidation_Blocks_2026-09-06.csv` (the frozen data it reads)
- `data/provider_validation_manifest.json` and `analysis/generate_provider_validation_manifest.py` (SHA-256 provenance record, same pattern as `generate_diagnostic_validation_manifest.py` — kept separate from the main `data/manifest.json` so regenerating one never touches the other)

**Full process record (not copied into this repo, stays in the qart-experiment source repo):**
`experiments/exp4/resolution_floor_derivation-provider-validation.md` — same role there as
`resolution_floor_derivation-exp4.md` plays for the companion injection-study delta.
