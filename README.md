# Manim Animation Collection

This repository is a collection of Manim scripts and utilities for creating mathematical animations. It's structured to organize scenes, reusable code, and assets effectively.

## Project Structure

The repository is organized as follows:

-   `README.md`: This file, providing an overview of the project.
-   `requirements.txt`: Specifies the Python dependencies for this project.
-   `.gitignore`: Lists files and directories that Git should ignore (e.g., cache files, virtual environments).
-   `scenes/`: Contains all Manim scene scripts. Each `.py` file in this directory typically defines one or more Manim scenes.
    -   `scenes/example_scene.py`: An example of how a scene file could be structured (you can create this or use an existing one as an example).
-   `src/`: Houses custom Python modules, utility functions, or custom Manim Mobjects that can be reused across different scenes.
    -   `src/__init__.py`: An empty file that makes the `src/` directory a Python package, allowing for easier imports.
    -   `src/custom_utils.py`: An example of a utility module where you might place helper functions or custom classes (you can create this).
-   `assets/`: Stores static files such as images, sound files, data files (e.g., CSV, JSON), etc., that your Manim scenes might need.
-   `tests/`: Contains unit tests for your custom modules and potentially for scenes to ensure they behave as expected.

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

3.  **Install LaTeX:**
    Manim requires a LaTeX distribution for rendering text and formulas. Install a LaTeX distribution suitable for your operating system:
    *   **Debian/Ubuntu:**
        ```bash
        sudo apt-get install texlive-full
        ```
    *   **macOS (using MacPorts):**
        ```bash
        sudo port install texlive-full
        ```
    *   **macOS (using Homebrew):**
        ```bash
        brew install --cask mactex
        ```
    *   **Windows (using MiKTeX):**
        Download and install MiKTeX from [https://miktex.org/download](https://miktex.org/download). A full installation is recommended.
    *   **Windows (using Chocolatey):**
        ```powershell
        choco install miktex --params="--shared"
        ```
        (Ensure you run PowerShell as Administrator)

4.  **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

## How to Use This Structure

-   **New Scenes:** Place all new Manim scene scripts (Python files containing classes derived from `Scene`) into the `scenes/` directory.
-   **Reusable Code:** If you develop utility functions, custom Mobjects, or any other Python code that you intend to reuse across multiple scenes, place it within the `src/` directory. You can organize `src/` into sub-modules if needed. For example, from a scene in `scenes/my_scene.py`, you could import a utility function like this:
    ```python
    from src.custom_utils import my_helper_function
    from src.custom_mobjects import MyCustomMobject
    ```
-   **Assets:** Any external files like images, sound clips, or data files should be placed in the `assets/` directory. When referencing these in your scenes, use a path relative to the project root, e.g., `assets/my_image.png` or `assets/data/my_data.csv`. Manim's `ImageMobject("assets/my_image.png")` will correctly locate the file.

## Running Examples

To run Manim scripts, navigate to the root directory of this project in your terminal. Here are examples of how to render scenes now that they are in the `scenes/` directory:

1.  **Atom Animation (`scenes/atom.py`)**
    *   Command:
        ```bash
        manim -pql scenes/atom.py AtomAnimation
        ```

2.  **Dice Roll Simulation (`scenes/dice.py`)**
    *   To run the `Dice` scene:
        ```bash
        manim -pql scenes/dice.py Dice
        ```

3.  **Calculus Explanations (`scenes/calculus.py`)**
    *   To run the `MaclaurinSine` scene:
        ```bash
        manim -pql scenes/calculus.py MaclaurinSine
        ```

4.  **Sorting Algorithm Visualizations (`scenes/sorts.py`)**
    *   To run the `InsertionSortScene`:
        ```bash
        manim -pql scenes/sorts.py InsertionSortScene
        ```

5.  **OpenGL Example (`scenes/openg.py`)**
    *   If you have scenes requiring the OpenGL renderer:
        ```bash
        manim --renderer=opengl -pql scenes/openg.py OpenGLIntro
        ```

**Note:**
*   The `-pql` flags stand for "preview", "quality low". Use `-pqm` for medium quality or `-pqh` for high quality.
*   To list all scenes in a file: `manim scenes/your_script_name.py`

## How to Contribute

Contributions to this repository are welcome! If you have new Manim scripts, improvements to existing ones, or bug fixes, please follow these steps:

1.  **Fork the repository.**
2.  **Clone your fork.**
3.  **Create a new branch** (`git checkout -b my-new-feature`).
4.  **Make your changes.** Ensure your code follows the project structure (scenes in `scenes/`, reusable code in `src/`).
5.  **Commit your changes** (`git commit -am 'Add some feature'`).
6.  **Push to your branch** (`git push origin my-new-feature`).
7.  **Create a Pull Request.**

## Inspirations

This repository and its structure draw inspiration from common practices in software development and from various sources in the Manim community, including:
- [https://github.com/kolibril13/mobject-gallery](https://github.com/kolibril13/mobject-gallery)
- [https://github.com/pedrovhb/anims](https://github.com/pedrovhb/anims)
- General Python project structuring guidelines.
