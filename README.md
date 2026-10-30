# Shark-Explorer
Interactive shark data explorer built with Python, Streamlit, and Plotly.
# 🦈 Shark Explorer – Interactive Shark Database

Shark Explorer is an interactive web application developed using Python and Streamlit. The purpose of this project is to allow users to explore different shark species, learn about their physical characteristics, and compare biological measurements through interactive data visualizations.

Users can search for a shark by name, select a species from a dropdown menu, and view information such as scientific name, length, weight, lifespan, swimming speed, habitat, appearance, diet, and conservation status.

The application also uses Plotly to create interactive charts that help users compare different shark species and explore patterns in the dataset.

# Project Objectives

- Develop an interactive web application using Streamlit.
- Display and analyze shark species information using Pandas.
- Allow users to search for and select different shark species.
- Create interactive data visualizations using Plotly.
- Practice Agile software development and project management techniques.
- Deploy a functional application that can be accessed through a public URL.

# Features

# 1. Shark Profiles
- Search for shark species by name.
- Select a shark from a dropdown menu.
- View scientific names and biological characteristics.
- Explore habitat, appearance, diet, and conservation status.
- Display shark images when image URLs are available.

# 2. Data Visualization
- Interactive bar chart comparing the reported maximum lengths of shark species.
- Scatter plot comparing shark length and weight.
- Select different measurements, including length, weight, lifespan, and speed, to generate comparison charts.

# 3. Shark Dataset
- Display the original shark dataset.
- View descriptive statistics for numerical measurements.
- Select specific columns to display.
- Upload a different shark CSV file through the sidebar.

# Dataset

The application uses a CSV file named `shark_data.csv`, containing information about 18 different shark species.

The dataset includes the following information:

| Column | Description |
|---|---|
| name | Common shark name |
| scientific_name | Scientific species name |
| length_m | Approximate maximum reported length in meters |
| weight_kg | Weight in kilograms |
| lifespan_years | Estimated lifespan in years |
| speed_kmh | Swimming speed in kilometers per hour |
| habitat | Typical marine environment |
| appearance | Physical characteristics |
| diet | Typical food sources |
| conservation_status | Conservation classification |
| measurement_note | Notes about the reliability and interpretation of measurements |

Some numerical fields are intentionally left blank when reliable species-specific measurements have not been verified. Missing values are not treated as zero.

The dataset can be expanded as additional verified information becomes available.

# Data Sources

The following resources can be used to research and verify shark species information:

- [NOAA Fisheries](https://www.fisheries.noaa.gov/fish-sharks)
- [Sharkipedia](https://www.sharkipedia.org/)
- [Sharkipedia Data Export](https://www.sharkipedia.org/data_export)

# Technologies Used

- **Python:** Main programming language.
- **Streamlit:** Development of the interactive web application.
- **Pandas:** Data manipulation and analysis.
- **Plotly Express:** Interactive charts and data visualization.
- **PyCharm:** Integrated development environment (IDE).
- **GitHub:** Version control and project hosting.
- **Streamlit Community Cloud:** Public application deployment.

# Installation and Setup

Follow these instructions to run Shark Explorer locally.

# 1. Clone the Repository

Clone the GitHub repository to your computer:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

# 2. Open the Project

Open the downloaded project folder in PyCharm.

# 3. Install Dependencies

Open the PyCharm terminal and run:

```bash
python -m pip install -r requirements.txt
```

# 4. Verify Project Files

Make sure the following files are in the project directory:

```text
SharkExplorer/
├── app.py
├── shark_data.csv
├── requirements.txt
├── README.md
└── .gitignore
```

# 5. Run the Application

In the PyCharm terminal, execute:

```bash
python -m streamlit run app.py
```

Streamlit will launch the application in your default web browser.

# Agile Software Development

This project follows Agile software development practices to organize tasks, manage development, and improve the application incrementally.

The development process includes:

- **Product Backlog:** Identify and prioritize application features and requirements.
- **Sprint Planning:** Organize development tasks into manageable stages.
- **Incremental Development:** Build the application one feature at a time, including data loading, search functionality, and visualizations.
- **Testing:** Test application functionality, user inputs, CSV uploads, and data visualizations.
- **Sprint Review:** Evaluate completed features and identify areas for improvement.
- **Sprint Retrospective:** Reflect on the development process and determine improvements for future development.

# Future Improvements

Potential improvements for future versions include:

- Integrating external APIs for additional shark information.
- Adding interactive maps to display shark habitats and geographic distributions.
- Including more shark species and verified biological measurements.
- Improving the visual design and user experience.
- Adding AI-powered features to answer questions about shark species.

# Project Links

*GitHub Repository: https://github.com/richardbernardin26-dev/Shark-Explorer

*Live Streamlit Application: https://shark-explorer-uk7se6u2c869tfparr4ygp.streamlit.app/

# Author
Richard Bernardin

Developed as part of CIS 3590 – Internship-Ready Software Development.
