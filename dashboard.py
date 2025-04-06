import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.title("📊Hourly report")

# Upload the Excel file
uploaded_file = st.file_uploader("Upload Excel File", type=["xlsx"])

if uploaded_file:
    df = pd.read_excel(uploaded_file)
    df.columns = df.columns.str.strip()  # Remove spaces from column names

    st.subheader("📄 Overview of your Data")
    st.dataframe(df)

    # Let user select columns for the graph
    with st.sidebar:
        st.header("📌 Select Columns for Chart")
        x_col = st.selectbox("X-axis (Category)", df.columns)
        bar1_col = st.selectbox("1st Bar (Y-axis)", df.columns)
        bar2_col = st.selectbox("2nd Bar (Y-axis)", df.columns)
      #  bar3_col = st.selectbox("3rd Bar (Y-axis)",df.columns)
        line_col = st.selectbox("Line Chart (Y-axis)", df.columns)

    try:
        fig = go.Figure()

        # Bar 1
        fig.add_trace(go.Bar(
            x=df[x_col],
            y=df[bar1_col],
            name=bar1_col,
            marker_color='steelblue'
        ))

        # Bar 2
        fig.add_trace(go.Bar(
            x=df[x_col],
            y=df[bar2_col],
            name=bar2_col,
            marker_color='lightgreen'
        ))
     

        # Line chart
        fig.add_trace(go.Scatter(
            x=df[x_col],
            y=df[line_col],
            name=line_col,
            mode='lines+markers',
            line=dict(color='darkgreen', width=3)
        ))

        fig.update_layout(
            barmode='group',
            title='📊 Custom Summary Chart',
            yaxis=dict(title='Values'),
            xaxis=dict(title=x_col),
            legend=dict(title='Legend'),
            height=500,
        )

        st.plotly_chart(fig, use_container_width=True)

    except Exception as e:
        st.error(f"❌ Error: {e}")
