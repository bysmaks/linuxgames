import random
import datetime
import ipaddress

def number(first=500, last=10000):
    return random.randint(first, last)

def generate_timestamp():
    now = datetime.datetime.now()
    return now.strftime("%H:%M:%S")

def generate_status():
    statuses = ["BAN", "INFO", "NOTICE"]
    return random.choice(statuses)

def generate_service():
    services = ["nginx", "postfix", "sshd", "httpd"]
    return random.choice(services)

def generate_ip():
    internal_ip = ipaddress.IPv4Address(random.randint(0x0A000000, 0x0AFFFFFF))
    external_ip = ipaddress.IPv4Address(random.randint(0xC0000000, 0xCFFFFFFF))
    return str(random.choice([internal_ip, external_ip]))

def generate_log_entry():
    timestamp = generate_timestamp()
    status = generate_status()
    service = generate_service()
    ip = generate_ip()
    return f"09/Nov/2024:{timestamp} fail2ban.action {status} {service} {ip}"

def generate_log_file(filename, num_entries):
    with open(filename, 'w') as file:
        for _ in range(num_entries):
            file.write(generate_log_entry() + '\n')

generate_log_file('fail2ban.log', number(2000, 3000))

def add_bruteforce_entries(filename, ip, num_entries):
    with open(filename, 'a') as file:
        for _ in range(num_entries):
            timestamp = generate_timestamp()
            status = "BAN"
            service = generate_service()
            file.write(f"09/Nov/2024:{timestamp} fail2ban.action {status} {service} {ip}\n")

bruteforce_ip = str(ipaddress.IPv4Address(random.randint(0xC0000000, 0xCFFFFFFF)))
print(bruteforce_ip)

add_bruteforce_entries('fail2ban.log', bruteforce_ip, 2050)

#external
for _ in range(number()):
    other_bruteforce_ip = str(ipaddress.IPv4Address(random.randint(0xC0000000, 0xCFFFFFFF)))
    add_bruteforce_entries('fail2ban.log', other_bruteforce_ip, number(1000, 1500))

#internal
for _ in range(number()):
    other_bruteforce_ip = str(ipaddress.IPv4Address(random.randint(0x0A000000, 0x0AFFFFFF)))
    add_bruteforce_entries('fail2ban.log', other_bruteforce_ip, number(1000, 1500))

print("Лог-файл успешно сгенерирован.")