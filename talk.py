from gtts import gTTS
from say import *
from playsound import playsound
import os
"""
x, nums, name = 12, list(range(4)), 'Fred'

say("There are {x} things.")
say("Nums has {len(nums)} items: {nums}")
say("Name: {name!r}")
"""
myText = "Hello there, my name is Lettie, and I'm learning how to code"
language = 'en'

out = gTTS(text=myText, lang=language, slow=False)
out.save("test.mp3")
playsound("test.mp3")
os.remove("test.mp3")
