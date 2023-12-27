#main.py

import json
from datetime import datetime
import SendEmail as e
import schedule
import time

class Exercise: # Exercise Class
    def __init__(self, name, reps, sets, weight):
        self.name = name
        self.reps = reps
        self.sets = sets
        self.weight = weight

#=============================================================

class WorkoutPlan:
    def __init__(self):
        self.days = {}

    # Adds Exercise to a Workout Plan
    def add_exercise(self, day, exercise):
        if day in self.days:
            self.days[day].append(exercise)
        else:
            self.days[day] = [exercise]

    # Displays the Workout Plan. Needs a String day. ex: "Monday" return -1 if workout not available
    def display_plan(self, today): 
        try:
            displayText = (f"({today}) Workout\n")
            
            for exercise in self.days[today]:
                displayText += f"\n{exercise.name}: {exercise.reps} (x{exercise.sets}) {exercise.weight}lbs"
            return displayText
        except:
            return -1

#=============================================================

# Read workoutData.json file and load its data
def read_workout_plan_from_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def getDayAsString(dayInt):
     match dayInt:
        case 0: # monday
            return "Monday"
        case 1: # tuesday
            return "Tuesday"
        case 2: # wednesday
            return "Wednesday"
        case 3: # thursday
            return "Thursday"
        case 4: # friday
            return "Friday"
        case 5: # saturday
            return "Saturday"
        case 6: # sunday
            return "Sunday"

# Confirm Todays Date
def ConfirmDateAndSendMessage(workout_plan, today):

    e.sender_email = 'youremail@gmail.com'
    e.receiver_email = 'youremail@gmail.com'
    e.password = 'YourPassword'
    e.subject = "GoodMorning"
    e.message = workout_plan.display_plan(today)

    if e.message != -1:
        e.send_email()
    else:
        print(f"No workout for {today}")

    print(workout_plan.display_plan(today))


# Workout Plan Setup:
def WorkoutPlanSetup():
    week = 1
    json_file_path = 'workoutData.json'
    workout_data = read_workout_plan_from_json(json_file_path)

    dt = datetime.now()
    date = dt.weekday()
    today = getDayAsString(date)

    workout_plan = WorkoutPlan()

    for day_data in workout_data:
        day = day_data['day']
        exercises = day_data['exercises']

        for exercise_data in exercises:
            exercise = Exercise(
                exercise_data['name'],
                exercise_data['reps'],
                exercise_data['sets'],
                exercise_data['weight']
            )
            workout_plan.add_exercise(day, exercise)

    ConfirmDateAndSendMessage(workout_plan, today)

# Schedule the script to run every day at 9 am
schedule.every().day.at("09:00").do(WorkoutPlanSetup)

#Keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)