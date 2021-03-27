# Import the Gtts module for text
# to speech conversion
from gtts import gTTS
from playsound import  playsound

mytext = 'Wellcome to convert text to speech using python'

# Language we want to use
language='en'

myobj=gTTS(text=mytext,lang=language,slow=True)

# Play the converted
myobj.save("welcome1.mp3")
playsound("welcome1.mp3")
