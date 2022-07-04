FROM python:3.9-alpine

# RUN apt-get install python3-dev python3-pip gcc -y
#RUN apk update && apk add python3-dev
#RUN apk add g++ gcc musl-dev libffi-dev openssl-dev

# Change work directory
WORKDIR /app

# Copy the application files into the image
COPY . .

# Crating user with limited lavrage to preventing any possible penetration
RUN addgroup -S app && adduser -S -G app app
USER app

# Define an Entrypoint
CMD ["python", "minimax.py"]
