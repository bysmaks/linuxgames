FROM ubuntu:latest as builder

COPY banner.sh /etc/banner
COPY entrypoint /etc/entrypoint
COPY main /root/main
COPY task.py /root/task.py

RUN apt update && apt install python3 -y
RUN chmod +x /root/main
RUN chmod +x /etc/entrypoint /etc/banner

COPY shell.sh /usr/local/bin/shell.sh
RUN chmod +x /usr/local/bin/shell.sh
RUN usermod --shell /usr/local/bin/shell.sh root
RUN mv /bin/kill /bin/wgett

WORKDIR /root

ENTRYPOINT ["/etc/entrypoint"]
