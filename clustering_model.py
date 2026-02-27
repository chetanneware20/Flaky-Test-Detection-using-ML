import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import DBSCAN

def detect_flaky_tests(feature_csv):
    df = pd.read_csv(feature_csv)
    X = df.drop(columns=['test_name'])

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    model = DBSCAN(eps=1.2, min_samples=2)
    df['cluster'] = model.fit_predict(X_scaled)

    df['flaky_label'] = df['cluster'].apply(
        lambda x: 'Flaky' if x == -1 else 'Stable'
    )

    return df

if __name__ == "__main__":
    result = detect_flaky_tests("data/test_features.csv")
    result.to_csv("data/flaky_results.csv", index=False)
    print("✅ Flaky test detection completed")
