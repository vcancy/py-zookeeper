from kazoo.client import KazooClient
import time

zk = KazooClient(hosts="127.0.0.1:2182")

zk.start()

# print('111111111111')

# time.sleep(10)

def test_ensure():
    print(__name__)
    zk.ensure_path("/my/path")


def test_create():
    print(__name__)
    nodename = "/my/path/node"
    index = 1
    while index < 10:
        zk.create(
            nodename,
            "10.0.0.1_{index}".format(index=index).encode(),
            ephemeral=True,
            sequence=True,
        )
        # time.sleep(10)
        index += 1


if __name__ == "__main__":
    # test_ensure()
    test_create()
    time.sleep(100)

    zk.stop()
