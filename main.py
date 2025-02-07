import turtle
import pandas as pd

# Load the CSV file containing state names and their coordinates
df = pd.read_csv('50_states.csv')

# Set up the screen for the game
screen = turtle.Screen()
screen.title("U.S States Game")

# Load the blank map image
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

# Initialize game variables
correct_states = 0
is_game_on = True
answed_states = []  # List to store correctly guessed states

while is_game_on:
    # Prompt the user for a state name
    answer_state = screen.textinput(
        title=f"{correct_states}/50 Correct",
        prompt="What's another state name?"
    ).lower().capitalize()  # Convert input to match case formatting

    # Check if the answer is in the dataset
    if answer_state in df['state'].values:
        data = df[df['state'] == answer_state]
        x = data['x']
        y = data['y']

        # Create a turtle to write the state name at its location
        pen = turtle.Turtle()
        pen.hideturtle()
        pen.penup()
        pen.goto(float(x), float(y))  # Move to the state's coordinates
        pen.pendown()
        pen.write(f"{answer_state}", align="center", font=("Arial", 12, "normal"))

        # Update correct answers count
        correct_states += 1
        answed_states.append(answer_state)

    # End game if all states are guessed
    if len(answed_states) == 50:
        is_game_on = False

    # If user types 'Exist', save the states they didn't guess
    if answer_state == 'Exist':
        Non_answered = {'state':[row['state'] for index , row in df.iterrows() if row['state'] not in answed_states ]}
        # Save unguessed states to a CSV file
        df2 = pd.DataFrame(Non_answered)
        df2.to_csv('non_answered_state.csv')
        break  # Exit the game loop

# Close the game window when clicked
screen.exitonclick()
