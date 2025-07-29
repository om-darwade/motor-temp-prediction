# Electric Motor Temperature Prediction

This project demonstrates a simple machine learning pipeline using Python to predict the temperature of an electric motor based on voltage, current, and ambient temperature inputs. The model uses **Linear Regression** from the `scikit-learn` library.

## 📌 Objective

To predict the **Motor Temperature** of a Permanent-Magnet Synchronous Machine (PMSM) using:
- Voltage
- Current
- Ambient Temperature

## 🔧 Tools and Libraries

- Python 3.x
- Pandas
- NumPy
- Matplotlib
- Scikit-learn

## 🚀 How It Works

1. **Data Simulation:** Random values are generated for voltage, current, ambient temperature, and motor temperature.
2. **Model Training:** The data is split into training and testing sets.
3. **Model Used:** Linear Regression.
4. **Evaluation:** The model is evaluated using Mean Squared Error and R² Score.
5. **Visualization:** A scatter plot is created comparing actual vs. predicted temperatures.

## 📊 Sample Output

- **Mean Squared Error:** Varies per run (due to random data)
- **R² Score:** Varies per run
- **Visualization:** Actual vs. Predicted motor temperature plot

## 📁 Files

- `motor_temp_prediction.py` - Main script to train and evaluate the model.

## 🧠 Future Improvements

- Use real-world dataset from PMSM drives.
- Experiment with advanced regression models (e.g., Random Forest, XGBoost).
- Build a Flask web interface for input and prediction.

## 👨‍💼 Author

**Om Darwade**

🔗 [LinkedIn Profile](https://www.linkedin.com/in/om-darwade-38118a340)

---

> *Feel free to fork or contribute to improve this project!*
