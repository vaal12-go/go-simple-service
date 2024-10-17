FROM golang:1.22-alpine3.19
# Build image: docker build -t golang-simple-service-image .

LABEL version="1.0_17Oct2024"
LABEL description="This is a service image which is used \
    for compilation of linux executable for simple-service."


RUN apk add --no-cache git
RUN apk add --no-cache tzdata

WORKDIR /app
# root folder (with main.go) must be mounted to /app volume
VOLUME ["/app"]

#This will build simple-service executable in linux-artifacts folder
CMD go build -o linux-artifacts/simple-service .

