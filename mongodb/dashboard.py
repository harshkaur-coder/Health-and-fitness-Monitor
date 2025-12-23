
import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px

# =====================================
# STEP 1: LOAD CSV DATA
# =====================================
df = pd.read_csv(
    "C:/Users/harshdeep kaur/OneDrive/Desktop/mongodb/fitness_logs_50.csv"
)

# Convert date column to datetime
df["date"] = pd.to_datetime(df["date"])

# =====================================
# STEP 2: CREATE DASH APP
# =====================================
app = dash.Dash(__name__)

# =====================================
# STEP 3: DASHBOARD LAYOUT
# =====================================
app.layout = html.Div(
    style={"padding": "20px", "fontFamily": "Arial"},
    children=[

        html.H1(
            "🏥 Health & Fitness Monitor Dashboard",
            style={"textAlign": "center"}
        ),

        html.Hr(),

        # -------- GRAPH 1: LINE CHART --------
        dcc.Graph(
            figure=px.line(
                df,
                x="date",
                y="steps",
                color="user_id",
                title="Daily Steps Trend (Line Chart)"
            )
        ),

        # -------- GRAPH 2: BAR CHART --------
        dcc.Graph(
            figure=px.bar(
                df,
                x="user_id",
                y="calories",
                title="Calories Burned by Each User (Bar Chart)"
            )
        ),

        # -------- GRAPH 3: PIE CHART --------
        dcc.Graph(
            figure=px.pie(
                df,
                values="workout_minutes",
                names="user_id",
                title="Workout Time Distribution (Pie Chart)"
            )
        ),

        # -------- GRAPH 4: SCATTER PLOT --------
        dcc.Graph(
            figure=px.scatter(
                df,
                x="steps",
                y="calories",
                color="user_id",
                size="heart_rate",
                title="Steps vs Calories Burned (Scatter Plot)"
            )
        ),

        # -------- GRAPH 5: BOX PLOT --------
        dcc.Graph(
            figure=px.box(
                df,
                x="user_id",
                y="heart_rate",
                title="Heart Rate Variation by User (Box Plot)"
            )
        ),

        # -------- GRAPH 6: HISTOGRAM --------
        dcc.Graph(
            figure=px.histogram(
                df,
                x="steps",
                nbins=10,
                title="Steps Distribution (Histogram)"
            )
        )
    ]
)

# =====================================
# STEP 4: RUN DASH APP (UPDATED VERSION)
# =====================================
if __name__ == "__main__":
    app.run(debug=True)
