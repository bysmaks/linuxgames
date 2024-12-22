FROM ubuntu:latest

COPY bash.bashrc /etc/
COPY banner.sh /etc/banner
COPY entrypoint /etc/entrypoint
COPY ./challenge /root/challenge

RUN chmod +x /etc/entrypoint /etc/banner
RUN mv /bin/kill /bin/wgett

WORKDIR /root

ENTRYPOINT ["/etc/entrypoint"]