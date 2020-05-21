## Designing Microservices Architecture with Django Framework

This is only example to scalable django features based on microservices pattern. Does django with microservices is a good idea? **depends** on your perspective. Somewhat, django might very bloated or might be overkill (since django its batteries included) when it comes to microservices, another perspective is possible to go with microservices with django if you've got a good reason to do so like you have a large services and you know that you need to scale different components independently or you pretty sure that your database can't handle all that things. 

The models example based on Django polls tutorial in django documentation, but i managed it to separated into three services: `Polls`, `Vote` and `Choice`.

Another big different, microservice propose loosely coupled and contradicted against django with tightly coupled style.

## Trade-offs with Separated Database within Containers

Possibly, depending how many traffics or services (that you wanted to scale up) or at least depends on your customization some requirements or features. There's several pros and cons to get going with this pattern, if you got a problem with reusability or customizable - this pattern might come handy to you since you can also independently integrating with any frontend framework or database and also container has a high start-up speed of less than a second. While your data is more important, **maybe** you can replace it with another pattern like isolated db without docker or shared db

## Tools

- Docker
- nginx
- MongoDB
- Django REST Framework

## Issues

Currently, there's a several issue with this project. The big issue is, i don't know how to fetching the data between each service with another services. As Tom Christie said, you can use synchronous request-response in the API, so i didn't know that maybe i'll try it later.

## Getting Started

- Clone this repository
- change directory where `docker-compose.yaml` within folder
- Build with `docker-compose build`
- After build completed, run `docker-compose up -d` or without detached flag `docker-compose up`
- Navigate to localhost, something like `0.0.0.0:8001` for `Poll` API and so on