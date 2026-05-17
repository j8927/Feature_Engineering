from pathlib import Path
from src.data_loader import load_titanic
from src.feature_engineering import add_titanic_features
from src.eda import run_eda
from src.modeling import run_experiments, run_grid_search_for_best
from src.visualize_results import plot_metrics


def main():
    Path("results/metrics").mkdir(parents=True, exist_ok=True)
    Path("results/figures").mkdir(parents=True, exist_ok=True)

    df = load_titanic("data/titanic.csv")
    print("Dataset shape:", df.shape)
    print(df.info())

    # EDA before feature engineering
    missing = run_eda(df)
    print("\nMissing ratio top 10")
    print(missing.head(10))

    # Feature engineering
    df_fe = add_titanic_features(df)
    df_fe.to_csv("results/metrics/titanic_feature_engineered.csv", index=False)

    # Model comparison
    results = run_experiments(df_fe)
    results.to_csv("results/metrics/experiment_results.csv", index=False)
    print("\nExperiment Results")
    print(results)
    plot_metrics(results)

    # Additional point: GridSearchCV
    grid_result = run_grid_search_for_best(df_fe)
    grid_result.to_csv("results/metrics/gridsearch_result.csv", index=False)
    print("\nGridSearchCV Result")
    print(grid_result)


if __name__ == "__main__":
    main()
