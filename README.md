# Food-Recommendation-App


## PROJECT PURPOSE AND GOALS
The purpose of the project is to create a Nutrition App that empowers users to explore nutritional information for various foods. The primary goals include providing a user-friendly interface for visualizing and analysing data related to food ingredients, offering descriptive statistics, and enabling users to export data in CSV or Excel formats. Additionally, the app aims to provide personalized food recommendations based on user input.

Dataset Description - A comprehensive dataset about common food ingredients that are used in cooking. It contains the quantity, calories and macronutrients. The ingredients are also classified into Categories.

1. Food: This column will carry the name of all the data, simply to have unique names for each ingredient, it is used as an identifier.
2. Grams: Used to indicate the amount of the given ingredient being used for the calculations, it is the main measuring criteria.
3. Calories: It contains the info on the amount of energy contained in the gram quantity of the given ingredient.
4. Protein: Used to indicate the amount protein content in the specified gram quantity of the ingredient, it is necessary for tissue repair and growth.
5. Fats: The amount of fat content present in the ingredient in the specified gram quantity, it is essential for fatty acids and also energy.
6. Saturated Fats: The amount of saturated fat in the ingredient, it isn’t the same as fats as it is mostly considered in heart health.
7. Fiber: It contains the amount of fiber in an ingredient per gram, fiber is present in most
plant based food and is important for digestive health.
8. Carbs: It is the amount of carbohydrates present in the ingredient, carbohydrates and the most important part for energy gain for the body.
9. Category: It is used to separate the food items into separate types, multiple ingredient can come under a single category.

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






## DOCUMENTATION ON DATA ANALYTICS METHODS USED

1. Data Loading and Exploration 
The app uses the `pandas` library to load a CSV file containing cleaned food ingredient data. It displays the first and last ten rows of the dataset, providing users with a quick overview of the data. Furthermore, the app generates a table with information about each column, including data type, non-null count, and null count.

2. Data Profiling 
To gain a comprehensive understanding of the dataset, the app leverages the `ydata_profiling` library to create a detailed profile report. The report includes key statistics, distribution visualizations, and insights about the dataset's structure. The generated report is saved as an HTML file and presented to the user.

3. Descriptive Statistics 
Utilizing the `describe` method in `pandas`, the app calculates descriptive statistics for numerical columns in the dataset. The computed statistics, such as mean, standard deviation, minimum, maximum, and quartiles, are then rendered in an HTML table, providing users with a summary of the dataset's central tendencies and variability.

4. Box Plot Visualization 
The app creates an interactive box plot using the `plotly` library, allowing users to explore the distribution of a numerical variable within different categories. Users can customize the box plot by selecting a category and a numerical value. The app validates user input to ensure the selected features exist in the dataset, providing a robust and user-friendly visualization tool.

5. Exploratory Data Analysis 
This view offers a suite of visualizations, including histograms, box plots, scatter plots, and pie charts, powered by the `plotly` library. Users can customize the visualizations by selecting features and adjusting parameters. The app validates user input to ensure the selected features exist in the dataset, providing a dynamic and interactive exploration experience.

6. Data Export 
The app provides users with the ability to export the loaded dataset to CSV or Excel format. Leveraging `pandas` capabilities, the app generates the corresponding file format and returns it as a downloadable file, offering users flexibility in working with the data.

7. Food Recommendation 
The recommendation system in the app employs the cosine similarity metric from the `scikit-learn` library. Based on user input for desired calories, protein, carbs, and fats, the app calculates the cosine similarity between the user's input vector and the food dataset. The top 5 foods with the highest similarity scores are then recommended to the user, providing a personalized and data-driven suggestion.
Cosine similarity is a metric used to measure the similarity between two vectors in a multi-dimensional space. It calculates the cosine of the angle between the vectors, providing a measure of their orientation rather than their magnitude. The resulting similarity score ranges from -1 (completely dissimilar) to 1 (completely similar), with 0 indicating orthogonality.
How the Project Uses Cosine Similarity:
1.	User Input: The project takes user input for desired nutritional values, such as calories, protein, carbs, and fats.
2.	User Vector: The input is then converted into a vector, creating a representation of the user's nutritional preferences.
3.	Food Matrix: The nutritional profiles of all food items in the dataset are organized into a matrix, where each row corresponds to a food item, and each column represents a nutritional attribute.
4.	Cosine Similarity Calculation: The cosine similarity is calculated between the user vector and each food vector in the matrix, generating        similarity scores.
5.	Recommendation: The top N food items with the highest similarity scores are recommended to the user, suggesting foods that align closely with their specified nutritional preferences.

