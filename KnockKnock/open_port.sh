#!/bin/bash

# Открываем порт 80 для доступа к веб-серверу
iptables -D INPUT -p tcp --dport 4444 -j DROP
iptables -A INPUT -p tcp --dport 4444 -j ACCEPT

# Удаляем правило через 60 секунд
sleep 60
iptables -D INPUT -p tcp --dport 4444 -j ACCEPT
iptables -A INPUT -p tcp --dport 4444 -j DROP
