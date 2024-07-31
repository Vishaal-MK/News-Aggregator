# News Aggregator Application

## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [New Search Feature](#new-search-feature)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Building and Deploying as a Container](#building-and-deploying-as-a-container)

## Introduction

The News Aggregator Application is a Django-based web application that collects and displays news articles from various sources. Users can browse the latest news, filter by category, and share articles on social media.

## Features

- Aggregates news from multiple sources
- Displays news articles with images and titles
- Category filtering
- Share articles on social media
- Copy article URL to clipboard
- Report article functionality
- Dark mode toggle

## New Search Feature

We have added a new search functionality to enhance the user experience. Users can now search for news articles directly from the homepage.

### How to Use the Search Feature

1. On the homepage, locate the search bar at the top right corner of the navigation bar.
2. Enter your search query and press the "Search" button.
3. The search results will be displayed showing articles that match your search criteria.

### Code Implementation

1. **View**:
   In `views.py`, modify the home view function to handle the search logic:
   ```python

   def news_list(request):
    query = request.GET.get('query', '')

    if query:
        headlines = Headline.objects.filter(title__icontains=query)
    else:
        headlines = Headline.objects.all()[::-1]
    context = {
        "object_list": headlines,
    }
    return render(request, "news/home.html", context)
   ```

2. **Template**:
   Ensure the search form is included in `home.html` template:
   ```html
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <a class="navbar-brand" href="#">Search</a>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <form class="form-inline my-2 my-lg-0" action="{% url 'home' %}">
                <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search" name="query">
                <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
            </form>
        </div>
    </nav>
   ```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Vishaal-MK/News-Aggregator/tree/aggregator-search
   cd News-Aggregator/News-Aggregator
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

3. Run migrations:
   ```bash
   python manage.py migrate
   ```

4. Start the development server:
   ```bash
   python manage.py runserver
   ```
## Usage

- Visit `http://127.0.0.1:8000` to access the application.
- Use the dropdown menu to load news by category.
- Use the buttons to copy the article URL, report an article, or share on social media.
- Use the search bar to search for specific headlines or keywords

### Screenshots
![](https://github.com/Vishaal-MK/News-Aggregator/blob/aggregator-search/screenshots/breaking_light_mode.PNG)
![](https://github.com/Vishaal-MK/News-Aggregator/blob/aggregator-search/screenshots/sports_light_mode.PNG)
![](https://github.com/Vishaal-MK/News-Aggregator/blob/aggregator-search/screenshots/sports_search_mode.png)

## Building and Deploying as a Container

### Building the Docker Image

To build the Docker image, run the following command in the root directory of your project (where the `Dockerfile` is located):

```bash
docker build -t news-aggregator .
```

### Running the Docker Container

To run the Docker container, use the following command:

```bash
docker run -d -p 8000:8000 news-aggregator
```

### Deploying to AWS Lambda