# Comprehensive Lecture Notes: Signals and Systems (Chapter 1)

## 1.0 Introduction & 1.1 Basic Signal Concepts
* [cite_start]**Signals:** Functions of one or more independent variables that contain information[cite: 9].
    * [cite_start]*Examples:* Voltage in a circuit, applied force vs. velocity, speech (acoustic pressure), monochromatic picture (brightness vs. spatial variables) [cite: 10-42].
* **Independent Variables:**
    * [cite_start]Continuous-time: $t$ (parentheses $x(t)$) [cite: 91-92].
    * [cite_start]Discrete-time: $n$ (brackets $x[n]$), defined only for integer values [cite: 91-96].
* **Signal Representation:**
    * [cite_start]Continuous signals are defined for a continuum of values[cite: 55].
    * [cite_start]Discrete signals are sequences; they can arise from sampling continuous signals or be inherently discrete (e.g., demographic data) [cite: 97-99].

## 1.1.2 Energy and Power
* [cite_start]**Physical Motivation:** Instantaneous power in a resistor is $p(t) = v(t)i(t) = \frac{1}{R}v^2(t)$ [cite: 127-128].
* **Total Energy ($E$) over finite interval:**
    * [cite_start]Continuous: $\int_{t_1}^{t_2} |x(t)|^2 dt$[cite: 143].
    * [cite_start]Discrete: $\sum_{n=n_1}^{n_2} |x[n]|^2$[cite: 147].
* [cite_start]**Average Power ($P$) over finite interval:** Energy divided by interval length ($t_2 - t_1$ or $N$)[cite: 135, 150].
* **Infinite Interval Definitions:**
    * [cite_start]Total Energy ($E_{\infty}$): $E_{\infty} \triangleq \lim_{T \to \infty} \int_{-T}^{T} |x(t)|^2 dt$[cite: 156].
    * [cite_start]Average Power ($P_{\infty}$): $P_{\infty} \triangleq \lim_{T \to \infty} \frac{1}{2T} \int_{-T}^{T} |x(t)|^2 dt$[cite: 169].
    * [cite_start]Discrete equivalents involve limits as $N \to \infty$ and dividing by $2N+1$[cite: 156, 169].
* **Three Classes of Signals:**
    1.  [cite_start]**Finite Energy:** $E_{\infty} < \infty$, which implies $P_{\infty} = 0$ [cite: 173-176].
    2.  [cite_start]**Finite Average Power:** $P_{\infty} > 0$, which implies $E_{\infty} = \infty$ (e.g., periodic signals) [cite: 180-182].
    3.  [cite_start]**Neither:** Infinite power and infinite energy (e.g., $x(t) = t$) [cite: 183-184].

## 1.2 Transformations of the Independent Variable
* **Time Shift:**
    * [cite_start]$x(t - t_0)$: Delayed if $t_0 > 0$, Advanced if $t_0 < 0$[cite: 197].
    * [cite_start]Used in radar/sonar (propagation delay) [cite: 198-199].
* **Time Reversal:**
    * [cite_start]$x(-t)$ or $x[-n]$: Reflection about $t=0$ or $n=0$ [cite: 200-202].
* **Time Scaling:**
    * $x(at)$: Compressed if $|a| > 1$, Stretched if $|a| [cite_start]< 1$ [cite: 203-206].
    * Linear transformation $x(\alpha t + \beta)$: Order of operations matters. [cite_start]Shift first, then scale/reverse [cite: 296-301].

## 1.2.2 Periodic Signals
* [cite_start]**Continuous-Time Definition:** $x(t) = x(t + T)$ for all $t$[cite: 308].
    * [cite_start]**Fundamental Period ($T_0$):** Smallest positive $T$ satisfying the condition[cite: 324].
    * [cite_start]Constant signals have undefined fundamental period [cite: 325-326].
* [cite_start]**Discrete-Time Definition:** $x[n] = x[n + N]$ for integer $N$[cite: 329].
    * [cite_start]Fundamental Period ($N_0$): Smallest positive integer $N$[cite: 331].
* [cite_start]**Aperiodic:** Signals that are not periodic[cite: 327].

## 1.2.3 Even and Odd Signals
* [cite_start]**Even:** $x(-t) = x(t)$ or $x[-n] = x[n]$ (Symmetric about origin) [cite: 353-356].
* [cite_start]**Odd:** $x(-t) = -x(t)$ or $x[-n] = -x[n]$ (Antisymmetric, must be 0 at origin) [cite: 357-365].
* **Decomposition Property:** Any signal can be represented as sum of Even and Odd parts.
    * [cite_start]$\mathcal{E}v\{x(t)\} = \frac{1}{2}[x(t) + x(-t)]$[cite: 390].
    * [cite_start]$\mathcal{O}d\{x(t)\} = \frac{1}{2}[x(t) - x(-t)]$[cite: 393].

## 1.3 Exponential and Sinusoidal Signals
### 1.3.1 Continuous-Time
* **Real Exponential ($Ce^{at}$):**
    * $a > 0$: Growing. [cite_start]$a < 0$: Decaying (e.g., radioactive decay, RC circuits) [cite: 409-411].
* [cite_start]**Periodic Complex Exponential:** $x(t) = e^{j\omega_0 t}$[cite: 430].
    * [cite_start]Fundamental Period $T_0 = \frac{2\pi}{|\omega_0|}$[cite: 443].
    * [cite_start]Euler's Relation: $e^{j\omega_0 t} = \cos \omega_0 t + j \sin \omega_0 t$[cite: 465].
    * [cite_start]Power/Energy: Infinite total energy, finite average power ($P_{\infty} = 1$) [cite: 484-509].
* **Harmonically Related Sets:**
    * Set of exponentials $e^{jk\omega_0 t}$ ($k = 0, \pm 1, \dots$).
    * [cite_start]All share common period $T_0$ [cite: 514-533].

### 1.3.2 Discrete-Time
* **Complex Exponential ($C\alpha^n$ or $Ce^{\beta n}$):**
    * Growing if $|\alpha| > 1$, Decaying if $|\alpha| [cite_start]< 1$[cite: 612].
    * [cite_start]Alternating signs if $\alpha$ is negative[cite: 613].
* **Discrete Sinusoids ($e^{j\omega_0 n}$):**
    * **Crucial Difference 1:** Frequencies separated by $2\pi$ are identical ($e^{j(\omega_0 + 2\pi)n} = e^{j\omega_0 n}$). [cite_start]We only need a frequency range of $2\pi$ [cite: 688-695].
    * **Crucial Difference 2:** Oscillation rate. Low freq is near $0, 2\pi$. [cite_start]High freq is near $\pi$ (oscillates every sample) [cite: 698-700].
    * **Crucial Difference 3:** Periodicity Condition. [cite_start]$e^{j\omega_0 n}$ is periodic **only if** $\frac{\omega_0}{2\pi}$ is a rational number ($m/N$) [cite: 705-716].
    * [cite_start]Fundamental Period: $N = m(\frac{2\pi}{\omega_0})$ [cite: 752-758].

## 1.4 The Unit Impulse and Unit Step
### 1.4.1 Discrete-Time
* [cite_start]**Unit Impulse ($\delta[n]$):** 1 at $n=0$, 0 otherwise[cite: 815].
* [cite_start]**Unit Step ($u[n]$):** 1 for $n \ge 0$, 0 otherwise[cite: 824].
* **Relationships:**
    * [cite_start]Impulse is first difference of step: $\delta[n] = u[n] - u[n-1]$[cite: 850].
    * [cite_start]Step is running sum of impulse: $u[n] = \sum_{m=-\infty}^{n} \delta[m]$[cite: 853].
    * [cite_start]**Sampling Property:** $x[n]\delta[n] = x[0]\delta[n]$ or $x[n]\delta[n-n_0] = x[n_0]\delta[n-n_0]$ [cite: 882-886].

### 1.4.2 Continuous-Time
* **Unit Step ($u(t)$):** 1 for $t > 0$, 0 for $t < 0$. [cite_start]Discontinuous at 0[cite: 891].
* **Unit Impulse ($\delta(t)$):** Defined as the derivative of the step.
    * [cite_start]It is the limit of a short pulse of area 1 as duration $\Delta \to 0$ [cite: 914-941].
    * [cite_start]Visualized as an arrow with height representing **area**[cite: 944].
* [cite_start]**Relationships:** $u(t) = \int_{-\infty}^{t} \delta(\tau) d\tau$ and $\delta(t) = \frac{du(t)}{dt}$ [cite: 904-908].
* [cite_start]**Sampling Property:** $x(t)\delta(t - t_0) = x(t_0)\delta(t - t_0)$[cite: 999].

## 1.5 Systems
* **Definition:** A process transforming inputs to outputs ($x \to y$). [cite_start]Can be Series (Cascade), Parallel, or Feedback interconnections [cite: 1079-1225].
* **Examples:**
    * [cite_start]RC Circuit (ODE): $\frac{dv_c(t)}{dt} + \frac{1}{RC}v_c(t) = \frac{1}{RC}v_s(t)$[cite: 1113].
    * [cite_start]Car Motion (ODE): First-order linear differential equation[cite: 1124].
    * [cite_start]Bank Account (Difference Equation): $y[n] = 1.01y[n-1] + x[n]$[cite: 1137].

## 1.6 Basic System Properties
* **1. Memory:**
    * [cite_start]**Memoryless:** Output depends *only* on input at current time (e.g., Resistor $y(t) = Rx(t)$) [cite: 1246-1252].
    * [cite_start]**Memory:** Output depends on past or future values (e.g., Capacitor, Accumulator $y[n] = \sum x[k]$) [cite: 1259-1266].
* **2. Invertibility:**
    * Distinct inputs lead to distinct outputs. [cite_start]An inverse system exists ($w(t) = x(t)$) [cite: 1290-1297].
    * [cite_start]Non-invertible example: $y(t) = x^2(t)$ (sign lost)[cite: 1330].
* **3. Causality:**
    * Output depends only on present and past inputs. [cite_start]"Non-anticipative" [cite: 1339-1340].
    * All physical real-time systems are causal. [cite_start]Non-causal examples involve averaging future data (image processing, recorded data) [cite: 1354-1358].
* **4. Stability:**
    * BIBO (Bounded Input Bounded Output). If $|x| < B$, then $|y| [cite_start]< C$[cite: 1406].
    * [cite_start]Unstable example: Bank account with interest (grows without bound) or Inverted Pendulum [cite: 1390-1398].
* **5. Time Invariance:**
    * [cite_start]A time shift in input causes identical time shift in output [cite: 1458-1469].
    * check: If $x(t) \to y(t)$, does $x(t-t_0) \to y(t-t_0)$?
    * [cite_start]Counter-example: Time scaling $y(t) = x(2t)$ is NOT time invariant [cite: 1506-1546].
* **6. Linearity:**
    * [cite_start]**Superposition Property:** Additivity + Scaling (Homogeneity)[cite: 1549].
    * [cite_start]Combined: $a x_1(t) + b x_2(t) \to a y_1(t) + b y_2(t)$[cite: 1560].
    * [cite_start]Zero-Input Property: A linear system must produce 0 output for 0 input[cite: 1568].
    * [cite_start]Incremental Linearity: Systems like $y = 2x + 3$ are non-linear (fail superposition) but incrementally linear [cite: 1633-1664].