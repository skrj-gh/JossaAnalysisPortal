

# JOSAA Analysis Portal

The JOSAA Analysis Portal is a web-based application designed to analyze, visualize, and predict seat allocations in Indian Institutes of Technology (IITs) and other participating institutions based on historical data. This project is divided into three phases: Data Scraping and Cleaning, Data Visualization, and Backend Integration with Django.

## Table of Contents

1. [Project Overview](#project-overview)
2. [Phase 1: Data Scraping and Cleaning](#phase-1-data-scraping-and-cleaning)
3. [Phase 1½: Data Analysis and Visualization](#phase-1½-data-analysis-and-visualization)
4. [Phase 2: Web Integration and Backend with Django](#phase-2-web-integration-and-backend-with-django)
5. [Project Setup](#project-setup)
6. [Running the Project](#running-the-project)
7. [Screenshots](#screenshots)
8. [Video Demonstration](#video-demonstration)

## Project Overview

The project aims to provide insights and predictions on seat allocations for various engineering institutions under the JOSAA framework. It involves:

- **Phase 1**: Scraping and cleaning data using Beautiful Soup, NumPy, and Pandas. (The final scraping file is in the directory `web_Scrapping_josaa`)
- **Phase 1½**: Conducting Exploratory Data Analysis (EDA) and creating visualizations.
- **Phase 2**: Developing a backend with Django to process queries, manage the database, and display visualizations on a web page.

## Phase 1: Data Scraping and Cleaning

### Technologies Used

- **HTML & CSS**: For basic web page structure and styling.
- **Beautiful Soup**: For scraping data from web pages.
- **NumPy**: For efficient numerical operations on data.
- **Pandas**: For data manipulation and analysis.

### Resources

- [HTML Tutorial](https://www.w3schools.com/html/)
- [CSS Tutorial](https://www.w3schools.com/css/default.asp)
- [Beautiful Soup Video](https://youtu.be/XVv6mJpFOb0)
- [NumPy Tutorials](https://cs231n.github.io/python-numpy-tutorial/)
- [Pandas Playlist](https://www.youtube.com/playlist?list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y)

## Phase 1½: Data Analysis and Visualization

### Technologies Used

- **Exploratory Data Analysis (EDA)**: To understand and explore the data.
- **Data Visualization**: Using Matplotlib and Seaborn for creating plots and graphs.

### Resources

- [EDA Introduction](https://youtu.be/xi0vhXFPegw)
- [Matplotlib Tutorial](https://youtube.com/playlist?list=PL-osiE80TeTvipOqomVEeZ1HRrcEvtZB_)

## Phase 2: Web Integration and Backend with Django

### Technologies Used

- **Django**: For backend development, managing the database, and handling web requests.
- **SQLite**: The database engine used for this project.

### Resources

- [Django Playlist by Corey Schafer](https://www.youtube.com/playlist?list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p)
- [Django Documentation on Queries](https://docs.djangoproject.com/en/4.2/topics/db/queries/)

## Project Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/josaa-analysis-portal.git
   cd josaa-analysis-portal
   ```

2. **Create and Activate Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```

3. **Install Python setuptools**:
   ```bash
   pip install setuptools
   ```

4. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Apply Migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

## Running the Project

To run the project locally, use the following command:
```bash
python manage.py runserver
```
Navigate to `http://127.0.0.1:8000/` in your web browser to access the application.

## Screenshots

![image](https://github.com/skrj-gh/JossaAnalysisPortal/assets/133494008/fa97927b-2404-4076-9fdf-a9975351d182)
![image](https://github.com/skrj-gh/JossaAnalysisPortal/assets/133494008/044f2e14-6fe4-48f2-a0c7-a01f77724518)
![image](https://github.com/skrj-gh/JossaAnalysisPortal/assets/133494008/fd1291e6-3ed7-441d-bd66-8eb517ade81b)
![image](https://github.com/skrj-gh/JossaAnalysisPortal/assets/133494008/36334cb1-d1d0-4de7-bda0-30ac55e2ff86)

## Video Demonstration

For a detailed walkthrough, watch the deployment video [here](https://youtu.be/aAf-nz4-P-s) (<--youtube video on deployment):


https://github.com/skrj-gh/JossaAnalysisPortal/assets/133494008/dda2713e-5675-46b0-ad63-bedb3afb480a



---

