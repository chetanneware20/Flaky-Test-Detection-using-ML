import pandas as pd

def generate_features(csv_path):
    df = pd.read_csv(csv_path)
    df['execution_date'] = pd.to_datetime(df['execution_date'])
    df['status_binary'] = df['status'].map({'Pass': 0, 'Fail': 1})

    features = []

    for test, group in df.groupby('test_name'):
        total_runs = len(group)
        failure_rate = group['status_binary'].mean()
        switches = group['status_binary'].diff().abs().sum()
        avg_duration = group['duration'].mean()
        duration_variance = group['duration'].var()

        features.append({
            'test_name': test,
            'failure_rate': failure_rate,
            'status_switches': switches,
            'avg_duration': avg_duration,
            'duration_variance': duration_variance
        })

    return pd.DataFrame(features)

if __name__ == "__main__":
    feature_df = generate_features("test_results.csv")
    feature_df.to_csv("test_features.csv", index=False)
    print("✅ Feature engineering completed")
