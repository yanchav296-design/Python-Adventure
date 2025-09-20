import time
import sys

def pause(t=2.5):
    time.sleep(t)

# Branch: Susan & Eric path
def branch_susan_eric(name):
    # Returns:
    #  - "checkpoint" to go back to the 3-choice checkpoint
    #  - "restart" to restart the whole demo (intro)
    #  - "quit" to exit
    while True:
        print()
        print("'By the time camp is fully set up, the last streaks of sunlight vanish behind the trees.'")
        print()
        pause(2.5)

        # Who searches?
        while True:
            print("Eric: 'It's getting dark, and Derek’s been gone too long. We need to decide something, fast.'")
            print()
            pause(2.5)
            print(f"Type 1: {name}: 'Eric, you go find him. I’ll stay here with Susan and keep the fire going.'")
            print()
            print(f"Type 2: {name}: 'Eric, you stay with Susan. I’ll go out and look for him myself.'")
            print()
            Reply = input().strip()
            if Reply == "1":
                Choice1 = "1"
                break
            elif Reply == "2":
                Choice1 = "2"
                break
            else:
                print("Invalid Choice. Try again.")
                print()

        # Stay with Susan (Eric goes)
        if Choice1 == "1":
            print()
            print("'The forest grows silent. The fire pops softly, but the darkness beyond feels alive.'")
            print()
            pause(2.5)
            print("Susan: 'I’m getting worried... it’s been too long.'")
            print()
            pause(2.5)

            # Comfort or scare
            while True:
                print("Type 1: Reassure Susan, tell her everything will be okay.")
                print()
                print("Type 2: Make a dark joke to try and scare her.")
                print()
                Reply = input().strip()
                if Reply == "1":
                    VersionA = "1"
                    break
                elif Reply == "2":
                    VersionA = "2"
                    break
                else:
                    print("Invalid choice. Try again.")
                    print()

            # If comfort
            if VersionA == "1":
                print()
                print("Susan: 'Thanks... I needed that. But I can’t just sit here anymore.'")
                print()
                pause(2.5)

                while True:
                    print("Type 1: Go search with Susan into the forest.")
                    print()
                    print("Type 2: Insist on staying and waiting by the fire.")
                    print()
                    Reply = input().strip()
                    if Reply == "1":
                        # Demo completion (survive)
                        print()
                        print(f"Susan and {name} pick up a lantern and step into the oppressive dark of the forest.")
                        print()
                        pause(2.5)
                        print("Moments later, a blood-curdling scream echoes back from camp. Your blood freezes.")
                        print()
                        pause(2.5)
                        print("Both of you break into a terrified sprint deeper into the woods, away from the sound.")
                        print()
                        pause(2.5)
                        print("Congratulations — you survived this nightmarish demo ending.")
                        print()
                        pause(2.5)
                        return "restart"
                    elif Reply == "2":
                        # Death — return to checkpoint
                        print()
                        print("The fire burns low. The woods whisper and creak as the night stretches on.")
                        print()
                        pause(2.5)
                        print("Then, a sound — slow footsteps. Something massive moves just out of sight.")
                        print()
                        pause(2.5)
                        print("Before you can react, a dark shape lunges. Susan screams — then silence.")
                        print()
                        pause(2.5)
                        print("YOU DIED.")
                        print()
                        pause(2.5)
                        return "checkpoint"
                    else:
                        print("Invalid choice. Try again.")
                        print()

            # If scare
            elif VersionA == "2":
                print()
                print(f"{name}: 'Boo!'")
                print()
                pause(2.5)
                print("Susan gasps, clutching her chest, before glaring at you with wide eyes.")
                print()
                pause(2.5)
                print("Susan: 'Not funny. Not out here... not with Derek missing.'")
                print()
                pause(2.5)
                print("Suddenly, a sharp SNAP echoes from the trees. Something big moves between the trunks.")
                print()
                pause(2.5)
                print("The two of you freeze, hardly daring to breathe. The air tastes metallic, like blood.")
                print()
                pause(2.5)
                # Demo completion (survive but unsettling)
                print("Hours later, dawn creeps in. You somehow made it through the night... shaken, but alive.")
                print()
                pause(2.5)
                print("Congratulations — you survived this ending of the demo.")
                print()
                pause(2.5)
                return "restart"

        # Go search for Derek (you go)
        elif Choice1 == "2":
            print()
            print(f"{name} grabs a flashlight and pushes into the suffocating darkness of the trees.")
            print()
            pause(2.5)
            print("The deeper you go, the heavier the silence becomes. Every branch snap feels deafening.")
            print()
            pause(2.5)

            while True:
                print("Type 1: Turn back now and head to camp.")
                print()
                print("Type 2: Keep searching along the shoreline for Derek.")
                print()
                Reply = input().strip()
                if Reply == "1":
                    print()
                    print(f"{name} retreats to camp, nerves fraying with every step back.")
                    print()
                    pause(2.5)
                    print("When you arrive, Susan and Eric stare at you with pale faces.")
                    print()
                    pause(2.5)
                    print("From the distance, a shrill, inhuman cry tears through the night air. None of you speak.")
                    print()
                    pause(2.5)
                    print("Congratulations — you lived through the demo (uneasy survival ending).")
                    print()
                    pause(2.5)
                    return "restart"
                elif Reply == "2":
                    # Shoreline death
                    print()
                    print(f"{name} edges along the shoreline, the water black and still as glass.")
                    print()
                    pause(2.5)
                    print("Suddenly — a violent splash. Freezing water coils around your ankle, iron-strong.")
                    print()
                    pause(2.5)
                    print("You’re yanked under with terrifying force. The lake closes over your head.")
                    print()
                    pause(2.5)
                    print("Your last scream is swallowed by the dark water.")
                    print()
                    pause(2.5)
                    print("YOU DIED.")
                    print()
                    pause(2.5)
                    return "checkpoint"
                else:
                    print("Invalid choice. Try again.")
                    print()


# Branch: Derek path
def branch_derek(name):
    # Returns "checkpoint" or "restart"
    print()
    print(f"{name} follows Derek. The two of you split up along the bank, rods in hand.")
    print()
    pause(2.5)
    print(f"The sun sinks lower. Hours pass, and {name} hasn’t caught a single fish.")
    print()
    pause(2.5)

    while True:
        print(f"Type 1: {name}: 'I should head back to camp before it’s too dark.'")
        print()
        print(f"Type 2: {name}: 'I’ll check along the shoreline for Derek first.'")
        print()
        Reply = input().strip()
        if Reply == "1":
            Choice3 = "1"
            break
        elif Reply == "2":
            Choice3 = "2"
            break
        else:
            print("Invalid Choice. Try again.")
            print()

    if Choice3 == "1":
        # Back at camp — look or wait
        print()
        print(f"{name} trudges back to camp. The tents are up... but eerily empty.")
        print()
        pause(2.5)
        while True:
            print("Type 1: Search the campsite for clues.")
            print()
            print("Type 2: Sit at the campfire and wait for everyone to return.")
            print()
            Reply = input().strip()
            if Reply == "1":
                # Look around
                print()
                print(f"As {name} searches, you notice a faint trail of blood smeared into the dirt leading into the trees.")
                print()
                pause(2.5)
                while True:
                    print(f"{name}: 'Something terrible happened here...'")
                    print()
                    print("Type 1: Follow the trail deeper into the forest.")
                    print()
                    print("Type 2: Forget the trail — go search for Derek instead.")
                    print()
                    Reply2 = input().strip()
                    if Reply2 == "1":
                        # See entity munching — completed demo (survive)
                        print()
                        print(f"{name} crouches low, peering past the trees... and sees it.")
                        print()
                        pause(2.5)
                        print("A hulking figure, bent over, feeding on something human. The wet tearing sound turns your stomach.")
                        print()
                        pause(2.5)
                        print("You back away slowly, then bolt into the night, desperate to find your friends.")
                        print()
                        pause(2.5)
                        print("You survived. Congratulations — demo completed.")
                        print()
                        pause(2.5)
                        return "restart"
                    elif Reply2 == "2":
                        print()
                        print(f"{name}: 'Derek! Where are you?!'")
                        print()
                        pause(2.5)
                        print("The silence breaks with a metallic CLANG, echoing in the distance.")
                        print()
                        pause(2.5)
                        while True:
                            print("Type 1: Investigate the noise, heart racing.")
                            print()
                            print("Type 2: Flee the area while you still can.")
                            print()
                            R = input().strip()
                            if R == "1":
                                print()
                                print(f"{name} follows the sound, breath shallow. You find Derek, broken on the ground.")
                                print()
                                pause(2.5)
                                print("He barely lifts his head, whispering with bloodied lips: 'Run...'")
                                print()
                                pause(2.5)
                                print("A monstrous cry erupts from the camp behind you. Panic surges, and you sprint blindly.")
                                print()
                                pause(2.5)
                                print("YOU SURVIVED — but just barely. You flee into the endless night.")
                                print()
                                pause(2.5)
                                return "checkpoint"
                            elif R == "2":
                                print()
                                print(f"{name} bolts into the darkness, lungs burning, refusing to look back.")
                                print()
                                pause(2.5)
                                print("To be continued...")
                                print()
                                pause(2.5)
                                return "checkpoint"
                            else:
                                print("Invalid choice. Try again.")
                                print()
                    else:
                        print("Invalid choice. Try again.")
                        print()

            elif Reply == "2":
                # Wait at camp -> sleeping death
                print()
                print(f"{name} sits by the weak fire. The flames shrink, shadows crawling closer.")
                print()
                pause(2.5)
                print("Exhaustion takes over. Your eyes close, and sleep drags you down.")
                print()
                pause(2.5)
                print("You never feel the thing that comes in the night to claim you.")
                print()
                pause(2.5)
                print("YOU DIED.")
                print()
                pause(2.5)
                return "checkpoint"
            else:
                print("Invalid choice. Try again.")
                print()

    elif Choice3 == "2":
        # You go look for Derek along shoreline — death
        print()
        print(f"{name} hears Derek shouting in the distance, his voice excited, almost triumphant.")
        print()
        pause(2.5)
        print(f"{name}: 'Derek! Come on, let’s head back!'")
        print()
        pause(2.5)
        print("The tall grass rustles. Something heavy moves, snapping reeds with deliberate steps.")
        print()
        pause(2.5)
        print("Before you can even scream, the world goes black as you’re struck down from behind.")
        print()
        pause(2.5)
        print("YOU DIED.")
        print()
        pause(2.5)
        return "checkpoint"

def Main():
    # Outer full-demo loop: restart whole demo when branch returns "restart"
    while True:
        # Intro / setup
        print("'Camping Nightmare'")
        print()
        print("Press Enter to Play")
        print()
        input()
        print("'Greeting Player'")
        pause(2.5)
        name = input("Type your Name: ").strip()
        print()
        print(f"'{name}, you’re about to step into the woods where shadows hold secrets.'")
        print()
        pause(2.5)
        print("'Your friends stumbled across a forgotten lake that isn’t on any maps.'")
        print()
        pause(3)
        print("'They invited you to spend a night camping and fishing there.'")
        print()
        pause(3)

        # Ready check
        while True:
            print("When you’re ready, type: start")
            print()
            start = input().lower().strip()
            if start != "start":
                print("Seems like you’re not ready...")
                pause(2.5)
                print(f"{name}, your hesitation cost you the trip.")
                pause(2.5)
                print("COME BACK WHEN YOU’RE READY!!")
                pause(2.5)
                retry = input("Press Enter to try again or type 'exit' to quit: ").strip()
                if retry.lower() == "exit":
                    print("Goodbye.")
                    sys.exit()
                else:
                    continue
            else:
                break

        # Short conversation
        print()
        print(f"Eric: 'About time, {name}. You’re always the last one to show.'")
        print()
        pause(2.5)
        print("Susan: 'We were beginning to think you bailed on us!'")
        print()
        pause(2.5)
        print(f"Derek: '{name}, quit dragging your feet. The fish won’t wait.'")
        print()
        pause(5)

        # Initial reply
        while True:
            print("'Type 1: My bad, it took longer than expected to get ready.'")
            print()
            print("'Type 2: I do what I want.'")
            print()
            Reply = input().strip()
            if Reply == "1":
                print()
                print("Derek: 'Knew you’d slow us down.'")
                print()
                pause(2.5)
                print("Susan: 'Relax, Derek. Everyone’s here now, that’s what matters.'")
                print()
                pause(2.5)
                print("'Derek’s sharp words leave you uneasy.'")
                print()
                break
            elif Reply == "2":
                print()
                print("Derek: 'What’s your problem? You think this is funny?'")
                print()
                pause(2.5)
                print(f"A fight sparks between Derek and {name}, tension boiling over instantly.")
                print()
                pause(2.5)
                print("The trip falls apart before it begins. You failed to keep the peace.")
                print()
                pause(2.5)
                break
            else:
                print("Invalid choice. Try again.")
                print()

        pause(2.5)

        # === CHECKPOINT LOOP ===
        while True:
            print()
            print("'What should you do next?'")
            print()
            pause(2.5)
            print("'Type 1: Go with the group into the woods.'")
            print()
            print("'Type 2: Leave while you still can.'")
            print()
            print("'Type 3: Lash out at Derek and fight.'")
            print()
            Reply = input().strip()
            if Reply == "1":
                pass  # continue below into trip flow
            elif Reply == "3":
                print(f"{name} snaps, charging Derek. The fight explodes, dragging the whole group into chaos.")
                print()
                pause(2.5)
                print("The trip is ruined. Everyone storms off, bitter and angry.")
                print()
                pause(2.5)
                continue
            elif Reply == "2":
                print("You turn back toward the road. The forest stays behind you, secrets left untouched.")
                print()
                pause(2.5)
                continue
            else:
                print("Invalid choice. Try again.")
                continue

            # Group ventures
            print()
            print("The four of you trek deeper into the forest. The sun vanishes, shadows thickening.")
            print()
            pause(2.5)
            print("The woods are unnaturally silent. Not even crickets sing here.")
            print()
            pause(2.5)
            print(f"A chill crawls up {name}’s spine. Something about this place feels wrong.")
            print()
            pause(2.5)
            print("Eventually, you reach a hidden lake, black and still as glass.")
            print()
            pause(2.5)
            print("Eric: 'We made it. Should we set up camp now or wait?'")
            print()
            pause(2.5)
            print("Susan: 'If we wait, we’ll be fumbling in the dark. Let’s do it now.'")
            print()
            pause(2.5)
            print("Derek: 'You guys handle it. I’m fishing. Don’t wait up.'")
            print()
            pause(2.5)
            print("Eric and Susan begin setting up the tents while Derek wanders off toward the water.")
            print()
            pause(2.5)

            # Who to join
            while True:
                print()
                print("'Who should you join?'")
                print()
                pause(2.5)
                print("Type 1: Stay with Susan and Eric to help set up camp.")
                print()
                print("Type 2: Go with Derek to fish by the water.")
                print()
                Reply = input().strip()
                if Reply == "1":
                    result = branch_susan_eric(name)
                    if result == "checkpoint":
                        break
                    elif result == "restart":
                        break
                    elif result == "quit":
                        sys.exit()
                elif Reply == "2":
                    result = branch_derek(name)
                    if result == "checkpoint":
                        break
                    elif result == "restart":
                        break
                    elif result == "quit":
                        sys.exit()
                else:
                    print("Invalid choice. Try again.")
                    continue

            try:
                if result == "checkpoint":
                    continue
                elif result == "restart":
                    break
            except NameError:
                continue

        continue

if __name__ == "__main__":
    Main()
