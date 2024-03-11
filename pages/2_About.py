import streamlit as st
from modules.shared_config import setup_page

setup_page()

st.title("About our Project")

st.divider()

st.markdown(
"""
At the intersection of governance and technology, this GovTech initiative takes a decisive stand against sextortion. Our comprehensive study aims
not only to confront this pernicious issue but also to elevate public service delivery to new standards of integrity and efficiency. Spearheaded by
Dr. Fernando Forattini and guided by the expert tutelage of Prof. Regina Connolly and Prof. Robert Gillanders, our project is a concerted effort
among renowned academic and research entities. With the generous support of the SyMeCo Post-Doctoral Fellowship at [Lero](https://lero.ie/),
the [DCU Business School's](https://www.dcu.ie/dcubs/dcu-business-school), [Anti-corruption Research Centre](https://www.dcu.ie/arc)
and [Corruption, Gender, and Sustainable Development (COGS)](https://www.dcu.ie/arc/cogs) we delve into the critical
task of creating an ethical governance model free from the influence of sextortion.
"""
)

st.subheader("Participants")
st.markdown(
    """
    - **Dr. Fernando Forattini:** *main researcher*, driving forward the investigation into sextortion's impact on public services.\n
    - **Prof. Regina Connolly:** *Tutor.* A distinguished scholar in information systems and expert in the area of Public Sector digital, whose insights into digital
    governance and societal implications enrich the project's approach to developing solutions.\n
    - **Prof. Robert Gillanders:** *Co-Tutor.* Renowned for his expertise in corruption and its economic impacts, Dr. Gillanders'
    scholarship critically informs our research trajectory.\n
    - **Lero & DCU Business School:** Our collaborative partners contribute advanced software systems understanding and managerial acumen, essential
    to the project's overarching goals.
    - **Anti-corruption Research Centre and Corruption, Gender, and Sustainable Development (COGS)**: At DCU, these centers are at the vanguard of
    anti-corruption research, providing the project with a rich bedrock of expertise and knowledge.\n
"""
)

st.subheader("Objectives and Importance")
st.markdown(
"""
Addressing the insidious impact of sextortion is central to our mission, as it threatens public trust and obstructs the path to gender equity. This project is committed to:
- Conducting in-depth empirical research to unearth the mechanisms of sextortion.
- Leveraging innovative technology to establish robust ethical governance frameworks.\n
Our objective is to pave the way for inclusive and transparent public administration, fortified against the exploitation of power.
"""
)

st.subheader("Platform Description")
st.markdown(
"""
Our digital platform stands as the confluence of our multifaceted activities, designed to:
- Provide stakeholders with empirical data and updates in real time.
- Incorporate a secure, blockchain-enabled whistleblowing feature within governance structures.
- Facilitate rigorous academic dialogue and stakeholder interaction through dedicated forums.
Policymakers, scholars, sector-specific experts, and citizens are invited to explore and engage with the platform, contributing to a collective effort towards a governance landscape imbued with integrity and accountability.
"""
)