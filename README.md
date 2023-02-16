# Web App Readme

Looking for a fast and easy way to stay on top of the news? Our web app is the perfect tool for anyone who wants to quickly retrieve and analyze news articles related to their favorite topics.

Using our app is easy - simply select a topic of interest from our dropdown menu, click a button, and we'll retrieve the latest news articles related to your topic. We use the powerful NewsAPI to ensure that our news feeds are always up-to-date and relevant.

But that's just the beginning - our app goes beyond simple news retrieval by analyzing the retrieved articles using the OpenAI API. Our AI technology generates a summary of the articles, so you can quickly understand what's happening in the world without having to read through multiple articles.

With our app, you'll be able to stay informed and up-to-date on the news in just a few clicks. Whether you're a busy professional who doesn't have time to read through dozens of news articles, or just someone who wants to stay on top of the latest happenings in the world, our app is the perfect solution. Try it out today and see for yourself how easy and effective it is!






This is a web app that analyzes news using AI. It retrieves news articles based on a user-selected topic, and then performs analysis on the news content using IBM Watson and OpenAI APIs.

![App Screenshot](https://venturebeat.com/wp-content/uploads/2018/09/natural-language-processing-e1572968977211.jpg?fit=750%2C375&strip=all)

## Dependencies

This web app requires the following Python packages to be installed:

- pandas
- plotly
- streamlit
- newsapi
- dotenv
- json
- ibm_watson
- requests

## Installation

To install the required packages, run the following command in your terminal:

pip install -r requirements.txt

markdown
Copy code

You will also need to create a `.env` file in the root directory of the project and add the following variables:

- `NEWS_API_KEY`: API key for NewsAPI
- `OPENAI_API_KEY`: API key for OpenAI

## Usage

To run the web app, execute the following command in your terminal:

streamlit run app.py


You will be prompted to select a news topic from a dropdown menu. Once you select a topic, click the "Retrieve Data" button to retrieve news articles on that topic. The app will display the retrieved data in a table.

You can then click the "Analyze Data" button to perform AI analysis on the news content. The app will display the analyzed data in a table.

## Contributors

- [Diego Torres](https://github.com/pentius00)

## License

This project is licensed under the [MIT License](https://github.com/yourusername/web-app/blob/main/LICENSE).


Remember to replace yourusername with your GitHub username in the links to your profile and license file.
