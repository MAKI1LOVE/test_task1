# test_task1

## Dependencies
* docker-compose

## Build
* `docker-compose up`

## Test
Open terminal and run twice:

`curl -X POST http://127.0.0.1:8080/api/question -H 'Content-Type: application/json' -d '{"questions_num": 1}'` 

First response will be null. Second response will be last added question.
