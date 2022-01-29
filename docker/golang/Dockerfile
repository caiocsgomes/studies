FROM golang

WORKDIR /app
COPY . .
RUN go build -o goexec
ENTRYPOINT ./goexec