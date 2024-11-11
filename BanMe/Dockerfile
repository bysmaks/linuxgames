FROM ubuntu:latest

COPY bash.bashrc /etc/
COPY banner.sh /etc/banner
COPY entrypoint /etc/entrypoint
COPY fail2ban.log /root/

RUN chmod +x /etc/banner /etc/entrypoint

WORKDIR /root
ENTRYPOINT ["/etc/entrypoint"]
