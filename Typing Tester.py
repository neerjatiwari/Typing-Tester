#OPTUM - PROJECT 1 - "TYPING TESTER"

import time

test_text = "Hello I am Neerja Tiwari . I am B.Tech 4th year undergrad from MAIT Delhi. My hoppy is Mandala Art."


def func(input, startTime, endTime):
    
    wordcount = len(input.split())
    timetaken = endTime - startTime
    wpm =  wordcount / (timetaken / 60)

    
    correctchars = 0
    for i in range(min(len(input), len(test_text))):
        if input[i] == test_text[i]:
            correctchars += 1
    accuracy = (correctchars / len(test_text)) * 100

    return wpm, accuracy


def typing_test():
    print("Typing Test: Type the above text.")
    print(test_text)

    input("Press Enter to start...")
    start_time = time.time()
    user_input = input("Start typing: ")
    end_time = time.time()

    wpm, accuracy = func(user_input, start_time, end_time)

    print("\n Typing speed is {:.2f} words per minute.".format(wpm))
    print(" Typing accuracy is {:.2f}%.".format(accuracy))


typing_test()
