# coding=utf-8
from kazoo.client import KazooClient
import time

zk = KazooClient(hosts="127.0.0.1:2182")

zk.start()

server_list = []


@zk.ChildrenWatch("/my/path")
def my_func(children):
    global server_list
    server_list = children


children = zk.get_children("/my/path", watch=my_func)

for child in children:
    server_list.append(child)

while True:
    print(server_list)
    time.sleep(1)

zk.stop()
