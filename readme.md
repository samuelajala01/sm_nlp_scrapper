# Social Media Sentiment Analysis Tool

A technical assessment task for internship

## Overview

A tool that analyzes public sentiment by scraping comments from social media platforms and processing them through a sentiment analysis model. The tool categorizes comments into positive, neutral, and negative sentiments, providing insights into public opinion on specific topics.

## Features

- 🔍 Scrapes comments from multiple social media platforms
- 📊 Performs sentiment analysis using a HuggingFace's RoBERTa model
- 📈 Categorizes sentiments (Positive, Neutral, Negative)
- 📑 Exports results to Excel for easy analysis
- ⚡ Processes up to 100 comments per sentiment category(original task, might expand later)

## Data Sources

Currently supported platforms:

- Nairaland
- Reddit

## Prerequisites

- Python 3.7 or higher
- A Hugging Face API token
- Reddit API tokens
- Internet connection for web scraping

## Installation

1. Clone the repository

```bash
git clone https://github.com/samuelajala01/sm_nlp_scrapper.git
cd sm_nlp_scrapper
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Set up environment variables

- Create a `.env` file in the project root
- Add your Hugging Face API token:

```
HF_BEARER_TOKEN=your_token_here
REDDIT_CLIENT_ID=your_token_here
REDDIT_CLIENT_SECRET=your_client_secret
```

## Usage

1. Run the web scraper to collect comments from Nairaland:

```bash
python nairaland_scraper.py
```

2. Run the web scraper to collect comments from Nairaland:

```bash
python reddit_scraper.py
```

3. Perform Data Cleaning on the collected comments

4. Run the sentiment analysis model:

```bash
python sentiment_model.py
```

## Output

The tool generates an Excel file (`model_output.xlsx`) containing:

- Original comments
- Sentiment classifications
- Up to 100 comments per sentiment category

## Project Structure

```
├── nairaland_scraper.py   # Nairaland Web scraping script
├── reddit_scraper.py      # Reddit Web scraping script
├── sentiment_model.py     # Sentiment analysis model
├── model_input.xlsx       # scrapped comments to be fed to model
├── model_output.xlsx      # model output after analysis
├── requirements.txt       # Project dependencies
├── .gitignore             # git ginore file
└── .env                   # Environment variables
```

## Limitations

- Maximum of 100 comments per sentiment category
- Requires a stable internet connection
- Rate limiting may apply for web scraping
- Huggingface API usage is limited.
- The model is unable to process very long comments
