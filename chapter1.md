--- PAGE 1 ---

         1
        SIGNALS AND SYSTEMS





1.0 INTRODUCTION

             As described in the Foreword, the intuitive notions of signals and systems arise in a rich va-
                  riety of contexts. Moreover, as we will see in this book, there is an analytical framework-
                  that is, a language for describing signals and systems and an extremely powerful set of tools
                  for analyzing them-that applies equally well to problems in many fields. In this chapter,
            we begin our development of the analytical framework for signals and systems by intro-
               ducing their mathematical description and representations. In the chapters that follow, we
                build on this foundation in order to develop and describe additional concepts and methods
                  that add considerably both to our understanding of signals and systems and to our ability
                   to analyze and solve problems involving signals and systems that arise in a broad array of
                 applications.

1. 1 CONTINUOUS-TIME AND DISCRETE-TIME SIGNALS

             1 . 1 . 1 Examples and Mathematical Representation
                Signals may describe a wide variety of physical phenomena. Although signals can be rep-
                resented in many ways, in all cases the information in a signal is contained in a pattern of
                 variations of some form. For example, consider the simple circuit in Figure 1.1. In this case,
                 the patterns of variation over time in the source and capacitor voltages, v, and Vc, are exam-
                 ples of signals. Similarly, as depicted in Figure 1.2, the variations over time of the applied
                 force f and the resulting automobile velocity v are signals. As another example, consider
                 the human vocal mechanism, which produces speech by creating fluctuations in acous-
                     tic pressure. Figure 1.3 is an illustration of a recording of such a speech signal, obtained by
                                                                                                  1

--- PAGE 2 ---

           2                                                                     Signals and Systems     Chap. 1


                         R


                                   c




                        ~pv

            Figure 1. 1  A simple RC circuit with source     Figure 1 .2   An automobile responding to an
               voltage Vs and capacitor voltage  Vc.                  applied force t from the engine and to a re-
                                                                     tarding frictional force pv proportional to the
                                                                 automobile's velocity  v.


~-------------------200msec--------------------~





I                                                                                                                 I                                                                                     I                            I
1_____   .!_ _____ 1 _____   !._ _____1 __________ ~ _____ I _____  J
j           sh                           oul              d


r -  -  -  - -~- -  -  -  -  I  -  -  -  -  I  -  -  -  -  -  ~- -  -  -  -  I  -  -  -  - -~- -  -  -  -  I  -  -  -  -  -~
I




                                                                                                                        I
                             I                            I                           I                            I                            I                            I                            I
~-------------------------------------------w                              e
                                                             Figure 1.3   Example of a record-
r -  -  -  - -~- -  -  -  -  I  -  -  -  -  I  -  -  -  -  -  ~- -  -  -  -  I  -  -  -  - -~- -  -  -  -  I  -  -  -  -  -~    ing of speech. [Adapted from Ap-
I                                                        I                                                                                                                                                                           I    plications of Digital Signal Process-
                                                                                         ing, A.V. Oppenheim, ed. (Englewood
                                                                                                    Cliffs, N.J.: Prentice-Hall, Inc., 1978),
                                                                                                                                                                                                        I~ _____ 1 _____ ~ ____ ~ _____ 1_____   .!_ _____ I _____ ~ _____ I     p. 121.] The signal represents acous-
                       ch                           a                        tic pressure variations as a function
                                                                                   of time for the spoken words "should
                                                          we chase." The top line of the figure
                                                                     corresponds to the word "should,"
                                                                             the second line to the word "we,"
                                                                   and the last two lines to the word
                                                                            "chase." (We have indicated the ap-
I                                                         I                                                                                                                                                                            I                                                                                                                                                                                                                                     I   proximate beginnings and endings1_____ ~ _____ 1             _____ ~ _____1 _____  I_____ ~                                     _____ 1_____  J
                    a                               se                  of each successive sound in each
                                                        I                                 word.)

           using a microphone to sense variations in acoustic pressure, which are then converted into
          an electrical signal. As can be seen in the figure, different sounds correspond to different
            patterns in the variations of acoustic pressure, and the human vocal system produces intel-
             ligible speech by generating particular sequences of these patterns. Alternatively, for the
          monochromatic picture, shown in Figure 1.4, it is the pattern of variations in brightness
           across the image, that is important.

--- PAGE 3 ---

   Sec. 1.1     Continuous-Time and Discrete-Time Signals                                     3





                                                     Figure 1 .4  A monochromatic
                                                                           picture.
        Signals are represented mathematically as functions of one or more independent
   variables. For example, a speech signal can be represented mathematically by acoustic
   pressure as a function of time, and a picture can be represented by brightness as a func-
   tion of two spatial variables. In this book, we focus our attention on signals involving a
   single independent variable. For convenience, we will generally refer to the independent
   variable as time, although it may not in fact represent time in specific applications. For
   example, in geophysics, signals representing variations with depth of physical quantities
   such as density, porosity, and electrical resistivity are used to study the structure of the
   earth. Also, knowledge of the variations of air pressure, temperature, and wind speed with
   altitude are extremely important in meteorological investigations. Figure 1.5 depicts a typ-
   ical example of annual average vertical wind profile as a function of height. The measured
   variations of wind speed with height are used in examining weather patterns, as well as
   wind conditions that may affect an aircraft during final approach and landing.
        Throughout this book we will be considering two basic types of signals: continuous-
   time signals and discrete-time signals. In the case of continuous-time signals the inde-
   pendent variable is continuous, and thus these signals are defined for a continuum of values


  26
  24
  22
  20
  18
:§'16
 0
~ 14
~ 12
~ 10
(f)
   8
   6
   4                                                     Figure 1 .s   Typical annual vertical
   2                                                       wind profile. (Adapted from Crawford
                                                           and Hudson, National Severe Storms     0    200   400   600   800  1,000 1,200 1,400 1,600                                                                Laboratory Report, ESSA ERLTM-NSSL
                          Height (feet)                             48, August 1970.)

--- PAGE 4 ---

4                                                                     Signals and Systems     Chap. 1


    400-

     350  -

     300

     250

     200

     150

     100

      50
      ot
    Jan. 5,1929                                                                      Jan. 4,1930

         Figure 1 .6  An example of a discrete-time signal: The weekly Dow-Jones
           stock market index from January 5, 1929, to January 4, 1930.

of the independent variable. On the other hand, discrete-time signals are defined only at
discrete times, and consequently, for these signals, the independent variable takes on only
a discrete set of values. A speech signal as a function of time and atmospheric pressure
as a function of altitude are examples of continuous-time signals. The weekly Dow-Jones
stock market index, as illustrated in Figure 1.6, is an example of a discrete-time signal.
Other examples of discrete-time signals can be found in demographic studies in which
various attributes, such as average budget, crime rate, or pounds of fish caught, are tab-
ulated against such discrete variables as family size, total population, or type of fishing
vessel, respectively.
     To distinguish between continuous-time and discrete-time signals, we will use the
symbol t to denote the continuous-time independent variable and n to denote the discrete-
time independent variable. In addition, for continuous-time signals we will enclose the
independent variable in parentheses ( · ), whereas for discrete-time signals we will use
brackets [ · ] to enclose the independent variable. We will also have frequent occasions
when it will be useful to represent signals graphically. Illustrations of a continuous-time
signal x(t) and a discrete-time signal x[n] are shown in Figure 1.7. It is important to note
that the discrete-time signal x[n]  is defined only for integer values of the independent
variable. Our choice of graphical representation for x[ n] emphasizes this fact, and for
further emphasis we will on occasion refer to x[n] as a discrete-time sequence.
   A discrete-time signal x[n] may represent a phenomenon for which the independent
variable is inherently discrete. Signals such as demographic data are examples of this. On
the other hand, a very important class of discrete-time signals arises from the sampling of
continuous-time signals. In this case, the discrete-time signal x[n] represents successive
samples of an underlying phenomenon for which the independent variable is continuous.
Because of their speed, computational power, and flexibility, modem digital processors are
used to implement many practical systems, ranging from digital autopilots to digital audio
systems. Such systems require the use of discrete-time sequences representing sampled
versions of continuous-time signals--e.g., aircraft position, velocity, and heading for an

--- PAGE 5 ---

Sec. 1.1     Continuous-Time and Discrete-Time Signals                                    5


                                                                 x(t)





                                           0

                                                                  (a)

                                                        x[n]


                                                          x[O]





                                                                                 n


         Figure 1. 7   Graphical representations of (a) continuous-time and (b) discrete-
           time signals.
autopilot or speech and music for an audio system. Also, pictures in newspapers-or in this
book, for that matter-actually consist of a very fine grid of points, and each of these points
represents a sample of the brightness of the corresponding point in the original image. No
matter what the source of the data, however, the signal x[n] is defined only for integer
values of n. It makes no more sense to refer to the 3 ~ th sample of a digital speech signal
than it does to refer to the average budget for a family with 2~ family members.
     Throughout most of this book we will treat discrete-time signals and continuous-time
signals separately but in parallel, so that we can draw on insights developed in one setting
to aid our understanding of another. In Chapter 7 we will return to the question of sampling,
and in that context we will bring continuous-time and discrete-time concepts together in
order to examine the relationship between a continuous-time signal and a discrete-time
signal obtained from it by sampling.
1. 1 .2 Signal Energy and Power
From the range of examples provided so far, we see that signals may represent a broad
variety of phenomena. In many, but not all, applications, the signals we consider are di-
rectly related to physical quantities capturing power and energy in a physical system. For
example, if v(t) and i(t) are, respectively, the voltage and current across a resistor with
resistance R, then the instantaneous power is
                                  p(t) = v(t)i(t) = ~v2 (t).                             (1.1)

--- PAGE 6 ---

6                                                                     Signals and Systems     Chap. 1

The total energy expended over the time interval t 1 :s  t :s t2 is
                                                               12                         12
                                                        {   p(t) dt =  {  ~v2 (t) dt,                             (1.2)                      Jt]                   Jf]
and the average power over this time interval is
                      1  J 12           1    Jt2 1       --    p(t)dt = --     -Rv2(t)dt.                     (1.3)
                                t2 -  t!      f]                t2 -  tl      f]
Similarly, for the automobile depicted in Figure 1.2, the instantaneous power dissipated
through friction is p(t) = bv2(t), and we can then define the total energy and average
power over a time interval in the same way as in eqs. (1.2) and (1.3).
     With simple physical examples such as these as motivation,  it is a common and
worthwhile convention to use similar terminology for power and energy for any continuous-
time signal x(t) or any discrete-time signal x[n]. Moreover, as we will see shortly, we will
frequently find it convenient to consider signals that take on complex values. In this case,
the total energy over the time interval  t 1 :s  t  :s t2 in a continuous-time signal x(t) is
defined as

                                                                                           (1.4)

where lxl denotes the magnitude of the (possibly complex) number x. The time-averaged
power is obtained by dividing eq. (1.4) by the length, t2  -   t 1, of the time interval. Simi-
larly, the total energy in a discrete-time signal x[n] over the time interval n 1 :s n :s n2 is
defined as

                                                                                           (1.5)

and dividing by the number of points in the interval, n2 - n 1 + 1, yields the average power
over the interval. It is important to remember that the terms "power" and "energy" are used
here independently of whether the quantities in eqs. (1.4) and (1.5) actually are related to
physical energy. 1 Nevertheless, we will find it convenient to use these terms in a general
fashion.
     Furthermore, in many systems we will be interested in examining power and energy
in signals over an infinite time interval, i.e., for -oo <  t < +oo or for -oo < n < +oo. In
these cases, we define the total energy as limits of eqs. (1.4) and (1.5) as the time interval
increases without bound. That is, in continuous time,

                                     T        2           +oc      2                            Eoo ~ }~ -T lx(t)l dt = I-oc  lx(t)l  dt,                     (1.6)                 I
and in discrete time,
                             +N                  +oo
                                                                                           (1.7)                             Eoo ~                            lim L   lx[nJI2 = L   lx[nJI2.                            N~oo
                           n=-N           n=-oc
          1Even if such a relationship does exist, eqs. ( 1.4) and ( 1.5) may have the wrong dimensions and scalings.
For example, comparing eqs. (1.2) and (1.4 ), we see that if x(t) represents the voltage across a resistor, then
eq. (1.4) must be divided by the resistance (measured, for example, in ohms) to obtain units of physical energy.

--- PAGE 7 ---

                   Sec. 1.2     Transformations of the Independent Variable                                     7

              Note that for some signals the integral in eq. (1.6) or sum in eq. (1.7) might not converge-
                    e.g., if x(t) or x[n] equals a nonzero constant value for all time. Such signals have infinite
                energy, while signals with E~ < co have finite energy.
                      In an analogous fashion, we can define the time-averaged power over an infinite
                  interval as

                                                                                                                                        (',                                                                               2 dt                            (1.8)                                                1 IT  /x(t)/                                                 lim                                                       PeN =                                                                               T---+~ -2 T  -T
              and
                                                 1    +N        2                                                                                                             (1.9)                                                    PeN ~  lim    L   /x[n]/                                                                        N---+~ 2N + 1 n=-N
                  in continuous time and discrete time, respectively. With these definitions, we can identify
                 three important classes of signals. The first of these is the class of signals with finite total
                energy, i.e., those signals for which Eoo <co. Such a signal must have zero average power,
                since in the continuous time case, for example, we see from eq. (1.8) that

                                                E~                                         P~ =   1.1m-= 0.                             (1.10)
                                                           T---+~2T
           An example of a finite-energy signal is a signal that takes on the value 1 for 0    ::::::  t     :::::: 1
              and 0 otherwise. In this case, E~ = 1 and Px = 0.
             A second class of signals are those with finite average power P oo. From what we
              have just seen, if Px > 0, then, of necessity, Ex =  co. This, of course, makes sense, since
                     if there is a nonzero average energy per unit time (i.e., nonzero power), then integrating
                 or summing this over an infinite time interval yields an infinite amount of energy. For
               example, the constant signal x[n] = 4 has infinite energy, but average power Px =  16.
              There are also signals for which neither P x nor Ex are finite. A simple example is the
                 signal x(t) =  t. We will encounter other examples of signals in each of these classes in
                 the remainder of this and the following chapters.

1.2 TRANSFORMATIONS OF THE INDEPENDENT VARIABlE

         A central concept in signal and system analysis is that of the transformation of a signal.
               For example, in an aircraft control system, signals corresponding to the actions of the pilot
                 are transformed by electrical and mechanical systems into changes in aircraft thrust or
                 the positions of aircraft control surfaces such as the rudder or ailerons, which in tum are
               transformed through the dynamics and kinematics of the vehicle into changes in aircraft
                 velocity and heading. Also, in a high-fidelity audio system, an input signal representing
              music as recorded on a cassette or compact disc is modified in order to enhance desirable
                  characteristics, to remove recording noise, or to balance the several components of the
                 signal (e.g., treble and bass). In this section, we focus on a very limited but important class
                of elementary signal transformations that involve simple modification of the independent
                  variable, i.e., the time axis. As we will see in this and subsequent sections of this chapter,
                these elementary transformations allow us to introduce several basic properties of signals
              and systems. In later chapters, we will find that they also play an important role in defining
              and characterizing far richer and important classes of systems.

--- PAGE 8 ---

8                                                                    Signals and Systems     Chap. 1

1 .2. 1 Examples of Transformations of the Independent Variable
A simple and very important example of transforming the independent variable of a signal
is a time shift. A time shift in discrete time is illustrated in Figure 1.8, in which we have
two signals x[n] and x[n- n0] that are identical in shape, but that are displaced or shifted
relative to each other. We will also encounter time shifts in continuous time, as illustrated
in Figure 1.9, in which x(t -  t0 ) represents a delayed (if to is positive) or advanced (if to
is negative) version of x(t). Signals that are related in this fashion arise in applications
such as radar, sonar, and seismic signal processing, in which several receivers at different
locations observe a signal being transmitted through a medium (water, rock, air, etc.). In
this case, the difference in propagation time from the point of origin of the transmitted
signal to any two receivers results in a time shift between the signals at the two receivers.
   A second basic transformation of the time axis is that of time reversal. For example,
as illustrated in Figure 1.1 0, the signal x[- n] is obtained from the signal x[ n] by a reflec-
tion about n = 0 (i.e., by reversing the signal). Similarly, as depicted in Figure 1.11, the
signal x(-t) is obtained from the signal x(t) by a reflection about t = 0. Thus, if x(t) rep-
resents an audio tape recording, then x( -t) is the same tape recording played backward.
Another transformation is that of time scaling. In Figure 1.12 we have illustrated three
signals, x(t), x(2t), and x(t/2), that are related by linear scale changes in the independent
variable. If we again think of the example of x(t) as a tape recording, then x(2t) is that
recording played at twice the speed, and x(t/2) is the recording played at half-speed.
        It is often of interest to determine the effect of transforming the independent variable
of a given signal x(t) to obtain a signal of the form x(at + {3), where a and {3 are given
numbers. Such a transformation of the independent variable preserves the shape of x(t),
except that the resulting signal may be linearly stretched if Ia I <  1, linearly compressed
if Ia I > 1, reversed in time if a < 0, and shifted in time if {3 is nonzero. This is illustrated
in the following set of examples.

              x[n]





                                                n


         x[n-n0]




                                                   Figure 1 .8   Discrete-time signals
                                                                      related by a time shift.  In this figure
                                                               n0 > 0, so that x[n- n0] is a delayed
            0                                     n    verson of x[n]  (i.e., each point in x[n]
                                                           occurs later in x[n- n0]).

--- PAGE 9 ---

                Sec. 1.2     Transformations of the Independent Variable                                     9


                                                                                         x[n)





                                                                                                n

                                                                                                           (a)


                                                                        x[-n)





                                                                                             n
Figure 1.9   Continuous-time signals related
by a time shift. In this figure  t0 < 0, so that                                           (b)
x(t -   to) is an advanced version of x(t)  (i.e.,
each point in x(t) occurs at an earlier time in     Figure 1 .1 O   (a) A discrete-time signal x[n]; (b) its reflec-
x(t -  to)).                                               tion x[-n] about n =  0.



                                      x(t)
                                                                                                                     x(t)
          d\

                                                                                                        x(2t)
                                              (a)


                             x(-t)        &

                                                                                                          x(t/2)
                                           (b) ~

  Figure 1.11    (a) A continuous-time signal x(t); (b)  its      Figure 1. 12   Continuous-time signals
    reflection x( -  t) about  t =  0.                                        related by time scaling.

--- PAGE 10 ---

10                                                                  Signals and Systems     Chap. 1

   Example 1.1
         Given the signal x(t) shown in Figure l.13(a), the signal x(t + 1) corresponds to an
         advance (shift to the left) by one unit along the taxis as illustrated in Figure l.13(b).
           Specifically, we note that the value of x(t) at t =  to occurs in x(t + 1) at t =  to -  1. For

                             11 'l'I


                                           0            1           2
                                                                                  (a)

      1~

                           -1          0            1          2
                                                                           (b)





                           -1           0           1
                                                                                  (c)


                               1  '1i11                I
                                          0-~2/3    4/3
                                                                           (d)





                            -2/3     0     2/3
                                                                                  (e)

              Figure 1. 13    (a) The continuous-time signal x(t) used in Examples 1.1-1.3
                  to illustrate transformations of the independent variable; (b) the time-shifted
                  signal x(t + 1); (c) the signal x(-t + 1) obtained by a time shift and a time
                   reversal; (d) the time-scaled signal       t); and (e) the signal       t + 1) obtained                                xa             xa                by time-shifting and scaling.

--- PAGE 11 ---

Sec. 1.2     Transformations of the Independent Variable                                    11

          example, the value of x(t) at t = 1 is found in x(t + 1) at t = 1 - 1 = 0. Also, since
             x(t) is zero fort < 0, we have x(t + 1) zero fort < -1. Similarly, since x(t) is zero for
                  t > 2, x(t + 1) is zero for t >  1.
                Let us also consider the signal x( -  t + 1), which may be obtained by replacing t
          with -t in x(t + 1). That is, x(-t + 1) is the time reversed version of x(t + 1). Thus,
            x( -  t + 1) may be obtained graphically by reflecting x( t + 1) about the t axis as shown
            in Figure 1.13(c).

    Example 1.2
         Given the signal x(t), shown in Figure l.13(a), the signal x(~t) corresponds to a linear
          compression of x(t) by a factor of~ as illustrated in Figure l.13(d). Specifically we note
            that the value of x(t) at  t =  to occurs in x(~t) at  t =  ~t0 . For example, the value of
             x(t) at t = 1 is found in x(~t) at t =  ~ (1) = ~-Also, since x(t) is zero fort< 0, we
          have x(~t) zero fort< 0. Similarly, since x(t) is zero fort> 2, x(~t) is zero fort>  ~-
    Example 1.3
         Suppose that we would like to determine the effect of transforming the independent vari-
           able of a given signal, x(t), to obtain a signal of the form x(at + /3), where a and f3 are
          given numbers. A systematic approach to doing this is to first delay or advance x(t) in
          accordance with the value of f3, and then to perform time scaling and/or time reversal on
           the resulting signal in accordance with the value of a. The delayed or advanced signal is
            linearly stretched if fa[ <  1, linearly compressed if fa[ >  1, and reversed in time if a < 0.
              To illustrate this approach, let us show how x( ~ t + 1) may be determined for the
            signal x(t) shown in Figure 1.13(a). Since f3 =  1, we first advance (shift to the left) x(t)
         by 1 as shown· in Figure 1.l 3(b ). Since fa [ =  ~, we may linearly compress the shifted
            signal of Figure 1.13(b) by a factor of~ to obtain the signal shown in Figure 1.13(e).

      In addition to their use in representing physical phenomena such as the time shift
in a sonar signal and the speeding up or reversal of an audiotape, transformations of the
independent variable are extremely useful in signal and system analysis. In Section 1.6
and in Chapter 2, we will use transformations of the independent variable to introduce and
analyze the properties of systems. These transformations are also important in defining
and examining some important properties of signals.

1.2.2 Periodic Signals
An important class of signals that we will encounter frequently throughout this book is
the class of periodic signals. A periodic continuous-time signal x(t) has the property that
there is a positive value of T for which
                                          x(t) =  x(t + T)                                (l.11)
for all values oft. In other words, a periodic signal has the property that it is unchanged by a
time shift of T. In this case, we say that x(t) is periodic with period T. Periodic continuous-
time signals arise in a variety of contexts. For example, as illustrated in Problem 2.61,
the natural response of systems in which energy is conserved, such as ideal LC circuits
without resistive energy dissipation and ideal mechanical systems without frictional losses,
are periodic and, in fact, are composed of some of the basic periodic signals that we will
introduce in Section 1.3.

--- PAGE 12 ---

              12                                                                   Signals and Systems     Chap. 1


                                                  x(t)




                                                                  Figure 1. 14  A continuous-time···!\-2T [\-T           0         T   !\···2T             periodic signal.  & [\
               An example of a periodic continuous-time signal is given in Figure 1.14. From the
                 figure or from eq. ( 1.11 ), we can readily deduce that if x(t) is periodic with period T, then
                   x(t) =  x(t + mT) for all t and for any integer m. Thus, x(t) is also periodic with period
              2T, 3T, 4T, .... The fundamental period To of x(t) is the smallest positive value ofT for
              which eq. ( 1.11) holds. This definition of the fundamental period works, except if x(t) is
               a constant. In this case the fundamental period is undefined, since x(t) is periodic for any
               choice ofT (so there is no smallest positive value). A signal x(t) that is not periodic will
              be referred to as an aperiodic signal.
                     Periodic signals are defined analogously in discrete time. Specifically, a discrete-
               time signal x[n] is periodic with period N, where N is a positive integer, if it is unchanged
             by a time shift of N, i.e., if
                                                    x[n] = x[n + N]                               (1.12)
                  for all values of n. If eq. (1.12) holds, then x[n] is also periodic with period 2N, 3N, ....
             The fundamental period N0 is the smallest positive value of N for which eq. ( 1.12) holds.
           An example of a discrete-time periodic signal with fundamental period No = 3 is shown
                 in Figure 1.15.

                                                      x[n]



                                                                  Figure 1 . 1 5  A discrete-time pe-
                                                                   n    riodic signal with fundamental period
                                                  No=  3.

             Example 1.4

                          Let us illustrate the type of problem solving that may be required in determining whether
                             or not a given signal is periodic. The signal whose periodicity we wish to check is given
                        by
                                             = { cos(t)   if t < 0                                                          X (t )           .            .              .                         (1.13)                                                                  sm(t)    If t ~ 0

                      From trigonometry, we know that cos(t + 27T) =  cos(t) and sin(t + 27T) =  sin(t). Thus,
                           considering  t > 0 and t < 0 separately, we see that x(t) does repeat itself over every
                               interval oflength 27T. However, as illustrated in Figure 1.16, x(t) also has a discontinuity
                                  at the time origin that does not recur at any other time. Since every feature in the shape of
                            a periodic signal must recur periodically, we conclude that the signal x(t) is not periodic.

--- PAGE 13 ---

Sec. 1.2     Transformations of the Independent Variable                                13


                                                                              x(t)





                      Figure 1. 16   The signal x{t) considered  in Example 1.4.

1 .2.3 Even and Odd Signals
Another set of useful properties of signals relates to their symmetry under time reversal.
A signal x(t) or x[n] is referred to as an even signal if it is identical to its time-reversed
counterpart, i.e., with its reflection about the origin. In continuous time a signal is even if
                              x(- t) =  x(t),                                (1.14)
while a discrete-time signal is even if
                              x[- n] = x[n].                                        ( 1.15)
A signal is referred to as odd if
                                       x( -t) =   -  x(t),                                       ( 1.16)
                              x[-n] = -x[n].                               (1.17)
An odd signal must necessarily be 0 at t = 0 or n = 0, since eqs. ( 1.16) and ( 1.17) require
that x(O) =  - x(O) and x[O] =  - x[O]. Examples of even and odd continuous-time signals
are shown in Figure 1.17.

                                           x(t)





                             0
                                            (a)


                                           x(t)





                                                   Figure 1. 1 7    (a) An even con-
                                                             tinuous-time signal; (b) an odd
                                                            continuous-time signal.

--- PAGE 14 ---

              14                                                                   Signals and Systems     Chap. 1


                                                   x[n] = { 1,  n;::::: 0
                                                                  0, n < 0




                        -3-2-1  0  1  2  3                n



                                  Sv{x[nl} = {                                                                  ~: ~: ~
                                                         2, n > 0
               t t 11 I~~ t t ...                        -3-2-1  0  1  2  3                n


                                                                           -  ~· n < 0
                               ea{x[nl}=   ?·n=O
                                                                        {    2, n > 0
                                                          1
                        -3-2-1                        2r r r
                                                                   n   Figure 1. 18   Example of the even-            ···11101231                              odd decomposition of a discrete-time
                           -2                                        signal.
               An important fact is that any signal can be broken into a sum of two signals, one of
              which is even and one of which is odd. To see this, consider the signal
                                                 1                                       8v { x(t)} =    [x(t) + x(-t)],                             ( 1.18)                                  2
              which is referred to as the even part of x(t). Similarly, the odd part of x(t) is given by
                                              1
                                             0d{x(t)} = 2[x(t)- x( -t)].                         (1.19)
                      It is a simple exercise to check that the even part is in fact even, that the odd part is odd,
              and that x(t) is the sum of the two. Exactly analogous definitions hold in the discrete-
               time case. An example of the even -odd decomposition of a discrete-time signal is given
                  in Figure 1.18.

1 .3 EXPONENTIAL AND SINUSOIDAL SIGNALS
                 In this section and the next, we introduce several basic continuous-time and discrete-time
                  signals. Not only do these signals occur frequently, but they also serve as basic building
                blocks from which we can construct many other signals.

--- PAGE 15 ---

Sec. 1.3     Exponential and Sinusoidal Signals                                      15

1 .3. 1 Continuous-Time Complex Exponential
     and Sinusoidal Signals
The continuous-time complex exponential signal is of the form
                                           x(t) = Ce 01,                                 (1.20)
where C and a are, in general, complex numbers. Depending upon the values of these
parameters, the complex exponential can exhibit several different characteristics.

Real Exponential Signals
As illustrated in Figure 1.19, if C and a are real [in which case x(t)  is called a real
exponential], there are basically two types of behavior. If a is positive, then as  t in-
creases x(t) is a growing exponential, a form that is used in describing many different
physical processes, including chain reactions in atomic explosions and complex chemical
reactions. If a is negative, then x(t) is a decaying exponential, a signal that is also used
to describe a wide variety of phenomena, including the process of radioactive decay and
the responses of RC circuits and damped mechanical systems. In particular, as shown
in Problems 2.61 and 2.62, the natural responses of the circuit in Figure 1.1 and the
automobile in Figure 1.2 are decaying exponentials. Also, we note that for a = 0, x(t)
is constant.


                                       x(t)





                                        (a)


                                       x(t)





                                                   Figure 1.19   Continuous-time real
                                                               exponential x(t) = Ce31 : (a) a >  0;
                                      (b)                                      (b) a< 0.

--- PAGE 16 ---

16                                                                   Signals and Systems     Chap. 1

Periodic Complex Exponential and Sinusoidal Signals
A second important class of complex exponentials is obtained by constraining a to be
purely imaginary. Specifically, consider
                                                                                     (1.21)

An important property of this signal is that it is periodic. To verify this, we recall from
eq. (1.11) that x(t) will be periodic with period T if
                                                                                     (1.22)

Or, since


it follows that for periodicity, we must have
                                                                                     (1.23)
If w 0 = 0, then x(t) = 1, which is periodic for any value ofT. If w 0  =/:- 0, then the fun-
damental period To of x(t)-that is, the smallest positive value ofT for which eq. (1.23)
holds-is

                                              21T
                                                                                     (1.24)                                   To =  lwol'

Thus, the signals eiwot and e- Jwot have the same fundamental period.
   A signal closely related to the periodic complex exponential is the sinusoidal signal
                                     x(t) = A cos(wot + cf>),                            (1.25)
as illustrated in Figure 1.20. With seconds as the units oft, the units of cf> and w 0 are radians
and radians per second, respectively. It is also common to write w 0 = 21T fo, where fo has
the units of cycles per second, or hertz (Hz). Like the complex exponential signal, the si-
nusoidal signal is periodic with fundamental period T0 given by eq. (1.24). Sinusoidal and


                x(t) = A cos (w0t + <!>)





                                                   Figure 1.20   Continuous-time sinu-
                                                                   soidal signal.

--- PAGE 17 ---

Sec. 1.3     Exponential and Sinusoidal Signals                                       17

complex exponential signals are also used to describe the characteristics of many physical
processes-in particular, physical systems in which energy is conserved. For example, as
shown in Problem 2.61, the natural response of an LC circuit is sinusoidal, as is the simple
harmonic motion of a mechanical system consisting of a mass connected by a spring to a
stationary support. The acoustic pressure variations corresponding to a single musical tone
are also sinusoidal.
    By using Euler's relation? the complex exponential in eq. (1.21) can be written in
terms of sinusoidal signals with the same fundamental period:
                                         e.iwot = cos Wot + j sin wot.                         (1.26)
Similarly, the sinusoidal signal of eq. (1.25) can be written in terms of periodic complex
exponentials, again with the same fundamental period:

                                                                                    (1.27)

Note that the two exponentials in eq. (1.27) have complex amplitudes. Alternatively, we
can express a sinusoid in terms of a complex exponential signal as
                                                                                    (1.28)
where, if cis a complex number, CRe{ c} denotes its real part. We will also use the notation
9m{c} for the imaginary part of c, so that, for example,
                   A sin(wot + ¢) =  A9m{ej(wut+¢l}.                      (1.29)
    From eq. (1.24), we see that the fundamental period T0 of a continuous-time sinu-
soidal signal or a periodic complex exponential is inversely proportional to lw0 j, which
we will refer to as the fundamental frequency. From Figure 1.21, we see graphically what
this means. If we decrease the magnitude of w 0 , we slow down the rate of oscillation and
therefore increase the period. Exactly the opposite effects occur if we increase the mag-
nitude of w 0 . Consider now the case w0 = 0. In this case, as we mentioned earlier, x(t)
is constant and therefore is periodic with period T for any positive value of T. Thus, the
fundamental period of a constant signal is undefined. On the other hand, there is no am-
biguity in defining the fundamental frequency of a constant signal to be zero. That is, a
constant signal has a zero rate of oscillation.
      Periodic signals-and in particular, the complex periodic exponential signal in
eq. (1.21) and the sinusoidal signal in eq. (1.25)-provide important examples of signals
with infinite total energy but finite average power. For example, consider the periodic ex-
ponential signal of eq. (1.21), and suppose that we calculate the total energy and average
power in this signal over one period:

                      E period =  f.oTo je.iwoti2 dt
                                                                                                       ( 1.30)
                                  =  foT"  I  · d t =  To.


       2Euler's relation and other basic ideas related to the manipulation of complex numbers and exponentials
are considered in the mathematical review section of the problems at the end of the chapter.

--- PAGE 18 ---

18                                                                  Signals and Systems     Chap. 1





                              (a)





                             (b)





                                                   Figure 1 .21   Relationship between
                                                                 the fundamental frequency and period
                                                                     for continuous-time sinusoidal signals;
                                                                    here, w1 >  £1>2 > w 3, which implies
                                  (c)                                       that  T1 <  T2 <  r3.

                                    1
                     P period = T  Eperiod =  1.                           (1.31)
                                                    0

Since there are an infinite number of periods as t ranges from -'X! to +oo, the total energy
integrated over all time is infinite. However, each period of the signal looks exactly the
same. Since the average power of the signal equals 1 over each period, averaging over
multiple periods always yields an average power of 1. That is, the complex periodic ex-

--- PAGE 19 ---

Sec. 1.3     Exponential and Sinusoidal Signals                                     19

ponential signal has finite average power equal to

                      Px = _lim _1   T  leiwotl2 dt =  1.                      (1.32)                          f                          r~x 2T  -T

Problem 1.3 provides additional examples of energy and power calculations for periodic
and aperiodic signals.
      Periodic complex exponentials will play a central role in much of our treatment of
signals and systems, in part because they serve as extremely useful building blocks for
many other signals. We will often find  it useful to consider sets of harmonically related
complex exponentials-that is, sets of periodic exponentials, all of which are periodic with
a common period T0 . Specifically, a necessary condition for a complex exponential ejwr to
be periodic with period T0 is that
                                                                                    (1.33)
which implies that wT0 is a multiple of 27T, i.e.,
                   wTo = 21Tk,      k =  0,::!::: 1, ±:2, 0.    0    0                          ( 1.34)
Thus, if we define
                              wo =  27T                                            ( 1.35)                                          To'
we see that, to satisfy eq. ( 1.34), w must be an integer multiple of w0 . That is, a harmoni-
cally related set of complex exponentials is a set of periodic exponentials with fundamental
frequencies that are all multiples of a single positive frequency w0 :
                                      k =  0,    ::!::: 1, ±:2,. 0.    0                        ( 1.36)
Fork = 0, ¢k(t) is a constant, while for any other value of k, ¢k(t) is periodic with fun-
damental frequency Iklwo and fundamental period
                                         27T  _  To                                                                                                           ( 1.37)                                       lklwo - m·
The kth harmonic ¢k(t) is still periodic with period T0 as well, as it goes through exactly
lkl of its fundamental periods during any time interval of length T0 .
    Our use of the term "harmonic" is consistent with its use in music, where it refers
to tones resulting from variations in acoustic pressure at frequencies that are integer mul-
tiples of a fundamental frequency. For example, the pattern of vibrations of a string on an
instrument such as a violin can be described as a superposition-i.e., a weighted sum-of
harmonically related periodic exponentials. In Chapter 3, we will see that we can build a
very rich class of periodic signals using the harmonically related signals of eq. ( 1.36) as
the building blocks.

    Example 1.5
               It is sometimes desirable to express the sum of two complex exponentials as the product
           of a single complex exponential and a single sinusoid. For example, suppose we wish to

--- PAGE 20 ---

20                                                                   Signals and Systems     Chap. 1

            plot the magnitude of the signal

                                                                                               (1.38)

         To do this, we first factor out a complex exponential from the right side of eq. (1.38),
         where the frequency of this exponential factor is taken as the average of the frequencies
           of the two exponentials in the sum. Doing this, we obtain

                                                                                               (1.39)

          which, because of Euler's relation, can be rewritten as

                                                x(t) =  2ej2.51 cos(0.5t).                           (1.40)

        From this, we can directly obtain an expression for the magnitude of x(t):
                                                           lx(t)l =  21 cos(0.5t)l.                            (1.41)

           Here, we have used the fact that the magnitude of the complex exponential ej2·51 is always
            unity. Thus, lx(t)l is what is commonly referred to as a full-wave rectified sinusoid, as
         shown in Figure 1.22.

                                                              lx(t)l
                                  2





                    Figure 1 .22   The full-wave rectified sinusoid of Example 1.5.

General Complex Exponential Signals
The most general case of a complex exponential can be expressed and interpreted in terms
of the two cases we have examined so far: the real exponential and the periodic complex
exponential. Specifically, consider a complex exponential C eat, where C is expressed in
polar form and a in rectangular form. That is,


and
                    a= r + Jwo.
Then

                                                                                     (1.42)

Using Euler's relation, we can expand this further as
            C eat =  ICiert cos(wot + 0) + JICiert sin(wot + 0).              (1.43)

--- PAGE 21 ---

Sec. 1.3     Exponential and Sinusoidal Signals                                         21

Thus, for r = 0, the real and imaginary parts of a complex exponential are sinusoidal. For
r > 0 they correspond to sinusoidal signals multiplied by a growing exponential, and for
r < 0 they correspond to sinusoidal signals multiplied by a decaying exponential. These
two cases are shown in Figure 1.23. The dashed lines in the figure correspond to the func-
tions ± ICiert. From eq. ( 1.42), we see that ICiert is the magnitude of the complex expo-
nential. Thus, the dashed curves act as an envelope for the oscillatory curve in the figure
in that the peaks of the oscillations just reach these curves, and in this way the envelope
provides us with a convenient way to visualize the general trend in the amplitude of the
oscillations.

                        x(t)





                               (a)

                        x(t)





                                                   Figure 1 .23    (a) Growing sinusoidal
                                                                    signal x(t) =  Cert cos (w0t + 8),
                                                                           r > 0; (b) decaying sinusoid x{t) =
                             (b)                                            Cert cos (w0t + 8), r < 0.

      Sinusoidal signals multiplied by decaying exponentials are commonly referred to as
damped sinusoids. Examples of damped sinusoids arise in the response of RLC circuits
and in mechanical systems containing both damping and restoring forces, such as automo-
tive suspension systems. These kinds of systems have mechanisms that dissipate energy
(resistors, damping forces such as friction) with oscillations that decay in time. Examples
illustrating such systems and their damped sinusoidal natural responses can be found in
Problems 2.61 and 2.62.

1.3.2 Discrete-Time Complex Exponential and Sinusoidal Signals
As in continuous time, an important signal in discrete time is the complex exponential
signal or sequence, defined by

                                                                                                                     ( 1.44)

--- PAGE 22 ---

22                                                                   Signals and Systems     Chap. 1

where C and a are, in general, complex numbers. This could alternatively be expressed
in the form
                                     x[n] = Cef3 11 ,                                (1.45)
where


Although the form of the discrete-time complex exponential sequence given in eq. (1.45) is
more analogous to the form of the continuous-time exponential, it is often more convenient
to express the discrete-time complex exponential sequence in the form of eq. (1.44).

Real Exponential Signals
If C and a are real, we can have one of several types of behavior, as illustrated in Fig-
ure 1.24. If Ia I > 1 the magnitude of the signal grows exponentially with n, while if Ia I < 1
we have a decaying exponential. Furthermore, if a is positive, all the values of Ca 11 are of
the same sign, but if a is negative then the sign of x[n] alternates. Note also that if a = 1
then x[n] is a constant, whereas if a = -1, x[n] alternates in value between +C and -C.
 Real-valued discrete-time exponentials are often used to describe population growth as
 a function of generation and total return on investment as a function of day, month, or
 quarter.

 Sinusoidal Signals
 Another important complex exponential is obtained by using the form given in eq. (1.45)
 and by constraining {3 to be purely imaginary (so that Ia I    1). Specifically, consider
                                                                                     (1.46)
 As in the continuous-time case, this signal is closely related to the sinusoidal signal
                                 x[n] = A cos(w0n + ¢).                           (1.47)
 If we taken to be dimensionless, then both wo and cp have units of radians. Three examples
 of sinusoidal sequences are shown in Figure 1.25.
     As before, Euler's relation allows us to relate complex exponentials and sinusoids:
                                ejwon = cos won + j sin w0n                         (1.48)
 and

                                                                                     (1.49)

 The signals in eqs. (1.46) and ( 1.47) are examples of discrete-time signals with infinite
  total energy but finite average power. For example, since lejwonl2 =  1, every sample of
 the signal in eq. (1.46) contributes 1 to the signal's energy. Thus, the total energy for
  -'X! < n <  'X! is infinite, while the average power per time point is obviously equal to 1.
 Other examples of energy and power calculations for discrete-time signals are given in
 Problem 1.3.

--- PAGE 23 ---

Sec. 1.3     Exponential and Sinusoidal Signals                                    23





                                              n
                                 (a)





                                                  n
                               (b)





                                                n





                                  (c)





                                                n

                                                  Figure 1 .24  The real exponential
                                                                    signal x[n] =  can:
                                                                           (a) a > 1; (b) 0 < a < 1;
                                (d)                                           (c) -1 <a< O; (d) a< -1.

--- PAGE 24 ---

24                                                                   Signals and Systems     Chap. 1


                                                                x[n] = cos (2Tin/12 )
                                '      I





                                                                                  n





                                                                      (a)


                                                               x[n] = cos (8Tin/31)





                                                                                  n





                                                                 (b)



                                                                 x[n] = cos (n/6)





                                                                                  n





                                                                      (c)

                     Figure 1 .25   Discrete-time sinusoidal signals.

General Complex Exponential Signals
The general discrete-time complex exponential can be written and interpreted in terms of
real exponentials and sinusoidal signals. Specifically, if we write C and a in polar form,

--- PAGE 25 ---

Sec. 1.3     Exponential and Sinusoidal Signals                                    25

viz.,
                        C = ICieiH
and


then

                                                                                                                   ( 1.50)
Thus, for Ia I =  1, the real and imaginary parts of a complex exponential sequence are
sinusoidal. For Ia I < 1 they conespond to sinusoidal sequences multiplied by a decaying
exponential, while for lal > 1 they conespond to sinusoidal sequences multiplied by a
growing exponential. Examples of these signals are depicted in Figure 1.26.





                                                                             n



                                                                     (a)


                                                                                                                                                                                                  '   \





                                                                            n



                                                                (b)



          Figure 1.26    (a) Growing discrete-time sinusoidal signals; (b) decaying
            discrete-time sinusoid.

1.3.3 Periodicity Properties of Discrete-Time Complex Exponentials
While there are many similarities between continuous-time and discrete-time signals,
there are also a number of important differences. One of these concerns the discrete-time
exponential signal e.iluon. In Section 1.3.1, we identified the following two properties of its

--- PAGE 26 ---

26                                                                   Signals and Systems     Chap. 1

continuous-time counterpart eiwor: ( 1) the larger the magnitude of w0, the higher is the rate
of oscillation in the signal; and (2) eiwor is periodic for any value of w0• In this section we
describe the discrete-time versions of both of these properties, and as we will see, there
are definite differences between each of these and its continuous-time counterpart.
    The fact that the first of these properties is different in discrete time is a direct conse-
quence of another extremely important distinction between discrete-time and continuous-
time complex exponentials. Specifically, consider the discrete-time complex exponential
with frequency w 0 + 2-rr:
                                                                                     (1.51)
From eq. ( 1.51 ), we see that the exponential at frequency w0 + 2-rr is the same as that
at frequency w 0 . Thus, we have a very different situation from the continuous-time case,
in which the signals eiwor are all distinct for distinct values of w 0 . In discrete time, these
signals are not distinct, as the signal with frequency w 0 is identical to the signals with
frequencies w0 ± 2-rr, w0 ± 4-rr, and so on. Therefore, in considering discrete-time com-
plex exponentials, we need only consider a frequency interval of length 2-rr in which to
choose w 0 . Although, according to eq. (1.51), any interval of length 2-rr will do, on most
occasions we will use the interval 0    ::::; w0 < 2-rr or the interval --rr    ::::; w 0 < 1r.
     Because of the periodicity implied by eq. ( 1.51), the signal eiwon does not have a
continually increasing rate of oscillation as w 0 is increased in magnitude. Rather, as il-
lustrated in Figure 1.27, as we increase w 0 from 0, we obtain signals that oscillate more
and more rapidly until we reach w 0 =  1r. As we continue to increase W(), we decrease the
rate of oscillation until we reach w 0 =  2-rr, which produces the same constant sequence as
w 0 = 0. Therefore, the low-frequency (that is, slowly varying) discrete-time exponentials
have values of w 0 near 0, 2-rr, and any other even multiple of 1r, while the high frequen-
cies (corresponding to rapid variations) are located near w 0 = ± 1r and other odd multiples
of 1r. Note in particular that for w 0 = 1r or any other odd multiple of 1r,
                                                                                     (1.52)
so that this signal oscillates rapidly, changing sign at each point in time [as illustrated in
Figure 1.27(e)].
     The second property we wish to consider concerns the periodicity of the discrete-
time complex exponential. In order for the signal eiwon to be periodic with period N > 0,
we must have
                                                                                     (1.53)
or equivalently,
                                                                                     (1.54)
For eq. ( 1.54) to hold, w 0N must be a multiple of 2-rr. That is, there must be an integer m
such that
                        woN = 2-rrm,                                 (1.55)
or equivalently,

                           m                                                                                     (1.56)
                             N

--- PAGE 27 ---

                                                                                                          (b)                                                                             (c)


                   x[n] = cos (Tin/2)                                                x[n] = cos Tin                                                 x[n] = cos (37Tn/2)

                                                                                                 n         -------    ....        n- - - - - - - -  -                n                                    ... ...


                                (d)                                                                           (e)                                                                                                  (f)


                   x[n] = cos (7Tin/4)                                             x[n] = cos (15Tin/8)                                              x[n] = cos 2Tin
~~ ~~···n ···llliiiiiiiiiiiiliiiiiiiiiiiiiii···n
                                                                                                                                                                                                                                                                                      (i)


                                 (g)                                                                       (h)

                         Figure 1 .27   Discrete-time sinusoidal sequences for several different frequencies.

--- PAGE 28 ---

28                                                                   Signals and Systems     Chap. 1

According to eq. (1.56), the signal ejwon is periodic if w0!27r is a rational number and is
not periodic otherwise. These same observations also hold for discrete-time sinusoids. For
example, the signals depicted in Figure 1.25( a) and (b) are periodic, while the signal in
Figure 1.25( c) is not.
     Using the calculations that we have just made, we can also determine the funda-
mental period and frequency of discrete-time complex exponentials, where we define the
fundamental frequency of a discrete-time periodic signal as we did in continuous time.
That is, if x[ n] is periodic with fundamental period N, its fundamental frequency is 27r/ N.
Consider, then, a periodic complex exponential x[n] = ejwon with w 0  =I= 0. As we have
just seen, w 0 must satisfy eq. (1.56) for some pair of integers m and N, with N > 0. In
Problem 1.35, it is shown that if w 0  =I= 0 and if N and m have no factors in common, then
the fundamental period of x[n] is N. Using this fact together with eq. (1.56), we find that
the fundamental frequency of the periodic signal ejwon is
                                        27r   wo                                                                                     (1.57)
                         N   m

Note that the fundamental period can also be written as

                                                                                     (1.58)

     These last two expressions again differ from their continuous-time counterparts. In
Table 1.1, we have summarized some of the differences between the continuous-time sig-
nal ejwot and the discrete-time signal ejwon. Note that, as in the continuous-time case, the
constant discrete-time signal resulting from setting w 0 = 0 has a fundamental frequency
of zero, and its fundamental period is undefined.
 TABLE 1.1   Comparison of the signals ejwot and ejwon.


  Distinct signals for distinct values of w0    Identical signals for values of w0
                                              separated by multiples of 27T

  Periodic for any choice of w 0               Periodic only if w 0 = 27Tm/N for some integers N > 0 and m.

  Fundamental frequency w0              Fundamental frequency* w0/m

  Fundamental period                    Fundamental period*
   w0 =  0: undefined                    w0 =  0: undefined
    wo ¥-0: ~                                                                     ¥- 0: m(~)wo               wo                           Wo

  *Assumes that m and N do not have any factors in common.
     To gain some additional insight into these properties, let us examine again the signals
depicted in Figure 1.25. First, consider the sequence x[n] = cos(27rn/12), depicted in
Figure 1.25(a), which we can think of as the set of samples ofthe continuous-time sinusoid
x(t) = cos(27rt/12) at integer time points. In this case, x(t) is periodic with fundamental
period 12 and x[n] is also periodic with fundamental period 12. That is, the values of x[n]
repeat every 12 points, exactly in step with the fundamental period of x(t).

--- PAGE 29 ---

Sec. 1.3     Exponential and Sinusoidal Signals                                   29

      In contrast, consider the signal x[ n] = cos(8 7Tn/31 ), depicted in Figure 1.25 (b),
which we can view as the set of samples of x(t) = cos (87Tt/31) at integer points in time.
In this case, x(t) is periodic with fundamental period 31/4. On the other hand, x[n] is pe-
riodic with fundamental period 31. The reason for this difference is that the discrete-time
signal is defined only for integer values of the independent variable. Thus, there is no
sample at timet = 3114, when x(t) completes one period (starting from t = 0). Similarly,
there is no sample at t = 2 · 31/4 or t = 3 · 31/4, when x(t) has completed two or three
periods, but there is a sample at t = 4 · 3114 = 31, when x(t) has completed four periods.
This can be seen in Figure 1.25(b), where the pattern of x[n] values does not repeat with
each single cycle of positive and negative values. Rather, the pattern repeats after four
such cycles, namely, every 31 points.
      Similarly, the signal x[n] = cos(n/6) can be viewed as the set of samples of the
signal x(t) = cos(t/6) at integer time points. In this case, the values of x(t) at integer
sample points never repeat, as these sample points never span an interval that is an exact
multiple of the period, 127T, of x(t). Thus, x[n] is not periodic, although the eye visually
interpolates between the sample points, suggesting the envelope x(t), which is periodic.
The use of the concept of sampling to gain insight into the periodicity of discrete-time
sinusoidal sequences is explored further in Problem 1.36.

    Example 1.6
         Suppose that we wish to determine the fundamental period of the discrete-time signal
                                         x[n] =  ei<27ri3Jn + ei<hl4ln.                         (1.59)

         The first exponential on the right-hand side of eq. (1.59) has a fundamental period of 3.
         While this can be verified from eq. ( 1.58), there is a simpler way to obtain that answer. In
            particular, note that the angle (27T/3)n of the first term must be incremented by a multiple
           of 27T for the values of this exponential to begin repeating. We then immediately see that
              if n is incremented by 3, the angle will be incremented by a single multiple of 27T. With
           regard to the second term, we see that incrementing the angle (37T/4)n by 27T would
           require n to be incremented by 8/3, which is impossible, since n is restricted to being an
            integer. Similarly, incrementing the angle by 47T would require a noninteger increment
           of 16/3 to n. However, incrementing the angle by 61r requires an increment of 8 to n,
          and thus the fundamental period of the second term is 8.
              Now, for the entire signal x[n] to repeat, each of the terms in eq. (1.59) must go
          through an integer number of its own fundamental period. The smallest increment of n
            that accomplishes this is 24. That is, over an interval of 24 points, the first term on the
           right-hand side of eq. ( 1.59) will have gone through eight of its fundamental periods, the
          second term through three of its fundamental periods, and the overall signal x[n] through
           exactly one of its fundamental periods.

    As in continuous time, it is also of considerable value in discrete-time signal and
system analysis to consider sets of harmonically related periodic exponentials-that is,
periodic exponentials with a common period N. From eq. (1.56), we know that these are
precisely the signals which are at frequencies which are multiples of 27T/N. That is,

                                          k =  0, ±1, ....                   (1.60)

--- PAGE 30 ---

             30                                                                   Signals and Systems     Chap. 1

                 In the continuous-time case, all of the harmonically related complex exponentials ei k(27TIT)t,
                k =  0, ± 1, ± 2, ... , are distinct. However, because of eq. ( 1.51 ), this is not the case in
                 discrete time. Specifically,
                                              <f>k+N[n] = ei<k+N)(2TT!N)n
                                                                                                      (1.61)
                                     =  eik(2TT!N)n e)27Tn =  <f>k[n].

               This implies that there are only N distinct periodic exponentials in the set given in
                  eq. ( 1.60). For example,
                                                                                                                            ( 1.62)
                 are all distinct, and any other cf>k[n] is identical to one of these (e.g., cf>N[n] =  <f>0[n] and
                    <f>-I[n] = cf>N-I[n]).

1 .4 THE UNIT IMPULSE AND UNIT STEP FUNCTIONS

                 In this section, we introduce several other basic signals-specifically, the unit impulse and
                 step functions in continuous and discrete time-that are also of considerable importance in
                 signal and system analysis. In Chapter 2, we will see how we can use unit impulse signals
                 as basic building blocks for the construction and representation of other signals. We begin
               with the discrete-time case.

             1 .4. 1 The Discrete-Time Unit Impulse and Unit Step Sequences
            One of the simplest discrete-time signals is the unit impulse (or unit sample), which is
                defined as

                                                        n=rfO                                                                                                      (1.63)                                                           ll[nj = { ~:  n = 0

              and which is shown in Figure 1.28. Throughout the book, we will refer too [n] interchange-
                ably as the unit impulse or unit sample.


                                                        8[n]


                                                                   Figure                                                                      1.28   Discrete-time unit im-                • • • • • • •    • • • • • • • •        n   pulse                                                                                         (sample).

             A second basic discrete-time signal is the discrete-time unit step, denoted by u[n]
              and defined by

                                  n<O                                                                                                                            ( 1.64)                                                u[n] = { ~:  n ~ o·

             The unit step sequence is shown in Figure 1.29.

--- PAGE 31 ---

     Sec. 1.4    The Unit Impulse and Unit Step Functions                                    31


                                          u[n]
• • • • • • • • • • • JIIIIII0                          n    sequence.Figure 1.29   Discrete-time unit step



 Interval of summation

                               o[m]





                                                                      I    • • • • • • n• • • • . I0 . . . . . . . .   m
                                           (a)

                              Interval of summation

                               o[m]

    • • • • • • • • •      0          n        m         ..I.........     Figure 1.30   Running sum of
                                         (b)                                     eq. (1.66): (a) n < 0; (b) n > 0.

         There is a close relationship between the discrete-time unit impulse and unit step. In
     particular, the discrete-time unit impulse is the first difference of the discrete-time step
                          B [n] = u[n] -  u[n -  1].                           (1.65)

    Conversely, the discrete-time unit step is the running sum of the unit sample. That is,

                                                               n
                                       u[n] = ~  B[m].                              (1.66)
                                    m= -oo

    Equation (1.66) is illustrated graphically in Figure 1.30. Since the only nonzero value of
     the unit sample is at the point at which its argument is zero, we see from the figure that the
    running sum in eq. (1.66) is 0 for n < 0 and 1 for n 2: 0. Furthermore, by changing the
     variable of summation from m to k = n - min eq. (1.66), we find that the discrete-time
     unit step can also be written in terms of the unit sample as

                                                    0
                                      u[n] = ~ B[n- k],
                                                    k='X

     or equivalently,

                                      u[n] = ~ B[n -  k].                             (1.67)
                                          k=O

--- PAGE 32 ---

32                                                                  Signals and Systems     Chap. 1


                                  Interval of summation

              o[n-k]      ~-----------

                                                                                                        I • • • • • • • •    k     • • •   n   • • • 0•       .I.
                                        (a)


                                     Interval of summation
                     '----- "3[n~k]----

      . . . . . . . . . . . . . . I . . . .                          0          n            k
                                                   Figure 1 .31    Relationship given in
                                       (b)                                 eq. (1.67): (a) n < 0; (b) n > 0.

Equation (1.67) is illustrated in Figure 1.31. In this case the nonzero value of 8[n- k] is
at the value of k equal ton, so that again we see that the summation in eq. (1.67) is 0 for
n < 0 and 1 for n  2:: 0.
    An interpretation of eq. ( 1.67) is as a superposition of delayed impulses; i.e., we can
view the equation as the sum of a unit impulse 8[n] at n = 0, a unit impulse 8[n- 1] at
n =  1, another, 8[n- 2], at n = 2, etc. We will make explicit use of this interpretation in
Chapter 2.
     The unit impulse sequence can be used to sample the value of a signal at n = 0. In
particular, since 8[n] is nonzero (and equal to 1) only for n = 0, it follows that

                                x[n]o[n] = x[O]o[n].                             (1.68)

More generally, if we consider a unit impulse 8[n -  n0] at n = n0 , then

                         x[n]8[n -  no] = x[no]8[n- no].                      (1.69)

This sampling property of the unit impulse will play an important role in Chapters 2
and 7.

1 .4.2 The Continuous-Time Unit Step
     and Unit Impulse Functions
The continuous-time unit step function u(t) is defined in a manner similar to its discrete-
time counterpart. Specifically,

                            t<O                                                                                     (1.70)                                      u(t) ~ { ~:     t > 0'

as  is shown in Figure  1.32. Note that the unit step  is discontinuous at  t     0. The
continuous-time unit impulse function 8(t) is related to the unit step in a manner analogous

--- PAGE 33 ---

Sec. 1.4    The Unit Impulse and Unit Step Functions                                33


                                u(t)





                                                   Figure 1 .32   Continuous-time unit
                       0                                     step function.

to the relationship between the discrete-time unit impulse and step functions. In particular,
the continuous-time unit step is the running integral of the unit impulse

                                                                                    (1.71)

This also suggests a relationship between 8(t) and u(t) analogous to the expression for
8[n] in eq. (1.65). In particular, it follows from eq. (1.71) that the continuous-time unit
impulse can be thought of as the first derivative of the continuous-time unit step:

                                        8(t) =  d~;t).                                (1.72)

      In contrast to the discrete-time case, there is some formal difficulty with this equa-
tion as a representation of the unit impulse function, since u(t) is discontinuous at t = 0
and consequently is formally not differentiable. We can, however, interpret eq. (1.72) by
considering an approximation to the unit step u11 (t), as illustrated in Figure 1.33, which
rises from the value 0 to the value 1 in a short time interval of length Ll. The unit step,
of course, changes values instantaneously and thus can be thought of as an idealization of
u11(t) for Ll so short that its duration doesn't matter for any practical purpose. Formally,
u(t) is the limit of Uf1 (t) as Ll ~ 0. Let us now consider the derivative

                                           ~  ( ) _  du11(t)                                        u 11  t   -   -----;[('                               (1.73)

as shown in Figure 1.34.



                       u~(t)





                                                                   0   11

        Figure 1 .33   Continuous approximation to    Figure 1.34   Derivative of
          the unit step, u~(t).                                   u~(t).

--- PAGE 34 ---

34                                                                   Signals and Systems     Chap. 1





                              0                              0

               Figure 1.35   Continuous-      Figure 1.36   Scaled im-
                  time unit impulse.                   pulse.

     Note that o~(t) is a short pulse, of duration~ and with unit area for any value of~.
As~ ~ 0, o~(t) becomes narrower and higher, maintaining its unit area. Its limiting form,
                                      o(t) = lim o~(t),                               (1.74)
                                                                             ~---->0

can then be thought of as an idealization of the short pulse o~(t) as the duration~ becomes
insignificant. Since o(t) has, in effect, no duration but unit area, we adopt the graphical
notation for it shown in Figure 1.35, where the arrow at t = 0 indicates that the area of the
pulse is concentrated at t = 0 and the height of the arrow and the "1" next to the arrow
are used to represent the area of the impulse. More generally, a scaled impulse ko(t) will
have an area k, and thus,
                   L% kD(r)dr = ku(t).

A scaled impulse with area k is shown in Figure 1.36, where the height of the arrow used
to depict the scaled impulse is chosen to be proportional to the area of the impulse.
    As with discrete time, we can provide a simple graphical interpretation of the running
integral of eq. (1.71); this is shown in Figure 1.37. Since the area of the continuous-time
unit impulse o( T) is concentrated at T = 0, we see that the running integral is 0 fort < 0
and 1 for t > 0. Also, we note that the relationship in eq. ( 1. 71) between the continuous-
time unit step and impulse can be rewritten in a different form, analogous to the discrete-
time form in eq. (1.67), by changing the variable of integration from T to u = t- T:
                          u(t) = L% (j( r) dr =    D(t -  <r)( -da"),             r
or equivalently,

                                     u(t) =   D(t- a) d<r.                            (1.75)          r
     The graphical interpretation of this form of the relationship between u(t) and o(t) is
given in Figure 1.38. Since in this case the area of o(t - u) is concentrated at the point
u =   t, we again see that the integral in eq. (1.75) is 0 fort < 0 and 1 fort> 0. This type
of graphical interpretation of the behavior of the unit impulse under integration will be
extremely useful in Chapter 2.

--- PAGE 35 ---

                 Sec. 1.4    The Unit Impulse and Unit Step Functions                                35



Interval of integration                                                                                 Interval of integration
                                                                    8(t-u)




                          0                                                  'T                         0                                                              (}'

                                      (a)                                                                                  (a)



             Interval of integration                                                                                                       Interval of integration
   --------------~-----,                                                                                         8(t-u)                                              8(-r)       :
                                                                                                                                I
                                                                                                                         I
                                                                                                                          I
                                                                                                                          I
                          0                                                     'T                         0                                                              (}'


                                    (b)                                                                            (b)

Figure 1.37   Running integral given in eq. (1.71 ):        Figure 1.38   Relationship given in eq. (1.75):
(a) t < 0; (b) t > 0.                                                     (a) t < 0; (b) t > 0.

                As with the discrete-time impulse, the continuous-time impulse has a very important
             sampling property. In particular, for a number of reasons it will be important to consider
               the product of an impulse and more well-behaved continuous-time functions x(t). The in-
               terpretation of this quantity is most readily developed using the definition of o(t) according
                  to eq. (1.74). Specifically, consider

                                                        Xt (t) =  x(t)Dtl.(t).

               In Figure 1.39(a) we have depicted the two time functions x(t) and Ofl.(t), and in Fig-
              ure 1.39(b) we see an enlarged view of the nonzero portion of their product. By construc-
                 tion, x 1(t) is zero outside the interval 0    ::::;  t    ::::; ~. For~ sufficiently small so that x(t) is
             approximately constant over this interval,


              Since o(t) is the limit as~ ~ 0 of Dfl.(t), it follows that
                                                      x(t)B(t) = x(O)o(t).                                    ( 1. 76)

          By the same argument, we have an analogous expression for an impulse concentrated at
             an arbitrary point, say, t0 . That is,
                                              x(t)o (t -  to) = x(to)D(t -  to).

--- PAGE 36 ---

36                                                                  Signals and Systems     Chap. 1


                                     o~(t)





                      0 ~
                                   (a)





             x(O)~

                                                   Figure 1.39  The product x(t)o~(t):
                                                                            (a) graphs of both functions; (b) en-                      0                                                                 larged view of the nonzero portion of
                                 (b)                                        their product.

     Although our discussion of the unit impulse in this section has been somewhat in-
formal,  it does provide us with some important intuition about this signal that will be
useful throughout the book. As we have stated, the unit impulse should be viewed as an
idealization. As we illustrate and discuss in more detail in Section 2.5, any real physi-
cal system has some inertia associated with it and thus does not respond instantaneously
to inputs. Consequently, if a pulse of sufficiently short duration is applied to such a sys-
tem, the system response will not be noticeably influenced by the pulse's duration or by
the details of the shape of the pulse, for that matter. Instead, the primary characteristic
of the pulse that will matter is the net, integrated effect of the pulse-i.e., its area. For
systems that respond much more quickly than others, the pulse will have to be of much
shorter duration before the details of the pulse shape or its duration no longer matter. Nev-
ertheless, for any physical system, we can always find a pulse that is "short enough."
The unit impulse then is an idealization of this concept-the pulse that is short enough
for any system. As we will see in Chapter 2, the response of a system to this idealized
pulse plays a crucial role in signal and system analysis, and in the process of devel-
oping and understanding this role, we will develop additional insight into the idealized
signal.3

      3The unit impulse and other related functions (which are often collectively referred to as singularity
functions) have been thoroughly studied in the field of mathematics under the alternative names of general-
ized functions and the theory of distributions. For more detailed discussions of this subject, see Distribution
Theory and Transfonn Analysis, by A. H. Zemanian (New York: McGraw-Hill Book Company, 1965), Gen-
eralised Functions, by R.F. Hoskins (New York: Halsted Press, 1979), or the more advanced text, Fourier
Analysis and Generalized Functions, by M.  J. Lighthill (New York: Cambridge University Press, 1958).
Our discussion of singularity functions in Section 2.5 is closely related in spirit to the mathematical theory
described in these texts and thus provides an informal introduction to concepts that underlie this topic in
mathematics.

--- PAGE 37 ---

Sec. 1.4    The Unit Impulse and Unit Step Functions                                37

   Example 1.7
          Consider the discontinuous signal x(t) depicted in Figure 1.40(a). Because of the rela-
           tionship between the continuous-time unit impulse and unit step, we can readily calculate
         and graph the derivative of this signal. Specifically, the derivative of x(t) is clearly 0,
          except at the discontinuities. In the case of the unit step, we have seen [eq. (1.72)] that
            differentiation gives rise to a unit impulse located at the point of discontinuity. Further-
          more, by multiplying both sides of eq. (1.72) by any number k, we see that the derivative
          of a unit step with a discontinuity of size k gives rise to an impulse of area k at the point
           of discontinuity. This rule also holds for any other signal with a jump discontinuity, such
           as x(t) in Figure 1.40(a). Consequently, we can sketch its derivative x(t), as in Fig-
           ure 1.40(b), where an impulse is placed at each discontinuity of x(t), with area equal to
           the size of the discontinuity. Note, for example, that the discontinuity in x(t) at t = 2
          has a value of- 3, so that an impulse scaled by -3 is located at t = 2 in the signal x(t).


                                          x(t)

                 2-     -

                              1  -
                                      2  3
                                                                                                                     (a)
                                                   4
                          -1 ~

                                     x(t)
                         2f-

                              1 r-
                                      2  3
                                                                                                             (b)
                                               4
                          -1  r-

                       -2 t-

                       -3 f-

                                    - - ~Interval of integration


                              1 -:
                                       2  3
                                                                                                                      (c)
                                                  4
                          -1  -

                 -2-

                 -3-

              Figure 1.40    (a) The discontinuous signal x(t) analyzed in Example 1.7;
                    (b) its derivative x(t); (c) depiction of the recovery of x(t) as the running inte-
                    gral of x(t), illustrated for a value of  t between 0 and 1.

--- PAGE 38 ---

             38                                                                   Signals and Systems     Chap. 1

                           As a check of our result, we can verify that we can recover x(t) from x(t). Specif-
                                   ically, since x(t) and x(t) are both zero fort     :::::: 0, we need only check that fort > 0,

                                                                                                                    1
                                                                         X(t) =    {  X( 7) dT.                              (1.77)
                                                                                   Jo
                      As illustrated in Figure 1.40(c), fort< 1, the integral on the right-hand side of eq. (1.77)
                                      is zero, since none of the impulses that constitute x(t) are within the interval of integra-
                                   tion. For 1 <  t < 2, the first impulse (located at t =  1) is the only one within the inte-
                              gration interval, and thus the integral in eq. (1.77) equals 2, the area of this impulse. For
                         2 <  t < 4, the first two impulses are within the interval of integration, and the integral
                          accumulates the sum of both of their areas, namely, 2 - 3 =  - 1. Finally, for t > 4, all
                              three impulses are within the integration interval, so that the integral equals the sum of
                                     all three areas-that is, 2 - 3 + 2 = + 1. The result is exactly the signal x(t) depicted
                                in Figure 1.40(a).

1 .5 CONTINUOUS-TIME AND DISCRETE-TIME SYSTEMS

                Physical systems in the broadest sense are an interconnection of components, devices,
                 or subsystems. In contexts ranging from signal processing and communications to elec-
                tromechanical motors, automotive vehicles, and chemical-processing plants, a system can
               be viewed as a process in which input signals are transformed by the system or cause the
               system to respond in some way, resulting in other signals as outputs. For example, a high-
                    fidelity system takes a recorded audio signal and generates a reproduction of that signal.
                   If the hi-fi system has tone controls, we can change the tonal quality of the reproduced sig-
                   nal. Similarly, the circuit in Figure 1.1 can be viewed as a system with input voltage Vs(t)
              and output voltage vc(t), while the automobile in Figure 1.2 can be thought of as a system
                with input equal to the force f(t) and output equal to the velocity v(t) of the vehicle. An
              image-enhancement system transforms an input image into an output image that has some
                desired properties, such as improved contrast.
             A continuous-time system is a system in which continuous-time input signals are
                applied and result in continuous-time output signals. Such a system will be represented
                  pictorially as in Figure 1.41(a), where x(t) is the input and y(t) is the output. Alterna-
                    tively, we will often represent the input-output relation of a continuous-time system by the
                 notation
                                                              x(t) ~ y(t).                                  (1.78)


                                               x(t) --~• Continuous-time  ......._...,. y(t)
                                              system

                                                                            (a)



                                                 Discrete-time                 x[n]--~                             ......-         ...... y[n]                                             system
                                                                   Figure 1 .41    (a) Continuous-time
                                                                       (b)                        system; (b) discrete-time system.

--- PAGE 39 ---

Sec. 1.5     Continuous-Time and Discrete-Time Systems                             39

Similarly, a discrete-time system-that is, a system that transforms discrete-time inputs
into discrete-time outputs-will be depicted as in Figure 1.41 (b) and will sometimes be
represented symbolically as

                                      x[n] ~ y[n].                                 (1.79)

In most of this book, we will treat discrete-time systems and continuous-time systems
separately but in parallel. In Chapter 7, we will bring continuous-time and discrete-time
systems together through the concept of sampling, and we will develop some insights
into the use of discrete-time systems to process continuous-time signals that have been
sampled.

1.5.1 Simple Examples of Systems
One of the most important motivations for the development of general tools for analyzing
and designing systems is that systems from many different applications have very similar
mathematical descriptions. To illustrate this, we begin with a few simple examples.

    Example 1.8
          Consider the RC circuit depicted in Figure 1.1. If we regard vs(t) as the input signal and
             vc(t) as the output signal, then we can use simple circuit analysis to derive an equation
           describing the relationship between the input and output. Specifically, from Ohm's law,
           the current i(t) through the resistor is proportional (with proportionality constant 11 R) to
           the voltage drop across the resistor; i.e.,

                                                                               '( )     Vs(t) -  Vc(t)                                                       1 t  =     R          .                            (1.80)

            Similarly, using the defining constitutive relation for a capacitor, we can relate i(t) to the
            rate of change with time of the voltage across the capacitor:

                                                                                  '( ) -  cdvc(t)                         lt-                         d['                               (1.81)

          Equating the right-hand sides of eqs. (1.80) and (1.81), we obtain a differential equation
           describing the relationship between the input vs(t) and the output vc(t):

                                         dvc(t)    1    ( ) _   1    ( )             dt + RC Vc  t   - RC Vs  t  .                       (1.82)

    Example 1.9
          Consider Figure 1.2, in which we regard the force f(t) as the input and the velocity v(t)
            as the output. If we let m denote the mass of the automobile and mpv the resistance due
             to friction, then equating acceleration-i.e., the time derivative of velocity-with net
           force divided by mass, we obtain

                                          dv(t)    1                                                                  -  [f(t)- pv(t) J,                         (1.83)                                         dt    m

--- PAGE 40 ---

40                                                                  Signals and Systems     Chap. 1

                i.e.,
                                           dv(t) + p_v(t) =  _!_ j(t).                          (1.84)
                                        dt   m     m

     Examining and comparing eqs. (1.82) and (1.84) in the above examples, we see that
the input-output relationships captured in these two equations for these two very different
physical systems are basically the same. In particular, they are both examples of first-order
linear differential equations of the form

                                 dy(t)
                                                   -----;[( + ay(t) = bx(t),                            (1.85)

where x(t) is the input, y(t) is the output, and a and bare constants. This is one very simple
example of the fact that, by developing methods for analyzing general classes of systems
such as that represented by eq. (1.85), we will be able to use them in a wide variety of
applications.

    Example 1. 1 0
        As a simple example of a discrete-time system, consider a simple model for the balance
            in a bank account from month to month. Specifically, let y[n] denote the balance at the
         end of the nth month, and suppose that y[n] evolves from month to month according to
           the equation
                                         y[n] = l.Oly[n- 1] + x[n],                        (1.86)
           or equivalently,
                                        y[n] - l.Oly[n- 1] =  x[n],                        (1.87)
         where x[n] represents the net deposit (i.e., deposits minus withdrawals) during the nth
         month and the term 1.01y[n- 1] models the fact that we accrue 1% interest each month.

    Example 1. 11
         As a second example, consider a simple digital simulation of the differential equation in
            eq. (1.84) in which we resolve time into discrete intervals oflength Ll and approximate
           dv(t)ldt at t = nLl by the first backward difference, i.e.,
                                               v(nLl) - v((n- 1)Ll)
                                                                     Ll
           In this case, if we let v[n] =  v(nLl) and f[n] =  j(nLl), we obtain the following discrete-
          time model relating the sampled signals f[n] and v[n]:

                         m                           Ll
                                 v[n] -  (m + pLl) v[n -  1] =  (m + pLl) f[n].                (1.88)

              Comparing eqs. (1.87) and (1.88), we see that they are both examples of the same
           general first-order linear difference equation, namely,
                                          y[n] + ay[n -  1] = bx [n].                         (1.89)

--- PAGE 41 ---

Sec. 1.5     Continuous-Time and Discrete-Time Systems                                  41

    As the preceding examples suggest, the mathematical descriptions of systems from
a wide variety of applications frequently have a great deal in common, and it is this fact
that provides considerable motivation for the development of broadly applicable tools for
signal and system analysis. The key to doing this successfully is identifying classes of
systems that have two important characteristics: ( 1) The systems in this class have prop-
erties and structures that we can exploit to gain insight into their behavior and to develop
effective tools for their analysis~ and (2) many systems of practical importance can be
accurately modeled using systems in this class. It is on the first of these characteristics
that most of this book focuses, as we develop tools for a particular class of systems re-
ferred to as linear, time-invariant systems. In the next section, we will introduce the prop-
erties that characterize this class, as well as a number of other very important basic system
properties.
    The second characteristic mentioned in the preceding paragraph is of obvious impor-
tance for any system analysis technique to be of value in practice. It is a well-established
fact that a wide range of physical systems (including those in Examples 1.8-1.10) can
be well modeled within the class of systems on which we focus in this book. However,
a critical point is that any model used in describing or analyzing a physical system rep-
resents an idealization of that system, and thus, any resulting analysis is only as good
as the model  itself. For example, the simple linear model of a resistor in eq. (1.80)
and that of a capacitor in eq. ( 1.81) are idealizations. However, these idealizations are
quite accurate for real resistors and capacitors in many applications, and thus, analy-
ses employing such idealizations provide useful results and conclusions, as long as the
voltages and currents remain within the operating conditions under which these simple
linear models are valid. Similarly, the use of a linear retarding force to represent fric-
tional effects in eq. (1.83) is an approximation with a range of validity. Consequently,
although we will not address this issue in the book,  it is important to remember that
an essential component of engineering practice in using the methods we develop here
consists of identifying the range of validity of the assumptions that have gone into a
model and ensuring that any analysis or design based on that model does not violate those
assumptions.


1.5.2 Interconnections of Systems
An important idea that we will use throughout this book is the concept of the interconnec-
tion of systems. Many real systems are built as interconnections of several subsystems.
One example is an audio system, which involves the interconnection of a radio receiver,
compact disc player, or tape deck with an amplifier and one or more speakers. Another is
a digitally controlled aircraft, which is an interconnection of the aircraft, described by its
equations of motion and the aerodynamic forces affecting it~ the sensors, which measure
various aircraft variables such as accelerations, rotation rates, and heading~ a digital au-
topilot, which responds to the measured variables and to command inputs from the pilot
(e.g., the desired course, altitude, and speed)~ and the aircraft's actuators, which respond
to inputs provided by the autopilot in order to use the aircraft control surfaces (rudder,
tail, ailerons) to change the aerodynamic forces on the aircraft. By viewing such a system
as an interconnection of its components, we can use our understanding of the component

--- PAGE 42 ---

42                                                                  Signals and Systems     Chap. 1



                    Input        System 1            System 2          Output


                                                                    (a)





                                                                 Output




                                                                 (b)


                  System 1

 Input~                                                    System 4        Output

                            System 3


                                                                    (c)

         Figure 1.42   Interconnection of two systems: (a) series (cascade) intercon-
            nection; (b) parallel interconnection; (c) series-parallel interconnection.

systems and of how they are interconnected in order to analyze the operation and behavior
of the overall system. In addition, by describing a system in terms of an interconnection of
simpler subsystems, we may in fact be able to define useful ways in which to synthesize
complex systems out of simpler, basic building blocks.
     While one can construct a variety of system interconnections, there are several basic
ones that are frequently encountered. A series or cascade interconnection of two systems
is illustrated in Figure 1.42(a). Diagrams such as this are referred to as block diagrams.
Here, the output of System 1 is the input to System 2, and the overall system transforms
an input by processing it first by System 1 and then by System 2. An example of a series
interconnection is a radio receiver followed by an amplifier. Similarly, one can define a
series interconnection of three or more systems.
   A parallel interconnection of two systems is illustrated in Figure 1.42(b ). Here, the
same input signal is applied to Systems 1 and 2. The symbol "EB" in the figure denotes
addition, so that the output of the parallel interconnection is the sum of the outputs of
Systems 1 and 2. An example of a parallel interconnection is a simple audio system with
several microphones feeding into a single amplifier and speaker system. In addition to the
simple parallel interconnection in Figure 1.42(b ), we can define parallel interconnections
of more than two systems, and we can combine both cascade and parallel interconnections

--- PAGE 43 ---

    Sec. 1.5     Continuous-Time and Discrete-Time Systems                              43





                                                      Figure 1 .43   Feedback interconnec-
                                                                               tion.

    to obtain more complicated interconnections. An example of such an interconnection is
   given in Figure 1.42(c).4
        Another important type of system interconnection is a feedback interconnection, an
   example of which is illustrated in Figure 1.43. Here, the output of System 1 is the input to
   System 2, while the output of System 2 is fed back and added to the external input to pro-
   duce the actual input to System 1. Feedback systems arise in a wide variety of applications.
   For example, a cruise control system on an automobile senses the vehicle's velocity and
   adjusts the fuel flow in order to keep the speed at the desired level. Similarly, a digitally
   controlled aircraft is most naturally thought of as a feedback system in which differences
   between actual and desired speed, heading, or altitude are fed back through the autopilot
   in order to correct these discrepancies. Also, electrical circuits are often usefully viewed
   as containing feedback interconnections. As an example, consider the circuit depicted in
   Figure 1.44(a). As indicated in Figure 1.44(b), this system can be viewed as the feedback
   interconnection of the two circuit elements.


                                +
                               i1 (t)                i2 (t)              t        t
                       i(t)      C        R          v(t)        t





                            Capacitori(t)   +              i1 (t)
~ +                                                                  v(t)                                  v(t) = ~ ~-~i 1 (T)dT                           -



                                                      Figure 1 .44    (a) Simple electrical                              i2 (t)         Resistor
                                                      .  (t) _ v(t)                                  circuit; (b) block diagram in which the                                                 12 -R                                circuit is depicted as the feedback inter-
                                                                connection of two circuit elements.


         40n occasion, we will also use the symbol 0  in our pictorial representation of systems to denote the
    operation of multiplying two signals (see, for example, Figure 4.26).

--- PAGE 44 ---

             44                                                                   Signals and Systems     Chap. 1

1 .6 BASIC SYSTEM PROPERTIES

                In this section we introduce and discuss a number of basic properties of continuous-time
              and discrete-time systems. These properties have important physical interpretations and
                  relatively simple mathematical descriptions using the signals and systems language that
            we have begun to develop.

             1 . 6. 1 Systems with and without Memory
          A system is said to be memory less if its output for each value of the independent variable
                    at a given time is dependent only on the input at that same time. For example, the system
                 specified by the relationship

                                                                                                      (1.90)

                      is memory less, as the value of y[n] at any particular time n0 depends only on the value of
                 x[n] at that time. Similarly, a resistor is a memory less system; with the input x(t) taken as
                 the current and with the voltage taken as the output y(t), the input-output relationship of a
                   resistor is
                                                               y(t) = Rx(t),                                 (1.91)

              where R is the resistance. One particularly simple memoryless system is the identity sys-
                 tem, whose output is identical to its input. That is, the input-output relationship for the
                continuous-time identity system is
                                                               y(t) =  x(t),

              and the corresponding relationship in discrete time is
                                                       y[n] = x[n].

               An example of a discrete-time system with memory is an accumulator or summer

                                                                                                                                                  II
                                                                                                       (1.92)                                                     y[n] = L   x[k],
                                                                          k=-CXJ

               and a second example is a delay

                                                     y[n] = x[n -  1].                               (1.93)

          A capacitor is an example of a continuous-time system with memory, since if the input is
                taken to be the current and the output is the voltage, then

                                                          y(t) = C1  -x x(r)dr,                             (1.94)                                                              f'

              where C is the capacitance.
                   Roughly speaking, the concept of memory in a system corresponds to the presence
                of a mechanism in the system that retains or stores information about input values at times

--- PAGE 45 ---

Sec. 1.6     Basic System Properties                                           45

other than the current time. For example, the delay in eq. (1.93) must retain or store the
preceding value of the input. Similarly, the accumulator in eq. (1.92) must "remember" or
store information about past inputs. In particular, the accumulator computes the running
sum of all inputs up to the current time, and thus, at each instant of time, the accumulator
must add the current input value to the preceding value of the running sum. In other words,
the relationship between the input and output of an accumulator can be described as

                                          n-1
                                y[n] = L  x[k] + x[n],                          (1.95)
                                k=-X

or equivalently,
                                 y[n] = y[n -  1] + x[n].                           (1.96)
Represented in the latter way, to obtain the output at the current time n, the accumulator
must remember the running sum of previous input values, which is exactly the preceding
value of the accumulator output.
      In many physical systems, memory is directly associated with the storage of energy.
For example, the capacitor in eq. (1.94) stores energy by accumulating electrical charge,
represented as the integral of the current. Thus, the simple RC circuit in Example 1.8
and Figure 1.1 has memory physically stored in the capacitor. Similarly, the automobile in
Figure 1.2 has memory stored in its kinetic energy. In discrete-time systems implemented
with computers or digital microprocessors, memory is typically directly associated with
storage registers that retain values between clock pulses.
     While the concept of memory in a system would typically suggest storing past input
and output values, our formal definition also leads to our referring to a system as having
memory if the current output is dependent on future values of the input and output. While
systems having this dependence on future values might at first seem unnatural, they in fact
form an important class of systems, as we discuss further in Section 1.6.3.

1.6.2 lnvertibility and Inverse Systems
A system is said to be invertible if distinct inputs lead to distinct outputs. As illustrated in
Figure 1.45( a) for the discrete-time case, if a system is invertible, then an inverse system
exists that, when cascaded with the original system, yields an output w[n] equal to the
input x[n] to the first system. Thus, the series interconnection in Figure 1.45(a) has an
overall input-output relationship which is the same as that for the identity system.
    An example of an invertible continuous-time system is
                                           y(t) = 2x(t),                                 (1.97)
for which the inverse system is

                                    1                                     w(t) =  2: y(t).                                (1.98)

This example is illustrated in Figure 1.45(b ). Another example of an invertible system
is the accumulator of eq. (1.92). For this system, the difference between two successive

--- PAGE 46 ---

46                                                                   Signals and Systems     Chap. 1


                                        y[n]
        x[n]         System                                             ......--...~~ w[n] = x[n]


                                                (a)



           x(t)


                                              (b)



                                                       y(n]                                                      w(n] ~ y[n] -  y(n -1] ~ w(n]    x[n]        x[n[ --I......__Y_[n_J_=_k _}___x _x[-kJ_   _.                                  •I

                                                  (c)

         Figure 1 .45   Concept of an inverse system for: (a) a general invertible sys-
           tem; (b) the invertible system described by eq. (1.97); (c) the invertible system
            defined in eq. (1.92).

values of the output is precisely the last input value. Therefore, in this case, the inverse
system is
                             w[n] = y[n] -  y[n -  1],                           (1.99)

as illustrated in Figure 1.45( c). Examples of noninvertible systems are
                                        y[n] = 0,                                (1.100)
that is, the system that produces the zero output sequence for any input sequence, and
                                                                                 (1.101)
in which case we cannot determine the sign of the input from knowledge of the output.
     The concept of invertibility is important in many contexts. One example arises in
systems for encoding used in a wide variety of communications applications. In such a
system, a signal that we wish to transmit is first applied as the input to a system known
as an encoder. There are many reasons for doing this, ranging from the desire to encrypt
the original message for secure or private communication to the objective of providing
some redundancy in the signal (for example, by adding what are known as parity bits)
so that any errors that occur in transmission can be detected and, possibly, corrected. For
lossless coding, the input to the encoder must be exactly recoverable from the output; i.e.,
the encoder must be invertible.

1 .6.3 Causality
A system is causal if the output at any time depends only on values of the input at the
present time and in the past. Such a system is often referred to as being nonanticipative, as

--- PAGE 47 ---

Sec. 1.6     Basic System Properties                                           47

the system output does not anticipate future values of the input. Consequently, if two inputs
to a causal system are identical up to some point in time to or n0 , the corresponding outputs
must also be equal up to this same time. The RC circuit of Figure 1.1 is causal, since
the capacitor voltage responds only to the present and past values of the source voltage.
Similarly, the motion of an automobile is causal, since it does not anticipate future actions
of the driver. The systems described in eqs. (1.92)- (1.94) are also causal, but the systems
defined by
                                y[n] = x[n] -  x[n + 1]                         (1.102)
and
                                          y(t) = x(t + 1)                             (1.103)
are not. All memory less systems are causal, since the output responds only to the current
value of the input.
     Although causal systems are of great importance, they do not by any means constitute
the only systems that are of practical significance. For example, causality is not often an
essential constraint in applications in which the independent variable is not time, such as in
image processing. Furthermore, in processing data that have been recorded previously, as
often happens with speech, geophysical, or meteorological signals, to name a few, we are
by no means constrained to causal processing. As another example, in many applications,
including historical stock market analysis and demographic studies, we may be interested
in determining a slowly varying trend in data that also contain high-frequency fluctuations
about that trend. In this case, a commonly used approach is to average data over an interval
in order to smooth out the fluctuations and keep only the trend. An example of a noncausal
averaging system is
                                 1    +M
                             y[n]                                                (1.104)                     2M + 1 k~M x[ n -  k].

    Example 1. 1 2
        When checking the causality of a system, it is important to look carefully at the input-
           output relation. To illustrate some of the issues involved in doing this, we will check the
           causality of two particular systems.
              The first system is defined by

                                               y[n] =  x[ -n].                             (1.105)

         Note that the output y[n0 ] at a positive time no depends only on the value of the input
           signal x[- no] at time (- n0 ), which is negative and therefore in the past of no. We may
          be tempted to conclude at this point that the given system is causal. However, we should
          always be careful to check the input-output relation for all times. In particular, for n < 0,
             e.g. n =  -4, we see that y[ -4] =  x[ 4], so that the output at this time depends on a future
          value of the input. Hence, the system is not causal.
                        It is also important to distinguish carefully the effects of the input from those of
          any other functions used in the definition of the system. For example, consider the system
                                                  y(t) =  x(t) cos(t + 1).                         (1.106)

--- PAGE 48 ---

48                                                                   Signals and Systems     Chap. 1

           In this system, the output at any time t equals the input at that same time multiplied by
          a number that varies with time. Specifically, we can rewrite eq. ( 1.1 06) as
                                                     y(t) = x(t)g(t),
         where g(t) is a time-varying function, namely g(t) =  cos(t + 1). Thus, only the current
          value of the input x(t) influences the current value of the output y(t), and we conclude
            that this system is causal (and, in fact, memoryless).

1 .6.4 Stability
Stability is another important system property. Informally, a stable system is one in which
small inputs lead to responses that do not diverge. For example, consider the pendulum in
Figure 1.46(a), in which the input is the applied force x(t) and the output is the angular
deviation y(t) from the vertical. In this case, gravity applies a restoring force that tends
to return the pendulum to the vertical position, and frictional losses due to drag tend to
slow it down. Consequently, if a small force x(t) is applied, the resulting deflection from
vertical will also be small. In contrast, for the inverted pendulum in Figure 1.46(b ), the
effect of gravity is to apply a force that tends to increase the deviation from vertical. Thus,
a small applied force leads to a large vertical deflection causing the pendulum to topple
over, despite any retarding forces due to friction.
    The system in Figure 1.46(a) is an example of a stable system, while that in Fig-
ure 1.46(b) is unstable. Models for chain reactions or for population growth with unlim-
ited food supplies and no predators are examples of unstable systems, since the system
response grows without bound in response to small inputs. Another example of an unsta-
ble system is the model for a bank account balance in eq. (1.86), since if an initial deposit
is made (i.e., x[O] = a positive amount) and there are no subsequent withdrawals, then
that deposit will grow each month without bound, because of the compounding effect of
interest payments.





                                                                             x(t)

                                                      (a)



                                                                             x(t)




                                                   Figure 1 .46    (a) A stable pendulum;
                                                    (b)                         (b) an unstable inverted pendulum.

--- PAGE 49 ---

Sec. 1.6     Basic System Properties                                           49

     There are also numerous examples of stable systems. Stability of physical systems
generally results from the presence of mechanisms that dissipate energy. For example,
assuming positive component values in the simple RC circuit of Example 1.8, the resistor
dissipates energy and this circuit is a stable system. The system in Example 1.9 is also
stable because of the dissipation of energy through friction.
    The preceding examples provide us with an intuitive understanding of the concept
of stability. More formally, if the input to a stable system is bounded (i.e., if its magnitude
does not grow without bound), then the output must also be bounded and therefore cannot
diverge. This is the definition of stability that we will use throughout this book. For exam-
ple, consider applying a constant force j(t) = F to the automobile in Figure 1.2, with the
vehicle initially at rest. In this case the velocity of the car will increase, but not without
bound, since the retarding frictional force also increases with velocity. In fact, the velocity
will continue to increase until the frictional force exactly balances the applied force; so,
from eq. (1.84), we see that this terminal velocity value V must satisfy

                              _eV=_!__F                               (1.107)
                       m   m'

i.e.,
                         v =   !'__,                                 (1.108)
                                       p

    As another example, consider the discrete-time system defined by eq. (1.1 04 ), and
suppose that the input x[n] is bounded in magnit~de by some number, say, B, for all values
of n. Then the largest possible magnitude for y[n] is also B, because y[n] is the average
of a finite set of values of the input. Therefore, y[n] is bounded and the system is stable.
On the other hand, consider the accumulator described by eq. (1.92). Unlike the system
in eq. ( 1.104 ), this system sums all of the past values of the input rather than just a finite
set of values, and the system is unstable, since the sum can grow continually even if x[n]
is bounded. For example, if the input to the accumulator is a unit step u[n], the output
will be

                                                                                                11
                            y[n]   :Z u[k] = (n + 1)u[n].
                                                 k =-'X

That is, y[O] =  1, y[l] = 2, y[2] = 3, and so on, and y[n] grows without bound.

    Example 1 . 1 3
             If we suspect that a system is unstable, then a useful strategy to verify this is to look for
           a specific bounded input that leads to an unbounded output. Finding one such example
           enables us to conclude that the given system is unstable. If such an example does not
            exist or is difficult to find, we must check for stability by using a method that does not
             utilize specific examples of input signals. To illustrate this approach, let us check the
             stability of two systems,

                                                    sl: y(t) =  tx(t)                            (1.109)

--- PAGE 50 ---

50                                                                   Signals and Systems     Chap. 1

         and

                                                                                           (1.110)

           In seeking a specific counterexample in order to disprove stability, we might try simple
         bounded inputs such as a constant or a unit step. For system S1 in eq. (1.109), a constant
           input x(t) = 1 yields y(t) =  t, which is unbounded, since no matter what finite con-
            stant we pick, iy(t)l will exceed that constant for some t. We conclude that system 5 1 is
           unstable.
               For system S2, which happens to be stable, we would be unable to find a bounded
           input that results in an unbounded output. So we proceed to verify that all bounded inputs
            result in bounded outputs. Specifically, let B be an arbitrary positive number, and let x(t)
          be an arbitrary signal bounded by B; that is, we are making no assumption about x(t),
          except that
                                                                 ix(t)i < B,                                (1.111)
           or
                            -B < x(t) < B,                            (1.112)
            for all  t. Using the definition of S2 in eq. (1.110), we then see that if x(t) satisfies
            eq. (1.111), then y(t) must satisfy

                                                                                           (1.113)

       We conclude that if any input to S2 is bounded by an arbitrary positive number B, the
          corresponding output is guaranteed to be bounded by e8 . Thus, S2 is stable.

    The system properties and concepts that we have introduced so far in this section
are of great importance, and we will examine some of these in more detail later in the
book. There remain, however, two additional properties-time invariance and linearity-
that play a particularly central role in the subsequent chapters of the book, and in the
remainder of this section we introduce and provide initial discussions of these two very
important concepts.

1.6.5 Time lnvariance
Conceptually, a system is time invariant if the behavior and characteristics of the system
are fixed over time. For example, the RC circuit of Figure 1.1  is time invariant if the
resistance and capacitance values R and C are constant over time: We would expect to
get the same results from an experiment with this circuit today as we would if we ran the
identical experiment tomorrow. On the other hand, if the values of R and C are changed
or fluctuate over time, then we would expect the results of our experiment to depend on
the time at which we run  it. Similarly, if the frictional coefficient b and mass m of the
automobile in Figure 1.2 are constant, we would expect the vehicle to respond identically
independently of when we drive it. On the other hand, if we load the auto's trunk with
heavy suitcases one day, thus increasing m, we would expect the car to behave differently
than at other times when it is not so heavily loaded.
    The property of time in variance can be described very simply in terms of the signals
and systems language that we have introduced. Specifically, a system is time invariant if

--- PAGE 51 ---

Sec. 1.6     Basic System Properties                                                   51

a time shift in the input signal results in an identical time shift in the output signal. That
is, if y[n] is the output of a discrete-time, time-invariant system when x[n] is the input,
then y [n- n0 ] is the output when x [n- n0 ] is applied. In continuous time with y(t) the
output corresponding to the input x(t), a time-invariant system will have y (t- to) as the
output when x (t -  to) is the input.
     To see how to determine whether a system is time invariant or not, and to gain some
insight into this property, consider the following examples:

    Example 1 . 1 4
          Consider the continuous-time system defined by
                                                    y(t) =  sin [ x(t)].                            (1.114)

         To check that this system is time invariant, we must determine whether the time-
           invariance property holds for any input and any time shift t0 • Thus, let x 1(t) be an
            arbitrary input to this system, and let

                                                                                           (1.115)

          be the corresponding output. Then consider a second input obtained by shifting x 1 (t) in
           time:

                                                  x2(t) = x, (t -  to).                           (1.116)

         The output corresponding to this input is

                                        Y2(t) = sin [ x2(t)] = sin [ x, (t -  to)].                  (1.117)

            Similarly, from eq. (1.115),
                                  y,(t- to) = sin[ Xt (t- to)].                      (1.118)
         Comparing eqs. (1.117) and (1.118), we see that y2(t) = y 1 (t- to), and therefore, this
          system is time invariant.

    Example 1 . 1 5
        As a second example, consider the discrete-time system

                                                y[n] =  nx[n].                             (1.119)

          This is a time-varying system, a fact that can be verified using the same formal procedure
           as that used in the preceding example (see Problem 1.28). However, when a system is
           suspected of being time varying, an approach to showing this that is often very useful
              is to seek a counterexample-i.e., to use our intuition to find an input signal for which
           the condition of time invariance is violated. In particular, the system in this example
           represents a system with a time-varying gain. For example, if we know that the current
           input value is  1, we cannot determine the current output value without knowing the
           current time.
                Consequently, consider the input signal x 1 [n] = 8[n], which yields an output
           y 1 [n] that is identically 0 (since n8[n] = 0). However, the input x2[n] = 8[n -1] yields
           the output y2[n] = n8[n- 1] = 8[n- 1]. Thus, while x2[n] is a shifted version of x 1 [n],
           Y2[n] is not a shifted version of y 1 [n].

--- PAGE 52 ---

52                                                                   Signals and Systems     Chap. 1

     While the system in the preceding example has a time-varying gain and as a result
is a time-varying system, the system in eq. (1.97) has a constant gain and, in fact, is time
invariant. Other examples of time-invariant systems are given by eqs. (1.91)-(1.104). The
following example illustrates a time-varying system.

    Example 1 . 1 6
          Consider the system

                                                       y(t) =  x(2t).                              (1.120)

          This system represents a time scaling. That is, y(t) is a time-compressed (by a factor of
           2) version of x(t). Intuitively, then, any time shift in the input will also be compressed
         by a factor of 2, and it is for this reason that the system is not time invariant. To demon-
             strate this by counterexample, consider the input x 1(t) shown in Figure 1.47(a) and the
            resulting output y 1 (t) depicted in Figure 1.47(b). If we then shift the input by 2-i.e.,
           consider x 2(t) = x 1 (t- 2), as shown in Figure 1.47(c)-we obtain the resulting output


                                                       x1(t)
                                       ~(t)



                         -2       2                    -1
                                                      (a)                                          (b)

                                                       x2(t) = x1(t-2)                            Y2(t)




                                   0        4                    0   2
                                                     (c)                                          (d)





                                                                             (e)

              Figure 1.47    (a) The input x1(t) to the system in Example 1.16; (b) the
                 output Y1 (t) corresponding to x1 (t); (c) the shifted input x2(t) =  x1 (t- 2);
                    (d) the output Y2(t) corresponding to x2(t); (e) the shifted signal Y1 (t -  2).
                Note that Y2 ( t)  =1= Y1 ( t -  2), showing that the system  is not time invariant.

--- PAGE 53 ---

Sec. 1.6     Basic System Properties                                            53

             y2(t) = x 2(2t) shown in Figure 1.47(d). Comparing Figures 1.47(d) and (e), we see that
            yz(t)  =I= y 1 (t- 2), so that the system is not time invariant. (In fact, y2(t) = y 1 (t- 1), so
            that the output time shift is only half as big as it should be for time in variance, due to the
          time compression imparted by the system.)

1 .6.6 Linearity
A linear system, in continuous time or discrete time, is a system that possesses the impor-
tant property of superposition: If an input consists of the weighted sum of several signals,
then the output is the superposition-that is, the weighted sum-of the responses of the
system to each of those signals. More precisely, let y 1 (t) be the response of a continuous-
time system to an input x 1 (t), and let y2(t) be the output corresponding to the input x 2(t).
Then the system is linear if:

       1. The response to x 1(t) + x2(t) is Yl (t) + Y2(t).
       2. The response to ax1(t) is ay1(t), where a is any complex constant.

The first of these two properties is known as the additivity property; the second is known
as the scaling or homogeneity property. Although we have written this description using
continuous-time signals, the same definition holds in discrete time. The systems specified
by eqs. (1.91)-(1.100), (1.102)-(1.104), and (1.119) are linear, while those defined by
eqs. (1.101) and (1.114) are nonlinear. Note that a system can be linear without being
time invariant, as in eq. (1.119), and it can be time invariant without being linear, as in
eqs. (1.1 0 1) and (1.114).
     The two properties defining a linear system can be combined into a single statement:
                 continuous time: ax1(t) + bx2(t) ~ ay1(t) + by2(t),           (1.121)
                   discrete time: ax1[n] + bx2[n] ~ ay1 [n] + by2[n].                ( 1.122)
Here, a and b are any complex constants. Furthermore, it is straightforward to show from
the definition of linearity that if xdn], k =  1, 2, 3, ... , are a set of inputs to a discrete-
time linear system with corresponding outputs ydn], k =  1, 2, 3, ... , then the response to
a linear combination of these inputs given by
               x[n] = ~ akxdn] = a1 XJ [n] + a2x2[n] + a3x3[n] + . . .        (1.123)
                                 k
is
               y[n] = ~ akyk[n] = G(VJ [n] + a2y2[n] + a3y3[n] + ....           ( 1.124)
                               k
This very important fact is known as the superposition property, which holds for linear
systems in both continuous and discrete time.
   A direct consequence of the superposition property is that, for linear systems, an
input which is zero for all time results in an output which is zero for all time. For example,
if x[n] ~ y[n], then the homogeneity property tells us that
                        0 = 0 · x[n] ~ 0 · y[n] =  0.                      (1.125)

--- PAGE 54 ---

54                                                                  Signals and Systems     Chap. 1

      In the following examples we illustrate how the linearity of a given system can be
checked by directly applying the definition of linearity.

    Example 1 . 1 7
          Consider a systemS whose input x(t) and output y(t) are related by

                                                        y(t) =  tx(t)
         To determine whether or not Sis linear, we consider two arbitrary inputs x 1(t) and x2(t).
                                                Xt (t) ~ Yt (t) =  tXt (t)
                                                x2(t) ~ Yz(t) =  tx2(t)
          Let x3(t) be a linear combination of x 1(t) and x2(t). That is,
                                                X3(t) = ax1 (t) + bx2(t)
         where a and b are arbitrary scalars. If x3(t) is the input to S, then the corresponding
           output may be expressed as
                                               y3(t) =  tx:,(t)
                                                =  t(ax1 (t) + bx2(t))
                                 = atx1 (t) + btx2(t)
                                                =  ay1 (t) + byz(t)
       We conclude that the system S is linear.

    Example 1 . 1 8
          Let us apply the linearity-checking procedure of the previous example to another system
       S whose input x(t) and output y(t) are related by
                                                       y(t) =  x 2(t)
          Defining x 1(t), xz(t), and x3(t) as in the previous example, we have
                                               Xt (t) ~ Yt (t) = xi(t)
                                                 Xz(t) ~ Yz(t) =  x~(t)
          and
                                 X3(t) ~ y3(t) = x~(t)
                               = (ax1 (t) + bx2(t)) 2
                               = a2 xi(t) + b2 x~(t) + 2abxt (t)xz(t)
                               = a2y 1(t) + b2yz(t) + 2abxt (t)xz(t)
            Clearly, we can specify x 1(t), xz(t), a, and b such that y3(t) is not the same as ay1(t) +
          byz(t).Forexample,ifx 1(t) =  l,x2(t) = O,a = 2,andb = O,theny3(t) = (2x 1(t))2 =
             4, but 2y 1(t) = 2(x1 (t))2 = 2. We conclude that the systemS is not linear.

    Example 1 . 1 9
           In checking the linearity of a system, it is important to remember that the system must
            satisfy both the additivity and homogeneity properties and that the signals, as well as
          any scaling constants, are allowed to be complex. To emphasize the importance of these

--- PAGE 55 ---

Sec. 1.6     Basic System Properties                                            55

            points, consider the system specified by
                                              y[n] =  (Re{x[n]}.                           (1.126)
        As shown in Problem 1.29, this system is additive; however, it does not satisfy the ho-
          mogeneity property, as we now demonstrate. Let
                                          x 1 [n] = r[n] + js[n]                         (1.127)
          be an arbitrary complex input with real and imaginary parts r[n] and s[n], respectively,
           so that the corresponding output is
                                                      y, [n] =  r[n].                             (1.128)

         Now, consider scaling x 1 [n] by a complex number, for example, a =  j; i.e., consider
           the input
                                     x2[n] = jx 1 [n] = j(r[n] + js[n])                                                                                          (1.129)
                               = -s[n] + jr[n].
         The output corresponding to x2 [n] is
                                        Y2[n] = CRe{x2[n]} = -s[n],                     (1.130)
         which is not equal to the scaled version of y 1 [n],
                                     ay 1 [n] = jr[n].                            (1.131)
       We conclude that the system violates the homogeneity property and hence is not linear.

    Example 1 .20

          Consider the system
                                              y[n] = 2x[n] + 3.                           (1.132)
          This system is not linear, as can be verified in several ways. For example, the system
            violates the additivity property: If x 1 [n] = 2 and x2[n] =  3, then
                                        x, [n] ~ y, [n] =  2x, [n] + 3 =  7,                   (1.133)
                                     x2[n] ~ Y2[n] = 2x2[n] + 3 = 9.                   (1.134)
         However, the response to x3[n] =  x 1[n] + x2[n] is
                                     y3[n] = 2[x,[n] + x2[n]] + 3 =  13,                  (1.135)
         which does not equal y 1 [n] + y2[n] = 16. Alternatively, since y[n] = 3 if x[n] = 0, we
           see that the system violates the "zero-in/zero-out" property of linear systems given in
            eq. (1.125).
                       It may seem surprising that the system in the above example is nonlinear, since
            eq. (1.132) is a linear equation. On the other hand, as depicted in Figure 1.48, the output
           of this system can be represented as the sum of the output of a linear system and another
            signal equal to the zero-input response of the system. For the system in eq. (1.132), the
            linear system is

                                               x[n] ~ 2x[n],
          and the zero-input response is

                                                 Yo[n] =  3.

--- PAGE 56 ---

              56                                                                  Signals and Systems     Chap. 1


                                                                                      Yo (t)



                                                                 Linear
                                                           ~-----~~ y(t)                              x(t)--~1 system  1---......~ +

                              Figure 1.48   Structure of an incrementally linear system. Here, y0[n]  is the
                                     zero-input response of the system.


                               There are, in fact, large classes of systems in both continuous and discrete time that
                          can be represented as in Figure 1.48-i.e., for which the overall system output consists
                            of the superposition of the response of a linear system with a zero-input response. As
                       shown in Problem 1.47, such systems correspond to the class of incrementally linear
                            systems-i.e., systems in continuous or discrete time that respond linearly to changes in
                              the input. In other words, the difference between the responses to any two inputs to an
                            incrementally linear system is a linear (i.e., additive and homogeneous) function of the
                              difference between the two inputs. For example, if x 1 [n] and x2[n] are two inputs to the
                          system specified by eq. (1.132), and if y 1 [n] and y2[n] are the corresponding outputs,
                            then

                                          y, [n] -  Y2[n] = 2x, [n] + 3 - {2x2[n] + 3} = 2 { x, [n] -  x2[n]} .      (1.136)



1.7 SUMMARY

                 In this chapter, we have developed a number of basic concepts related to continuous-time
              and discrete-time signals and systems. We have presented both an intuitive picture of what
                 signals and systems are through several examples and a mathematical representation for
                 signals and systems that we will use throughout the book. Specifically, we introduced
                graphical and mathematical representations of signals and used these representations in
               performing transformations of the independent variable. We also defined and examined
                 several basic signals, both in continuous time and in discrete time. These included com-
                plex exponential signals, sinusoidal signals, and unit impulse and step functions. In ad-
                   dition, we investigated the concept of periodicity for continuous-time and discrete-time
                  signals.
                       In developing some of the elementary ideas related to systems, we introduced block
               diagrams to facilitate our discussions concerning the interconnection of systems, and we
                defined a number of important properties of systems, including causality, stability, time
                 invariance, and linearity.
                  The primary focus in most of this book will be on the class of linear, time-invariant
                (LTI) systems, both in continuous time and in discrete time. These systems play a par-
                  ticularly important role in system analysis and design, in part due to the fact that many
               systems encountered in nature can be successfully modeled as linear and time invariant.
                Furthermore, as we shall see in the following chapters, the properties of linearity and time
                  in variance allow us to analyze in detail the behavior of LTI systems.

--- PAGE 57 ---

Chap. 1  Problems                                                          57




     Basic problems emphasize the mechanics of using concepts and methods in a man-
ner similar to that illustrated in the examples that are solved in the text.
    Advanced problems explore and elaborate upon the foundations and practical im-
plications of the textual material.
     The first section of problems belongs to the basic category, and the answers are pro-
vided in the back of the book. The next two sections contain problems belonging to the
basic and advanced categories, respectively. A final section, Mathematical Review, pro-
vides practice problems on the fundamental ideas of complex arithmetic and algebra.

BASIC PROBLEMS WITH ANSWERS
  1.1. Express each of the following complex numbers in Cartesian form (x + jy): ~ei1T,
      le-                }1r                      e.i1T12                  e- }1r!2                                        e.i51T!2      2                        ,                                    ,                                                   ,                       ,yL                                                   - f2e.i1T14 ,-JLf2e.i91TI4 ,yLf2e- j91TI4 ,yLf2e- )1TI4 .           ~
  1.2. Express each of the following complex numbers in polar form (re.i8, with -  'TT <
             () ~  'TT): 5, -2, -3j, ~ -   j J!' 1 + j, (1- j)2, j(l- j), (1 + j)/(1- j), ( h + Jfi)l
     (l+j}3).              -        -
  1.3. Determine the values of P x and Ex for each of the following signals:
       (a) x 1(t) = e- 21 u(t)      (b)  x2(t) =  e.i(:21+1T/4J         (c)  x3(t) = cos(t)
       (d) x1[n] = (~)''u[n]      (e) x2[n] =  e.i(1TI2n+1TI'd)       (f) x3[n] = cos(*n)
  1.4. Let x[n] be a signal with x[n] = 0 for n < -2 and n > 4. For each signal given
      below, determine the values of n for which it is guaranteed to be zero.
       (a) x[n -  3]       (b) x[n + 4]        (c) x[- n]
       (d)  x[ -n + 2]      (e)  x[ -n- 2]
  1.5. Let x(t) be a signal with x(t) = 0 fort < 3. For each signal given below, determine
       the values oft for which it is guaranteed to be zero.
       (a)  x(l  -  t)     (b) x(l  -  t) + x(2- t)     (c)  x(l  -  t)x(2 -  t)
       (d)  x(3t)         (e)  x(t/3)
  1.6. Determine whether or not each of the following signals is periodic:
       (a) x 1(t) =  2e.i(1+1TI4lu(t)                              (b) x2[n] = u[n] + u[ -n]
        (c)  x3[n] = ~7=-Y~{8[n- 4k]- 8[n- 1- 4k]}
  1.7. For each signal given below, determine all the values of the independent variable at
     which the even part of the signal is guaranteed to be zero.
       (a) x 1 [n] = u[n] -  u[n -  4]     (b)  x2(t) =  sin( ~t)
        (c)  x3[n] = (~)''u[n- 3]        (d)  x4(t) = e- 51~(t + 2)
  1.8. Express the real part of each of the following signals in the form Ae-ar cos(wt + cp),
     where A, a, w, and cp are real numbers with A> 0 and -7r < cp ~  'TT:
       (a) x 1(t) = -2                 (b)  x2(t) = heJ1TI4 cos(3t + 27T)
                                1 sin(3t + 'TT)     (d)  x4(t) = je(-2-r JIOO)t        (c)  x3(t) = e-
  1.9. Determine whether or not each of the following signals is periodic. If a signal  is
       periodic, specify its fundamental period.
                       jej\Ot             (b)  x2(t) = e(-l+iJr           (c)  x3(n) = ej71rn       (a) x 1(t) =       (d)  x4[n] = 3ej31T!n+l/2)/5      (e)  x5[n] = 3ei3/5(n+l/2)

--- PAGE 58 ---

58                                                                  Signals and Systems     Chap. 1

1.10. Determine the fundamental period of the signal x(t) = 2cos(10t + 1)- sin(4t -1).
1.11. Determine the fundamental period of the signal x[n] = 1 + ej4mzn  -  ej2mz!S.
1.12. Consider the discrete-time signal
                                 x[n] = 1 - .L o[n -  1 -  k].
                                          k=3
     Determine the values of the integers M and n0 so that x[n] may be expressed as
                                     x[n] = u[Mn- no].
1.13. Consider the continuous-time signal
                                      x(t) = o(t + 2) -  o(t -  2).
      Calculate the value of Eoo for the signal

                                           y(t) =     X(T)dT.                          tx
1.14. Consider a periodic signal
                                          0 ~  t ~ 1
                          l<t<2

      with period T = 2. The derivative of this signal is related to the "impulse train"
                                        g(t) = .L o(t- 2k)
                                    k=-x
      with period T = 2. It can be shown that
                             dx(t)
                                       ----;[( = A I g(t -  tJ) + A2g(t -  t2)·

     Determine the values of A 1, t1, A2, and t2.
1.15. Consider a systemS with input x[ n] and output y[ n]. This system is obtained through
      a series interconnection of a system S1 followed by a system S2. The input-output
      relationships for S 1 and S2 are
                                       YI [n] = 2xi [n] + 4xi [n -  1],
                                              1
                                   Y2[n] = x2[n- 2] + 2x2[n- 3],

     where x 1 [n] and x2[n] denote input signals.
       (a) Determine the input-output relationship for systemS.
       (b) Does the input-output relationship of systemS change if the order in which S1
         and S2 are connected in series is reversed (i.e., if S2 follows SJ)?
1.16. Consider a discrete-time system with input x[n] and output y[n]. The input-output
      relationship for this system is
                                     y[n] = x[n]x[n -  2].

--- PAGE 59 ---

Chap. 1  Problems                                                        59

       (a)  Is the system memoryless?
       (b) Determine the output of the system when the input is A8[n], where A is any
           real or complex number.
       (c)  Is the system invertible?
1.17. Consider a continuous-time system with input x(t) and output y(t) related by
                                             y(t) = x(sin(t)).
       (a)  Is this system causal?
       (b)  Is this system linear?
1.18. Consider a discrete-time system with input x[n] and output y[n] related by
                                                 n+n0
                                      y[n] = L    x[k],
                                            k= n-no
     where n0 is a finite positive integer.
       (a)  Is this system linear?
       (a)  Is this system time-invariant?
        (c) If x[n] is known to be bounded by a finite integer B (i.e., jx[n]j < B for all n), it
         can be shown that y[n] is bounded by a finite number C. We conclude that the
          given system is stable. Express C in terms of Band n0 .
1.19. For each of the following input-output relationships, determine whether the corre-
      sponding system is linear, time invariant or both.
       (a)  y(t) = t2 x(t- 1)                (b) y[n] = x 2[n- 2]
        (c) y[n] = x[n + 1] - x[n- 1]     (d) y[n] = Od{x(t)}
1.20. A continuous-time linear systemS with input x(t) and output y(t) yields the follow-
      ing input-output pairs:

                                    x(t) =  ei2t ~  y(t) =  ei3t,
                                    x(t) = e-i 2t ~  y(t) = e-131.
       (a) If x 1(t) = cos(2t), determine the corresponding output y 1 (t) for systemS.
       (b) If x2(t) = cos(2(t -  ~)), determine the corresponding output y2(t) for sys-
         temS.

BASIC PROBLEMS
1.21. A continuous-time signal x(t) is shown in Figure P1.21. Sketch and label carefully
      each of the following signals:
       (a) x(t- 1)     (b) x(2- t)                 (c) x(2t + 1)
       (d) x(4- ~)     (e)  [x(t) + x(-t)]u(t)      (f)  x(t)[8(t + ~) - 8(t- ~)]
1.22. A discrete-time signal is shown in Figure P1.22. Sketch and label carefully each of
      the following signals:
       (a) x[n- 4]                 (b) x[3 -  n]          (c) x[3n]
       (d) x[3n + 1]                  (e) x[n]u[3 -  n]       (f) x[n - 2]8[n -  2]
                                                              11 x[n]     (h) x[(n -  1)2]       (g)  ~x[n] + ~( -1)

--- PAGE 60 ---

      60                                                                   Signals and Systems     Chap. 1



                                      2,....____ _





-2                      0                   2


                      -1                                                                            .l 1                          .l
                                                                                                2                         2


                                                                    -1   0   1   2   3   4   5      n


                                                       -1

               Figure P1.21                                      Figure P1.22

        1.23. Determine and sketch the even and odd parts of the signals depicted in Figure Pl.23.
             Label your sketches carefully.





                                        1     2
                                                 (a)
                                                   x(t)
                -2~-1          1
                                               (b)




           The line                           --..__The line
                    x(t) =   - 2t for t < 0                           x(t) =  t for t > 0

                        -1
                                                 (c)                               Figure P1.23

        1.24. Determine and sketch the even and odd parts of the signals depicted in Figure P 1.24.
            Label your sketches carefully.

--- PAGE 61 ---

Chap. 1  Problems                                                              61




                            1 23                 n
    ···llllllt                                       (a)

                        3

                      2




                                               n
                                     (b)


                  2




                                                 n


                                                    Figure P 1 .24

1.25. Determine whether or not each of the following continuous-time signals is periodic.
      If the signal is periodic, determine its fundamental period.
       (a)  x(t) = 3cos(4t+ })       (b)  x(t) = ei(7Tf-l)
       (c)  x(t) = [cos(2t- })f      (d)  x(t) = 8v{cos(47Tt)u(t)}
        (e)  x(t) = 8v{sin(47Tt)u(t)}      (f)  x(t) = L  e-<2t-n) u(2t - n)
                                              n= -oo
1.26. Determine whether or not each of the following discrete-time signals is periodic. If
      the signal is periodic, determine its fundamental period.
       (a) x[n] = sin( 6; n + 1)        (b) x[n] = cos(i- 7T)     (c) x[n] = cos(in2)
       (d) x[n] = cos(~n)cos(*n)     (e) x[n] = 2cos(*n) +sin( in)- 2cos(~n + ~)
1.27. In this chapter, we introduced a number of general properties of systems. In partic-
       ular, a system may or may not be
       (1) Memoryless
       (2) Time invariant
       (3) Linear
       (4) Causal
       (S) Stable
      Determine which of these properties hold and which do not hold for each of the
      following continuous-time systems. Justify your answers. In each example, y(t) de-
      notes the system output and x(t) is the system input.

--- PAGE 62 ---

62                                                                  Signals and Systems     Chap. 1

       (a)  y(t) = x(t -  2) + x(2 -  t)               (b) y(t) = [cos(3t)]x(t)
                                                t<O        (c)  y(t) = J   x( T)dT               !:                                (d) y(t) = { ~(t) + x(t -  2),    t  2:: 0
                 0                    x(t) < 0
        (e)  y(t) = { x'(t) + x(t -  2),   x(t)  2:: 0       (f) y(t) = x(t/3)
       (g)  y(t) =  d~~~t)
1.28. Determine which of the properties listed in Problem 1.27 hold and which do not
      hold for each of the following discrete-time systems. Justify your answers. In each
      example, y[n] denotes the system output and x[n] is the system input.
       (a) y[n] = x[- n]                (b) y[n] = x[n -  2] - 2x[n -  8]
        (c)  y[n] = nx[n]                 (d) y[n] = Sv{x[n -  1]}
                       x[n],      n  2:: 1                  {  x[n],  n  2:: 1
        (e)  y[n] =    0,         n = 0   (f)  y[n] =    0,     n = 0
                          {                   x[n + 1],  n    ::::: -1                x[n],  n    ::::: -1
       (g) y[n] = x[4n + 1]
1.29.  (a) Show that the discrete-time system whose input x[n] and output y[n] are related
         by y[n] = ffi-e{x[n]} is additive. Does this system remain additive if its input-
          output relationship is changed to y[n] = ffi-e{ei7Tnl4x[n]}? (Do not assume that
           x[n] is real in this problem.)
       (b) In the text, we discussed the fact that the property of linearity for a system is
          equivalent to the system possessing both the additivity property and homogene-
             ity property. Determine whether each of the systems defined below is additive
          and/or homogeneous. Justify your answers by providing a proof for each prop-
           erty if it holds or a counterexample if it does not.
                                                              x[n]x[n-2]            [      1]    .....1- 0
               (i)  y(t) =  _l__[dx(t)]2      (ii) y[n] =      x[n-1]       '   X n-         '
                                   x(t)   dt                                         {  0,          x[n -  1] = 0
1.30. Determine if each of the following systems is invertible. If it is, construct the inverse
      system. If it is not, find two input signals to the system that have the same output.
        (a)  y(t) = x(t- 4)                        (b)  y(t) = cos[x(t)]
        (C)  y[n] = nx[n]                         (d)  y(t) = cry: X( T)dT
                    x[n -  1],    n  2:: 1
         (e) y[n] =    0,           n = 0           (f)  y[n] = x[n]x[n -  1]
                           {                        x[n],        n   ::::: -1
                                                                       e-(t-T) X( T)dT        (g) y[n] = x[l -  n]                      (h)  y(t) = cr£
          (i) y[n] = L~= -r£(4yz-k x[k]                (j)  y(t) =  d~;t)
       (k)   [n] = { x[n + 1],    n  2:: 0           (I)  y(t) = x(2t)           y          x[n],        n    ::::: -1
                                                                  n even     (m) y[n] = x[2n]                         (n) y[n] = { x[n/2],                                                                                  0,        nodd
1.31. In this problem, we illustrate one of the most important consequences of the prop-
       erties of linearity and time invariance. Specifically, once we know the response
      of a linear system or a linear time-invariant (LTI) system to a single input or the
      responses to several inputs, we can directly compute the responses to many other

--- PAGE 63 ---

Chap. 1  Problems                                                        63

      input signals. Much of the remainder of this book deals with a thorough exploitation
      of this fact in order to develop results and techniques for analyzing and synthesizing
     LTI systems.
        (a) Consider an LTI system whose response to the signal x 1(t) in Figure P1.31(a) is
           the signal y 1 ( t) illustrated in Figure P 1.31 (b). Determine and sketch carefully
           the response of the system to the input x2(t) depicted in Figure P1.31(c).
       (b) Determine and sketch the response of the system considered in part (a) to the
           input x 3(t) shown in Figure P1.31(d).





   0        2                                 0   1   2
               (a)                                                        (b)





               I                I
            2  3   4)     t              -1   0   1   2
-1  -
               (c)                                                       (d)              Figure P 1. 31

ADVANCED PROBLEMS
1.32. Let x(t) be a continuous-time signal, and let
                                   Yt (t) = x(2t) and Y2(t) = x(t/2).
     The signal y 1 (t) represents a speeded up version of x(t) in the sense that the duration
      of the signal is cut in half. Similarly, y2(t) represents a slowed down version of
       x(t) in the sense that the duration of the signal is doubled. Consider the following
       statements:
        (1) If x(t) is periodic, then y 1 (t) is periodic.
        (2)  If y 1(t) is periodic, then x(t) is periodic.
        (3) If x(t) is periodic, then y2(t) is periodic.
        (4)  If y2(t) is periodic, then x(t) is periodic.
      For each of these statements, determine whether it is true, and if so, determine the
       relationship between the fundamental periods of the two signals considered in the
       statement. If the statement is not true, produce a counterexample to it.
1.33. Let x[ n] be a discrete-time signal, and let
                                                     x[n/2]     n even                     y 1 [n] = x[2n] and Y2[n] =    O,           '                                                                             {           n odd   ·

--- PAGE 64 ---

64                                                                   Signals and Systems     Chap. 1

     The signals y 1 [n] and y2[n] respectively represent in some sense the speeded up and
     slowed down versions of x[n]. However, it should be noted that the discrete-time
      notions of speeded up and slowed down have subtle differences with respect to their
      continuous-time counterparts. Consider the following statements:
        (1) If x[n] is periodic, then y 1 [n] is periodic.
        (2) If y 1 [n] is periodic, then x[n] is periodic.
        (3) If x[n] is periodic, then y2[n] is periodic.
        (4) If y2[n] is periodic, then x[n] is periodic.
      For each of these statements, determine whether it is true, and if so, determine the
      relationship between the fundamental periods of the two signals considered in the
      statement. If the statement is not true, produce a counterexample to it.
1.34. In this problem, we explore several of the properties of even and odd signals.
        (a) Show that if x[n] is an odd signal, then
                                      +x
             ~ x[n] = 0.
                                  n=-x
       (b) Show that if x 1 [n] is an odd signal and x2[n] is an even signal, then x 1 [n]x2[n]
               is an odd signal.
        (c) Let x[n] be an arbitrary signal with even and odd parts denoted by
                                         Xe[n] = 8v{x[n]}
          and
                                           X0 [n] = 0d{x[n]}.
        Show that
                           +x                +oo                +oo
         ~  x2[n] = ~ x;[n] + ~  x~[n].
                        n=-x        n=-x        n= -oo
       (d) Although parts (a)-(c) have been stated in terms of discrete-time signals, the
          analogous properties are also valid in continuous time. To demonstrate this,
         show that



         where Xe(t) and X0 (t) are, respectively, the even and odd parts of x(t).
1.35. Consider the periodic discrete-time exponential time signal
                                      x[n] =  eim(27TIN)n.
     Show that the fundamental period of this signal is
                               No = Nlgcd(m, N),
     where gcd(m, N) is the greatest common divisor of m and N-that is, the largest
      integer that divides both m and Nan integral number of times. For example,
                         gcd(2, 3) =  1, gcd(2, 4) =  2, gcd(8, 12) = 4.
     Note that No = N if m and N have no factors in common.

--- PAGE 65 ---

Chap. 1  Problems                                                        65

1.36. Let x(t) be the continuous-time complex exponential signal
                                               x(t) =  e.iwot
      with fundamental frequency w0 and fundamental period To = 27T!w0 . Consider the
      discrete-time signal obtained by taking equally spaced samples of x(t)-that is,
                                   x[n] = x(nT) =  e.iwonT.
        (a) Show that x[n] is periodic if and only if TIT0 is a rational number-that is, if
          and only if some multiple of the sampling interval exactly equals a multiple of
           the period of x(t).
       (b) Suppose that x[n] is periodic-that is, that
                              T    p                                                                         (P1.36-1)
                                         To     q'
         where p and q are integers. What are the fundamental period and fundamental
          frequency of x[n]? Express the fundamental frequency as a fraction of w0T.
        (c) Again assuming that T!T0 satisfies eq. (Pl.36-1), determine precisely how
        many periods of x(t) are needed to obtain the samples that form a single period
           of x[n].
1.37. An important concept in many communications applications is the correlation be-
     tween two signals. In the problems at the end of Chapter 2, we will have more to
      say about this topic and will provide some indication of how it is used in practice.
      For now, we content ourselves with a brief introduction to correlation functions and
     some of their properties.
           Let x(t) and y(t) be two signals; then the correlation function is defined as
                                      "'""(!) = r~ x(t + T)y( T)dT.

     The function <f>xxCt) is usually referred to as the autocorrelation function of the signal
        x(t), while </>xy(t) is often called a cross-correlation function.
        (a) What is the relationship between </>xy(t) and </>yx(t)?
       (b) Compute the odd part of <f>xxU).
        (c) Suppose that y(t) = x(t + T). Express </>xy(t) and </>yy(t) in terms of <f>xx(t).
1.38. In this problem, we examine a few of the properties of the unit impulse function.
        (a) Show that
                                           1
                                           8(2t) =  28(t).

           Hint: Examine Dtl(t). (See Figure 1.34.)
       (b) In Section 1.4, we defined the continuous-time unit impulse as the limit of the
            signal Dtl(t). More precisely, we defined several of the properties of 8(t) by
          examining the corresponding properties of Dtl(t). For example, since the signal

                                                ULI(t) =    ih(T)dT                            t%

--- PAGE 66 ---

66                                                                   Signals and Systems     Chap. 1

          converges to the unit step
                                              u(t) = lim Ut,.(f),                   (Pl.38-1)
                                                                                              t. ---->0
        we could interpret B(t) through the equation
                                              u(t) ~ Loc li(T)dT

           or by viewing B(t) as the formal derivative of u(t).
                This type of discussion is important, as we are in effect trying to define
            B(t) through its properties rather than by specifying its value for each t, which
              is not possible. In Chapter 2, we provide a very simple characterization of the
          behavior of the unit impulse that is extremely useful in the study of linear time-
           invariant systems. For the present, however, we concentrate on demonstrating
            that the important concept in using the unit impulse is to understand how it
           behaves. To do this, consider the six signals depicted in Figure P1.38. Show

               rl (t)                                             r~(t)
    ~m                          1!                          t1       t1                                ~D2~
           2   2
                   (a)                                               (b)

                r~ (t)                                          ri  (t)





                   (c)                                              (d)

             r; (t)

            2
        ~





    -~



                   (e)                                                               (f)               Figure P1.38

--- PAGE 67 ---

Chap. 1  Problems                                                        67

            that each "behaves like an impulse" as Ll ~ 0 in that, if we let
                                        u~(t) = L~ ,-it,(r)dr,

           then

                                     lim u~ (t) =  u(t).
                                                             Ll-->0
           In each case, sketch and label carefully the signal u~ (t). Note that
                                   ri (0) = ri (0) = 0 for all Ll.
           Therefore, it is not enough to define or to think of o(t) as being zero fort  =/= 0
          and infinite fort = 0. Rather, it is properties such as eq. (P1.38-1) that define
           the impulse. In Section 2.5 we will define a whole class of signals known as
           singularity functions, which are related to the unit impulse and which are also
           defined in terms of their properties rather than their values.
1.39. The role played by u(t), o(t), and other singularity functions in the study of linear
      time-invariant systems is that of an idealization of a physical phenomenon, and, as
    we will see, the use of these idealizations allow us to obtain an exceedingly impor-
       tant and very simple representation of such systems. In using singularity functions,
     we need, however, to be careful. In particular, we must remember that they are ideal-
       izations, and thus, whenever we perform a calculation using them, we are implicitly
     assuming that this calculation represents an accurate description of the behavior of
      the signals that they are intended to idealize. To illustrate, consider the equation
                                         x(t)o(t) = x(O)o(t).                    (P1.39-l)
      This equation is based on the observation that
                                          x(t)o11(t) =  x(O)o11(t).                   (P1.39-2)
     Taking the limit of this relationship then yields the idealized one given by eq.
      (P1.39-1). However, a more careful examination of our derivation of eq. (P1.39-2)
     shows that that equation really makes sense only if x(t) is continuous at t = 0. If it
        is not, then we will not have x(t) = x(O) for t small.
          To make this point clearer, consider the unit step signal u(t). Recall from eq.
      (1.70) that u(t) = 0 fort < 0 and u(t) = 1 fort > 0, but that its value at t = 0 is
      not defined. [Note, for example, that u11(0) = 0 for all Ll, while ui(O) = 4 (from
     Problem 1.38(b)).] The fact that u(O) is not defined is not particularly bothersome,
      as long as the calculations we perform using u(t) do not rely on a specific choice for
       u(O). For example, if f(t) is a signal that is continuous at t = 0, then the value of
                                               roooo f(u)u(u)da

      does not depend upon a choice for u(O). On the other hand, the fact that u(O) is
      undefined is significant in that it means that certain calculations involving singular-
       ity functions are undefined. Consider trying to define a value for the product u(t)o(t).

--- PAGE 68 ---

68                                                                  Signals and Systems     Chap. 1

     To see that this cannot be defined, show that
                                  lim [u 11(t)o(t)] = 0,
                                      11~o
      but



            In general, we can define the product of two signals without any difficulty,
      as long as the signals do not contain singularities (discontinuities, impulses, or the
      other singularities introduced in Section 2.5) whose locations coincide. When the
      locations do coincide, the product is undefined. As an example, show that the signal

                                                          +oc
                                      g(t) =   -oc U(T)O(t- T)dT                         J
        is identical to u(t); that is, it is 0 fort < 0, it equals 1 fort > 0, and it is undefined
      fort = 0.
1.40.  (a) Show that if a system is either additive or homogeneous, it has the property
            that if the input is identically zero, then the output is also identically zero.
       (b) Determine a system (either in continuous or discrete time) that is neither ad-
            ditive nor homogeneous but which has a zero output if the input is identically
            zero.
        (c) From part (a), can you conclude that if the input to a linear system is zero be-
          tween times t1 and t2 in continuous time or between times n1 and n2 in discrete
           time, then its output must also be zero between these same times? Explain your
           answer.
1.41. Consider a systemS with input x[n] and output y[n] related by
                                 y[n] = x[n]{g[n] + g[n- 1]}.
        (a) If g[n] = 1 for all n, show that Sis time invariant.
       (b) If g[n] = n, show that Sis not time invariant.
        (c) If g[n] = 1 + ( -l)n, show that Sis time invariant.
1.42.  (a)  Is the following statement true or false?

         The series interconnection of two linear time-invariant systems is itself a linear,
           time-invariant system.

            Justify your answer.
       (b)  Is the following statement true or false?

         The series interconnection of two nonlinear systems is itself nonlinear.

            Justify your answer.
        (c) Consider three systems with the following input-output relationships:
                                           y[n] =  { x[n/2],     n even                      System 1:                                                                  0,         n odd    '

--- PAGE 69 ---

  Chap. 1  Problems                                                       69

                                           1          1                    System 2:     y[n] = x[n] +           1] +           2],                                     2x[n-    4x[n-
                    System 3:     y[n] = x[2n].
           Suppose that these systems are connected in series as depicted in Figure P1.42.
           Find the input-output relationship for the overall interconnected system. Is this
           system linear? Is it time invariant?


                                                                                   y[n]
                                                             Figure P1.42
  1.43.  (a) Consider a time-invariant system with input x(t) and output y(t). Show that if
               x(t) is periodic with period T, then so is y(t). Show that the analogous result
              also holds in discrete time.
         (b) Give an example of a time-invariant system and a nonperiodic input signal x(t)
            such that the corresponding output y(t) is periodic.
  1.44.  (a) Show that causality for a continuous-time linear system is equivalent to the
             following statement:
            For any time to and any input x(t) such that x(t) = 0 fort < t0, the correspond-
             ing output y(t) must also be zero fort < t0 .
          The analogous statement can be made for a discrete-time linear system.
         (b) Find a nonlinear system that satisfies the foregoing condition but is not causal.
           (c) Find a nonlinear system that is causal but does not satisfy the condition.
         (d) Show that invertibility for a discrete-time linear system is equivalent to the
             following statement:
          The only input that produces y[n] = 0 for all n is x[n] = 0 for all n.
          The analogous statement is also true for a continuous-time linear system.
           (e) Find a nonlinear system that satisfies the condition of part (d) but is not invert-
                ible.
  1.45. In Problem 1.37, we introduced the concept of correlation functions. It is often im-
        portant in practice to compute the correlation function cf>hx(t), where h(t) is a fixed
       given signal, but where x(t) may be any of a wide variety of signals. In this case,
       what is done is to design a systemS with input x(t) and output cf>hx(t).
          (a) IsS linear? IsS time invariant? IsS causal? Explain your answers.
         (b) Do any of your answers to part (a) change if we take as the output cf>xh(t) rather
             than cf>hx(t)?
  1.46. Consider the feedback system of Figure P1.46. Assume that y[n] = 0 for n < 0.

       +      e [n]               I        'i2
x[n]                                                                                                     ......                                                                                 y[n]   ----t•~~...~~----_-_....._·~-· -y-[n_]_=_e-[n---1]-~~~~~~                                           ---!•~

                                                            Figure P1.46

--- PAGE 70 ---

70                                                                   Signals and Systems     Chap. 1

        (a) Sketch the output when x[n] = 8[n].
       (b) Sketch the output when x[n] = u[n].
1.47.  (a) LetS denote an incrementally linear system, and let x 1 [n] be an arbitrary input
            signal to S with corresponding output y 1 [n]. Consider the system illustrated in
           Figure Pl.47(a). Show that this system is linear and that, in fact, the overall
           input-output relationship between x[n] and y[n] does not depend on the partic-
            ular choice of x 1 [ n].
       (b) Use the result of part (a) to show that Scan be represented in the form shown
            in Figure 1.48.
        (c) Which ofthe following systems are incrementally linear? Justify your answers,
          and if a system is incrementally linear, identify the linear system Land the zero-
           input response y0[n] or y0(t) for the representation of the system as shown in
          Figure 1.48.
                (i)   y[n] = n + x[n] + 2x[n + 4]
                              n/2,                  n even
                (ii)    [  ]                     (n-1 )/2
                                            n odd           Y n =  { (n -  1)/2 + k~-n x[k],

                           x[n]   ·+~          s                                                         )t   y[n]                                  ·I       :cp
                                                                         (a)
                                          x1[n]                                  Y1[n]

                                                                     t


                                                                                                                                                                                )t  y (t)                           X (t)           w (t)        y(t) ~ d~?)          .~     ·I

                                                                      (b)


                               cos (1rn)


                                            v [n]                     z [n]                                                     z [n] = v2 [n]

                                                    +
              x [n]                ~y[n]

                                         w [n]                                w [n] = x2 [n]


                                                                           (c)

                                      Figure P1.47

--- PAGE 71 ---

Chap. 1  Problems                                                                 71

               (.111")   [  ]   { x[n] - x[n -  1] + 3,   if x[O]  2: 0            Y n =   x[n] - x[n- 1] -  3,   if x[O] < 0
             (iv) The system depicted in Figure P1.47(b).
             (v)  The system depicted in Figure P1.47(c).
       (d) Suppose that a particular incrementally linear system has a representation as
            in Figure 1.48, with L denoting the linear system and y0[n] the zero-input re-
           sponse. Show that Sis time invariant if and only if Lis a time-invariant system
         and y0 [ n] is constant.

MATHEMATICAL REVIEW

The complex number z can be expressed in several ways. The Cartesian or rectangular
form for z is
                                     Z =X+ jy,
where  j = J=1 and x andy are real numbers referred to respectively as the real part and
the imaginary part of z. As we indicated earlier, we will often use the notation
                            x = CRe{z}, y = 9m{z}.
The complex number z can also be represented in polar form as
                                   z = rej8 ,
where r > 0 is the magnitude of z and (} is the angle or phase of z. These quantities will
often be written as
                                                   r =  lzi, 8 =  <t:z.
    The relationship between these two representations of complex numbers can be de-
termined either from Euler s relation,
                                    eje =  cos(} + j sin 8,
or by plotting z in the complex plane, as shown in Figure P1.48, in which the coordinate
axes are CRe{z} along the horizontal axis and 9m{z} along the vertical axis. With respect to
this graphical representation, x andy are the Cartesian coordinates of z, and rand (} are its
polar coordinates.


                         !1m


                      y





                                               Figure P1.48

--- PAGE 72 ---

72                                                                  Signals and Systems     Chap. 1

1.48. Let zo be a complex number with polar coordinates (r0, 00 ) and Cartesian coordi-
      nates (x0, y0 ). Determine expressions for the Cartesian coordinates of the following
     complex numbers in terms of x0 and YO· Plot the points zo, Zt, Z2, Z3, Z4, and zs in
      the complex plane when r0 = 2 and 00 =  TTI4 and when r0 = 2 and 00 =  TTI2.
      Indicate on your plots the real and imaginary parts of each point.
        (a)  Zt = roe- J&o          (b)  Z2 =  ro                (c)  Z3 = roef(&o+1T)
       (d)  Z4 = roei(-&o+1T)      (e)  zs =  roe.i(&o+21T)
1.49. Express each of the following complex numbers in polar form, and plot them in the
     complex plane, indicating the magnitude and angle of each number:
        (a) 1 + jj3              (b) -5                         (c) -5- 5j
       (d) 3 + 4j                   (e)  (1  - j}3)3                   (f)  (1 + j)s
                                                  j(6/jj)                                                                      Jfi                       ·3)(1 _                                               ")     (h)  2-                                                                                        (i)  I+               l3 +      (        ) (                                                   j(6Jjj)                                     2+                                                                                                                                                                                 .i                1                       1       g                                                                 J3+                "':J
      G)  j(l + j)e.i7TI6          (k)  ( j3 + j)2j2e- j7T/4        (I)   eirrl~-1
                                                                   I+Jfi
1.50.  (a) Using Euler's relationship or Figure Pl.48, determine expressions for x andy
            in terms of r and (J.
       (b) Determine expressions for r and (J in terms of x and y.
        (c) If we are given only rand tan 0, can we uniquely determine x andy? Explain
          your answer.
1.51. Using Euler's relation, derive the following relationships:
        (a) cos (J =  ~(e.i 8 + e- .i8)
       (b) sin (J =  -d-J(e.i8  -  e-.i8 )
         (c) cos2 (J = ~(1 + cos 20)
       (d)  (sinO)(sin<f>) =  ~ cos((J- </>)- ~ cos((J + </>)
        (e)  sin( (J + </>) = sin (J cos </> + cos (J sin </>
1.52. Let z denote a complex variable; that is,
                                  z = x + jy =  re.i8 .
     The complex conjugate of z is
                                             z* = x- jy = re- J&_
      Derive each of the following relations, where z, z1, and z2 are arbitrary complex
      numbers:
                 2        (a)  zz* =  r
       (b) ~ =  e.i2&
         (c) z + z* = 2CRe{z}
       (d) z -  z* = 2jdm{z}
         (e)  (zt + z2)* =  z~ + z;
          (f)  (l!Zt z2)* ~~ az~ z;, where a is any real number
        (g)  (:-'-)* = ~                                                                               .... 2                                                       ...... 2
       (h) Cfl~{~} =  _!_[z1z~+~:)'z2]
                                    .c2      2       ~2"-2
1.53. Derive the following relations, where z, z1, and z2 are arbitrary complex numbers:
        (a) (e 2)* =  e2*
       (b) ztz; + z~z2 = 2Cfl~{ztz;} = 2eR~{z~z2}

--- PAGE 73 ---

Chap. 1  Problems                                                         73

        (c)  lzl =  lz*l
       (d)  lz1 z2l =  lz1llz2l
        (e) CRe{z}   :::;  lzl, dm{z}   :::;  lzl
          (f)  lz1z; + ziz2l   :::; 21z1z2l
        (g)  (lzii -  lz2l)2  :::;  lz1 + z2l2 :::; (lzii + lz2l?
1.54. The relations considered in this problem are used on many occasions throughout the
      book.
        (a) Prove the validity of the following expression:
                    N-1Lan =  { Nl~aN,      fora=any1 complex number a  =I= 1 ·                    n=O         1-a

          This is often referred to as the finite sum formula.
       (b) Show that if Ia I < 1, then
                                                                                     00        1
                   Lan = 1-a·
                                     n=O

          This is often referred to as the infinite sum formula.
        (c) Show also if lal < 1, then


                                                                             00
                              2.:nan = __a_-=-                                   n=O          (1 - a)2.

       (d) Evaluate


          assuming that Ia I <  1.
1.55. Using the results from Problem 1.54, evaluate each of the following sums and ex-
      press your answer in Cartesian (rectangular) form:
        (a) L~=Oej1Tnl2          (b) L~=-2ej1Tnl2
        (c) "L:=o(~)nej1Tn!2     (d) "L:=2(~)nej1Tn/2
        (e) L~=O cos(~n)         (f) "L:=o(~)n cos(~n)
1.56. Evaluate each of the following integrals, and express your answer in Cartesian (rect-
      angular) form:
                               6        (a)  fo4ejml2dt          (b)  f0 ejm12dt
        (c)   8 ejm12dt          (d)   fooc e-(1 + j)t dt              f2
         (e)  fooc e-t cos(t)dt       (f)    e-2t sin(3t)dt                                                        f0oc