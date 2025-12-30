Course Guide: The Fourier Transform in Medical Imaging

From Principles to Practice

Lecturer Role: Senior Lecturer in Medical Physics
Target Audience: Graduate Students (Physics background, minimal signal processing experience)
Duration: 120 Minutes (4 Modules, ~30 mins each)

Module 1: The Foundation

Duration: 0–30 Minutes

1.1 Intuition First: The Musical Chord (0-10 mins)

The Concept:
Before we touch a single equation, we must understand decomposition. We often think of signals (sound, light, MR echoes) as single, unified entities. In reality, they are composites. Imagine striking a C-Major chord on a piano. You hear one rich sound. But that sound is actually composed of three distinct notes (C, E, G) vibrating at specific frequencies. The Fourier Transform is simply the mathematical ear that hears the chord (the complex signal) and tells you exactly which notes (frequencies) created it and how loud each one is.

Visual Aid Description:

Slide 1: A picture of a prism splitting white light into a rainbow.

Slide 2: A waveform diagram showing three distinct sine waves (frequencies $f$, $1.5f$, $2f$) in different colors, and then a fourth graph showing them summed together into a complex, jagged waveform.

Lecturer Script:
"Good morning, everyone. Welcome to what is arguably the most important mathematical concept in medical imaging: The Fourier Transform.

I want to start by asking you to close your eyes for a second. Imagine I am sitting at a grand piano. I strike three keys simultaneously—a C, an E, and a G. You hear a single, rich sound—a chord. Your ear doesn't need to do any calculations to understand this. Instantly, your brain processes that complex pressure wave hitting your eardrum and breaks it down: you hear the bass of the C, the harmony of the E, and the treble of the G.

Open your eyes. What your ear just did is exactly what we need to do in MRI.

In Magnetic Resonance Imaging, we do not take a picture of the brain. We cannot simply 'photograph' protons. Instead, we listen to them. We record the 'musical chord' sung by the hydrogen atoms in your body. This signal is a complex, jumbled mess of radio waves.

The Fourier Transform is the mathematical machine that acts like your ear. It takes that complex signal and unmixes it. It tells us: 'This much signal came from the left ear, and this much came from the nose.' It acts like a prism, splitting the white light of the raw data into the color spectrum of the final image. Without Fourier, MRI is just a noisy radio recording. With it, it is a diagnostic miracle."

1.2 The Fourier Series (10-20 mins)

The Concept:
Joseph Fourier's insight was that any periodic function, no matter how jagged, discontinuous, or square, can be constructed by adding together infinite smooth sine and cosine waves.

The Math:
The Fourier Series for a periodic function $f(t)$ with period $T$:

$$f(t) = a_0 + \sum_{n=1}^{\infty} \left( a_n \cos(n\omega_0 t) + b_n \sin(n\omega_0 t) \right)$$

Where:

$a_0$: The "DC offset" or average value of the signal.

$\omega_0$: The fundamental frequency ($2\pi/T$).

$n$: The harmonic index (1st harmonic, 2nd harmonic, etc.).

$a_n, b_n$: The "weights" or amplitudes of each frequency component.

Lecturer Script:
"Let's formalize this. In the early 1800s, Joseph Fourier proposed an idea that his contemporaries thought was insane. He claimed that you could build any repeating shape using only smooth, curving waves.

Look at the equation on the board.
$a_0$ is simply the average. If we are imaging a liver, $a_0$ is the average brightness of the whole liver.
Then we have the summation. We start with a fundamental frequency—a simple sine wave. It's too round to look like a square pixel. So, what do we do? We add a second wave, twice as fast, but maybe with a smaller amplitude. Then a third, three times as fast.

If I want to build a square wave—which represents a sharp edge in an image—I need to stack many sine waves. The low-frequency waves give me the general 'up and down' shape. The high-frequency waves—the ones where $n$ is large—sharpen the corners.

Crucial Point: If we stop the summation early—say we only add the first 5 waves—our square wave looks 'wobbly.' The corners are soft. In MRI, this corresponds to a low-resolution image. If we want sharp edges (high resolution), we need to collect high values of $n$. We need the high frequencies."

1.3 Euler's Formula: The Rotation Machine (20-30 mins)

The Concept:
Sines and cosines are difficult to manipulate algebraically. We use Euler's formula to treat oscillation as rotation. This allows us to visualize the Fourier Transform not just as waves, but as a "winding" process.

The Math:
Euler's Identity:

$$e^{i\theta} = \cos(\theta) + i\sin(\theta)$$

The General Fourier Transform equation:

$$F(\omega) = \int_{-\infty}^{\infty} f(t) e^{-i\omega t} dt$$

Lecturer Script:
"Now, we transition from the Series (for repeating signals) to the Transform (for any signal). And we meet the equation that scares every undergraduate: the complex exponential.

Don't let the imaginary number $i$ intimidate you. In this class, we treat $e^{i\theta}$ physically. It is a rotation machine.
Imagine a clock hand spinning on a face. If you look at that clock from the side, the tip of the hand traces a sine wave moving up and down.

So, look at the Transform equation: $\int f(t) e^{-i\omega t} dt$.
What is this actually doing?

We take our signal, $f(t)$.

We multiply it by a 'winding machine', $e^{-i\omega t}$, which spins at a specific speed $\omega$.

We sum up (integrate) the result over time.

Think of it this way: We wrap our signal around a circle.
If the signal has a periodic pattern that matches the winding speed $\omega$, all the 'bumps' in the signal line up on one side of the circle. The center of mass shifts. The integral becomes large. We get a spike in the spectrum.
If the winding speed $\omega$ doesn't match the signal, the signal wraps around the circle randomly. The positive parts cancel the negative parts. The average is zero.

The Fourier Transform is effectively asking: 'If I wind this signal at speed $\omega$, does it pile up?' If yes, that frequency exists in the signal."

1.4 Python Code: Square Wave Approximation

Code to demonstrate the summation of sines to create a square wave.

import numpy as np
import matplotlib.pyplot as plt

# Setup time domain
t = np.linspace(0, 4*np.pi, 1000)
square_approx = np.zeros_like(t)
# We use odd harmonics for a square wave (1, 3, 5, etc.)
terms = [1, 3, 5, 7, 9, 11, 13, 15]

plt.figure(figsize=(12, 8))

# Subplot 1: The individual components
plt.subplot(2, 1, 1)
plt.title("Individual Frequency Components")
colors = plt.cm.viridis(np.linspace(0, 1, len(terms[:4])))
for i, n in enumerate(terms[:4]): # Plot first 4 components
    amplitude = (4/np.pi) * (1/n)
    component = amplitude * np.sin(n * t)
    plt.plot(t, component, label=f'Harmonic n={n}', color=colors[i], linewidth=1.5)
plt.legend(loc='upper right')
plt.grid(True, alpha=0.3)

# Subplot 2: The Summation
plt.subplot(2, 1, 2)
plt.title("Summation: Building the Square Wave")
for n in terms:
    square_approx += (4/np.pi) * (1/n) * np.sin(n * t)

plt.plot(t, square_approx, 'k-', linewidth=2, label=f'Sum of first {len(terms)} terms')
# Overlay the ideal square wave for comparison
ideal_square = np.sign(np.sin(t))
plt.plot(t, ideal_square, 'r--', alpha=0.4, label='Ideal Square Wave')

plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend(loc='upper right')
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()


Module 2: The Digital Domain & FFT

Duration: 30–60 Minutes

2.1 Continuous to Discrete (30-40 mins)

The Concept:
Real life physics is continuous (analog). However, computers and MRI scanners are discrete (digital). We cannot integrate from $-\infty$ to $+\infty$. We have to take snapshots (samples) at fixed intervals. This creates the "pixel."

The Math:
The Discrete Fourier Transform (DFT):

$$X_k = \sum_{n=0}^{N-1} x_n e^{-i 2\pi k n / N}$$

Lecturer Script:
"The integral we just looked at is mathematically beautiful, but computationally impossible. A computer cannot store a continuous function; it has finite memory. It can only store a list of numbers.
In MRI, the scanner reads the signal at specific time points: $t_0, t_1, t_2...$ This is called sampling.

Consequently, we must swap our tools.

The Integral ($\int$) becomes a Summation ($\sum$).

The continuous time $t$ becomes an index $n$ (sample number 1, sample number 2...).

The infinite range becomes a finite number of samples $N$.

This equation on the slide—the DFT—is the workhorse of modern medical imaging. Every time you see a reconstructed MR image, this specific summation has been calculated millions of times."

2.2 Sampling and Aliasing (40-50 mins)

The Concept:
The Nyquist-Shannon Theorem states that to accurately digitize a signal of frequency $f$, you must sample at a rate of at least $2f$. If you sample too slowly, high-frequency signals are misinterpreted as low-frequency signals. This is called Aliasing.

Visual Aid Description:

Slide: The "Wagon Wheel" effect. A diagram showing a sine wave oscillating rapidly. Below it, sample points are taken at large intervals. When you connect the dots of the sample points, it draws a new wave that is much slower than the original.

Lecturer Script:
"We have to be careful when we sample. Has anyone ever watched a video of a car driving on the highway, and the wheels look like they are spinning backwards?
That is Aliasing.
The camera is taking pictures (sampling) at 30 frames per second. The wheel is spinning faster than that. Between one frame and the next, the wheel spins almost all the way around, so it looks like it moved slightly backward.

The camera—the sampler—lied to you. It told you the frequency was $-5$ Hz when it was actually $+100$ Hz.

In MRI, this is a disaster. If the signal from the patient changes faster than our scanner samples it, that high-frequency data (usually edges or noise) will 'fold over' and appear as low-frequency data in the wrong part of the image. This leads to the 'Wrap-Around Artifact,' where a patient's nose might wrap around and appear inside the back of their head."

2.3 The Fast Fourier Transform (FFT) (50-60 mins)

The Concept:
The FFT is not a new mathematical concept; it is an efficient algorithm for calculating the DFT.

Naive DFT: Complexity $O(N^2)$. If $N=1000$, operations = $1,000,000$.

FFT: Complexity $O(N \log N)$. If $N=1000$, operations = $\approx 10,000$.
This speed difference is the only reason real-time MRI is possible.

Lecturer Script:
"You will often hear 'DFT' and 'FFT' used interchangeably. They result in the same numbers, but the difference is speed.
Imagine you have an image that is $256 \times 256$ pixels.
If you use the standard DFT definition, the computer has to do roughly $N$ squared operations. For high-resolution medical images, this would take minutes, maybe hours on older hardware.

In 1965, Cooley and Tukey popularized the FFT. They realized that the calculation repeats itself. By dividing the samples into even and odd groups, computing them separately, and combining them, you save massive amounts of time.
The FFT allows us to reconstruct an MRI slice in milliseconds. Without this algorithm, MRI would be a slow, academic curiosity, not a clinical tool used in emergency rooms."

Module 3: Higher Dimensions & K-Space

Duration: 60–90 Minutes

3.1 The Leap to 2D (60-70 mins)

The Concept:
So far we discussed 1D signals (sound). An image is a 2D signal. A 1D wave is a ripple on a string; a 2D wave is a "corrugated sheet" or a pattern of stripes. It has three properties:

Amplitude: How bright the stripes are.

Frequency: How close the stripes are packed.

Orientation: The angle of the stripes (vertical, horizontal, diagonal).

Visual Aid Description:

Slide: Images of 2D sine waves ("gratings").

Image A: Wide vertical bars (Low freq, x-direction).

Image B: Thin horizontal bars (High freq, y-direction).

Image C: Diagonal bars.

Lecturer Script:
"Now we move from sound to sight. From 1D to 2D.
When we perform a Fourier Transform on an image, we are decomposing the picture into layers of stripes.
I want you to imagine a clear plastic sheet with wide vertical black bars painted on it.
Now imagine another sheet with thin horizontal bars.
If I stack thousands of these sheets—some with diagonal bars, some thick, some thin—and I look through the whole stack, the overlapping patterns will form a picture. That is the Inverse 2D Fourier Transform. We are building an image out of gratings."

3.2 Defining K-Space (70-80 mins)

The Concept:
K-Space is the "frequency domain" map of the image. It is a coordinate system $(k_x, k_y)$.

$k_x$ axis: Represents horizontal frequencies (vertical stripes).

$k_y$ axis: Represents vertical frequencies (horizontal stripes).

Center $(0,0)$: Zero frequency. This is the average brightness (contrast) of the image. It contains the most energy.

Periphery: High frequencies. These represent the fine details and sharp edges.

Lecturer Script:
"This is the concept that trips up most students. When you look at the raw data file coming off an MRI scanner, you do not see a brain. You see a galaxy of bright dots. This is K-Space.

K-space is a map. But it's not a map of 'where things are' (like a nose or an ear). It is a map of 'how fast things change.'

Let's navigate this map:

Stand in the center: You are at low frequency. This data tells us about the large, smooth shapes. The general contrast of the brain vs the skull. If we delete the center of K-space, the image turns grey and ghostly; we lose the contrast.

Walk to the edge: You are at high frequency. This data tells us about sharp changes—the edges of the ventricles, the boundary of a tumor. If we delete the edges of K-space, the image gets blurry. The details vanish."

3.3 Python Code: 2D FFT and K-Space

Code to demonstrate the visual relationship between an object and its K-space representation.

import numpy as np
import matplotlib.pyplot as plt
from scipy import fftpack

# 1. Create a simple 2D phantom (A box with a smaller box inside)
phantom = np.zeros((256, 256))
phantom[64:192, 80:176] = 1 # Big rectangle
phantom[100:150, 100:150] = 0 # Hole in the middle

# 2. Perform 2D FFT
f_transform = fftpack.fft2(phantom)

# 3. Shift the zero-frequency component to the center of the spectrum
# Without this, DC is at the corners. We want it in the middle.
f_shift = fftpack.fftshift(f_transform)

# 4. Calculate magnitude spectrum
# We use log scale because the center is usually 1,000,000x brighter than edges
magnitude_spectrum = 20 * np.log(np.abs(f_shift) + 1)

# Visualization
plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
plt.imshow(phantom, cmap='gray')
plt.title('Input Image (Space Domain)\nYour Brain')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(magnitude_spectrum, cmap='inferno')
plt.title('Magnitude Spectrum (K-Space)\nThe Raw Data')
plt.axis('off')

plt.tight_layout()
plt.show()
