from socket import *
import time
begin = time.time()

if __name__ == "__main__":
    addresstarget = input('enter host for scanning:')
    t_IP = gethostbyname(addresstarget)
    print('Scanning for open ports on : ', t_IP)

    for i in range(50, 500):
        soc = socket(AF_INET, SOCK_STREAM)
        connectioncheck = soc.connect_ex((t_IP, i))
        if (connectioncheck == 0):
            print('Port %d: OPEN' % (i,))
        soc.close()
print("The time taken for the scan:", time.time() - begin)


