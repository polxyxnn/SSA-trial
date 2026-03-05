import streamlit as st

# -----------------------------
# LOGO
# -----------------------------

logo_url = "utils/Philsa_whitename_color.png"
st.logo(
    iamge= logo_url, 
    size="large"
)

# -----------------------------
# SIDEBAR STYLE
# -----------------------------
st.markdown(
    """
    <style>
        section[data-testid="stSidebar"] {
            width: 300px !important;
        }

        [data-testid="stSidebarNav"]::before {
            content: "Philippine Space Agency";
            font-size: 22px;
            font-weight: 600;
            display: block;
            text-align: center;
            margin-bottom: 20px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# SESSION STATE
# -----------------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False


# -----------------------------
# LOGIN / LOGOUT
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
# PAGES
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
if st.session_state.logged_in:
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