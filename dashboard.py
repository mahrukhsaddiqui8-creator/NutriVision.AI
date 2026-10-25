"""
dashboard.py

Interactive dashboard for NutriVision AI
"""

import plotly.graph_objects as go
import plotly.express as px
import streamlit as st


# ---------------------------------------------------
# Macronutrient Pie Chart
# ---------------------------------------------------

def show_macro_chart(nutrition):

    labels = ["Protein", "Carbohydrates", "Fat"]

    values = [
        nutrition["protein"],
        nutrition["carbs"],
        nutrition["fat"]
    ]

    fig = px.pie(
        values=values,
        names=labels,
        title="Macronutrient Distribution"
    )

    fig.update_traces(textposition="inside")
    fig.update_layout(height=420)

    st.plotly_chart(fig, use_container_width=True)


# ---------------------------------------------------
# Nutrition Score Gauge
# ---------------------------------------------------

def show_score_gauge(score):

    fig = go.Figure(go.Indicator(

        mode="gauge+number",

        value=score,

        title={
            "text": "NutriVision Score"
        },

        gauge={

            "axis": {
                "range": [0,100]
            },

            "bar": {
                "color":"green"
            },

            "steps":[

                {
                    "range":[0,40],
                    "color":"#ff4d4d"
                },

                {
                    "range":[40,70],
                    "color":"#ffd633"
                },

                {
                    "range":[70,100],
                    "color":"#66cc66"
                }

            ]
        }

    ))

    fig.update_layout(height=350)

    st.plotly_chart(fig, use_container_width=True)


# ---------------------------------------------------
# Healthy vs Less Healthy Foods
# ---------------------------------------------------

def show_food_quality(nutrition):

    healthy = len(nutrition["healthy_components"])

    unhealthy = len(nutrition["less_healthy_components"])

    fig = px.bar(

        x=["Healthy Foods","Less Healthy Foods"],

        y=[healthy, unhealthy],

        title="Meal Quality"

    )

    fig.update_layout(height=400)

    st.plotly_chart(fig, use_container_width=True)


# ---------------------------------------------------
# Nutrition Summary
# ---------------------------------------------------

def show_summary(nutrition):

    st.subheader("Nutrition Summary")

    c1,c2,c3 = st.columns(3)

    c1.metric(
        "Calories",
        f"{nutrition['calories']} kcal"
    )

    c2.metric(
        "Protein",
        f"{nutrition['protein']} g"
    )

    c3.metric(
        "Fiber",
        f"{nutrition['fiber']} g"
    )

    c1,c2 = st.columns(2)

    c1.metric(
        "Carbohydrates",
        f"{nutrition['carbs']} g"
    )

    c2.metric(
        "Fat",
        f"{nutrition['fat']} g"
    )


# ---------------------------------------------------
# Healthy Foods
# ---------------------------------------------------

def show_healthy_foods(nutrition):

    st.subheader("Healthy Components")

    if len(nutrition["healthy_components"]) == 0:

        st.info("No healthy foods detected.")

    else:

        for item in nutrition["healthy_components"]:

            st.success(item)


# ---------------------------------------------------
# Less Healthy Foods
# ---------------------------------------------------

def show_unhealthy_foods(nutrition):

    st.subheader("Less Healthy Components")

    if len(nutrition["less_healthy_components"]) == 0:

        st.success("No less healthy foods detected.")

    else:

        for item in nutrition["less_healthy_components"]:

            st.warning(item)


# ---------------------------------------------------
# Dashboard
# ---------------------------------------------------

def show_dashboard(nutrition):

    st.header("Nutrition Dashboard")

    show_summary(nutrition)

    st.divider()

    col1,col2 = st.columns(2)

    with col1:

        show_macro_chart(nutrition)

    with col2:

        show_score_gauge(
            nutrition["score"]
        )

    st.divider()

    show_food_quality(nutrition)

    st.divider()

    col1,col2 = st.columns(2)

    with col1:

        show_healthy_foods(nutrition)

    with col2:

        show_unhealthy_foods(nutrition)
