import random

# Sample food database with Indian and English meal options
food_database = {
    "Indian": {
        "breakfast": {
            "high protein": ["Masala omelet", "Paneer bhurji", "Greek yogurt with fruit"],
            "vegan": ["Besan chilla (gram flour pancake)", "Smoothie bowl with almond milk", "Oats idli"],
            "low carb": ["Egg and spinach bhurji", "Almond flour dosa", "Avocado and poached eggs"],
            "gluten free": ["Rawa upma (made with gluten-free rawa)", "Idli with sambar", "Poha (flattened rice)"],
            "keto": ["Paneer and spinach stir-fry", "Egg curry", "Avocado chutney with cheese"],
        },
        "lunch": {
            "high protein": ["Chicken tikka salad", "Rajma (kidney beans) with brown rice", "Chole (chickpeas)"],
            "vegan": ["Chickpea curry with brown rice", "Vegetable biryani", "Palak tofu"],
            "low carb": ["Grilled tandoori chicken with salad", "Saag paneer with cauliflower rice", "Baingan bharta (mashed eggplant)"],
            "gluten free": ["Grilled fish with quinoa salad", "Dal tadka (spiced lentils) with rice", "Vegetable korma"],
            "keto": ["Butter chicken with cauliflower rice", "Keto chicken salad", "Tandoori shrimp"],
        },
        "dinner": {
            "high protein": ["Lentil soup with grilled chicken", "Tandoori chicken with sautéed vegetables", "Paneer tikka"],
            "vegan": ["Vegetable curry with quinoa", "Dal makhani (black lentils)", "Stuffed bell peppers with spices"],
            "low carb": ["Grilled lamb with mint yogurt sauce", "Chicken curry with cabbage rice", "Methi chicken (fenugreek chicken)"],
            "gluten free": ["Baked fish with herbs", "Chicken stew with vegetables", "Vegetable stew with coconut milk"],
            "keto": ["Keto-friendly butter chicken", "Fish curry with coconut milk", "Paneer tikka masala"],
        },
    },
    "English": {
        "breakfast": {
            "high protein": ["Scrambled eggs with spinach", "Greek yogurt with honey and berries", "Protein smoothie"],
            "vegan": ["Oatmeal with almond milk", "Fruit salad", "Avocado toast"],
            "low carb": ["Egg and cheese omelet", "Cottage cheese with nuts", "Bacon and eggs"],
            "gluten free": ["Smoothie bowl", "Chia seed pudding", "Fruit salad"],
            "keto": ["Egg and cheese muffins", "Bacon-wrapped asparagus", "Avocado and smoked salmon"],
        },
        "lunch": {
            "high protein": ["Grilled chicken salad", "Tuna salad", "Quinoa and black beans"],
            "vegan": ["Mixed bean salad", "Vegetable soup", "Falafel wrap"],
            "low carb": ["Zucchini noodles with pesto", "Cauliflower rice stir-fry", "Chicken Caesar salad"],
            "gluten free": ["Grilled chicken with mixed greens", "Stuffed bell peppers", "Quinoa salad"],
            "keto": ["Chicken salad with avocado", "Keto chili", "Cauliflower fried rice"],
        },
        "dinner": {
            "high protein": ["Steak with asparagus", "Salmon with broccoli", "Turkey stir-fry"],
            "vegan": ["Stir-fried vegetables with tofu", "Veggie curry", "Stuffed peppers"],
            "low carb": ["Grilled shrimp with salad", "Pork chops with Brussels sprouts", "Stuffed chicken breast"],
            "gluten free": ["Baked chicken with herbs", "Roasted vegetables", "Grilled fish"],
            "keto": ["Grilled steak with mushrooms", "Baked chicken thighs with herbs", "Pork chops with cauliflower mash"],
        },
    },
}

def get_user_preferences():
    print("Welcome to the Personalized Nutrition Plan Generator!")
    name = input("What's your name? ")
    weight = float(input("What's your weight (in kg)? "))
    cuisine = input("Please choose your preferred cuisine (Indian or English): ").strip().lower()
    
    while cuisine not in ["indian", "english"]:
        print("Invalid choice. Please choose 'Indian' or 'English'.")
        cuisine = input("Please choose your preferred cuisine (Indian or English): ").strip().lower()

    diet_type = input("What's your dietary preference? (high protein, vegan, low carb, gluten free, keto): ")
    meals_per_day = int(input("How many meals per day do you want to plan? (1-3): "))
    
    return name, weight, cuisine.capitalize(), diet_type, meals_per_day

def suggest_workout(weight):
    if weight < 60:
        return "30 minutes of light jogging or brisk walking."
    elif weight < 80:
        return "30 minutes of cycling or bodyweight exercises."
    else:
        return "30 minutes of strength training or high-intensity interval training (HIIT)."

def generate_meal_plan(cuisine, diet_type, meals_per_day):
    meal_plan = {}
    for meal_time in food_database[cuisine].keys():
        available_meals = food_database[cuisine][meal_time][diet_type]
        if len(available_meals) < meals_per_day:
            meals_per_day = len(available_meals)  # Adjust to the maximum available
        meal_plan[meal_time] = random.sample(available_meals, meals_per_day)
    
    return meal_plan

def display_meal_plan(name, meal_plan, workout):
    print(f"\nHello, {name}! Here’s your personalized meal plan:")
    for meal_time, meals in meal_plan.items():
        print(f"{meal_time.capitalize()}:")
        for meal in meals:
            print(f" - {meal}")
    print(f"\nSuggested workout for today: {workout}")
    print("\nEnjoy your meals and stay active!")

def main():
    name, weight, cuisine, diet_type, meals_per_day = get_user_preferences()
    workout = suggest_workout(weight)
    meal_plan = generate_meal_plan(cuisine, diet_type, meals_per_day)
    display_meal_plan(name, meal_plan, workout)

if __name__ == "__main__":
    main()
