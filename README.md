# Ancient Battles

Two leaders go in, one leader comes out. Which pictured leader won the battle?

React / Redux / NodeJS / Scrapy / Celery

Using Wikipedia battle entries, this app pulls a collection of battles that have all of the required details to be featured. It then shows the user just the pictures and names of the leaders of each side in the conflict. The user can request more details, such as year, and location of the battle, but must otherwise choose one leader that they think won the particular battle. They are told whether they were correct or not, and then can try again with a new battle.

## Setup for Development

### Run Backend with Docker

Copy the `.env.SAMPLE` file and rename it `.env`.

Set your POSTGRES_USER and POSTGRES_PASSWORD variables in the `docker-compose.yml` file.

In the `.env` file, update the DATABASE_URI variable by adding the Username and Password.

Bring up the site with:
`docker-compose up`

### Frontend

Start up the development server
`cd ui && npm start`

### Database

To initialize the database, run the docker-compose and enter the flask container:
`docker ps`
`docker exec -it CONTAINER_ID sh`
`flask db upgrade`

If you want to start a clean db with no migrations, delete the migrations folder and run:
`flask db init`

If you need to make changes to the database (add or update db classes) then run:
`flask db migrate -m "Some message."`
`flask db upgrade`

To wipe the database, first take down the postgres container, then run:
`docker ps -a` - get the postgres container ID
`docker rm POSTGRES_CONTAINER_ID`
`docker volume ls` - get the pgdata volume name
`docker volume rm PGDATA_VOLUME_NAME`
Then clear the contents of the migrations folder.

### Scraper

Scrape to a CSV with
`cd src/scraper/scraper`
`scrapy crawl -o battles.csv wikispider`

## Deployment Steps

ui process.env.REACT_APP_PROD_API_URL

## Tasks

- data clean up - 0.5 hr
- more battles - 1 hr
- deploy - 0.5 hr

-- MVP (2 hr)

- needs time to complete
  Battles should be broken up into sections
  Players select which "War" or Period they want to get battles from, rather than just totally random battles

* testing (1 hr)
* scraping (.5 hr)
* celery job (0.5 hr)
* react - api (0.5 hr)
* redux (2 hr)
* local storage (1 hr)
* build react + uwsgi (2 hr)
* host on heroku (0.5 hr)

- CICD
- add reporting bad matches
- logger output to file
- backend tests
- automated testing with git connect
- configure web crawler
- configure task runner
- score card (see how wordle does it)
- local storage to track seen battles
- vector graphic for VS icon
- VS icon between leaders
- Report button for battles with incorrect information (or displayed improperly)
- battles are ordered, new players start at a random place in the order
- can shuffle DB by adding an order column

Issues:

- Belligerent detection can be improved.

https://github.com/AlecJ/ancient-battles
