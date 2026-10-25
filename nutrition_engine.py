nutrition_engine.py

Nutrition calculation engine for NutriVision AI
"""

# -----------------------------
# Food Database
# Values are approximate per serving
# -----------------------------

FOOD_DATABASE = {

    "Rice": {
        "calories": 205,
        "protein": 4.3,
        "carbs": 45,
        "fat": 0.4,
        "fiber": 0.6,
        "healthy": True
    },

    "Brown Rice": {
        "calories": 216,
        "protein": 5,
        "carbs": 45,
        "fat": 1.8,
        "fiber": 3.5,
        "healthy": True
    },

    "Chicken": {
        "calories": 165,
        "protein": 31,
        "carbs": 0,
        "fat": 3.6,
        "fiber": 0,
        "healthy": True
    },

    "Beef": {
        "calories": 250,
        "protein": 26,
        "carbs": 0,
        "fat": 15,
        "fiber": 0,
        "healthy": False
    },

    "Fish": {
        "calories": 180,
        "protein": 25,
        "carbs": 0,
        "fat": 8,
        "fiber": 0,
        "healthy": True
    },

    "Egg": {
        "calories": 72,
        "protein": 6,
        "carbs": 0.4,
        "fat": 5,
        "fiber": 0,
        "healthy": True
    },

    "Noodles": {
        "calories": 220,
        "protein": 7,
        "carbs": 43,
        "fat": 4,
        "fiber": 2,
        "healthy": False
    },

    "Bread": {
        "calories": 80,
        "protein": 3,
        "carbs": 15,
        "fat": 1,
        "fiber": 1,
        "healthy": False
    },

    "Carrot": {
        "calories": 25,
        "protein": 0.5,
        "carbs": 6,
        "fat": 0.1,
        "fiber": 2,
        "healthy": True
    },

    "Broccoli": {
        "calories": 30,
        "protein": 2.5,
        "carbs": 6,
        "fat": 0.3,
        "fiber": 2.4,
        "healthy": True
    },

    "Bell Pepper": {
        "calories": 24,
        "protein": 1,
        "carbs": 6,
        "fat": 0.2,
        "fiber": 2,
        "healthy": True
    },

    "Onion": {
        "calories": 22,
        "protein": 0.6,
        "carbs": 5,
        "fat": 0,
        "fiber": 1.2,
        "healthy": True
    },

    "French Fries": {
        "calories": 365,
        "protein": 4,
        "carbs": 48,
        "fat": 17,
        "fiber": 4,
        "healthy": False
    },

    "Pizza": {
        "calories": 285,
        "protein": 12,
        "carbs": 36,
        "fat": 10,
        "fiber": 2,
        "healthy": False
    },

    "Burger": {
        "calories": 354,
        "protein": 17,
        "carbs": 29,
        "fat": 18,
        "fiber": 2,
        "healthy": False
    }

}

# -----------------------------
# Nutrition Calculation
# -----------------------------

def calculate_nutrition(food_list):

    total = {
        "calories": 0,
        "protein": 0,
        "carbs": 0,
        "fat": 0,
        "fiber": 0
    }

    healthy = []
    less_healthy = []

    for food in food_list:

        for item in FOOD_DATABASE:

            if item.lower() in food.lower():

                values = FOOD_DATABASE[item]

                total["calories"] += values["calories"]
                total["protein"] += values["protein"]
                total["carbs"] += values["carbs"]
                total["fat"] += values["fat"]
                total["fiber"] += values["fiber"]

                if values["healthy"]:
                    healthy.append(item)
                else:
                    less_healthy.append(item)

    return {
        "calories": round(total["calories"]),
        "protein": round(total["protein"],1),
        "carbs": round(total["carbs"],1),
        "fat": round(total["fat"],1),
        "fiber": round(total["fiber"],1),
        "healthy_components": list(set(healthy)),
        "less_healthy_components": list(set(less_healthy))
    }

# -----------------------------
# NutriVision Score
# -----------------------------

def calculate_score(nutrition):

    score = 100

    if nutrition["fiber"] < 5:
        score -= 10

    if nutrition["protein"] < 20:
        score -= 10

    if nutrition["fat"] > 30:
        score -= 10

    if nutrition["calories"] > 800:
        score -= 15

    if len(nutrition["less_healthy_components"]) > 0:
        score -= len(nutrition["less_healthy_components"]) * 5

    score = max(score, 0)

    return score

# -----------------------------
# Final Analysis
# -----------------------------

def generate_report(food_list):

    nutrition = calculate_nutrition(food_list)

    nutrition["score"] = calculate_score(nutrition)

    return nutrition
