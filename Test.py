
import time
#Main Script
def Main():
    print("'Camping Nightmare'")
    print()
    print("Enter anything to Play")
    print()
    input() == print("'Greeting Player'")
    time.sleep(2.5)
    name = input("Type your Name:")
    for _ in range(300):
        print(f"'{name}, you're about to venture into the woods'")
        print()
        time.sleep(2.5)
        print("'Your friends recently discover an unknown lake'")
        print()
        time.sleep(3)
        print("'You were invited to camp and fish for a night'")
        print()
        time.sleep(3)
# Checkpoint Start
        while True:
            print("When you're ready type: start")
            print()
            start = input().lower()
            if start != "start":
                print("Seems like you're not ready...")
                time.sleep(2.5)
                print(f"{name}, you let your friends down!!")
                time.sleep(2.5)
                print("COMEBACK WHEN YOU'RE READY!!")
                time.sleep(2.5)
                retry = input("Enter anything to go back to the menu or type 'exit' to quit: ")
                if retry.lower() == "exit":
                    exit()
                else:
                    continue  # Repeats the loop
            else:
                break  # Player typed 'start', exit loop and continue story
        print()
        print(f"Eric: 'Goodmorning {name}, late as usual'")
        print()
        time.sleep(2.5)
        print("Susan: 'There you are, slow-poke!!'")
        print()
        time.sleep(2.5)
        print(f"Derek:'{name}, comon on man, the fish aren't gonna bite by the time we get there..'")
        print()
        time.sleep(5)
#Checkpoint Main Story     
        while True:
            print("'Type 1: My bad it took longer than I'd expected to prep,'")
            print()
            print("'Type 2: I do what I want'")
            print()
            Reply = input()
            if(Reply == "1"):
                print()
                print("Derek:'I told yall we shouldn't had brought him along'")
                print()
                time.sleep(2.5)
                print("Susan:'Chill Derek. We all make mistakes'")
                print()
                time.sleep(2.5)
                print("'Derek made you uncomfortable'")
                print()
                break
            else:
                print("Derek:'Is this a Joke to you'")
                print()
                time.sleep(2.5)
                print(f"'Derek and {name} got into a fight")
                print()
                time.sleep(2.5)
                print("'The trip is canceled. You Failed'")
                print()
                time.sleep(2.5)
                continue
        time.sleep(2.5)
#Checkpoint 1
        while True: 
            print("'What should you do'")
            print()
            time.sleep(2.5)
            print("'Type 1:Go with them'")
            print()
            print("'Type 2:Leave'")
            print()
            print("'Type 3:Fight Derek'")
            print()
            Reply = input()
            if(Reply == "1"):
                break
            elif(Reply == "3") :
                print(f"'{name} ran up and round house kick Derek from behind'")
                print()
                time.sleep(2.5)
                print(f"'{name} and Derek got into a brawl'")
                print()
                time.sleep(2.5)
                print("'Trip got Cancel, try again another day'")
                print()
                time.sleep(2.5)
                continue
            
            else:
                print("'You left safely home'")
                print()
                time.sleep(2.5)
                print("'You didn't get to enjoy the trip'")
                print()
                time.sleep(2.5)
                print("'The End'")
                print()
                time.sleep(2.5)
                Restart = input("'Enter to Play again'")
                continue
        print()
        print("'The Group venture into the woods for Hours'")
        print()
        time.sleep(2.5)
        print("'As the group gets deeper and deeper into the forest'")
        print()
        time.sleep(2.5)
        print(f"'{name} felt a chill and notice the woods is too quiet'")
        print()
        time.sleep(2.5)
        print("'Yall made it to the lake!'")
        print()
        time.sleep(2.5)
        print("Erik:'We're here finally. Should we set up camp now, later?'")
        print()
        time.sleep(2.5)
        print("Susan:'I rather set up camp now then later'")
        print()
        time.sleep(2.5)
        print("Derek:'Whatever yall want. I'm going, FISHIING!'")
        print()
        time.sleep(2.5)
        print("'Eric decided to help Susan set up camp'")
        print()
        time.sleep(2.5)
#checkpoint Version A/B        
        while True:
            print("'Who should you join?")
            print()
            time.sleep(2.5)
            print("'Type 1: Susan and Eric'")
            print()
            print("'Type 2: Derek'")
            print()
            Reply = input()
            if Reply == "1":
                (Choice) = "1"  
                break
            elif Reply == "2":
                (Choice) = "2"
                break
            else:
                print("Invalid choice, try again")
#checkpoint Version A
        if (Choice) == "1":    
            print("'By the time camp is set up the sun is setting'")
            print()  
        while True:
            time.sleep(2.5)
            print("Eric:'It's getting dark soon and Derek has been gone for awhile. What should we do'")
            print()
            time.sleep(2.5)
            print(f"'Type 1: {name}: Eric, you go find him, I'll stay with Susan'")
            print()
            print(f"'Type 2: {name}: Eric you stay with Susan, I'll go look for him")
            print()
            Reply = input()
            if(Reply == "1"):
                Choice1 = "1"
                break
            elif Reply == "2":
                 Choice1 = "2"
                 break
            else:
                 print("Invalid Choice")
#checkpoint                
        if Choice1 == "1":  
            print()
            print("'Sun is gone. Can't see anything from 20ft away'")
            print()
            time.sleep(2.5)
            print("Sunsan:'I'm starting to get worried, they're both been gone for a min'")
            print()        
            time.sleep(2.5)
        while True:
            time.sleep(2.5)
            print("'Type 1:Comfort Susan'")
            print()
            print("'Type 2: Scared Susan'")
            print()
            Reply = input()
            if(Reply == "1"):
                VersionA = "1"
                break
            elif Reply == "2":
                VersionA = "2"
                break
            else:
                print("Invalid choice")

        if VersionA == "1":            
            print()
            print("Sunsan:'Let's go look for them'")
            print()
        while True:    
            time.sleep(2.5)
            print("'Type 1: Go'")
            print()
            print("'Type 2: Stay and wait'")
            print()
            Reply = input()
            if(Reply == "1"):
                VersionA1 = "1"
                break
            elif Reply == "2":
                VersionA1 = "2"
                break
            else:
                print("Invalid choice")
        
        if VersionA1 == "1":
            print()
            print(f"'Susan and {name} left camp'")
            print()
            time.sleep(2.5)
            print("'They're a mile from camp'")
            print()
            time.sleep(2.5)
            print("They heard a chilling cry from an unknown creature at camp'")
            print()
            time.sleep(2.5)
            print("'Both of them made a panic run for it'")
            print()
            time.sleep(2.5)
            print("'Congratulation you completed the demo'")
            print()
            time.sleep(2.5)
            Restart = input("Enter anything to retry all demo ending")
            if(Restart == "") : Main()
        elif VersionA1 == "2":
            print("'You both waited and waited'")
            print()
            time.sleep(2.5)
            print(f"'{name} heard something slowly creeping up behind them'")
            print()
            time.sleep(2.5)
            print(f"'{name} turn around.' Unknown Entity: 'Scream!!'")
            print()
            time.sleep(2.5)
            print(f"'An Entity slaughter Susan and {name}")
            print()
            time.sleep(2.5)
            print("'You died'")
            print()
            time.sleep(2.5)
            print("'Thank you for playing the demo'")
            print()
            time.sleep(2.5)
            Restart = input("Enter anything to retry all demo ending")
            if(Restart == "") : Main()
                    
        elif VersionA == "2":
            print(f"{name} made Susan cried loudly")
            print()
            time.sleep(2.5)
            print(f"'{name} tried to calmed her down'")
            print()
            time.sleep(2.5)
            print("Unknown creature:'Chilling cry loudly from afar in the woods")
            print()
            time.sleep(2.5)
            print(f"Susan and {name}, stop all action to focus on the sound")
            print()
            time.sleep(2.5)
            print(f"{name}:'What is that'")
            print()
        while True:
            time.sleep(2.5)
            print("In a panic, Susan stand up, and start running toward the direction Eric went looking for Derek")
            print()
            time.sleep(2.5)
            print("'Type 1: Follow her'")
            print()
            print("'Type 2: Climb up the closest tree'")
            print()
            Reply = input()
            if(Reply == "1"):
                VersionA2 = "1"
                break
            elif Reply == "2":
                VersionA2 = "2"
                break
            else:
                print("Invalid choice")
        
        if VersionA2 == "1":
            print()
            print(f"'Susan and {name} both ran as hard as they could'")
            print()
            time.sleep(2.5)
            print("'But an Unknown creature catch up and slaughter them both'")
            print()
            time.sleep(2.5)
            print("'Thank you for trying the demo'")
            print()
            time.sleep(2.5)
            Restart = input("Enter anything to retry all demo ending")
            if(Restart == "") : Main()
        elif VersionA2 == "2":
            print(f"'{name} saw a huge entity passed by camp and ran toward Susan direction'")
            print()
            time.sleep(2.5)
            print(f"'{name} climb down and ran the opposite direction'")
            print()
            time.sleep(2.5)
            print("'Thank you for playing the demo'")
            print()
            Restart = input("Enter anything to retry all demo ending")
            if(Restart =="") : Main()

        elif Choice1 == "2":
            print(f"{name}: 'Derek where are you!'")
            print()
            time.sleep(2.5)
            print(f"{name}: 'It's getting dark maybe I should head back'")
            print()
            time.sleep(2.5)
            print(f"'{name} heard a noise of metal clanging from a distant'")
            print()
            print("'Type 1: Go investigate'")
            print()
            print("'Type 2: Go back to camp'")
            print()
            Reply = input()
            if(Reply == "1"):
                    Choice2 = "1"
                    break
            elif Reply == "2":
                 Choice2 = "2"
                 break
            else:
                 print("Invalid Choice")
#checkpoint                
        if Choice2 == "1":
            print()
            print(f"'{name} check the noise'")
            print()
            time.sleep(2.5)
            print(f"'{name} find Derek lying on the ground. Torse torned in half.'")
            print()
            time.sleep(2.5)
            print(f"{name}:'Derek! what happen'")
            print()
            time.sleep(2.5)
            print("'Derek spoke softly with a dying voice'")
            print()
            time.sleep(2.5)
            print("Derek:'Run'")
            print()
            time.sleep(2.5)
            print("A loud unknown chilling cried from camp")
            print()
            time.sleep(2.5)
            print(f"'{name} made a run for it without looking back'")
            print()
            time.sleep(2.5)
            print("'Thank you for playing the demo'")
            print()
            time.sleep(2.5)
            Restart = input("Enter anything to retry all demo ending")
            if(Restart == "") : Main()
        elif Choice2 == "2":       
            print(f"'{name} got back near camp'")
            print()
            time.sleep(2.5)
            print(f"'{name} see a big creature creeping up from a distant on the opposite side'")
            print()
            time.sleep(2.5)
            print(f"{name}:'Run!! Something is coming up from behind!!'")
            print()
            time.sleep(2.5)
            print("'Thank you for playing the demo'")
            print()
            time.sleep(2.5)
            Restart = input("Enter anything to retry all demo ending")
            if(Restart == "") : Main()

        elif (Choice) == "2":
            print(f"'{name}, join Derek, but they went to there separate fishing spot soon after'")
            print()
            time.sleep(2.5)
            print(f"'The sun is setting and {name} hasn't caught a single fish'")
            print()
                        
        while True:    
            time.sleep(2.5)
            print(f"{name}: 'It's getting dark'")
            print()
            time.sleep(2.5)
            print(f"Type 1:{name}:' I need to head back'")
            print()
            print(f"Type 2:{name}:' I should go look for Derek'")
            print()
            Reply = input()
            if(Reply == "1"):
                Choice3 = "1"
                break
            elif Reply == "2":
                Choice3 = "2"
                break
            else:
                print("Invalid Choice")              
        
        if Choice3 == "1":
            print()
            print(f"'{name} made it back. Camp is set up, but no one is here'")
            print()
        while True:    
            time.sleep(2.5)
            print("'Type 1: look around'")
            print()
            print("'Type 2: Sit at the campfire and wait for everyone'")
            print()
            Reply = input()
            if(Reply == "1"):
                Choice4 = "1"
                break
            elif Reply == "2":
                Choice4 = "2"
                break
            else:
                print("Invalid Choice")

        if Choice4 == "1":              
            print()
            print(f"'{name} looked arounded and saw a trail of bloods leading into the wood'")
            print()
            time.sleep(2.5)
            print(f"'{name} freak out'")
            print()
            while True:                        
                time.sleep(2.5)
                print(f"{name}:'Something bad must've happened at camp'")
                print()
                time.sleep(2.5)
                print("'Type 1: Go investigate'")
                print()
                print("'Type 2: GO back and look for Derek'")
                print()
                Reply = input()
                if(Reply == "1"):
                    Choice5 = "1"
                    break
                elif Reply == "2":
                    Choice5 = "2"
                    break
                else:
                    print("Invalid choice")
        elif Choice4 == "2":
            print(f"'{name} waited for a while, but no has came back yet'")
            print()
            time.sleep(2.5)
            print(f"'{name} fell asleep around that campfire'")
            print()
            time.sleep(2.5)
            print(f"'Something killed {name} while {name} was asleep'")
            print()
            time.sleep(2.5)
            Restart = input("Enter anything to retry")
            if(Restart == "") : Main()
       
        elif Choice3 == "2":
            print(f"'{name} heard Derek shouting from enjoyment in a distance'")
            print()
            time.sleep(2.5)
            print(f"{name}:' Derek, Let's head back!'")
            print()
            time.sleep(2.5)
            print(f"'{name} heard grass thrashes as if something unseen is slicing through it, each step punctuated by the sharp snap of breaking wood'")
            print()
            time.sleep(2.5)
            print(f"'Something swiftly came by and took the light out of {name}'")
            print()
            time.sleep(2.5)
            print("'Killed by an entity'")
            print()
            time.sleep(2.5)
            Restart = input("Enter anything to retry")
            if(Restart == "") : Main()

        if Choice5 == "1":
            print(f"'{name} See an entity munching on something'")
            print()
            time.sleep(2.5)
            print(f"'{name} slowly back up to camp and made a run to look for the others'")
            print()
            time.sleep(2.5)
            print("'You complete the demo'")
            print()
            time.sleep(2.5)
            Restart = input("Enter anything to start over")
            if(Restart == "") : Main()
                                
        elif Choice5 == "2":
            print(f"{name}:'Derek, where are you!'")
            print()
            time.sleep(2.5)
            print(f"'{name} heard a metal noise clanging from a distance'")
            print()
        while True:
            time.sleep(2.5)
            print("'Type 1: Go investigate'")
            print()
            print("'Type 2: Get out of here'")
            Reply = input()
            if(Reply == "1"):
                print()
                print(f"'{name} check the noise'")
                print()
                time.sleep(2.5)
                print(f"'{name} find Derek lying on the ground. Torse torned in half.'")
                print()
                time.sleep(2.5)
                print(f"{name}:'Derek! what happen'")
                print()
                time.sleep(2.5)
                print("'Derek spoke softly with a dying voice'")
                print()
                time.sleep(2.5)
                print("Derek:'Run'")
                print()
                time.sleep(2.5)
                print("A loud unknown chilling cried from camp")
                print()
                time.sleep(2.5)
                print(f"'{name} made a run for it without looking back'")
                print()
                time.sleep(2.5)
                print("'Thank you for playing the demo'")
                print()
                time.sleep(2.5)
                Restart = input("Enter anything to retry all demo ending")
                if(Restart == "") : Main()
            else:
                print(f"'{name} made a run for it'")
                print()
                time.sleep(2.5)
                print("'To be continue'")
                print()
                time.sleep(2.5)
                Restart = input("Enter anything to play again")
                if(Restart == "") : Main()
Main()
            
