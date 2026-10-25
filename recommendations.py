recommendations.py

Generates personalized nutrition recommendations
based on user's health goal and meal analysis.
"""

def generate_recommendations(goal, nutrition):

    recommendations = []

    score = nutrition["score"]

    calories = nutrition["calories"]
    protein = nutrition["protein"]
    carbs = nutrition["carbs"]
    fat = nutrition["fat"]
    fiber = nutrition["fiber"]

    # -----------------------------
    # General Advice
    # -----------------------------

    if score >= 85:
        recommendations.append(
            "✅ Excellent meal quality! Keep maintaining a balanced diet."
        )

    elif score >= 70:
        recommendations.append(
            "👍 Good meal overall. Small improvements can make it even healthier."
        )

    else:
        recommendations.append(
            "⚠️ This meal could be improved by increasing vegetables, fiber and lean protein."
        )

    # -----------------------------
    # Fiber
    # -----------------------------

    if fiber < 5:
        recommendations.append(
            "🥦 Increase fiber by adding vegetables, fruits, legumes or whole grains."
        )

    # -----------------------------
    # Protein
    # -----------------------------

    if protein < 20:
        recommendations.append(
            "🍗 Add a good protein source such as chicken, fish, eggs, beans or yogurt."
        )

    # -----------------------------
    # Calories
    # -----------------------------

    if calories > 800:
        recommendations.append(
            "🔥 This meal is relatively high in calories. Consider reducing portion size."
        )

    # -----------------------------
    # Fat
    # -----------------------------

    if fat > 30:
        recommendations.append(
            "🫒 Reduce fried foods and choose healthier cooking methods such as grilling or baking."
        )

    # -----------------------------
    # Goal-Based Recommendations
    # -----------------------------

    if goal == "Weight Loss":

        recommendations.extend([

            "🥗 Fill half of your plate with vegetables.",

            "🥛 Choose low-fat dairy products.",

            "🚶 Aim for at least 30 minutes of physical activity daily."

        ])

    elif goal == "Weight Gain":

        recommendations.extend([

            "🥜 Add healthy calorie-dense foods like nuts, seeds and avocado.",

            "🍌 Include nutritious snacks between meals.",

            "🥛 Increase protein intake throughout the day."

        ])

    elif goal == "Muscle Gain":

        recommendations.extend([

            "💪 Consume high-quality protein after exercise.",

            "🥚 Include eggs, chicken, fish or legumes in every meal.",

            "🏋️ Combine resistance training with adequate protein intake."

        ])

    elif goal == "Diabetes":

        recommendations.extend([

            "🌾 Prefer whole grains instead of refined carbohydrates.",

            "🥦 Increase non-starchy vegetables.",

            "🍬 Limit sugar-sweetened beverages and desserts."

        ])

    elif goal == "Hypertension":

        recommendations.extend([

            "🧂 Reduce sodium intake by limiting processed foods.",

            "🍌 Increase potassium-rich foods such as bananas and spinach.",

            "❤️ Choose healthy fats like olive oil and nuts."

        ])

    else:

        recommendations.extend([

            "💧 Drink adequate water throughout the day.",

            "🍎 Eat a variety of colorful fruits and vegetables.",

            "🏃 Stay physically active."

        ])

    return recommendations


# ---------------------------------------------------------
# Nutrition Explanation
# ---------------------------------------------------------

def explain_score(nutrition):

    score = nutrition["score"]

    explanation = []

    if score >= 90:

        explanation.append(
            "🌟 Outstanding nutritional quality."
        )

    elif score >= 75:

        explanation.append(
            "✅ Good nutritional balance with room for improvement."
        )

    elif score >= 60:

        explanation.append(
            "⚠️ Moderate nutritional quality."
        )

    else:

        explanation.append(
            "❌ Poor nutritional quality. Consider healthier food choices."
        )

    if nutrition["fiber"] < 5:
        explanation.append(
            "Low fiber content reduces the overall nutrition score."
        )

    if nutrition["protein"] < 20:
        explanation.append(
            "Protein intake is below the recommended level for a balanced meal."
        )

    if nutrition["fat"] > 30:
        explanation.append(
            "High fat content lowered the nutrition score."
        )

    if nutrition["calories"] > 800:
        explanation.append(
            "High calorie content reduced the overall score."
        )

    return explanation
