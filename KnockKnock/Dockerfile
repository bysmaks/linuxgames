FROM ubuntu:latest

RUN apt-get update && \
    apt-get install -y gnupg && \
    apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 3B4FE6ACC0B21F32 && \
    apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 871920D1991BC93C && \
    apt-get update

# Устанавливаем необходимые пакеты
RUN apt-get install -y knockd iptables netcat-traditional curl golang tcpdump 

COPY knockd.conf /etc/knockd.conf
COPY open_port.sh /usr/local/bin/open_port.sh

COPY banner.sh /etc/banner
COPY bash.bashrc /etc/
COPY entrypoint /etc/entrypoint

COPY main.go /usr/local/bin/server
COPY go.mod main.go /
RUN go mod download
RUN go build -o /usr/local/bin/server main.go
RUN rm /main.go /go.mod

RUN chmod +x /usr/local/bin/open_port.sh /usr/local/bin/server
RUN sed -i 's/START_KNOCKD=0/START_KNOCKD=1/' /etc/default/knockd

RUN chmod +x /etc/banner /etc/entrypoint

ENTRYPOINT ["/etc/entrypoint"]
