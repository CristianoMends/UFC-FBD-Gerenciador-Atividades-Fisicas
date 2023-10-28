class Exercise:
    def __init__(self, exercise_id, name, muscle_group, muscle_part, equipment, weight_used, date, hour, repetitions):
        self.exercise_id = exercise_id
        self.name = name
        self.muscle_group = muscle_group
        self.muscle_part = muscle_part
        self.equipment = equipment
        self.weight_used = weight_used
        self.date = date
        self.hour = hour
        self.repetitions = repetitions

    def __str__(self):
        return f"Exercise ID: {self.exercise_id}, Name: {self.name}, Muscle Group: {self.muscle_group}, Muscle Part: {self.muscle_part}, Equipment: {self.equipment}, Weight Used: {self.weight_used}, Date: {self.date}, Hour: {self.hour}, Repetitions: {self.repetitions}"
