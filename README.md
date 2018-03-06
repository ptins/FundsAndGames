# It's All Funds and Games

This is a logistic regression project using Kickstarter data for CSE40647 - Data Science.

## Step 1 - Find An Interesting Application

- [ ] Is the PDF updated?

For the semester project, we decided to test how well a model could **classify** whether or not a Kickstarter campaign would be successful. In order to be deemed a success, the campaign needs to meet or exceed the crowd-sourced funding goal proposed by the initial project producer by a set deadline; anyone can contribute to the project as long as the campaign is still active. Each row in our dataset represents a unique project or campaign, followed by fifteen features; these include a project name, a short description, a few keywords, a financial goal in some currency, a project deadline and a number of backers contributing to the project. Combining **logistic regression** techniques with sentiment analysis-based clustering, we hope to deliver a model capable of predicting the binary final_status field, indicating project success (final_status=1) or project failure (final_status=0). 

## Step 2 - Find Available Datasets

- [ ] Is the PDF updated?

Initially, our team planned to build a web crawler to collect the necessary data from the Kickstarter website. However, upon browsing several Kaggle competitions, we found a prebuilt dataset that contained nearly all our features of interest. Readily available in this dataset are 108,129 project instances, each representing a unique, **real** project that was submitted between May 2009 and May 2015. Each row contains the following fourteen features: Project ID, Name, Description, Funding Goal, Keywords, Communication Status, Country, Currency, Deadline Date, State Change Date, Creation Date, Launch Date, Backer Count and finally, the target variable, Final Status.

Supplied by Kaggle are two data files: train.csv and test.csv. For the purpose of this project, we are only using train.csv. To see how we plan on splitting the data for model evaluation, see Step 9. 

The dataset we used can be found at <https://www.kaggle.com/codename007/funding-successful-projects/data>.

## Step 3 - Data Cleaning

- [ ] Is the code done?
- [ ] Is the PDF updated?


## Step 4 - Data Integration

- [ ] Is the code done?
- [ ] Is the PDF updated?

## Step 5 - Define A Data Mining Task

- [ ] Is the code done?
- [ ] Is the PDF updated?

## Step 6 - Task-Based Data Selection

- [ ] Is the code done?
- [ ] Is the PDF updated?

## Step 7 - Define A Formal Data Mining Problem

- [ ] Is the code done?
- [ ] Is the PDF updated?

## Step 8 - Develop The Model

- [ ] Is the code done?
- [ ] Is the PDF updated?

## Step 9 - Evaluation

- [ ] Is the code done?
- [ ] Is the PDF updated?