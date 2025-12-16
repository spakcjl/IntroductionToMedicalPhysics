Role: Expert Data Scientist and Professor of Signals and Systems.

Task: Create a massive, detailed RMarkdown presentation (Output: Powerpoint) covering "Chapter 1: Signals and Systems".

Input: Read the file 'chapter1.md' in this repository for definitions and equations.

Note: The source file is a raw text extraction from a PDF. It contains OCR artifacts (e.g., 'Tin' instead of 'pi n', broken integrals like '}~'). You must infer the correct mathematical equations from context and standard Signal Processing conventions.

Constraints:
1.  **Length:** EXACTLY 50 slides. Do not stop early.
2.  **Visual Density:** You must generate **30 to 40 distinct graphical figures**.
    * **Rule:** Almost every concept slide must be accompanied by a generated plot illustrating the math.
    * **Tools:** Use `ggplot2` (R) for discrete plots (stem plots) and `reticulate/matplotlib` (Python) for continuous plots.
3.  **Math:** Use LaTeX for all equations.
4.  **Detail:** No bullet-point only slides. Use the "Speaker Notes" section for deep explanations.

Structure & Coding Requirements (Follow Strictly):

**Section 1: Signals Basics (Slides 1-10)**
* **Slide 2 (R):** Plot a "Speech Signal" simulation (high frequency variations) vs "Vertical Wind Profile" (smooth curve).
* **Slide 3 (R):** Plot a Continuous Sine wave vs. a Discrete Sampled version (Stem plot) on the same graph to define CT vs DT.
* **Slide 5 (Python):** Plot Instantaneous Power $p(t) = v^2(t)/R$ for a decaying exponential voltage $v(t)$.
* **Slide 7 (R):** Calculate and plot the Energy accumulation over time for a finite signal.
* **Slide 9 (Python):** Generate 3 subplots: A signal, the signal shifted right, the signal shifted left.

**Section 2: Transformations (Slides 11-20)**
* **Slide 12 (Python):** Time Reversal. Plot $x(t)$ (an asymmetric triangle) and $x(-t)$.
* **Slide 14 (Python):** Time Scaling. Plot $x(t)$, $x(2t)$ (compressed), and $x(0.5t)$ (stretched).
* **Slide 16 (R):** Periodic vs Aperiodic. Plot $\cos(t)$ (periodic) vs $\cos(t) + \sin(\sqrt{2}t)$ (aperiodic).
* **Slide 18 (R):** Even/Odd Decomposition. Generate an arbitrary sequence $x[n]$ and plot 3 panels: $x[n]$, $Ev\{x[n]\}$, and $Od\{x[n]\}$.

**Section 3: Exponentials (Slides 21-35)**
* **Slide 22 (Python):** Real Exponentials. Plot a family of curves $Ce^{at}$ for various positive and negative $a$.
* **Slide 25 (R):** Complex Exponentials. Plot the Real and Imaginary parts of $e^{j\omega t}$ as 3D or 2-panel 2D plots.
* **Slide 28 (Python):** Damped Sinusoid. Plot $e^{-at}\cos(\omega t)$ to show the "envelope" concept.
* **Slide 30 (R):** **CRITICAL:** Plot Discrete Cosine sequences $\cos(\omega n)$ for $\omega = \pi/8$ (periodic) and $\omega = 1$ (non-periodic) to demonstrate DT periodicity rules.
* **Slide 32 (R):** Frequency Aliasing. Plot $\cos(\omega_0 n)$ and $\cos((\omega_0 + 2\pi)n)$ to show they are identical samples.

**Section 4: Impulses & Steps (Slides 36-42)**
* **Slide 37 (R):** Visualizing the Unit Step $u[n]$ as a running sum of impulses. Animate or show 3 stages of summation.
* **Slide 39 (Python):** The derivative of a step is an impulse. Plot a steep sigmoid function (approx step) and its derivative (approx impulse).
* **Slide 41 (R):** The Sifting Property. Plot a signal $x[n]$ and an impulse $\delta[n-3]$. Show their multiplication isolates the value at $n=3$.

**Section 5: Systems (Slides 43-50)**
* **Slide 44 (Python):** Memory vs Memoryless. Plot input vs output for a Resistor (linear line) vs a Capacitor (hysteresis loop/integral effect).
* **Slide 46 (R):** Invertibility. Plot $y=x^2$ (show ambiguity) vs $y=2x$ (clear mapping).
* **Slide 48 (Python):** Causality. Simulate a non-causal "Smoothing" filter (uses future data) vs a causal filter. Plot the lag.
* **Slide 50 (R):** Stability. Plot the response of a Stable system (decaying) vs Unstable system (exploding) to a step input.

Execution: Generate the RMarkdown code now.