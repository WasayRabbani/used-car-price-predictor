# Used Car Price Predictor 🚗💰

This project predicts the prices of used cars based on various features like brand, mileage, age, fuel type, engine horsepower, transmission, colors, accident history, and turbo engine.  

The model is built using **Python** and **scikit-learn**, and deployed as a **Streamlit web app** for interactive prediction.

---

## **Features Used**
- Brand
- Fuel Type
- Transmission (Automatic/Manual)
- Exterior Color
- Interior Color
- Mileage
- Car Age
- Engine Horsepower
- Engine Displacement
- Accident History (Yes/No)
- Turbo Engine (Yes/No)

---

## **Models Implemented**
We experimented with 4 models:

1. **Linear Regression**
2. **Polynomial Regression**
3. **Decision Tree Regressor**
4. **Gradient Boosting / Random Forest Regressor**

**Evaluation Metrics:**

- **R² Score**
- **Cross-Validation R²**
- **MAPE (Mean Absolute Percentage Error)**

| Model | R² Score | CV R² | MAPE |
|-------|----------|-------|------|
| Linear Regression | 0.53 | 0.78 | 27.57% |
| Polynomial Regression | 0.62 | 0.80 | 27.35% |
| Decision Tree | 0.66 | 0.82 | 25.00% |
| Gradient Boosting | 0.72 | 0.87 | 21.87% |

> Gradient Boosting gives the best performance among all tested models.

---

## **How to Run Locally**

1. Clone the repository:

```bash
git clone https://github.com/yourusername/used-car-price-predictor.git
cd used-car-price-predictor
