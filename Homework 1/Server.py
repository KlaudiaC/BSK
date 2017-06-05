# -*- coding: utf-8 -*-

import sys
import socket
import getopt
import threading

SERVER_ADDRESS = "localhost"
SERVER_PORT = 9999
clients_limit = 0
clients_counter = 0

if __name__ == '__main__':
    try:
        opts, args = getopt.getopt(sys.argv[1:], "p:")
    except getopt.GetoptError:
        print "Server.py -p <port>"
        sys.exit(2)

    def handler(c, counter, limit):
        if counter < limit:
            counter += 1
            request = c.recv(1024)
            print "Odebrano zapytanie: %s" % request
            c.send("OK")
            c.close()
            counter -= 1

    for opt, arg in opts:
        if opt == '-p':
            SERVER_PORT = int(arg)
        if opt == '-c':
            clients_limit = int(arg)

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((SERVER_ADDRESS, SERVER_PORT))
    server.listen(5)
    print "Nasłuchuję na porcie: %s:%d" % (SERVER_ADDRESS, SERVER_PORT)

    while True:
        client, address = server.accept()
        print "Odezwał się klient spod adresu: %s:%d" % (address[0], address[1])
        thread = threading.Thread(target=handler, args=(client, clients_counter, clients_limit,))
        thread.start()
