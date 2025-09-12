# Time-Sense Journal 🕰️

*A cognitive journaling tool for estimating temporal awareness*

## 🩺 Purpose

This app is designed **strictly for medical and cognitive assessment purposes**. It helps users develop and evaluate their **time-telling and orientation ability** by prompting them to estimate the current:

* Time (HH\:MM)
* Day of the week
* Date (DD/MM/YYYY)
* Month and Year

The app logs both the user's input and the actual correct values for review and analysis by medical or psychological professionals.

---

## 📦 Features

* Simple and minimal command-line interface (CLI)
* Prompts for time, day, date, month, and year
* Compares user input with actual system time
* Stores entries in a local journal file (e.g., CSV or JSON)
* Optional daily reminders
* Easy export for review by professionals

---

## 🧠 Use Cases

* Cognitive rehabilitation for patients with memory impairments
* Self-monitoring tool for neuropsychological assessments
* Part of routine for individuals recovering from brain injury or neurological conditions
* Medical research into time orientation and temporal estimation

---

## 🛠️ Installation

```bash
git clone https://github.com/abed5/time-sense-journal.git  
cd time-sense-journal  
pip install -r requirements.txt  
python app.py  
```

---

## ▶️ Usage

```bash
python app.py
```

You will be prompted to enter your best guess for:

* Current time (HH\:MM, 24-hour format)
* Day of the week
* Full date
* Current month and year

All guesses are logged with timestamps and compared to the actual values.

---

## 🗂️ Data Logging

Data is saved locally in a `.csv` or `.json` file, containing:

* User estimates
* Actual system values
* Time difference metrics (e.g., minutes off)
* Timestamp of entry

Example:

```
| Timestamp          | Guessed Time | Actual Time | Error (min) | Guessed Date | Actual Date | ... |
|--------------------|--------------|-------------|-------------|---------------|--------------|-----|
| 2025-08-03 10:12AM | 10:30        | 10:12       | +18         | ...           | ...          |     |
```

---

## ⚠️ Medical Disclaimer

> **This tool is not a diagnostic device.**
> It is intended as a **support tool for medical professionals** or for **personal use under medical supervision**. Do not use this software for self-diagnosis or decision-making without consulting a qualified health provider.

---

## 🚧 Future Improvements

* GUI version with calendar and analog clock interface
* User profiles for long-term tracking
* Data encryption for privacy and HIPAA compliance
* Integration with medical data systems

---

## 📄 License

MIT License – see [LICENSE](LICENSE) for more information.

---

## 🙋 Support & Contributions

If you are a medical professional or developer interested in collaborating or improving the app, feel free to open an issue or submit a pull request.

---