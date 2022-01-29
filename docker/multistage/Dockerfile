FROM golang AS buildando

WORKDIR /app
COPY . .
RUN go build -o goexec
ENTRYPOINT ./goexec

FROM alpine
WORKDIR /app
COPY --from=buildando /app/goexec /app

ENTRYPOINT ./goexec