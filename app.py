import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load Data
@st.cache_data
def load_data():
    advancement_df = pd.read_csv("advancement_probabilities.csv")
    winners_df = pd.read_csv("bracket_winners.csv")
    return advancement_df, winners_df

advancement_df, winners_df = load_data()

# Title
st.title("March Madness Bracket Insights")

# Sidebar - Team Selection
teams = advancement_df["Team"].unique()
selected_team = st.sidebar.selectbox("Select a team to view advancement probabilities", sorted(teams))

# Display Advancement Probabilities for selected team
st.header(f"Advancement Probabilities: {selected_team}")
team_probs = advancement_df[advancement_df["Team"] == selected_team]

if not team_probs.empty:
    st.bar_chart(team_probs.set_index("Round")["Probability"])
else:
    st.warning("No data found for selected team.")

# Display Full Advancement Table
st.subheader("Full Advancement Probability Table")
st.dataframe(advancement_df)

# Bracket Winner Analysis
st.subheader("Bracket Winners Distribution")

winner_counts = winners_df["Winner"].value_counts().reset_index()
winner_counts.columns = ["Team", "Times Picked as Winner"]

fig, ax = plt.subplots()
ax.barh(winner_counts["Team"], winner_counts["Times Picked as Winner"])
ax.set_xlabel("Times Picked")
ax.set_ylabel("Team")
ax.set_title("Bracket Winners Frequency")
st.pyplot(fig)

# Footer
st.markdown("---")
st.caption("Built with ❤️ using Streamlit")

