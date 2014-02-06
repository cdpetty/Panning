import socket
import errno
import random

def scan(host, port_min, port_max):
    ##List for scanned ports
    scanned = []
    
    ##configure timeout for socket connection
    socket.setdefaulttimeout(.5)
    host = socket.gethostbyname(host)
    
    ##establish port range
    ports = range(port_min, port_max + 1)
    random.shuffle(ports)
    
    ##Iterate over ports
    for port in ports:
        ##establish appropriate protocols
        ipv4 = socket.AF_INET
        tcp = socket.SOCK_STREAM
        
        ##Connect and close conection
        sock = socket.socket(ipv4, tcp)
        connection = sock.connect_ex((host, port));
        sock.close()
        
        ##Append port and connection code
        scanned.append({'port' : port, 'connection_code' : connection})
        
        ##Inform user on port information
        if connection == 0:
            print 'Port %d is open' % port
        else:
            print 'Port %d is closed with error code: %d (%s)' % (port, connection, errno.errorcode[connection])
            
    ##return ports and results
    return scanned

def main():
    print '-------------------------------------------'
    print 'Welcome to Pan, your personal port scanner!'
    print '-------------------------------------------\n'
    
    ##Input user requirements
    host = raw_input('Please input the website or ip address you would like to pan: ')
    port_min = int(raw_input('Please input the lowest port you would like to scan: '))
    port_max = int(raw_input('Please input the highest port you would like to scan: '))
    
    ##execute scan
    scanned_ports = scan(host, port_min, port_max)

if __name__=='__main__':
    main()