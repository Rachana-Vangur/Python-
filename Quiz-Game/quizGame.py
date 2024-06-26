##This is a QUIZ GAME
print("#######################################################################")
print("\n")
text = "WELCOME TO THE QUIZ"
print(text.center(50))
print("\n")

print("#######################################################################")

topics = ("General Knowledge", "Basic CS", "Sports", "Social", "Movies")

questions = (("What is the capital of France?",
              "What is the largest animal on Earth?",
              "How many legs does a spider have?",
              "Who was the first person to walk on the moon?",
              "What color are bananas when they ripe?"),

              ("What does CPU stand for?",
               "What is the name of device used to point and click on the screen?",
               "What does HTML stand for?",
               "What does www mean?",
               "What is the main storage device in a computer called?"),
               
               ("How many players are in basketball team on the court at one time?",
                "In which sport do you perform slam dunk?",
                "How many bases are there in baseball?",
                "In soccer, what card is shown to the player when sent off?",
                "What is national sport of India?") ,
                
                ("What is the traditional dress worn by women in India?",
                 "Who was the first Prime Minister of India?",
                 "When was World War fought?",
                 "Name the country which was known as the country where sun never sets?",
                 "Name the company which ruled India?"),
                 
                 ("Which franchise has a character called Neville Longbottom?",
                  "What does MCU stand for?",
                  "Which telugu was nominated and won Oscar?",
                  "Name the movie which tells the story of young Mark Zuckerberg?",
                  "Name the actor who played as main lead in DUNE?")
                  
                  )


print("The topics are\n")
print("A. General Knowledge\nB. Basics in CS\nC. Sports\nD. Social Knowledge\nE. Movies\n")
chosen_topic = input("Choose any one topic\n").upper()

topic_number = -1
if chosen_topic == 'A':
    topic_number = 0
elif chosen_topic == 'B':
    topic_number = 1
elif chosen_topic == 'C':
    topic_number = 2
elif chosen_topic == 'D':
    topic_number = 3
elif chosen_topic == 'E':
    topic_number = 4
else:
    print("Invalid topic chosen.")
    exit()

print("Which level of difficulty would you like to play?")
print("A. Easy\nB. Medium\nC. Hard\n")
chosen_level = input("Enter your choice:")

if chosen_level == 'A':
    diff_level = 0
elif chosen_level == 'B':
    diff_level = 1
elif chosen_level == 'C':
    diff_level = 2
else:
    print("Invalid option")
    # exit()


options = ((("A. London", "B. Rome", "C. Paris", "D. Osaka"),
            ("A. Elephant", "B. Blue Whale", "C. Giraffe", "D. Polar Bear"),
            ("A. Six", "B. Eight", "C. Ten", "D. Twelve"),
            ("A. Neil Armstrong", "B. Buzz Aldrin", "C. Yuri Gagarin", "D. John Glenn"),
            ("A. Red", "B. Green", "C. Purple", "D. Yellow")),

           (("A. Central Processing Unit", "B. Central Process Unit", "C. Computer Personal Unit", "D. Central Processor Unit"),
            ("A. Monitor", "B. Keyboard", "C. Mouse", "D. Printer"),
            ("A. Hyper Text Markup Language", "B. Hyperlinks and Text Markup Language", "C. Home Tool Markup Language", "D. Hyperlinking Text Marking Language"),
            ("A. World Wide Web", "B. World Web Wide", "C. Web Wide World", "D. Wide World Web"),
            ("A. RAM", "B. Hard Disk", "C. SSD", "D. CPU")),

           (("A. Five", "B. Six", "C. Seven", "D. Eight"),
            ("A. Soccer", "B. Basketball", "C. Tennis", "D. Football"),
            ("A. Two", "B. Three", "C. Four", "D. Five"),
            ("A. Red Card", "B. Yellow Card", "C. Green Card", "D. Blue Card"),
            ("A. Cricket", "B. Hockey", "C. Kabaddi", "D. Football")),

           (("A. Saree", "B. Kimono", "C. Hanbok", "D. Cheongsam"),
            ("A. Indira Gandhi", "B. Jawaharlal Nehru", "C. Mahatma Gandhi", "D. Rajiv Gandhi"),
            ("A. 1914-1918", "B. 1939-1945", "C. 1917-1921", "D. 1941-1945"),
            ("A. France", "B. England", "C. Spain", "D. Russia"),
            ("A. British East India Company", "B. Dutch East India Company", "C. French East India Company", "D. Portuguese East India Company")),

           (("A. Hunger Games", "B. Lord of the Rings", "C. Star Wars", "D. Harry Potter"),
            ("A. Magic Cinematic Universe", "B. Monster Cinematic Universe", "C. Marvel Cinematic Universe", "D. Machine Cinematic Universe"),
            ("A. Baahubali", "B. RRR", "C. Pushpa", "D. KGF"),
            ("A. The Social Network", "B. The Facebook Story", "C. The Zuck Life", "D. The Internet Giant"),
            ("A. Tom Holland", "B. Chris Pratt", "C. Robert Pattinson", "D. Timothée Chalame")))

answers = (("C", "B", "B", "A", "D"),
           ("A", "C", "A", "A", "B"),
           ("B", "B", "C", "A", "B"),
           ("A", "B", "B", "B", "A"),
           ("D", "C", "B", "A", "D"))

guess = []


for i in range(0,5):
    print(questions[topic_number][i])
    
    for option in (options[topic_number][i]):
        print(option)
    print("\n")
    guess.append(input("Your choice:\n").upper())    

score = 0
for i in range(0, 5):
    if(guess[i] == answers[topic_number][i]):
        score += 1
    
print("Your answers were:")
for i in range (0,5):
    print(guess[i])
print("\n")
print("Correct answers are:")
for i in range(0, 5):
    print(answers[topic_number][i])
print("\n")
print(f"Hence, your score is:\n{score}")
if score == 0:
    print("Better luck next time!")
elif score > 0 and score <= 3:
    print("You can do better")
else:
    print("You did fantastic!")

