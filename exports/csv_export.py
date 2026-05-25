import pandas as pd

def export_csv(df, filename):

    df.to_csv(filename, index=False)