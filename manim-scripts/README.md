# Manim Animations for AI Use Cases in Social Security

This project contains Manim scripts to generate animations explaining various AI techniques applicable to social security organizations.

## Animations Created

1.  **Anomaly Detection**: Visualizes the identification of unusual data points in a stream of normal transactions.
    *   Script: `anomaly_detection_script.py`
    *   Scene name: `AnomalyScene`
2.  **Linear Regression**: Demonstrates how historical data can be used to fit a trend line and make forecasts.
    *   Script: `linear_regression_script.py`
    *   Scene name: `LinearRegressionScene`
3.  **Classification**: Shows how items (e.g., documents) are sorted into predefined categories.
    *   Script: `classification_script.py`
    *   Scene name: `ClassificationScene`

A combined video, `media/videos/combined_ai_use_cases.mp4`, sequences these three animations.

## Setup and Rendering

### Prerequisites
*   Python 3.12 (recommended, as used for development)
*   FFmpeg (Manim dependency for rendering videos)
*   A LaTeX distribution (Manim dependency for text rendering)

### Installation
1.  Clone this repository.
2.  It's highly recommended to use a Python virtual environment:
    ```bash
    python3 -m venv manim_env
    source manim_env/bin/activate
    ```
3.  Install Manim and other Python dependencies:
    ```bash
    pip install manim scikit-learn
    ```
    (Note: `scikit-learn` is used by `linear_regression_script.py`)

### Rendering Individual Animations
To render an animation, navigate to the `manim-scripts` directory and use the `manim` command. For example, to render the Anomaly Detection scene in low quality:

*   **Anomaly Detection:**
    ```bash
    manim -pql anomaly_detection_script.py AnomalyScene
    ```
*   **Linear Regression:**
    ```bash
    manim -pql linear_regression_script.py LinearRegressionScene
    ```
*   **Classification:**
    ```bash
    manim -pql classification_script.py ClassificationScene
    ```
The output videos will be saved in `./media/videos/<script_name>/480p15/`.

## Combined Video
A pre-rendered combined video showcasing all three animations is available at:
`./media/videos/combined_ai_use_cases.mp4`
This video has a total duration of approximately 63 seconds.

## Voiceover Script Draft
The following script is timed for the combined video (approx. 63 seconds):

---

**Segment 1: Introduction & Anomaly Detection (0:00 - 0:26)**
*(Video: `AnomalyScene.mp4` - 26 seconds)*

*   **(0:00 - 0:03) Opening:**
    *   "Artificial Intelligence is transforming how organizations operate, bringing new efficiencies and insights. Let's explore some core AI techniques relevant to social security organizations."
*   **(0:03 - 0:10) Introducing Normal Data:**
    *   "Imagine a constant stream of data, like daily transactions or member interactions. Most of these are routine, forming a baseline of normal activity."
*   **(0:10 - 0:18) Anomalies Appear:**
    *   "But sometimes, unusual events occur – data points that deviate significantly from the norm. These are anomalies."
*   **(0:18 - 0:26) Detection and Importance:**
    *   "AI-powered Anomaly Detection systems are designed to automatically identify these outliers. This is crucial for applications like spotting fraudulent claims, irregular employer contributions, or suspicious account activity, helping to safeguard resources and maintain integrity."

---

**Segment 2: Linear Regression (0:26 - 0:47)**
*(Video: `LinearRegressionScene.mp4` - 21 seconds)*

*   **(0:26 - 0:33) Introducing Linear Regression:**
    *   "Next, let's look at Linear Regression, a statistical method AI uses for prediction. By analyzing historical data, we can uncover trends and relationships."
*   **(0:33 - 0:40) Fitting the Line:**
    *   "Here, we see various data points representing past observations, perhaps contribution amounts over time. Linear regression fits a line that best represents the underlying trend in this data."
*   **(0:40 - 0:47) Forecasting:**
    *   "Once this trend is established, AI can extend this line to forecast future values. This is invaluable for predicting future contribution trends, estimating claim processing times, or projecting long-term pension liabilities."

---

**Segment 3: Classification (0:47 - 1:03)**
*(Video: `ClassificationScene.mp4` - 16 seconds)*

*   **(0:47 - 0:53) Introducing Classification:**
    *   "Another powerful AI technique is Classification. Organizations deal with vast amounts of diverse information that needs to be organized."
*   **(0:53 - 1:00) Sorting into Categories:**
    *   "AI classification models learn to automatically sort these items into predefined categories. For instance, automatically identifying claim types – like withdrawal, pension, or advance – or sorting submitted documents like Aadhaar, PAN, or bank statements."
*   **(1:00 - 1:03) Benefits of Classification:**
    *   "This automated categorization routes information to specialized teams efficiently and can even help in risk profiling of claims for faster processing."

---
