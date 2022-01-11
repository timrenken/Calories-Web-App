class Calorie:
    """Represents amount of calories calculated with
    BMR = 10 * weight (kg) + 6.25 * height (cm) - 5 * age (years) - 161 (women)."""

    def __init__(self, weight, height, age, temperature, sex):
        self.weight = weight
        self.height = height
        self.age = age
        self.temperature = temperature
        self.sex = int(-161) if sex == 'woman' else int(5)

    def calculate(self):
        return (4.536 * self.weight) + (15.88 * self.height) - (5 * self.age) + self.sex

# Male = (4.536 × weight in pounds) + (15.88 × height in inches) − (5 × age) + 5
# Female = (4.536 × weight in pounds) + (15.88 × height in inches) − (5 × age) − 161
