# StyleGenius

**Overview:** StyleGenius is a Flask-based web application for fashion discovery. It allows users to search clothing items using natural language, explore categories, read fashion articles, and save favorite items. The app includes a basic AI-powered similarity comparison engine that matches user prompts with item descriptions and compares those results with popular platforms like Amazon and Pinterest.

---
## How to Build & Run the App

### Prerequisites

- Python 3.8+
- Flask
- Jinja2
- scikit-learn (for cosine similarity comparison)
- numpy

### Installation Steps

1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/stylegenius.git
   cd stylegenius
2. Set up a virtual environment:
- python3 -m venv venv
- source venv/bin/activate  # On Windows use venv\Scripts\activate
3. Run the flsk app:
- Python server.py

4. Open in browser:
- http://localhost:5000

### Running the Cosine Similarity Experiment

To replicate the similarity comparison experiment across platforms (e.g., your app vs Amazon vs H&M):

1. Make sure compare_recommendations.py and data.py are in the root directory.
2. Run the script: 
- python compare_recommendations.py
3. The file will print out similarity scores based on a set of prompts using cosine similarity and log the results

### External Software / Libraries Used
- Flask
- Bootstrap 5
- jQuery & jQuery UI
- scikit-learn

### Features
- Search by natural language or category
- Curated articles for fashion education
- Save favorites to revisit later
- Cosine similarity prompt evaluation engine

### Author
Mario Pauldon
Computer Science @ Columbia University
Email: marioipauldon@gmail.com
