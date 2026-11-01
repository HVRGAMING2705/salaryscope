from pptx import Presentation
from pptx.util import Inches, Pt
prs = Presentation(); prs.slide_width = Inches(13.33); prs.slide_height = Inches(7.5)
def add(i, title, lines):
    s = prs.slides.add_slide(prs.slide_layouts[1])
    s.shapes.title.text = title
    tf = s.placeholders[1].text_frame; tf.word_wrap = True
    for j, ln in enumerate(lines):
        p = tf.paragraphs[0] if j == 0 else tf.add_paragraph()
        p.text = ln; p.font.size = Pt(20); p.space_after = Pt(10)
add(0, "SalaryScope — Salary Predictor", ["An AI/ML project by Vikranth Reddy", "B.Tech CSE (AI & ML), 2nd Year — Woxsen University", "Ridge regression that estimates annual salary right in your browser"])
add(1, "The Problem", ["Job seekers and students have no quick way to check what a profile is worth", "Salary depends on experience, education, skills, internships and city together", "Job-board averages hide how each factor changes the number", "A simple, explainable estimate turns a profile into a realistic salary range"])
add(2, "The Solution — SalaryScope", ["Enter experience, education level, skills, internships, certifications and city tier", "A trained ridge regression model predicts the annual salary in LPA", "The result also shows the approximate yearly amount in rupees", "Runs fully in the browser — no backend, no waiting"])
add(3, "Tech Stack", ["Python + scikit-learn: data generation and model training", "Ridge regression (alpha = 1.0) on standardised features", "HTML, CSS and vanilla JavaScript for the interactive demo", "GitHub for source control, Vercel for free hosting"])
add(4, "Architecture", ["Synthetic dataset: 600 job profiles, 6 features, seed 42", "Standardisation (mean / std) -> Ridge regression -> model.json", "model.json ships with the site; JavaScript applies the same formula", "Prediction is clipped to a realistic 2.5–40 LPA range"])
add(5, "Live Demo", ["Try it: enter a job profile and press Estimate Salary", "Example: 2 years experience, bachelor's, 5 skills, 1 internship, 2 certifications, tier-1 city -> about 12.81 LPA", "Change any input and the estimate updates instantly", "Demo: https://salaryscope.vercel.app"])
add(6, "Results", ["5-fold cross-validation R-squared: 0.938", "Mean absolute error: 1.22 LPA (RMSE 1.54 LPA)", "Baseline (always guessing the average): MAE 5.13 LPA", "The model is about 4.2x better than the baseline guess", "Browser demo matches Python predictions to within 0.01 LPA"])
add(7, "Future Scope", ["Train on real, anonymised salary survey data", "Add a role selector (developer, analyst, designer) and industry", "Compare gradient boosting and small neural networks", "Add a skill-gap panel: which extra skill raises the estimate most"])
add(8, "Thank You", ["SalaryScope — Salary Predictor", "Vikranth Reddy, B.Tech CSE (AI & ML), Woxsen University", "Source: github.com/HVRGAMING2705/salaryscope", "Questions welcome!"])
prs.save("/home/hatch/workspace/goals/daily-ai-ml-project-factory/files/AIML_SalaryScope_2026-11-01.pptx")
print("slides:", len(prs.slides._sldIdLst))
