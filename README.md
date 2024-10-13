## The Problem
Current weight-tracking apps are incompatible with less mainstream and uncommon foods, which makes it difficult to estimate the nutritional value of foods eaten at Penn State. While nutritional information is available on each Penn State menu, it’s tedious to record each value and inaccurate to estimate using other resembling foods, often leading to failure in reaching dietary goals. Eating properly is a crucial component of anyone’s health and well-being, and therefore finding nutritious meals should be as streamlined as possible. 

## The Solution
Macromate is a personalized application that both tabulates and records a user's eating habits while providing optimized macronutrient feedback, enabling users to meet their specified dietary goals in an intuitive way. Our team scrapes data from all 5 of University Park’s dining halls on a regular basis, storing nutritional data in our SQLite database. While our team members have all faced the tedious nature of tracking macros, we were compelled to develop this technology after watching a friend bring a food scale to the dining halls for more accurate macros. Our accessible technology allows a wider range of people to easily control what they eat and how they eat.

## Our Technology
For our backend, we implemented a web scraper using the BeautifulSoup Python library and used FastAPI to connect the scraped information and store it in a database. Our scraped information comes from the weekly dining hall menus given by Penn State. We used Streamlit to deploy a Web application and connected it with FastAPI, allowing for streamlined data querying and transferring from the backend to the frontend using SQLite and SQLAlchemy. There we implemented an OpenAI chatbot that, depending on your height, weight, goals, etc., generates a personalized daily meal plan. To promote scalability and accessibility, we also created an iOS application using Flutter that includes all the features implemented on the website onto the app. 

## Challenges and Solutions
This was our first hackathon experience, so we had to adapt to HackPSU’s fast-paced environment. One of the challenges was that most of our members had to quickly learn how to implement certain coding frameworks like FastAPI, SQLAlchemy, and Flutter. We got around this issue by having our most experienced team member help guide everyone through learning each of these frameworks. Everyone was engaged and determined to learn these foreign concepts quickly because they understood the dire nature of this contest, and so we mastered these frameworks incredibly quickly. Another challenge that came up was the issue of integrating all of the different aspects of our code into one seamlessly. Again, our most experienced coder handled most of this while the rest worked separately in their respective sectors (like website and database work).

## Achievements that we’re proud of
Our team is immensely proud of the application we developed within the 24-hour time constraint. We were able to finalize our product that is compatible with all Penn State dining halls and accounts for personal preferences such as allergies, dietary restrictions, unique individual macronutrient goals, etc. The results of our application function accurately and utilize an intuitive UI to support people of all needs.

## What we learned
As an all-freshmen team, we had to overcome a lot and learn to build this final product. We first had to come up with solutions to scrape the data from the PSU website and extract this data. We learned about Fast API and utilized this tool to scrape the data using Python. We then created a website in HTML, CSS, and JavaScript as the landing page for the product. Finally, we wanted to try new technologies such as Streamlit so we designed the main web app using this technology.

## Open-Source Technology Used
Streamlit, Flutter, Fast API, SQLite  
