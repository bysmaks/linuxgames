FROM ubuntu:latest as builder

COPY bash.bashrc /etc/
COPY banner.sh /etc/banner
COPY entrypoint /etc/entrypoint
COPY dontdelete /root/dontdelete
COPY main /root/main

RUN chmod +x /root/main
RUN chmod +x /etc/entrypoint /etc/banner

WORKDIR /root

ENTRYPOINT ["/etc/entrypoint"]
