import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, PowerTransformer

folder = "/Users/jacquelinezhu/Desktop/SleepdB/acoustic_project/04162025_05142025"
input_file = os.path.join(folder, "AcousticFeatures_April16_May14_soo.xlsx")
df = pd.read_excel(input_file).dropna(how='all')

def preprocess(series: pd.Series) -> tuple[pd.Series, pd.Series]:
    series_numeric = pd.to_numeric(series, errors='coerce')
    log_series = np.log1p(series_numeric)
    return series_numeric, log_series

def plot_feature(series: pd.Series, feature_name: str) -> None:
    original, log_transformed = preprocess(series)
    n_samples = len(original)

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    sns.histplot(original, kde=True, bins=n_samples, ax=axes[0], color="steelblue")
    axes[0].set_title(f"Original {feature_name}")

    sns.histplot(log_transformed, kde=True, bins=n_samples, ax=axes[1], color="orange")
    axes[1].set_title(f"Log {feature_name}")

    plt.tight_layout()
    plt.show()

plot_feature(df['AHI'], 'AHI')

def plot_spectral_contrast(df: pd.DataFrame) -> None:
    for i in range(0, 7, 2):
        col1, col2 = f"spec_contrast{i}", f"spec_contrast{i+1}"

        if col1 in df.columns and col2 in df.columns:
            fig, axes = plt.subplots(1, 2, figsize=(16, 5))

            series1 = pd.to_numeric(df[col1], errors='coerce')
            sns.histplot(series1, kde=True, bins=len(series1), color="steelblue", ax=axes[0])
            axes[0].set_title(f"Original {col1}")

            series2 = pd.to_numeric(df[col2], errors='coerce')
            sns.histplot(series2, kde=True, bins=len(series2), color="steelblue", ax=axes[1])
            axes[1].set_title(f"Original {col2}")

            plt.tight_layout()
            plt.show()

plot_spectral_contrast(df)

def plot_all_transformations(series: pd.Series, feature_name: str) -> None:
    series_numeric, _ = preprocess(series)

    transformer = PowerTransformer(method='yeo-johnson', standardize=False)
    yeo_transformed = transformer.fit_transform(series_numeric.values.reshape(-1, 1)).ravel()
    yeo_series = pd.Series(yeo_transformed, index=series.index)

    scaler = StandardScaler()
    scaled_values = scaler.fit_transform(series_numeric.values.reshape(-1, 1)).ravel()
    scaled_series = pd.Series(scaled_values, index=series.index)

    data_list = [series_numeric, yeo_series, scaled_series]
    titles = ["Original", "Yeo-Johnson", "Scaled"]

    plt.figure(figsize=(12, 3))
    for i, (data, title) in enumerate(zip(data_list, titles), start=1):
        plt.subplot(1, 3, i)
        sns.histplot(data, bins=37, kde=True)
        plt.title(f"{title}: {feature_name}")

    plt.tight_layout()
    plt.show()

plot_all_transformations(df['AHI'], 'AHI')
