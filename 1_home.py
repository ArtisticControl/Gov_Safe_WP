import streamlit as st
from modules.shared_config import setup_page

setup_page()

#End of Sidebar Configuration ------

st.title("Sextortion in Public Service Delivery and the Role of GovTech")

st.divider()

st.markdown(
    """
    In the shadow of global crises and escalating inequalities, corruption remains a formidable adversary against socio-economic
    development and justice. Among its many manifestations, **sextortion** — the exploitation of power for sexual favors — *remains
    particularly insidious, yet underexplored*. This form of corruption not only violates human rights but also undermines trust
    in public institutions, with profound effects on women and the most vulnerable in society. \n
    Despite progress in anti-corruption measures, traditional approaches often overlook the complex socio-historical dimensions of
    sextortion. This gap necessitates innovative solutions informed by both scholarly research and practical insights.\n
    Enter this webapp: a groundbreaking initiative designed to illuminate and combat sextortion through a synergy of academic inquiry,
    policy development, and community engagement. With years of dedicated research underpinning its development, the platform offers a
    comprehensive suite of tools — from dynamic mapping and real-time analysis to legal and policy resources — all aimed at empowering
    users to devise and implement effective strategies against sextortion.\n 
    Beyond serving as a repository of knowledge, the webapp aspires to be a catalyst for change, providing a foundation upon which to
    build a more just and equitable society.\n
    *Join us in leveraging the power of GovTech to dismantle the structures of corruption and sextortion, forging a path toward integrity
    and trust in public service.*
    """
    )

st.text("")
