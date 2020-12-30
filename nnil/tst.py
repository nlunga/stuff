import glob
import subprocess
from playsound import playsound
from gtts import gTTS
import os

#rc = subprocess.call("connected.sh")
#while True:
#    subprocess.call("connected.sh")
# """
def finder():
    subprocess.call("./connected.sh")
    subprocess.call("clear")
    scan_result = "The device does not exist"
    for filename in glob.glob('output.txt'):
        with open("output.txt",'a') as outfile ,open(filename, 'r') as infile:
            for tweet in infile.readlines():
#                temp=tweet.split(' ')
#                print('{}'.format(' '.join(temp[7:])))
#                if tweet.find("innocent-Vostro-3550") != -1:
                if tweet.find("android-aa732f396822ffc1") != -1:
                    # print(tweet)
                    # scan_result = tweet
                    scan_result = "Innocent is connected"
                    break
    return scan_result

def playScanResults():
    found = True
    language = 'en'
    while found:
        if finder() == "Innocent is connected":
            answer = gTTS(text=finder(), lang=language, slow=False)
            answer.save("answer.mp3")
            playsound("answer.mp3")
            os.remove("answer.mp3")
        else:
            print("Fail")
            found = False

# while True:
# 	finder()
if __name__ == "__main__":
    playScanResults()
# """
# subprocess.call("ls -R ../../")
