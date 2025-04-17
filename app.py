import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load Data
@st.cache_data
def load_data():
    advancement_df = pd.read_csv("advancement_probabilities.csv")
    winners_df = pd.read_csv("bracket_winners.csv")

    # Clean column names
    advancement_df.rename(columns={"Unnamed: 0": "Team"}, inplace=True)
    winners_df.rename(columns={"Most Likely Winner": "Winner"}, inplace=True)

    # Optional: strip any spaces
    advancement_df.columns = advancement_df.columns.str.strip()
    winners_df.columns = winners_df.columns.str.strip()
    
    return advancement_df, winners_df

advancement_df, winners_df = load_data()

# Title
st.title("March Madness Bracket Insights")

# Sidebar - Team Selection
teams = advancement_df["Team"].unique()
selected_team = st.sidebar.selectbox("Select a team", sorted(teams))

# Display Advancement Probabilities for selected team
st.header(f"{selected_team} Advancement Probabilities")
team_probs = advancement_df[advancement_df["Team"] == selected_team].drop(columns="Team").T
team_probs.columns = ["Probability"]
team_probs.index.name = "Round"

st.bar_chart(team_probs)

# Full Advancement Table
st.subheader("All Teams Advancement Probabilities")
st.dataframe(advancement_df)

# Bracket Winner Visualization
st.subheader("Bracket Winners Frequency")
winner_counts = winners_df["Winner"].value_counts().reset_index()
winner_counts.columns = ["Team", "Times Picked as Winner"]

fig, ax = plt.subplots()
ax.barh(winner_counts["Team"], winner_counts["Times Picked as Winner"])
ax.set_xlabel("Times Picked")
ax.set_ylabel("Team")
ax.set_title("Bracket Winners")
st.pyplot(fig)

# Footer
st.markdown("---")
st.caption("Built by Aaron using Streamlit 🏀")

