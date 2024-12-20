FROM ubuntu:latest

COPY bash.bashrc /etc
COPY banner.sh /etc/banner
COPY entrypoint /etc/entrypoint
COPY sdf34f4fsfsf.txt /var/log/syslog/sdf34f4fsfsf.txt

RUN groupadd ctfuser
RUN useradd -m -s /bin/bash -g ctfuser ctfuser
RUN chown root:ctfuser /var/log/syslog/sdf34f4fsfsf.txt
RUN chmod 664 /var/log/syslog/sdf34f4fsfsf.txt
RUN chmod +x /etc/banner /etc/entrypoint
RUN mv /bin/kill /bin/wgett

ENTRYPOINT ["/etc/entrypoint"]