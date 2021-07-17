# Fabnacci API

## Requirements
1. An endpoint that returns the value from the Fibonacci sequence for a given number.
2. An endpoint that returns a list of numbers and the corresponding values from the Fibonacci sequence from 1 to N with support for pagination. Page size should be parameterized with a default of 100.
3. An endpoint to blacklist a number to permanently stop it from being shown in Fibonacci results when requested. The blacklisted numbers should persist in application state.
4. An endpoint to remove a number from the blacklist.

## Summary
1. Requirement 1, 3 and 4 are implemented in about 4 hours. Pagination is added to the Fibonacci endpoint.
2. Requirement 2 is skipped. Firsly, I ran out of time as the assignment is expected to be finished in 4 hours. Secondly, it's not cristal clear what is expected with this API, especially the pagination part. It would be nice to have an example of response when N=10 with page size being 10 to help me fully understand the requirement.
3. The solution is only for dev/demo purpose. When Flask framework runs in dev mode, requests are handled one-by-one, i.e. no concurrency concerns. 
4. In production, the service could be deployed in any hosting solutions that Flask supports, e.g. AWS Beanstalk. We must use a proper cache solution, e.g. redis, to replace the global variable cache. API must support authentication and the blacklist is very likely user account specific. Furthermore, the service can pre populate very long Fibonacci sequence to the cache as part of the service warm up. 
5. Regarding optimizating the service for memory, cpu, time and network, there is a bit of using cache to save cpu, to reduce response time. More optimization is only applicalbe in a staging environment and a specification, e.g. response time P99 is less than 20ms etc; support peak 100 request per second etc.

## Setup
+ OS: Windows 10
+ Editor: Visual Studio Code
+ Browser: Chrome
+ Python: V3.9.2
+ Flask: V1.1.4
+ Flask-restx: V0.4.0

## Quick Instructions
### Start RESTAPI 
    python ./main.py
### RESTAPI URL
    http://localhost:5000/
### Start Unit Test
    python ./test.py
                

