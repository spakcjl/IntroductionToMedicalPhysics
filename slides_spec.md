###**New Master Prompt**

**Role:** Expert Signal Processing Professor and RMarkdown Developer.

**Task:** Create a massive, **highly granular** RMarkdown presentation (Output: PowerPoint) for "Chapter 1: Signals and Systems".

**Input:** Read `chapter1.md`. Use specific definitions/examples (Dow Jones, Wind Profile) from the text.

**Critical Adjustments for Length & Depth:**

1. **Slide Count:** You must generate **at least 55 slides**.
2. **Pacing:** Do not compress topics. Use a **"Concept \to Math \to Visualization \to Real-world Example"** flow for *every* major topic.
3. **Dynamical Visuals:** You must use **`gganimate` (in R)** to create animated visualizations for time-shifting and sampling. *Note: If compiling to static PPTX, output these as a sequence of 3 distinct "frame" plots instead of a GIF, but write the code to support animation.*
4. **Math:** Use LaTeX for all equations.

**Detailed Execution Plan (Follow Exactly):**

**Part 1: Deep Dive into Signals (Slides 1-12)**

* **Slides 1-3:** Introduction. Define CT vs DT.
* *Visual (R):* Plot the "Vertical Wind Profile" (CT) from the text data.


* **Slides 4-7:** The Concept of Sampling.
* *Visual (R):* **Sequence:** Plot a Sine wave. Next slide: Overlay sample points. Next slide: Show *only* the stem plot. Explain that information between points is lost.


* **Slides 8-12:** Energy vs. Power.
* *Visual (Python):* Define a voltage signal v(t) = 5e^{-0.2t}. Plot Instantaneous Power p(t) in top panel and Cumulative Energy E(t) in bottom panel. Show how Energy converges while Power goes to zero.



**Part 2: Dynamic Transformations (Slides 13-26)**

* **Slides 13-16:** Time Shifting (t-t_0).
* *Visual (R - Dynamic):* Create a plot showing a pulse signal x(t). Generate 3 separate plots showing the pulse at t=0, t=2 (delayed), and t=-2 (advanced) to simulate motion.


* **Slides 17-20:** Time Scaling (at).
* *Visual (Python):* Plot x(t) vs x(2t) vs x(0.5t). Explicitly mark the zero-crossings to prove compression/expansion.


* **Slides 21-26:** Even/Odd Decomposition.
* *Theory:* Prove algebra for Ev\{x\} and Od\{x\}.
* *Visual (R):* Generate a random discrete sequence. Plot the Original, the Even component, and the Odd component on 3 separate slides to show how they sum back to the original.



**Part 3: The Complex Exponential Family (Slides 27-42)**

* **Slides 27-30:** Real Exponentials.
* *Visual (Python):* Plot the "Time Constant" concept. Show e^{-t/\tau} for \tau = 0.5, 1, 5. Explain decay rates.


* **Slides 31-36:** Periodic Complex Exponentials & Euler.
* *Visual (R):* **3D Plot:** Use `plotly` or 2D projection to show a "Corkscrew" spiral of e^{j\omega t} in 3D (Time, Real, Imag) to explain why it projects to Sine/Cosine.


* **Slides 37-42:** Discrete Periodicity (The "Aliasing" Trap).
* *Visual (R):* Plot \cos(\omega n) for \omega = \pi/4 (8 samples/cycle) and \omega = 9\pi/4. Show they land on the *exact same points*. This explains why high frequencies alias in DT.



**Part 4: Singularity Functions (Slides 43-52)**

* **Slides 43-47:** The Unit Impulse \delta[n] and Step u[n].
* *Visual (R):* **"Running Sum" Animation Sequence.** Show \delta[n], then \delta[n] + \delta[n-1], then the full step u[n].


* **Slides 48-52:** The Continuous Impulse \delta(t).
* *Visual (Python):* The "Rectangular Approximation". Plot rectangles of width \Delta and height 1/\Delta. Show 3 plots as \Delta gets smaller (0.5, 0.1, 0.01) to visualize the limit approaching an impulse.



**Part 5: System Properties (Slides 53-60+)**

* **Slides 53-56:** Linearity (Superposition).
* *Visual (Python):* Define a nonlinear system y=x^2. Plot T(x_1+x_2) vs T(x_1)+T(x_2) to visually prove they do not match.


* **Slides 57-60:** Time Invariance.
* *Visual (R):* Input a pulse at t=0, record output. Input pulse at t=5. Plot both outputs to check if they are identical (shifted) shapes.


## Styling
* Use standard academic theme.
* Ensure all LaTeX equations are rendered correctly (e.g., $$E_{\infty}$$).
* **Speaker Notes:** Use Pandoc div syntax for all speaker notes. Format them exactly as: `::: notes` [line break] (Note content) [line break] `:::`. Do NOT use `>` blockquotes.

**Output Generation:**
Generate the full RMarkdown code now. Ensure `echo=FALSE` for plots so code is hidden in slides.





