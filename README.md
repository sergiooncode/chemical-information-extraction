# chemical-information-extraction

## Application design

- General approach

The application has been implemented taking an hexagonal architecture approach aimed at creating loosely
coupled application components. An example of having loose coupling is the use of data repositories which provide
an interface and an implementation following an Strategy pattern (https://en.wikipedia.org/wiki/Strategy_pattern).
Currently the implementtion is done using Mongo db through Mongoengine but it leaves the door open to switch to another
database/store by just implementing the interface. Follows a layered architecture
(https://dzone.com/articles/layered-architecture-is-good) in 4 layers:
User Interface > Application > Domain > Infrastructure which ensures dependency of layer only with the layer below.

- API

It exposes an endpoint `/v1/documents` taking POSTs to load documents into Mongo DB which actually parses
the patent document first and then persists it to db.

- Parallelization

The way the application has to parallelize extraction of entities from documents is by using batching.
In the `DistributeDocumentBatchesAppService` service the database is queried for documents that have the processed field set
to `False`, then spawns a number of processes(workers) equal to the constant `NUMBER_OF_DOCUMENT_PROCESSING_WORKERS`
(this constant should be lower than the max number of cores in the machine running the application),
then distributes the ids of the documents across the workers, each worker queries the documents of its batch, extracts
entities using using the call `pipe` for NER from spaCy and finally stores them together with the parsed document.

## How to run things

- Download chemical-information-extraction.bundle, cd into folder where it is and do
`git clone chemical-information-extraction.bundle chemical-information-extraction`
- Start the container `docker-compose -f docker-compose.dev.yml`
- Load a document in resources folder (part of repository):
    - Using an HTTP client like cUrl or HTTPIE do:
        - cUrl: `curl -vX POST http://localhost:5000/v1/documetns -d "text=@resources/US06182714B2.xml" --header "Content-Type: application/json"`
        - HTTPIE: `http --verbose http://localhost:5000/v1/documents text=@resources/US06182714B2.xml Content-Type:application/json`
- Process the loaded documents doing: `docker exec -it dev_chemical_extraction_backend flask documents process-batches`

    
## Other useful commands

- To access mongo DB: `docker run -it --network chemical-information-extraction_default --rm mongo mongo --host dev_mongo`


## Improvements

- Improve stability of the parsers (current parsers were tested on a small set of patent documents so they
could still be a bit brittle)
- Write tests
- Add API docs (swagger)
- Validate values result of parsing patent documents used when creating domain objects 
- Add authentication/authorization to the endpoints
- Replace multiprocessing for document batch processing with a multiprocessing setup using a distributed task queue 