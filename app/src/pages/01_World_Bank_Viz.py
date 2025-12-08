# pages/01_World_Bank_Viz.py
# Stratify - Global Macro Data
# Legacy redirect page for the renamed Global Macro Data view.

import streamlit as st


def main() -> None:
    """
    Legacy placeholder page.

    The canonical page now lives at:
    `pages/01_Global_Macro_Data.py` and is linked in the sidebar as
    "Global Macro Data".
    """
    st.set_page_config(
        page_title="Global Macro Data (Legacy Redirect)",
        layout="wide",
    )

    st.markdown(
        """
        ## This page was renamed

        The working page now lives at **`pages/01_Global_Macro_Data.py`**  
        and is linked in the sidebar as **Global Macro Data**.
        """,
        unsafe_allow_html=True,
    )

    st.write("Use the button below to reload the app and navigate via the sidebar.")

    if st.button("Go to Global Macro Data"):
        # Clear any query parameters so the app loads the sidebar-linked page.
        st.experimental_set_query_params()
        st.experimental_rerun()


if __name__ == "__main__":
    main()