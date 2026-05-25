import plotly.express as px

def create_bar_chart(df):

    fig = px.bar(
        df,
        x="category",
        y="amount",
        title="Expenses by Category"
    )

    return fig