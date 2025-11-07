# src/config.py
from __future__ import annotations
import os

# Carrega .env se existir (não explode se não existir)
try:
    from dotenv import load_dotenv  # pip install python-dotenv
    load_dotenv(override=False)
except Exception:
    pass

# Suporte a Streamlit secrets (opcional)
def _from_streamlit(key: str) -> str | None:
    try:
        import streamlit as st  # type: ignore
        sect = st.secrets.get("oracle", {})
        return sect.get(key) if isinstance(sect, dict) else None
    except Exception:
        return None

def get_oracle_cfg() -> dict:
    user = _from_streamlit("user") or os.getenv("ORACLE_USER")
    pwd  = _from_streamlit("pwd")  or os.getenv("ORACLE_PWD")
    host = _from_streamlit("host") or os.getenv("ORACLE_HOST", "oracle.fiap.com.br")
    port = _from_streamlit("port") or int(os.getenv("ORACLE_PORT", "1521"))
    sid  = _from_streamlit("sid")  or os.getenv("ORACLE_SID", "ORCL")

    if not user or not pwd:
        raise RuntimeError(
            "Credenciais Oracle ausentes. Defina ORACLE_USER/ORACLE_PWD via .env "
            "ou configure em .streamlit/secrets.toml [oracle]."
        )
    return {"user": user, "pwd": pwd, "host": host, "port": port, "sid": sid}
