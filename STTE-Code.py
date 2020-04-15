import os
import speech_recognition as sr

#After importing the speech recognition module then next step is to initialize
#the speech which I mentioned in function as below

def main():
    r = sr.Recognizer()
    #Now the speech is going to use online recogniser
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Hi, which shell command do you want to execute ? ")
        #Now we should give speech input and going to listening
        audio = r.listen(source)

        #Here using recognizer to convert into text as well as to execute
        #the input shell command
        try:
            r1=r.recognize_google(audio)
            print("You said : \n "+r1)
            os.system("{t1}".format(t1=r1))
            print("Okay")
        except Exception as e:
            print("Error : " + str(e))

#calling main function
if __name__=="__main__":
    main()
