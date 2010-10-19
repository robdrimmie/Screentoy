I first wrote this back in 2007, when my oldest was about a year old. I'd been intending on dusting it off for my youngest (9 months as of this writing) and decided to do it this morning because we're watching my two-year-old nephew. He giggled and squealed for like 5 minutes while playing with it, and keeps coming back to the laptop to try again so it was worth the very minimal effort. 

He, like every other child, was fascinated by my laptop but it was much too easy for him to be destructive. I had read about pyglet (http://www.pyglet.org/) on some blog somewhere and was interested in playing around with it, so I wrote this super simple little toy.

All it does is display whatever character was input in a very large size on the screen. If the letter keys are pressed, the background colour changes. The top row affects red, middle is blue and bottom is green. The further left-of-center the key, the greater te colour value is icreased. The further right-of-center the key, the greater the colour value is decreased.

There's something about pyglet and Snow Leopard 10.6 that don't play nice, so the shell script sets an environment variable to force 32-bit python. For details, see: http://code.google.com/p/pyglet/issues/detail?id=438

Run the program by running st.sh, exit by pressing the ESC key.
