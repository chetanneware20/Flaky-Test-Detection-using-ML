import pandas as pd
import sys

df = pd.read_csv("data/flaky_results.csv")

flaky_count = len(df[df['flaky_label'] == 'Flaky'])

if flaky_count > 0:
    print(f"⚠️ Build unstable: {flaky_count} flaky tests detected")
    sys.exit(0)  # unstable but not failed
else:
    print("✅ No flaky tests detected")
    sys.exit(0)
