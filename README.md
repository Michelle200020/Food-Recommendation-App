# Food-Recommendation-App


## PROJECT OVERVIEW

The Nutrition App is a Django-based web application designed to help users explore nutritional information for various foods. The app offers a range of features, including data loading and exploration, data profiling, descriptive statistics, interactive visualizations, data export functionality, and personalized food recommendations based on user input.

## STEP-BY-STEP GUIDE ON HOW TO RUN THE PROJECT

Prerequisites
- Python installed on your system
- Django framework installed (`pip install Django`)
- Required libraries (`pip install pandas ydata-profiling seaborn matplotlib plotly scikit-learn`)

Steps (Using Git)
1. Clone the project repository from GitHub
   git clone <repository_url>
   cd <project_directory>
 
2.  Install the required Python packages.
     pip install -r requirements.txt

3. Run the Django development server.
   python manage.py runserver

4. Open your web browser and go to [http://localhost:8000/] (http://localhost:8000/) to access the Nutrition App.

Steps (Using Django)

1.  Download the project files from the repository.

2. Navigate to Project Directory
   - Open a terminal or command prompt.
   - Navigate to the directory where you downloaded the project files using the `cd` command.
     cd path/to/project_directory

3. Create a Virtual Environment (Optional but Recommended)
   - It's recommended to use a virtual environment to isolate the project dependencies.
     python -m venv venv

4.  Activate Virtual Environment:
   - Activate the virtual environment.
   - On Windows
        venv\Scripts\activate 

5.  Install Project Dependencies:
   - Install the required Python packages.
     pip install -r requirements.txt


6. Run Migrations
   - Apply database migrations to set up the database.
     python manage.py migrate

7. Run the Django Development Server
   - Start the Django development server
     python manage.py runserver

8.  Access the App
   - Open your web browser and go to [http://localhost:8000/](http://localhost:8000/) to access the Nutrition App.






## USAGE GUIDELINES

### Data Tab

Navigate to the "Data" tab to explore the dataset.
View the first and last ten rows of the dataset.
Get insights into each column, including data types, non-null counts, and null counts.

### Profile View:

Access the "Profile" view to generate a comprehensive profile report for the dataset.
Save and review the report in HTML format.

### Descriptive Statistics Tab:

Go to the "Descriptive Statistics" tab to view statistics like mean, standard deviation, min, max, etc., for numerical columns.
Understand the central tendencies and variability of the dataset.

### Box Plot:

Explore the "Box Plot" feature to visualize the distribution of a numerical variable within different categories.
Customize the box plot by selecting a category and a numerical value.
Validate your selections to avoid errors.

### Exploratory Data Analysis Tab:

Visit the "Exploratory Data Analysis" tab for a suite of visualizations:
Histograms: Explore the distribution of a numerical feature.
Box Plots: Visualize the spread of data within categories.
Scatter Plots: Analyze relationships between two numerical features.
Pie Charts: Understand the composition of categorical data.
Customize each visualization by selecting features and adjusting parameters.
Validate your selections to ensure they exist in the dataset.

### Export to CSV/Excel:

Use the "Export to CSV" and "Export to Excel" features to download the loaded dataset in your preferred format.

### Recommend Food:

Head to the "Recommend Food" section to receive personalized food recommendations based on your nutritional preferences.
Input desired values for calories, protein, carbs, and fats.
Review the top 5 recommended foods based on cosine similarity scores.

