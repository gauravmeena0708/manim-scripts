# Manim Animation Collection

This repository is a collection of Manim scripts and utilities for creating mathematical animations. It showcases various features and capabilities of the Manim library.

## Purpose

The main purpose of this repository is to:
- Provide a diverse set of examples for users learning Manim.
- Serve as a testing ground for different animation techniques.
- Offer reusable components and scenes that can be adapted for other projects.
- Explore the creative possibilities of mathematical visualization.

## Environment Setup

To run the scripts in this repository, you'll need to set up a Python environment with Manim and its dependencies.

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/your-repository-name.git
    cd your-repository-name
    ```
    (Replace `your-username/your-repository-name` with the actual path if different)

2.  **Create and activate a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

## Running Examples

Manim scripts are typically run from the command line. Here are a few examples from this repository:

1.  **Atom Animation (`atom.py`)**
    *   Description: This script animates a simple model of an atom with a nucleus (proton) and an orbiting electron.
    *   Command:
        ```bash
        manim -pql atom.py AtomAnimation
        ```

2.  **Dice Roll Simulation (`dice.py`)**
    *   Description: This script shows various animations related to dice, including rolling a 3D die, displaying different dice faces, and a grid of 100 dice.
    *   To run the `Dice` scene (3D die roll):
        ```bash
        manim -pql dice.py Dice
        ```
    *   To run the `RoundSquareDots` scene (various 2D dice faces):
        ```bash
        manim -pql dice.py RoundSquareDots
        ```
    *   To run the `HundredDice` scene (grid of 100 dice):
        ```bash
        manim -pql dice.py HundredDice
        ```

3.  **Calculus Explanations (`calculus.py`)**
    *   Description: This file contains multiple scenes demonstrating calculus concepts like Maclaurin series for Sine and equation transformations.
    *   To run the `MaclaurinSine` scene:
        ```bash
        manim -pql calculus.py MaclaurinSine
        ```
    *   To run the `MatchingEquationParts` scene:
        ```bash
        manim -pql calculus.py MatchingEquationParts
        ```

4.  **Sorting Algorithm Visualizations (`sorts.py`)**
    *   Description: This script visualizes sorting algorithms like Insertion Sort and Selection Sort using animated bars.
    *   To run the `InsertionSortScene`:
        ```bash
        manim -pql sorts.py InsertionSortScene
        ```
    *   To run the `SelectionSortScene2` (selection sort with more highlighting):
        ```bash
        manim -pql sorts.py SelectionSortScene2
        ```

**Note:**
*   The `-pql` flags stand for "preview", "quality low". You can use `-pqm` for medium quality or `-pqh` for high quality for rendering videos.
*   Some scripts might contain multiple scenes. You can list them by running `manim <filename>.py` without specifying a scene name.
*   OpenGL-based scripts (like those in `openg.py`) might require a different renderer flag:
    ```bash
    manim --renderer=opengl -pql openg.py OpenGLIntro
    ```

## How to Contribute

Contributions to this repository are welcome! If you have new Manim scripts, improvements to existing ones, or bug fixes, please follow these steps:

1.  **Fork the repository:** Click the 'Fork' button at the top right of this page.
2.  **Clone your fork:**
    ```bash
    git clone https://github.com/your-username/your-forked-repository-name.git
    cd your-forked-repository-name
    ```
3.  **Create a new branch:**
    ```bash
    git checkout -b my-new-feature
    ```
    (Choose a descriptive branch name)
4.  **Make your changes:** Write your code, add comments, and ensure scripts run correctly.
5.  **Commit your changes:**
    ```bash
    git commit -am 'Add some feature'
    ```
6.  **Push to your branch:**
    ```bash
    git push origin my-new-feature
    ```
7.  **Create a Pull Request:** Go to the original repository on GitHub and click the 'New pull request' button. Choose your fork and branch to compare, and submit the pull request with a clear description of your changes.

We appreciate your contributions to making this a valuable resource for the Manim community!

## Inspirations

This repository draws inspiration from various sources, including:
- [https://github.com/kolibril13/mobject-gallery](https://github.com/kolibril13/mobject-gallery)
- [https://github.com/pedrovhb/anims](https://github.com/pedrovhb/anims)
