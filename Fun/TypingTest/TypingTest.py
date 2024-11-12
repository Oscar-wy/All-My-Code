import time
from datetime import datetime

done = False
tests = {"Easy": "This is an easy typing test to see how fast you type!", "Medium": "This is a medium typing test to see if you can type properly; Heres a word: Superficial.", "Hard": "Now this, is a very hard typing test. Good luck: Supercalifragilisticexpialidocious;", "1 Minute": "In today’s fast-paced world, technology has become an integral part of daily life, transforming how we communicate, work, and entertain ourselves. With the advent of smartphones, social media platforms, and instant messaging apps, staying connected with friends and family is easier than ever. At the same time, these advancements have also brought about new challenges, such as the constant pressure to stay updated and the growing concern over privacy. As we embrace these changes, it's important to strike a balance—leveraging the convenience and benefits of technology while being mindful of its potential drawbacks. Understanding how to use these tools responsibly is key to maintaining a healthy relationship with the digital world and ensuring that technology serves us, rather than the other way around."}

def Typer(choice):
    done = False
    print("Get Ready...")
    time.sleep(2)
    print(tests[choice])
    st = time.time()
    while not done:
        a = input("")
        if choice == "1 Minute":
            if tt >= 60:
                done = True
        if a == tests[choice]:
            done = True
        else:
            print("Try Again!")
    ft = time.time()
    tt = ft - st
    print(f"It took you: {time.strftime('%M:%S', time.gmtime(tt))}")
    words = tests[choice].strip(".").split(" ")
    wpm = (len(words) / int(tt)) * 60
    print(f"WPM: {wpm}")

print("Hello Choose Difficulty Of Test")
difs = ["Easy", "Medium", "Hard", "1 Minute"]
print("\n1 - Easy")
print("\n2 - Medium")
print("\n3 - Hard")
print("\n4 - 1 Minute Test")
choice = ""
while not done:
    choice = int(input("> "))
    if choice == 1 or choice == 2 or choice == 3:
        done = True
    elif choice == 4:
        print("Idk how to do this in python")
    else:
        print("Not A Correct Option")
done = False
Typer(difs[choice-1])