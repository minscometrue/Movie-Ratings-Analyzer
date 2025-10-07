# 🎬 Movie Ratings Analyzer

A small data science project to scrape, analyze, and visualize movie rating data from IMDb using Python.

## 📌 Features

- Scrapes IMDb Top 250 movies using `requests` and `BeautifulSoup`
- Extracts key data: Title, Year, Rating
- Saves the data to CSV using `pandas`
- Visualizes trends and insights using `matplotlib`
- Modular project structure for easy expansion

## 🛠 Tech Stack

- Python 3
- pandas
- matplotlib
- BeautifulSoup
- requests

## 📦 Requirements

- `requests`: for making HTTP requests
- `beautifulsoup4`: for parsing HTML
- `pandas`: for data manipulation and analysis
- `matplotlib`: for data visualization

## 📁 Folder Structure

movie-ratings-analyzer/
├── data/ # CSV files
├── plots/ # Generated visualizations
├── imdb_scraper.py # Web scraping logic
├── analysis.py # Analysis & visualization
└── README.md # Project overview

## 🔍 How to Determine If a Web Page Is Static or Dynamic

Before starting web scraping, it's important to determine whether a page is **static** or **dynamic**.  
This helps you choose the right tools:  
- Use `requests` + `BeautifulSoup` for static pages  
- Use `Selenium` or `Playwright` for dynamic pages

### ✅ Simple Methods to Identify Static vs Dynamic Pages

1. **Disable JavaScript (DevTools Settings → Disable JavaScript)**
   - Refresh the page.  
   - If the data still appears → ✅ **Static**  
   - If the data disappears or shows "Loading..." → ❌ **Dynamic**

