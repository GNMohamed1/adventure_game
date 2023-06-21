# region Imports
import random
import time
import os
import sys

# endregion


# region variables declerations

score: int = 0
game_lost: bool = False
start: bool = False
has_shovel: bool = False
has_key: bool = False
flip_switch: bool = False
water_pump: bool = True
intelligence: bool = False
negotiatied: bool = False
sperator: str = (
    "=================================="
    "==================================="
    "================================="
    "================================="
)

puzzles: list[list[str | list[str]]] = [
    [
        "I speak without a mouth and hear without ears."
        " I have no body, but I come alive with wind. What am I?",
        [
            "Whisper",
            "Thought",
            "Shadow",
            "An echo.",
        ],
    ],
    [
        "What has keys but can't open locks?",
        [
            "Typewriter",
            "Guitar",
            "Computer",
            "A piano.",
        ],
    ],
    [
        "The more you take, the more you leave behind. What am I?",
        [
            "Memories",
            "Experience",
            "Footprints",
            "Footsteps.",
        ],
    ],
    [
        "I am taken from a mine, and shut in a wooden case,"
        " from which I am never released. I am used by everyone. What am I?",
        [
            "Coal",
            "Gemstone",
            "Graphite",
            "Pencil lead.",
        ],
    ],
    [
        "I have keys but no locks. I have space but no room."
        " You can enter, but you can't go outside. What am I?",
        [
            "Calculator",
            "Phone",
            "Television",
            "A keyboard.",
        ],
    ],
    [
        "I have no legs but can run. I have no eyes but can cry. What am I?",
        [
            "Wind",
            "Nightmare",
            "Shadow",
            "A cloud.",
        ],
    ],
    [
        "I am full of holes, yet I can hold water. What am I?",
        [
            "Strainer",
            "Sieve",
            "Net",
            "A sponge.",
        ],
    ],
    ["What gets wet while drying?", ["Soap", "Clothes", "Hair", "Towel"]],
    [
        "I am an odd number. Take away one letter,"
        " and I become even. What number am I?",
        [
            "Three",
            "Nine",
            "Five",
            "Seven.",
        ],
    ],
    [
        "I have cities, but no houses. I have forests,"
        " but no trees. I have rivers, but no water. What am I?",
        [
            "Globe",
            "Book",
            "Atlas",
            "A map.",
        ],
    ],
]

# endregion of variables declerations


# region Utils
def type_writing(text: str) -> None:
    """
    The function types out a given text character by
    character with a slight delay between each
    character.

    :param text: A string representing the text that needs to be typed out
    :type text: str
    """

    # Iterate through each character in the text
    for char in text:
        # Write the current character to standard output and flush the
        # buffer
        sys.stdout.write(char)
        sys.stdout.flush()

        # Wait for 0.01 seconds before printing the next character
        time.sleep(0.01)

    # Print a newline character at the end of the text
    sys.stdout.write("\n\n")


def clear_screen() -> None:
    """
    A static method that clears the screen.
    """
    cmd = "cls" if os.name == "nt" else "clear"
    os.system(cmd)


def decision(options: dict):
    """
    The function displays a table of options and
    prompts the user to choose one, validating and
    executing the chosen option.

    :param options: The `options` parameter is a
    dictionary containing the available options for the
    user to choose from. The keys represent the
    option names, and the values represent their
    descriptions
    :type options: dict
    :return: the value of the chosen option from the input dictionary.
    """
    # Create a table to display the options
    table_data: list[str | list[str]] = [["Option", "Description"]]
    table_data += [
        [f"{index}", option]
        for index, (option, _) in enumerate(options.items(), start=1)
    ]
    print_table(table_data)

    while True:
        # Prompt for user input
        choice = input(
            f"Please choose one of the following "
            f"({','.join(map(str, range(1, len(options) + 1)))}): "
        )

        # Validate and execute the chosen option
        if choice.isdigit() and int(choice) in range(1, len(options) + 1):
            return list(options.values())[int(choice) - 1]
        else:
            print("Invalid choice.")


def print_table(data):
    """
    The function takes a list of strings or
    lists of strings as input and prints a formatted table.

    :param data: A list of strings or lists of
    strings representing the data to be displayed in the
    table. Each inner list represents a row in the table,
    and each string represents a cell in that
    row
    :type data: list[str | list[str]]
    """
    column_widths = []
    for column in zip(*data):
        max_width = 0
        for item in column:
            if len(str(item)) > max_width:
                max_width = len(str(item))
        column_widths.append(max_width)

    table = ""
    for row in data:
        row_string = ""
        for item, width in zip(row, column_widths):
            cell = str(item)
            cell += " " * (width - len(cell))
            row_string += f"| {cell} "
        table += row_string + "|\n"

    separator = "+".join("-" * (width + 2) for width in column_widths)
    table = separator + "+\n" + table + separator + "+\n"

    print(table)


def title_print(text: str):
    """
    The function takes in a string and a separator and
    prints the string with the separator above and
    below it.

    :param text: A string that represents the text
    to be printed in the center of the separator
    :type text: str
    :param sperator: The "sperator" parameter is a
    string that will be used as a separator or border
    around the printed text. It will be printed before
    and after the text to create a visual boundary
    :type sperator: str
    """

    print(sperator)
    type_writing(
        f"{text: ^10} \t\t\t\t\t\t\t\t\t\t | "
        f"Your current Score is :- {score:^10}"
    )
    print(f"{sperator}\n")


def riddle_print(score: int) -> int:
    riddle: list[str | list[str]] = random.choice(puzzles)
    title_print(riddle[0])  # type: ignore

    correct_answer = riddle[1][len(riddle[1]) - 1]

    answers: list[str | list[str]] = [["Option", "answer"]]
    answers += [
        [f"{index}", option] for index, option in enumerate(riddle[1], start=1)
    ]

    print_table(answers)

    responses: list[str] = [
        "The Grim Reaper statue's eyes flash with a malevolent crimson glow,"
        "as a chilling whisper fills the air, rejecting your response.",
        "A shiver runs down your spine as the Grim Reaper statue's "
        "features contort into a sinister grin, "
        "casting an ominous shadow over your answer.",
        "A bone-chilling gust of wind whispers through the cemetery, "
        "accompanied by a mournful wail, as the Grim Reaper statue's "
        "presence darkens with disappointment.",
    ]
    while input("What is the correct answer: ").lower() not in [
        correct_answer.lower(),
        "4",
    ]:
        score -= 1
        type_writing(f"{random.choice(responses)}\n\n")

    score += random.randint(1, 5)
    type_writing(f"Your score now is: {score}")

    return score


def story_node_choice(options: dict):
    """
    This function takes a dictionary of options,
    prompts the user to make a decision, clears the
    screen, and returns the user's choice.

    :param options: A dictionary containing the possible
    choices for the user to make in a story
    node. The keys of the dictionary are the choices
    and the values are the corresponding actions or
    story nodes that will be taken based on the user's choice.
    The function uses the
    decision() method to prompt the user to make
    :type options: dict
    :return: the user's choice from the given options
    dictionary after clearing the screen.
    """

    choice = decision(options)
    clear_screen()
    return choice


# endregion


# region Main game functions
def play():
    crypt()


def crypt():
    """
    The function simulates a scenario where the
    player wakes up in a crypt and has to make decisions
    to escape.
    """
    options = {"Escape The Crypt": outside}
    title_print("Inside a Crypt")

    type_writing(
        "As you regain consciousness, the chill of a "
        "stone slab greets your senses.\n"
        "Faint moonlight casts a dim glow, revealing only "
        "fragments of your surroundings.\n"
    )

    decision(
        {"Take a moment to survey your surroundings.": lambda: print("")}
    )

    type_writing(
        "You come across decayed remnants of life, scattered and crumbling.\n"
        "It dawns upon you that you are ensnared within a crypt!\n"
        "With urgency, you locate the door and make your escape.\n"
    )

    story_node_choice(options)()


def outside():
    """
    This function presents the player with
    options to explore different areas outside of a crypt in
    a cemetery.
    """
    global start
    options = {
        "North -> Fountain": fountain,
        "East -> Gate": gate,
        "South -> Bench": bench,
        "West -> Path": path,
    }

    title_print("Outside the Crypt")

    if not start:
        type_writing(
            "As you dash outside, the crypt"
            " door slams shut, sealing your entry."
        )
        start = True

    type_writing(
        "You find your standing in the midst of a "
        "cemetery, freed from the crypt's confines."
    )
    type_writing("Regrettably, the door cannot be reopened.")

    type_writing("To the North, a mesmerizing "
                 "fountain captures your attention.")
    type_writing("The East leads to the cemetery's entrance.")
    type_writing("In the South, an old bench beckons you to rest.")
    type_writing("A winding West stretches before you, tempting exploration.")

    story_node_choice(options)()


def gate():
    """
    This function presents options for the player
    to navigate through a cemetery gate and provides
    information about the surrounding areas.
    """
    options = {
        "North -> Graves": graves,
        "South -> Cottage": cottage,
        "West -> Outside": outside,
    }

    title_print("Gateway to the Cemetery")

    if not flip_switch:
        type_writing("The cemetery gate stands "
                     "firmly shut, refusing to yield.")
        type_writing("There must be a mechanism to"
                     " unlock it hidden somewhere.")
    else:
        type_writing("The gates now stand open, granting passage.")
        type_writing("You are free to exit the cemetery.")
        options["Leave -> End"] = good_ending

    type_writing("A multitude of graves extends to the North.")
    type_writing(
        "To the South, the flickering glow from a "
        "small cottage's windows catches your attention."
    )
    type_writing("The crypt awaits you West, "
                 "a haunting presence in the distance.")

    story_node_choice(options)()


def graves():
    """
    The function displays a description of a cemetery
    and provides options for the player to
    interact with it.
    """
    options = {"South -> Gate": gate, "West -> Fountain": fountain}

    title_print("Avenue of Resting Souls")

    type_writing("Before your gaze stretch countless rows of graves.")

    if not has_shovel:
        type_writing(
            "Among them, an open grave captures your attention,"
            " accompanied by a shovel left nearby."
        )
        options["Retrieve the shovel."] = take_shovel

    else:
        type_writing("Another open grave lies within sight.")

    type_writing("To the South, the cemetery gate beckons.")
    type_writing("Towards the West, you spot a tranquil fountain.")

    while True:
        choice = decision(options)

        if choice != take_shovel:
            break

        choice()
        del options["Retrieve the shovel."]

    clear_screen()
    choice()


def take_shovel():
    """
    This function sets the "has_shovel"
    attribute to True and prints a message indicating that the
    player has taken the shovel.
    """
    global has_shovel
    type_writing("You claim the shovel as your own.")
    has_shovel = True


def fountain():
    """
    The function presents options to the player
    in a game scenario involving a fountain, graves, a
    statue, and a crypt.
    """
    options = {"East -> Graves": graves, "South -> Outside": outside}

    title_print("A Mystical Fountain")

    if not water_pump:
        type_writing(
            "Before you stands a desiccated fountain,"
            " adorned with a statue of the Grim Reaper."
            "the water pump is leading to the top of the hill"
        )

    else:
        type_writing("The fountain has been revitalized, "
                     "its waters flowing once more,")
        type_writing(
            "as the statue of the Grim Reaper emits an"
            " ethereal glow, casting captivating reflections."
        )
        if not intelligence:
            type_writing(
                "You notice an inscription on the water's surface,"
                " beckoning you to decipher its riddle."
            )
            options["Read the message"] = riddle

    type_writing(
        "To the East, an array of graves extends into the distance."
    )

    type_writing("A silhouette catches your attention tp West.")

    if negotiatied or has_key:
        options["West -> Unconscious"] = negotiation
    else:
        options["West -> Gravedigger"] = gravedigger

    type_writing("To the South, the crypt awaits "
                 "in all its enigmatic allure.")

    story_node_choice(options)()


def riddle():
    global score
    global intelligence
    options = {"South -> Fountain": fountain}

    title_print("The Grim Reaper's Riddle")

    score = riddle_print(score)

    intelligence = True

    story_node_choice(options)()


def bench():
    """
    The function displays a description of a
    bench and provides options for the player to choose
    their next story node.
    """
    options = {
        "North -> Outside": outside,
        "East -> Cottage": cottage,
        "West -> Hill": hill,
    }
    title_print("An Quiet Bench")

    type_writing("An old bench sits in front of you.")

    type_writing("The crypt lies to the North.")
    type_writing("You see light in the windows of a"
                 " small cottage to the East.")
    type_writing("You notice a hill rising to the West.")

    story_node_choice(options)()


def path():
    """
    The function presents a path with different
    options for the player to choose from and progresses
    the story based on their choice.
    """
    options = {"East -> Outside": outside, "South -> Hill": hill}

    title_print("A Desolate Pathway")
    type_writing(
        "You find yourself traversing a desolate path,"
        " enclosed by solemn graves."
    )

    type_writing("A shadowy figure catches your attention,"
                 " beckoning from the North.")

    if negotiatied:
        options["North -> Negotiation"] = negotiation
    else:
        options["North -> Gravedigger"] = gravedigger

    type_writing("To the East, the crypt conceals its secrets.")
    type_writing(
        "A gentle hill rises towards the South,"
        " its prominence tempting your curiosity."
    )

    story_node_choice(options)()


def hill():
    """
    The function displays a description of a hilltop
      location and presents options for the player to
    choose from.
    """
    global water_pump

    options = {"North -> Path": path, "East -> Bench": bench}

    title_print("Perched on the Hilltop")

    type_writing(
        "You find yourself atop a desolate hill,"
        " a mysterious bush lurking nearby."
    )
    type_writing(
        "From this vantage point, your gaze extends"
        " to a distant, foreboding shape in the north."
    )
    type_writing("To the northeast, a crypt stands"
                 " solemnly among numerous graves.")
    type_writing("In the far east, a feeble glow emanates"
                 " from a diminutive structure.")

    if not water_pump:
        options["Search the bush"] = search_bush

    type_writing("A path winds its way North,"
                 " beckoning you to explore further.")
    type_writing("To the East, an old bench awaits,"
                 " inviting moments of respite.")

    while True:
        choice = decision(options)
        if choice != search_bush:
            break
        choice()
        del options["Search the bush"]

    clear_screen()
    choice()


def search_bush():
    """
    This function searches for a water pump valve hidden inside a bush,
    prompts the player with a decision to turn it on or not,
    and sets the global variable water_pump to True if the valve is turned on.

    Parameters:
    None

    Return:
    None
    """
    global water_pump
    type_writing(
        "Intrigued, you investigate the suspicious"
        " bush and uncover a valve for a water pump"
    )
    options = {"Turn the valve": turn_the_valve}
    decision(options)()
    water_pump = True


def turn_the_valve():
    """
    Execute the action of turning the valve. This function
      does not take any parameters and does not
    return anything. It simply calls the `type_writing`
    function to print a message confirming that the
    valve has been turned.
    """
    type_writing("You twist the valve, a creaking "
                 "sound echoing through the stillness.")


def cottage():
    """
    The function displays a description of
    the Gravekeeper's Cottage and provides options for the
    player to interact with it.
    """
    options = {"North -> Gate": gate, "West -> Bench": bench}

    title_print("The Abode of the Gravekeeper")

    type_writing(
        "The flickering glow of dim lights permeates "
        "the worn windows of the gravedigger's crumbling cottage."
    )
    if flip_switch:
        type_writing(
            "Your instincts scream against stepping foot inside"
            " the cottage again, compelling you to resist its lure."
        )
    elif not has_key:
        type_writing("The entrance stands firmly locked,"
                     " barring your passage.")
    else:
        type_writing(
            "With the key clutched tightly in "
            "your hand, you boldly approach the entrance,"
        )
        type_writing("ready to unlock the mysterious"
                     " secrets that lie beyond the door.")
        options["Open the door"] = inside

    type_writing("The cemetery gate is to the North.")
    type_writing("An old bench lies to the West.")

    story_node_choice(options)()


def inside():
    """
    The function describes the actions and
    options available to the player when inside the cottage
    in a text-based adventure game.
    """
    global flip_switch
    options = {"Flee the Cottage": cottage}

    title_print("Within the Cottage's Depths")

    type_writing(
        "Within the dimly lit cottage, "
        "an air of neglect permeates the musty atmosphere."
    )
    type_writing("Your gaze falls upon a conspicuous switch,")
    type_writing("rumored to hold the power to unlock the main gates.")

    decision({"Flip the Switch.": lambda: print("")})

    type_writing(
        "As your hand reaches out to engage the switch,"
        " movement in your periphery catches your attention."
    )

    type_writing(
        "Your eyes widen in surprise as the mirror "
        "reflects an image of a gallant, confident figure staring back at you."
    )
    type_writing(
        "For a fleeting moment, you entertain the "
        "idea of seeking assistance from this imagined savior,"
    )
    type_writing("only to realize the truth of your own reflection.")
    type_writing(
        "A profound sense of astonishment overcomes you, "
        "jolting your perception of self,"
        " urging you to swiftly depart from the cottage."
    )

    flip_switch = True

    story_node_choice(options)()


def gravedigger():
    """
    The function presents a scenario where the player
    encounters a gravedigger and provides options
    for the player to interact with the gravedigger.
    """
    options = {"East -> Fountain": fountain, "South -> Path": path}

    title_print("An Eerie Encounter")

    type_writing(
        "Amidst the graves, a peculiar "
        "figure stands, his murmurs lost to the wind."
    )

    if not has_shovel and not intelligence:
        type_writing(
            "A shiver runs down your spine,"
            " rendering you too paralyzed by fear to approach him."
        )

    type_writing(
        "Dangling from his belt, you spot an "
        "ancient key that catches the faint light."
    )

    if has_shovel:
        type_writing(
            "An unsettling thought crosses your mind"
            " as you consider confronting him, wielding the shovel."
        )
        options["Hit him with the Shovel"] = lose

    if intelligence:
        type_writing(
            "Summoning your newfound intellect,"
            " you cautiously decide to engage in negotiation."
        )
        options["Engage in negotiation"] = negotiation

    type_writing("To the East, a haunting fountain looms in the shadows.")
    type_writing(
        "A worn path stretches before you, extending South,"
        " seemingly leading you deeper into the unknown."
    )

    story_node_choice(options)()


def negotiation():  # sourcery skip: extract-duplicate-method
    global has_key
    global score

    score += random.randint(1, 5)

    options = {"West -> Path": path}
    title_print("A Sinister Encounter with the Gravedigger")
    type_writing("As you cautiously approach the gravedigger,")
    type_writing("his head slowly rotates towards you with an eerie,")
    type_writing("creaking motion, his eyes fixating on your presence.")

    if not has_key:
        type_writing("As you engage in negotiation,"
                     " your intellect shines through,")
        type_writing("captivating the gravedigger's attention.")
        type_writing(
            "Recognizing your astuteness, "
            "he relents and reluctantly hands you the key,"
        )
        type_writing("relinquishing its mysterious"
                     " power into your possession.")
        has_key = True

    type_writing(
        "In a hoarse whisper, he instructs"
        " you to proceed to the nearby cottage,"
    )
    type_writing(
        "emphasizing that unlocking its entrance "
        "holds the key to unlocking the front gate."
    )

    type_writing(
        "With this newfound knowledge, you determine"
        " it is time to retrace your steps, "
        "making your way back towards the West."
    )

    decision(options)()


def take_the_key():
    """
    This function sets the "has_key" attribute to
    True and prints a message indicating that the key
    has been grabbed.
    """
    global has_key
    type_writing("You swiftly claim the key "
                 "from the gravedigger's possession.")
    has_key = True


def lose():
    """
    The function displays the ending of a game and
      allows the player to choose whether to continue
    or end the game.
    """
    global score
    score -= random.randint(1, 5)
    options = {"Continue": game_over}

    title_print("You Have Lost")

    type_writing("The gravedigger swiftly retaliates to your attack!")
    type_writing("With a firm grip, he wrenches the shovel from your grasp.")
    type_writing("In a swift and merciless strike, he ends your life.")
    type_writing(
        "You find yourself consumed by the"
        " mysterious darkness that envelops you."
    )

    title_print("The End")

    story_node_choice(options)()


def good_ending():
    global score
    title_print("A Boundless Journey")
    score += random.randint(1, 5)
    type_writing(
        "Emerging from the cemetery, you embrace your"
        " extraordinary nature and embark on a transformative path."
    )
    type_writing(
        "With unique gifts, you bring light to darkness,"
        " fostering harmony and protecting the vulnerable."
    )
    type_writing(
        "Joined by fellow seekers, you form a community"
        " united in nurturing beauty and celebrating diversity."
    )
    type_writing(
        "Together, you shape a brighter future,"
        " where understanding triumphs over fear."
    )
    type_writing(
        "Onwards you venture, as the world transforms,"
        " embracing the harmony of light and dark."
    )

    title_print("The Final Embrace")


def game_over():
    title_print("Game Over")

    type_writing("You have reached the end of the journey.")
    type_writing(f"Your score is:- {score}")


# endregion


# region Execution
if __name__ == "__main__":
    while True:
        play()
        # Ask if the player want to play again
        again = input("do you want to play again [y/n]: ").lower().strip()
        while again not in ["yes", "y", "no", "n"]:
            print("Invalid input")
            again = input("do you want to play again [y/n]: ").lower().strip()
        # if the answer is yes then clear the screen and play again else exit
        if again not in ["yes", "y"]:
            break
        clear_screen()
        continue
# endregion
