import plotly.express as px

def create_pie_chart(df):

    fig = px.pie(
        df,
        names="category",
        values="amount",
        title="Expense Categories"
    )

    return fig