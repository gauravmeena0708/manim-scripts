
**Objective:** Create a complete Python Manim script for a short educational animation (approximately 30-60 seconds) explaining the concept of **[INSERT YOUR CORE CONCEPT HERE - e.g., "Photosynthesis," "The Doppler Effect," "Basic Structure of a Neural Network Neuron," "How a Transistor Works as a Switch"].**

**Target Audience:** [Specify - e.g., "High school biology students," "General public with an interest in physics," "Beginners learning about AI," "Electronics hobbyists"]

**Core Visual Narrative & Key Scenes:**

1.  **Scene 1: Introduction & Title (approx. 5-7 seconds)**
    *   **Visuals:** Clean title card. The main concept title should be prominent. Perhaps a subtle, related background icon or element.
    *   **Text:** "[Your Concept Title]" and optionally a subtitle like "A Visual Explanation."
    *   **Animation:** Title animates in (e.g., `Write`, `FadeIn`, `GrowFromCenter`).

2.  **Scene 2: Breaking Down [Component/Step 1 of your concept] (approx. 10-15 seconds)**
    *   **Visuals:**
        *   Introduce the first key element(s) visually. [Describe the shapes, icons, or simple diagrams you envision - e.g., "For Photosynthesis: Show a sun, a leaf, and water molecules (H2O) as simple circles/icons."].
        *   Use arrows or motion to show interaction or input if applicable.
    *   **Text (Labels/Annotations):** Short, clear labels for each element introduced. [e.g., "Sunlight," "Water (H2O)," "Carbon Dioxide (CO2)"].
    *   **Animation:** Elements fade in or are drawn. Labels appear near their respective elements. Use `Transform` or `Indicate` to highlight key interactions.

3.  **Scene 3: Explaining [Component/Step 2 or Process of your concept] (approx. 10-15 seconds)**
    *   **Visuals:**
        *   Show the transformation or process occurring. [Describe this - e.g., "For Photosynthesis: Inside the leaf (perhaps a magnified chloroplast-like shape), show H2O and CO2 combining/transforming. Represent energy input from the sun."].
        *   Introduce new elements or outputs if they arise here. [e.g., "Oxygen (O2) molecules and Glucose (C6H12O6) as different icons/shapes."].
    *   **Text (Labels/Annotations):** Labels for new elements or process steps. A very brief caption explaining what's happening.
    *   **Animation:** Use `Transform` to show changes. Output elements could `GrowFromCenter` or move out from the reaction site. Animate a simple equation if relevant [e.g., `CO2 + H2O + Light -> C6H12O6 + O2` using `Tex` or `MathTex`].

4.  **Scene 4: [Optional: Further detail, application, or consequence] (approx. 5-10 seconds)**
    *   **Visuals:** [Describe - e.g., "For Photosynthesis: Show the O2 being released from the leaf. Briefly show the glucose being used by the plant for growth (e.g., a small sapling growing slightly)."].
    *   **Text:** A short concluding point or significance.
    *   **Animation:** Simple fades or transformations.

5.  **Scene 5: Summary/Outro (approx. 5 seconds)**
    *   **Visuals:** A clean screen, perhaps with a key takeaway visual or a "Thank You" / "Learn More" message.
    *   **Text:** "Key Takeaway: [Your brief summary]" or "End."
    *   **Animation:** Text fades in and out.

**Manim Specifics & Style:**

*   **Overall Style:** [Choose one or combine: "Clean and minimalist," "Colorful and engaging," "Textbook diagram style," "3Blue1Brown-inspired (if applicable to the concept, e.g., using NumberPlanes, vectors, transformations for math/physics concepts)"].
*   **Colors:** Suggest a primary color palette (e.g., "Use blues, greens, and yellows primarily. Use RED for emphasis/warnings if needed.").
*   **Fonts:** Prefer clear, sans-serif fonts for text and labels.
*   **Mobject Usage:**
    *   Use `Text` for titles and labels.
    *   Use `Circle`, `Square`, `Rectangle`, `Line`, `Arrow`, `Dot` for basic shapes.
    *   Use `Tex` or `MathTex` for formulas or chemical equations.
    *   Consider `VGroup` to group related elements for easier animation.
    *   Use animations like `Write`, `Create`, `FadeIn`, `FadeOut`, `Transform`, `MoveTo`, `Indicate`, `GrowFromCenter`, `LaggedStart`.
*   **Code Structure:**
    *   Generate a single Python file.
    *   Use separate Manim `Scene` classes for each of the scenes described above (e.g., `TitleScene`, `Step1Scene`, `ProcessScene`, etc.) if it helps with organization, OR combine into fewer scenes if the flow is very continuous.
    *   Include necessary imports (e.g., `from manim import *`).
    *   Add comments in the code to explain key sections or complex animations.
*   **Transitions:** Smooth transitions between scenes (e.g., `FadeOut` all elements of the previous scene, then `FadeIn` elements of the new one, or more creative transitions if you have ideas).

**Example Placeholder (Replace with your actual concept details):**
*   **[INSERT YOUR CORE CONCEPT HERE]:** "The Basic Water Cycle"
*   **Target Audience:** "Elementary school students"
*   **Scene 2 Visuals for Water Cycle:** "Show sun icon, a body of water (blue rectangle), and small water drop icons."
*   **Scene 2 Labels for Water Cycle:** "Sun," "Ocean," "Water."
*   **Scene 3 Visuals for Water Cycle:** "Show water drops rising from ocean (evaporation - animated with upward motion and becoming 'cloud' like shapes). Clouds moving. Then drops falling from clouds (precipitation)."
*   **Overall Style for Water Cycle:** "Colorful and engaging with simple, friendly icons."

**Please generate the Manim script based on these specifications.**
