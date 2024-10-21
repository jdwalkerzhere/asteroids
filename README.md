# Asteroids

## Summary
It's the old Atari game we all know and love, but crappy!

There's no scoring system yet, the asteroids are just circles, etc. etc. The code is also mostly undocumented, but I'll eventually go back and add some explanations for the critical, less-clear sections.

Either way it's still fun to plink around with and play!

## To Play
Outside of Python, the only other non-standard library dependency for this project is pygame. If you want to play the game, but don't want to install pygame globally, then when you clone this repo, do the following steps:

1. Create a virtual environment in the project directory (in this case `asteroids`)
```python3 -m venv venv```

2. Activate the virtual environment (obviously if you're on Windows flip the slashes)
```source venv/bin/activate```

3. Install pygame via the `requirements.txt` doc
```pip3 install -r requirements.txt```

4. Play the Game!
```python3 main.py```

That's it!

I'd love feedback on the project, but this was mostly a guided learning exercise, and I'm moving on to some unguided projects quickly, so I may or may not actually change anything to this repo.
