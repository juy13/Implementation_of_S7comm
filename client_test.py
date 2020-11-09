import os

import snap7

ip = '127.0.0.1'
tcpport = 102
db_number = 1
rack = 1
slot = 1


def start_client():
    client = snap7.client.Client()
    client.connect(ip, rack, slot, tcpport)
    return client


def get_cpu_state(client):
    """this tests the get_cpu_state function"""
    return client.get_cpu_state()


def test_db_read(client):
    size = 40
    start = 0
    db = 1
    data = bytearray(40)
    client.db_write(db_number=db, start=start, data=data)
    result = client.db_read(db_number=db, start=start, size=size)
    return result


def test_db_write(client):
    size = 40
    data = bytearray(size)
    client.db_write(db_number=1, start=0, data=data)


def test_db_get(client):
    return client.db_get(db_number=db_number)


def test_list_blocks(client):
    blockList = client.list_blocks()
    return blockList


def test_get_block_info(client):
    """test Cli_GetAgBlockInfo"""
    return client.get_block_info('DB', 1)


def menu():
    print("1. Start client")
    print("2. Get cpu state")
    print("3. Test DB read")
    print("4. Test DB write")
    print("5. Test DB get")
    print("6. Test list blocks")
    print("7. Test get block_info")


if __name__ == '__main__':
    client = None
    while True:
        menu()
        ans = int(input("Enter your choice: "))
        if ans <= 0 or ans >= 8:
            continue
        if ans == 1 and client is None:
            client = start_client()
        if ans == 2 and client is not None:
            print(get_cpu_state(client))
        if ans == 3 and client is not None:
            print(test_db_read(client))
        if ans == 4 and client is not None:
            test_db_write(client)
        if ans == 5 and client is not None:
            print(test_db_get(client))
        if ans == 6 and client is not None:
            print(test_list_blocks(client))
        if ans == 7 and client is not None:
            print(test_get_block_info(client))

        ans = input("Continue? [y/n]: ")
        if ans == 'y':
            os.system("clear")
            continue
        if ans == 'n':
            client.destroy()
