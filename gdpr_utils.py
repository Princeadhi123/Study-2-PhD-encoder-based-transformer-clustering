"""GDPR helpers: pseudonymise IDs + strip quasi-identifiers.

Usage:
    from gdpr_utils import pseudonymise_df, hash_id

    df["IDCode"] = df["IDCode"].apply(hash_id)
    df = pseudonymise_df(df, drop_demographic=True)
"""
import hashlib
import os
import pandas as pd


def hash_id(raw: str, salt: str | None = None) -> str:
    """SHA-256 hash of raw ID.  Deterministic per salt."""
    if salt is None:
        salt = os.environ.get("ID_HASH_SALT", "Study2-default-salt-CHANGE-ME")
    text = f"{salt}:{raw}".encode("utf-8")
    return hashlib.sha256(text).hexdigest()[:16]


def pseudonymise_df(df: pd.DataFrame, id_col: str = "IDCode", drop_demographic: bool = True) -> pd.DataFrame:
    """Return copy with hashed IDs and optional PII columns removed."""
    df = df.copy()
    if id_col in df.columns:
        df[id_col] = df[id_col].astype(str).apply(hash_id)
    if drop_demographic:
        drop_cols = [c for c in df.columns if c.lower() in {"sex", "gender", "name", "email", "dob", "birthdate"}]
        df = df.drop(columns=drop_cols, errors="ignore")
    return df
