import pandas as pd

def rolling_failure_rate(csv_path, window=3):
    df = pd.read_csv(csv_path)
    df['execution_date'] = pd.to_datetime(df['execution_date'])
    df['status_binary'] = df['status'].map({'Pass': 0, 'Fail': 1})

    df.sort_values(by=['test_name', 'execution_date'], inplace=True)

    df['rolling_failure_rate'] = (
        df.groupby('test_name')['status_binary']
          .rolling(window)
          .mean()
          .reset_index(level=0, drop=True)
    )

    return df

if __name__ == "__main__":
    ts_df = rolling_failure_rate("test_results.csv")
    ts_df.to_csv("data/time_series_output.csv", index=False)
    print("✅ Time-series analysis completed")
