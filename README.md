# Cloud-Test
Cloud test is a test driven development framework for microservice applications.

Before starting writing your microservices, you write your tests to this progrm and deploy them as an individual service. As the TDD approach, all your test should fail in the beginning. 

You start developing your microservices and as you deploy them, you rerun the tests and they start to turn green. Because this app is also deployed to your cluster, tests can act as a internal service that can do queries to internal endpoints.

When deploying a project to staging, you can also deploy this testing suite and define an endpoint to it's frontend. That way, your customers and colleagues can run the tests again through the interface and see the results themselves.


## Technologies
- Python -> v3.7.2
- Vue.js
- Nes.css

# Usage
- User functions are defined in System.py. This is SUT.
- Tests are defined in tests.py. This is the interface between Testing Suite and SUT. It is also the entry point of the program.
