#this is the programs that tells you about photos usages

import sys

print("Can you use this picture?")
print("Answer the following questions to find out!")
#clearer to see see the sentences
print(" ")
print(" ")


if input("Did you take or create the image yourself? (y/n) ") == "y":
    if input("Was the picture you created an original idea? (y/n) ") == "y":
        sys.exit("Yes! You automatically have the copyright to this picture")
    elif input("Not sure about it? (y/n) ") == "y":
        print("If you are not sure about it, do some researches!")
    else:
        sys.exit("No! You cannot use it if it is similar to someone else's picture")
else:
    print("Ask yourself the Fair Use Questions")
    if input("Are you using the image for personal, non-profit, educational, research, or scholarly purposes AND are you using the image sparingly, only for limited purposes? (y/n) ") == "y":
        sys.exit("Yes! It should be safe without the permission")
    else:
        if input("Are you transforming or repurposing the image to create a new purpose or meaning? (y/n) ") == "y":
            sys.exit("Yes! It should be safe without the permission")
        else:
            if input("Are you publishing the image in a fact-based context or publication that benefits the public as a whole (such as in a news source where it is important that people see the image)? (y/n) ") == "y":
                sys.exit("Probably! It will be safer to use under the laws")
            else:
                if input("Would it be considered impossible to obtain permission from the original source? (y/n) ") == "y":
                    sys.exit("Yes! ! It should be safe without the permission")
                else:
                    answer = input("Will you be using the image for personal or commercial gain? (If you answered 'n' to all the fair use questions, the use of your image would most likely be considered for personal or commercial gain.) (y/n) ")
                    if answer == "y":
                        if input("Is the image in the public domain or protected by creative commons agreements? (y/n) ") == "y":
                            sys.exit("Yes! It should be safe without the permission")
                        else:
                            if input("Did you purchase the image or obtain permission from the original source? (y/n) ") == "y":
                                sys.exit("Yes! It should be safe without the permission")
                            else:
                                sys.exit("No! This is illegal")
                    else:
                        while answer != "y":
                            if input("Are you using the image for personal, non-profit, educational, research, or scholarly purposes and are you using the image sparingly, only for limited purposes? (y/n) ") == "y":
                                sys.exit("Yes! It should be safe without the permission")
                            else:
                                if input("Are you transforming or repurposing the image to create a new purpose or meaning? (y/n) ") == "y":
                                    sys.exit("Yes! It should be safe without the permission")
                                else:
                                    if input("Are you publishing the image in a fact-based context or publication that benefits the public as a whole (such as in a news source where it is important that people see the image)? (y/n) ") == "y":
                                        sys.exit("Yes! It should be safe without the permission")
                                    else:
                                        if input("Would it be considered impossible to obtain permission from the original source? (y/n) ") == "y":
                                            sys.exit("Yes! It should be safe without the permission")
                                        else:
                                            answer = input("Will you be using the image for personal or commercial gain? (If you answered 'n' to all the fair use questions, the use of your image would most likely be considered for personal or commercial gain.) (y/n) ")
                        if input("Is the image in the public domain or protected by creative commons agreements? (y/n) ") == "y":
                            sys.exit("Yes! It should be safe without the permission")
                        else:
                            if input("Did you purchase the image or obtain permission from the original source? (y/n) ") == "y":
                                sys.exit("Yes! It should be safe without the permission")
                            else:
                                sys.exit("No! This is illegal")
