#%%
import pandas as pd
import streamlit as st

# data = pd.read_csv('shraddha.csv')

sb = st.sidebar.selectbox('Select a Category', ['Project Details', 'Stock Performance', 'Company Overview'])

if sb == 'Project Details':
    st.image('https://www.snewcomputers.com/snewcomputers/uploads/2023/02/call-us.jpg')

    # Project Details section
    st.title("Analytics Of IT Companies")

    st.markdown("## Overview\n"
                "This project offers a wealth of information about IT companies, presenting users with a multitude of benefits. Firstly, the financial details, including revenue and profit and loss (PNL), provide stakeholders with key insights into the economic health of these organizations. Investors can make informed decisions based on the financial performance, while analysts can identify trends and patterns.\n\n"
                "## Global and Indian Presence\n"
                "The dataset's inclusion of global and Indian locations, CEO names, and origin countries fosters a deeper understanding of the companies' structures and backgrounds. Users can assess the global reach of these organizations and appreciate the diversity in leadership. This information is invaluable for market researchers, policymakers, and industry observers seeking to comprehend the global IT landscape.\n\n"
                "## Historical Perspective\n"
                "Furthermore, the details on the year of founding, ratings, and current employee count offer a historical perspective and gauge of organizational success. Researchers can analyze growth trajectories, while job seekers and professionals can evaluate the companies' reputations. The internship bond details provide insights into talent acquisition strategies.\n\n"
                "## Headquarters Information\n"
                "The inclusion of headquarters information, both globally and in India, is crucial for those interested in the companies' physical presence. This information aids in regional economic analysis and supports policymakers in making informed decisions about the industry's impact.\n\n"
                "## Market Positioning\n"
                "Additionally, the dataset covers services offered and stock market listings, allowing users to assess the companies' market positioning and competitiveness. This information is of particular interest to industry analysts, competitors, and potential collaborators.\n\n"
                "## Summary\n"
                "In summary, the benefits of this comprehensive IT companies dataset extend to investors, analysts, researchers, job seekers, policymakers, and industry enthusiasts. It serves as a valuable resource for making informed decisions, conducting thorough analyses, and gaining a nuanced understanding of the IT sector.")
elif 'Stock Performance':
    st.write("I'll work on it later")

elif 'Company Overview':
    st.write("I'll work on it later")

