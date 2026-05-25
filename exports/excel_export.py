import pandas as pd

def export_excel(df, filename):

    df.to_excel(filename, index=False)