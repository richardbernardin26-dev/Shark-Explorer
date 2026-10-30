
import streamlit as st
import pandas as pd
import plotly.express as px

# To run:
# python -m streamlit run app.py

st.set_page_config(
    page_title="Shark Explorer",
    page_icon="🦈",
    layout="wide"
)

st.title("🦈 Shark Explorer")
st.header("Interactive Shark Species Database")
st.subheader("By Richard Bernardin")
st.write(
    "Explore shark species, learn about their characteristics, "
    "and compare their physical features using interactive charts."
)

st.divider()

# Sidebar: Upload data
st.sidebar.header("Shark Data")
st.sidebar.info(
    "Upload a CSV file containing shark species information, "
    "or use the default dataset."
)

uploaded_file = st.sidebar.file_uploader(
    "Upload a shark CSV file",
    type=["csv"]
)

# Load dataset
try:
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_csv("shark_data.csv")

except (FileNotFoundError, pd.errors.EmptyDataError):
    st.error(
        "Could not load shark_data.csv. "
        "Place the CSV file in the same folder as app.py."
    )
    st.stop()

# Required columns
required_columns = [
    "name",
    "scientific_name",
    "length_m",
    "weight_kg",
    "lifespan_years",
    "speed_kmh",
    "habitat",
    "appearance",
    "diet",
    "conservation_status"
]

missing_columns = [
    column for column in required_columns
    if column not in df.columns
]

if missing_columns:
    st.error(
        "Your CSV is missing these columns: "
        + ", ".join(missing_columns)
    )
    st.stop()

# Prepare data
df["name"] = df["name"].fillna("").astype(str)
df = df[df["name"].str.strip() != ""].copy()

numeric_columns = [
    "length_m",
    "weight_kg",
    "lifespan_years",
    "speed_kmh"
]

for column in numeric_columns:
    df[column] = pd.to_numeric(df[column], errors="coerce")

if df.empty:
    st.error("The dataset contains no valid shark records.")
    st.stop()

# Tabs
profiles, charts, data = st.tabs([
    "Shark Profiles",
    "Charts",
    "Data"
])

# ---------------------------------
# SHARK PROFILES
# ---------------------------------
with profiles:
    st.header("Explore a Shark Species")

    search = st.text_input(
        "Search for a shark by name",
        placeholder="Example: Great White"
    )

    names = sorted(df["name"].unique())

    if search.strip():
        matches = [
            name for name in names
            if search.strip().casefold() in name.casefold()
        ]
    else:
        matches = names

    if not matches:
        st.warning("No sharks match your search.")
    else:
        selected_shark = st.selectbox(
            "Select a shark",
            options=matches
        )

        shark = df[df["name"] == selected_shark].iloc[0]

        st.subheader(shark["name"])
        st.caption(shark["scientific_name"])

        # Optional shark image
        if "image_url" in df.columns:
            image_url = shark.get("image_url")

            if (
                pd.notna(image_url)
                and str(image_url).startswith("https://")
            ):
                st.image(image_url, width=450)

        # Display measurements
        col1, col2 = st.columns(2)

        def format_value(value, unit):
            if pd.isna(value):
                return "Not available"
            return f"{value:g} {unit}"

        col1.metric(
            "Maximum reported length",
            format_value(shark["length_m"], "m")
        )

        col2.metric(
            "Reported weight",
            format_value(shark["weight_kg"], "kg")
        )

        col1, col2 = st.columns(2)

        col1.metric(
            "Estimated lifespan",
            format_value(shark["lifespan_years"], "years")
        )

        col2.metric(
            "Reported speed",
            format_value(shark["speed_kmh"], "km/h")
        )

        st.subheader("Appearance")
        st.write(shark["appearance"])

        st.subheader("Habitat")
        st.write(shark["habitat"])

        st.subheader("Diet")
        st.write(shark["diet"])

        st.subheader("Conservation Status")
        st.write(shark["conservation_status"])

# ---------------------------------
# CHARTS
# ---------------------------------
with charts:
    st.header("Shark Data Visualization")

    st.write(
        "Use the charts below to compare shark species "
        "and explore differences in their physical characteristics."
    )

    # Bar chart
    st.subheader("Compare Shark Lengths")

    length_data = df.dropna(subset=["length_m"])

    if not length_data.empty:
        fig1 = px.bar(
            length_data,
            x="name",
            y="length_m",
            title="Maximum Reported Length by Shark Species",
            labels={
                "name": "Shark Species",
                "length_m": "Length (meters)"
            },
            hover_data=["scientific_name"]
        )

        st.plotly_chart(fig1, use_container_width=True)
    else:
        st.info("No length measurements are available.")

    # Scatter plot
    st.subheader("Length vs. Weight")

    comparison_data = df.dropna(
        subset=["length_m", "weight_kg"]
    )

    if not comparison_data.empty:
        fig2 = px.scatter(
            comparison_data,
            x="length_m",
            y="weight_kg",
            color="name",
            hover_name="scientific_name",
            title="Shark Length Compared with Weight",
            labels={
                "length_m": "Length (meters)",
                "weight_kg": "Weight (kilograms)",
                "name": "Shark Species"
            }
        )

        st.plotly_chart(fig2, use_container_width=True)
    else:
        st.info(
            "Add verified length and weight measurements "
            "to display the scatter plot."
        )

    # Select a measurement
    st.subheader("Explore a Measurement")

    parameter_options = {
        "Maximum Length (m)": "length_m",
        "Weight (kg)": "weight_kg",
        "Lifespan (years)": "lifespan_years",
        "Speed (km/h)": "speed_kmh"
    }

    selected_parameter = st.selectbox(
        "Choose a measurement",
        options=list(parameter_options.keys())
    )

    parameter = parameter_options[selected_parameter]

    chart_data = df.dropna(subset=[parameter])

    if not chart_data.empty:
        fig3 = px.bar(
            chart_data,
            x="name",
            y=parameter,
            title=f"{selected_parameter} by Shark Species",
            labels={
                "name": "Shark Species",
                parameter: selected_parameter
            }
        )

        st.plotly_chart(fig3, use_container_width=True)
    else:
        st.info(
            f"No data is available for {selected_parameter}."
        )

# ---------------------------------
# DATA
# ---------------------------------
with data:
    st.header("Shark Dataset")

    st.write(
        "Browse the original dataset and review descriptive "
        "statistics for the numerical measurements."
    )

    st.subheader("Raw Data")
    st.dataframe(df, use_container_width=True)

    st.subheader("Descriptive Statistics")
    st.dataframe(
        df[numeric_columns].describe(),
        use_container_width=True
    )

    st.subheader("Select Columns")

    selected_columns = st.multiselect(
        "Choose the columns to display",
        options=df.columns.tolist(),
        default=["name", "scientific_name", "length_m", "habitat"]
    )

    if selected_columns:
        st.dataframe(
            df[selected_columns],
            use_container_width=True
        )
    else:
        st.info("Select at least one column to display.")

st.divider()

st.caption(
    "Shark Explorer | Educational Data Visualization Project"
)

