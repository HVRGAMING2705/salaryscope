# SalaryScope — Salary Predictor

A 2nd-year B.Tech AI/ML project by Vikranth Reddy (Woxsen University).

## What it does
Predicts annual salary (in LPA) from years of experience, education level, technical skills, internships, certifications and city tier.

## Model
- Ridge regression (alpha = 1.0) on standardised features
- Trained on 600 synthetic job profiles (seed 42)
- 5-fold cross-validation: R² = 0.938, MAE = 1.22 LPA, RMSE = 1.54 LPA
- Baseline (predict the mean): MAE = 5.13 LPA — the model is ~4.2x better

## Files
- `train.py` — generates data, trains the model, writes `model.json`
- `model.json` — learned means, standard deviations, coefficients, intercept
- `index.html` — interactive demo; the browser runs the exact same weights as Python

## Live demo
https://salaryscope-omega.vercel.app
