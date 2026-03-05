import streamlit as st

# -----------------------------
# SIDEBAR LOGO + TITLE
# -----------------------------
def add_logo():
    st.markdown(
        """
        <style>
            [data-testid="stSidebarNav"] {
                background-image: url(https://philsa.gov.ph/wp-content/themes/philsa/src/assets/images/logo.png);
                background-repeat: no-repeat;
                background-position: 20px 20px;
                padding-top: 120px;
            }

            [data-testid="stSidebarNav"]::before {
                content: "Philippine Space Agency";
                margin-left: 20px;
                margin-top: 20px;
                font-size: 24px;
                font-weight: 600;
                position: relative;
                top: 80px;
            }

            section[data-testid="stSidebar"] {
                width: 300px !important;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

add_logo()


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