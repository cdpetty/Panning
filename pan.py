import socket
import errno
import random

def scan(host, port_min, port_max):
    scanned = []
    
    socket.setdefaulttimeout(.5)
    host = socket.gethostbyname(host)
    ports = range(port_min, port_max + 1)
    random.shuffle(ports)
    for port in ports:
        ipv4 = socket.AF_INET
        tcp = socket.SOCK_STREAM
        sock = socket.socket(ipv4, tcp)
        connection = sock.connect_ex((host, port));
        sock.close()
        scanned.append({'port' : port, 'connection_code' : connection})
        if connection == 0:
            print 'Port %d is open' % port
        else:
            print 'Port %d is closed with error code: %d (%s)' % (port, connection, errno.errorcode[connection])
        
    return scanned

def main():
    print '-------------------------------------------'
    print 'Welcome to Pan, your personal port scanner!'
    print '-------------------------------------------\n'
    
    host = raw_input('Please input the website or ip address you would like to pan: ')
    port_min = int(raw_input('Please input the lowest port you would like to scan: '))
    port_max = int(raw_input('Please input the highest port you would like to scan: '))
    
    scanned_ports = scan(host, port_min, port_max)
    
    #for scanned in scanned_ports:
    #    if scanned['connection_code'] == 0:
    #        print 'Port %d is open' % scanned['port']
    #    else:
    #        print 'Port %d is closed with error code: %d (%s)' % (scanned['port'], scanned['connection_code'], errno.errorcode[scanned['connection_code']])

        
if __name__=='__main__':
    main()