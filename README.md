# Historic Battles
Two leaders go in, one leader comes out. Which pictured leader won the battle?

Flask App with VueJS Front End

Python Scrapy package used for scraping wikipedia
Celery used to automate scraping job and populate DB with cached battles


## Features
Using Wikipedia battle entries, this app pulls a collection of battles that have all of the required details to be featured. It then shows the user just the pictures and names of the leaders of each side in the conflict. The user can request more details, such as year, and location of the battle, but must otherwise choose one leader that they think won the particular battle. They are told whether they were correct or not, and then can try again with a new battle.

## To Run
First create a `.env` file in the base directory and include the following fields:

Bring up the site with:
`docker-compose up`

## Database


## To Do
* move results div up (hidden under leader pics)
* guess scrolls hints and buttons down
* guess scrolls in from top answer, link to wikipedia page, and NEXT button
* use SCSS
* python scraping
* standardize data
* python API
* tests
* Vue JS to get battle
* tests
* celery task for scraping
* Report button for battles with incorrect information (or displayed improperly)
* host on Heroku