import plotly.express as px

def create_line_chart(df):

    fig = px.line(
        df,
        x="date",
        y="amount",
        title="Expense Trend"
    )

    return fig