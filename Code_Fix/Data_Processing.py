import pandas as pd

def retrieve_data(df):

        if 'Date' in df.columns:
            df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y')

            # Extract additional date-related features
            df['WeekNumber'] = df['Date'].dt.isocalendar().week
            df['Month'] = df['Date'].dt.month
            df['Year'] = df['Date'].dt.isocalendar().year

        return df


