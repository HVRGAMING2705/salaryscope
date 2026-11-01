import json, numpy as np
from sklearn.linear_model import Ridge
from sklearn.model_selection import cross_val_predict, KFold
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

rng = np.random.default_rng(42)
n = 600
exp = rng.uniform(0, 20, n)          # years of experience
edu = rng.integers(1, 5, n)          # 1 diploma, 2 bachelor's, 3 master's, 4 PhD
skills = rng.integers(0, 16, n)      # relevant technical skills
intern = rng.integers(0, 6, n)       # internships completed
certs = rng.integers(0, 11, n)       # certifications
city = rng.integers(1, 4, n)         # 1 tier-2 city, 2 tier-1 city, 3 metro
# Generative salary in LPA: experience and education dominate, skills/internships/certs add, metros pay more
y = (3.0 + 0.90 * exp + 1.20 * edu + 0.35 * skills + 0.80 * intern
     + 0.40 * certs + 1.00 * city + rng.normal(0, 1.5, n))
y = np.clip(y, 2.5, 40.0)
X = np.column_stack([exp, edu, skills, intern, certs, city]).astype(float)
names = ["exp_years", "edu_level", "skills_count", "internships", "certs_count", "city_tier"]
mu, sd = X.mean(0), X.std(0)
Xs = (X - mu) / sd
model = Ridge(alpha=1.0).fit(Xs, y)
kf = KFold(5, shuffle=True, random_state=42)
pred_cv = cross_val_predict(Ridge(alpha=1.0), Xs, y, cv=kf)
r2 = float(r2_score(y, pred_cv)); mae = float(mean_absolute_error(y, pred_cv))
rmse = float(np.sqrt(mean_squared_error(y, pred_cv)))
base_mae = float(mean_absolute_error(y, np.full(n, y.mean())))
print(f"CV R2={r2:.3f} MAE={mae:.2f} RMSE={rmse:.2f} baseline_MAE={base_mae:.2f} mean_salary={y.mean():.2f}")
print("coef", model.coef_, "intercept", model.intercept_)
mj = {"features": names, "means": mu.tolist(), "stds": sd.tolist(),
      "coef": model.coef_.tolist(), "intercept": float(model.intercept_),
      "metrics": {"cv_r2": r2, "cv_mae": mae, "cv_rmse": rmse, "baseline_mae": base_mae, "mean_salary": float(y.mean()), "n": n}}
with open("model.json", "w") as f: json.dump(mj, f, indent=1)

def predict(v):
    z = (np.array(v, dtype=float) - mu) / sd
    return float(model.intercept_ + z @ model.coef_)
samples = [[2, 2, 5, 1, 2, 2], [10, 3, 10, 3, 5, 3],
           [0, 1, 2, 0, 0, 1], [15, 4, 14, 5, 8, 3],
           [5, 2, 8, 2, 3, 2]]
for s in samples: print(s, round(predict(s), 2))
