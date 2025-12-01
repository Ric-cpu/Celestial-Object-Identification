import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.metrics import classification_report

# Paths 
EXO_PATH = "data/exoplanets_clean.csv"  # hosts (positives)
STARS_PATH = "data/stars_gaia_sample.csv" # non-hosts (negatives)

if __name__ == "__main__":
    # Load host (positives)
    hosts = pd.read_csv(EXO_PATH).rename(columns={"sy_plx": "parallax"})
    hosts = hosts[["ra", "dec", "parallax"]].assign(label=1)
#load non-host (negatives)
    stars = pd.read_csv(STARS_PATH)
    stars = stars[["ra", "dec", "parallax"]].assign(label=0)
#combine and clean
    df = pd.concat([hosts, stars], ignore_index=True).dropna()
    X = df[["ra", "dec", "parallax"]]
    y = df["label"]

    print("class counts:", y.value_counts().to_dict())

#Train/Val split and model
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, stratify=y, random_state=42
    )

    clf = make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000, class_weight="balanced"))
    clf.fit(X_train, y_train)
    #evaluate 
    y_pred = clf.predict(X_test)
    print(classification_report(y_test, y_pred, target_names=["nonhost", "host"]))
