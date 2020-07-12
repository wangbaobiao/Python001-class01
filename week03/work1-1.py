import subprocess, os
import fire
import socket
import threading
from concurrent.futures import ThreadPoolExecutor
from ipaddress import ip_address

success_ports = []
ip_used = []
lock = threading.Lock()

def pg_ip(ip01):
    try:
        res = subprocess.call('ping -n 2 -w 5 %s' % ip01, stdout=subprocess.PIPE)  # linux 系统将 '-n' 替换成 '-c'
        print(ip01, True if res == 0 else False)
        if res == 0: ip_used.append(ip01)
    except Exception as e:
        print(e)

def tcp_link(ip_port_tuple):
    if lock.acquire():
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect(ip_port_tuple)
            port_ok = ip_port_tuple[1]
            success_ports.append(port_ok)

        except Exception as e:
            print('Error:', e)
        finally:
            s.close()
            lock.release()


def ping_func(n, f, ip):

    if f == 'ping':
        if "-" in ip:
            seed = []
            ip_start, ip_end = ip.split('-')
            ip_start = ip_address(ip_start)
            ip_end = ip_address(ip_end)
            while ip_start <= ip_end:
                seed.append(str(ip_start))
                ip_start += 1

        else:
            seed = []
            seed.append(ip)
        with ThreadPoolExecutor(n) as executor:
            executor.map(pg_ip, seed)


    elif f == 'tcp':
        seed = [(ip, port) for port in range(0, 1024)]
        with ThreadPoolExecutor(n) as executor:
            executor.map(tcp_link, seed)
        print(f'IP地址{ip}的开放端口：{success_ports}\n')
    else:
        print("你只能 'ping' or 'tcp' function!")


fire.Fire(ping_func)
print(ip_used)
