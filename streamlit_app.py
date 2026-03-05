import streamlit as st
import os

# -----------------------------
# CONFIG
# -----------------------------
LOGO_PATH = "utils/PhilSA_v1-01.png"  # change path if needed


# -----------------------------
# SIDEBAR STYLE
# -----------------------------
st.markdown(
    """
    <style>
        section[data-testid="stSidebar"] {
            width: 300px !important;
        }

        /* Center image inside sidebar */
        [data-testid="stSidebar"] img {
            display: block;
            margin-left: auto;
            margin-right: auto;
        }

        /* Center title text */
        [data-testid="stSidebar"] h1 {
            text-align: center;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# SIDEBAR HEADER (LOGO + TITLE)
# -----------------------------
with st.sidebar:
    if os.path.exists(LOGO_PATH):
        st.image(LOGO_PATH, width=250)
    else:
        st.warning("⚠️ Logo not found")

    st.title("Philippine Space Agency")


# -----------------------------
# SESSION STATE
# -----------------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False


# -----------------------------
# LOGIN / LOGOUT FUNCTIONS
# -----------------------------
def login():
    st.title("Login")

    if st.button("Log in"):
        st.session_state.logged_in = True
        st.rerun()


def logout():
    st.title("Logout")

    if st.button("Log out"):
        st.session_state.logged_in = False
        st.rerun()


# -----------------------------
# PAGE DEFINITIONS
# -----------------------------
login_page = st.Page(login, title="Log in", icon=":material/login:")
logout_page = st.Page(logout, title="Log out", icon=":material/logout:")

dashboard = st.Page(
    "reports/dashboard.py",
    title="Dashboard",
    icon=":material/dashboard:",
    default=True
)

ssa_rocket = st.Page(
    "SSA-tools/rocket.py",
    title="Rocket Launch",
    icon=":material/rocket_launch:"
)

ssa_collision = st.Page(
    "SSA-tools/collision.py",
    title="Collision",
    icon=":material/compare_arrows:"
)


# -----------------------------
# NAVIGATION
# -----------------------------
if st.session_state.get("logged_in"):
    pg = st.navigation(
        {
            "Account": [logout_page],
            "Reports": [dashboard],
            "Tools": [ssa_rocket, ssa_collision],
        }
    )
else:
    pg = st.navigation([login_page])

pg.run()