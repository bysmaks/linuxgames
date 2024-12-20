FROM ubuntu:latest as builder

COPY bash.bashrc /etc/
COPY banner.sh /etc/banner
COPY entrypoint /etc/entrypoint
COPY dontdelete /root/dontdelete
COPY main /root/main

RUN chmod +x /root/main
RUN chmod +x /etc/entrypoint /etc/banner
RUN mv /bin/kill /bin/wgett

WORKDIR /root

ENTRYPOINT ["/etc/entrypoint"]
