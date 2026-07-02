# GDPR / Data Privacy Notice

## Scope
This repository contains **analysis code only**.  No personal data is committed to version control.

## What is NOT in this repo
- Raw student response files.
- Subject marks spreadsheets.
- Diagnostic CSVs that link cluster labels to real identifiers.
- Figures with embedded raw IDs.

These are excluded via `.gitignore` (`data/`, `diagnostics/`, `figures/`, `outputs/`).

## Your responsibilities when using this code

1. **Pseudonymise before sharing outputs**
   Use `gdpr_utils.py`:
   ```python
   from gdpr_utils import pseudonymise_df
   df = pseudonymise_df(df, id_col="IDCode", drop_demographic=True)
   ```
   or set `ID_HASH_SALT` to a strong random string.

2. **Never commit raw data**
   Keep input files outside the repository or in a sibling folder not tracked by git.

3. **Minimise demographic data**
   Columns such as `sex`, `gender`, `name`, `email`, `dob` should only be retained if your ethics protocol explicitly authorises it.  Drop them before any sharing or publication step.

4. **Review generated artefacts**
   Open exported PNG/PDF plots to confirm axis labels, annotations, and legends do not expose individual identifiers.

## Environment variables for safe path handling
Set these instead of hardcoding filenames that may contain personal names:

- `STUDY2_ITEMWISE_PATH` — itemwise CSV
- `STUDY2_MARKS_PATH` — marks Excel file
- `STUDY2_EXTERNAL_DATA_PATH` — external validity data
- `ID_HASH_SALT` — salt for SHA-256 ID hashing
