import streamlit as st
import pandas as pd
import numpy as np

# Generate sample data
data = pd.DataFrame(
    np.random.randn(100, 3),
    columns=['a', 'b', 'c']
)
st.line_chart(data)
# Display the area chart
st.area_chart(data)
