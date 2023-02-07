# Introduction 
This python project is about a data pipeline that is able to process data coming from the vehicles.
The scope of the data is the GPS position of all the vehicles in a fleet that are collected during the operating periods.
The purpose is to process these data faster, efficiently and in scale and this is a reason to divide these data in chunks.
The chunks concept is applied for the number of files and for the rows of the JSON files, and it provides several
advantages:
1. Scalability: while the pipeline read a chunk, it can load and transform another one
2. Fast processing: no need to load every row in memory, but only a bunch of them and this avoids to have memory overflow
3. Fail soon: this can be seen also related to the fast processing, because the pipeline would fail sooner by loading
only a bunch of records in memory
4. Maintainable: it can work for large dataset by just setting up the chunk size (both for leveraging the number of 
files and the json documents)

# Project structure
It is organized in python modules.
### utilities
Are separated from the core code of the pipeline: src/app/utils.py
### database
Functions required for Database connection and to execute queries: src/database/* 

Schema of the tables : door2door-schema.sql
SQL script that creates three tables in a MySQL database named "door2door".

The first table named "events" has the following columns: id, file, event, on_event, at_event and organization_id. The "id" column is set as the primary key and is unique and not null.

The second table named "vehicles" has the following columns: id_event, id_vehicle, lat, lng and at_vehicle. The "id_event" column is set as a foreign key referencing the "id" column in the "events" table.

The third table named "operating_period" has the following columns: id_event, id_operating, start, finish and on_finish. The "id_event" column is set as a foreign key referencing the "id" column in the "events" table

These commands create the structure of the database and the relationships between the tables, so that data can be inserted and queried in a logical and consistent way.
### core of the pipeline
1. src/app/etl.py: Pipeline object to execute the extraction of the JSON rows, transform them and loading into a DB
2. src/app/data_extraction_from_files.py: Functions to extract the JSON rows in chunks
3. src/app/transformation_db.py : processing the daa by generating an event_id , matching a specific row within the 
set of the events [events on vehicle, events on operating_period]

### Dockerfile
This contains the code to build a docker image that will be linked to a container. \
It basically inherits from mysql/mysql-server image. Then we need to set env variables to run the mysql server in a container.  
```MYSQL_DATABASE``` : database name, please mind your door2door-schema.sql file 

```MYSQL_ROOT_PASSWORD``` : it's required to access mysql server via your app or via your mysql client.

## Requirements
1. Python = 3.8.10
2. Pip == 23.0

## Installation and run
1. Cloning the repository
```git clone  https://github.com/simone-agliano-dev/data-engineering-pipeline```

2. Run your Docker container to have a mysql server, mind to cd in the root of this project 

>docker build -t <image-name>:latest . 
> 
>docker run -dp --net=host --name=mysql_container <image-name> //you  do not need --net=host if you run it in a different host
>
> To check whether your container is running: docker ps (it should be healthy and running)

3. Run the pipeline
> python src/main.py
4. Test whether you tables in your databases are filled with the right data
> Install mysql client : sudo apt-get install mysql 
> 
> mysql -h 127.0.0.1 -uroot -p
> Use door2door
> SELECT * FROM events

## Improvements
This pipeline is only working with json files, it might require additional changes to ingest other data-sources.
In addition, the pipeline can be dockerized too, and we might have two containers (one for the ETL pipeline and
another one for the mysql server container).




