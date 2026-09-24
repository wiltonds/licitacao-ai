"""Recruiter-facing tender-intelligence demo with synthetic data."""
import streamlit as st

st.set_page_config(page_title="Public Procurement AI | Demo",page_icon="📄",layout="wide")
st.title("📄 Public Procurement AI")
st.caption("Demo executável · edital → extração → evidências → compliance → decisão humana")
c1,c2,c3,c4=st.columns(4)
for c,t,v,s in [(c1,"Documents","3","synthetic tender set"),(c2,"Facts extracted","14","structured fields"),(c3,"Evidence hits","9","retrieval layer"),(c4,"Review status","HUMAN","final decision")]:
    with c: c.metric(t,v,s)
st.divider()
st.subheader("Tender: Training Services — Synthetic Example")
left,right=st.columns(2)
with left:
    st.markdown("### Structured extraction")
    st.write("**Object:** contratação de capacitação em segurança e processos industriais")
    st.write("**Location:** Maceió/AL")
    st.write("**Service type:** technical training")
    st.write("**Qualification:** technical capability + documentation")
with right:
    st.markdown("### Evidence & compliance")
    checks=[("Object identified","PASS"),("Qualification requirement extracted","PASS"),("Legal evidence retrieved","PASS"),("Potential pending item","REVIEW")]
    for label,status in checks:
        st.write(f"**{status}** — {label}")
st.divider()
st.subheader("Agentic workflow")
st.code("Tender PDF → Extraction Agent → RAG / Law Base → Compliance Agent → Human Review",language="text")
st.warning("DEMO — legal text, tender facts and compliance results are synthetic. This interface is not legal advice and does not automate a bidding decision.")
