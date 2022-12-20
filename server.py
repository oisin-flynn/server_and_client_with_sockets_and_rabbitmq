import socket
import threading
import pika

# set up RabbitMQ connection
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
# queue for messages
channel.queue_declare(queue='activity_log')

HEADER = 64
PORT = 5050
# get local machine name
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
# create socket object
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def send_to_queue(employee_id, command, options, ip_address):
    channel.basic_publish(exchange='',
                          routing_key='activity_log',
                          body=f'{employee_id}, {command}, {options}, {ip_address}')


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    # get client IP address
    client_ip = addr[0]

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False

            # id boolean
            exists = (msg == "E00123" or msg == "E01033")

            if msg in ['E00123', 'E01033']:
                print(f"[{addr}] Valid command received: {msg}")
                conn.send(f"[{addr}] Value exists: {exists}".encode(FORMAT))
                # send message to queue
                send_to_queue(msg, "command", "options", client_ip)

            elif msg in ['s', 'l', 'c', 't', '2018', '2016', 'x', 'y', "!DISCONNECT"]:
                # Handle valid command
                print(f"[{addr}] Valid command received: {msg}")
                conn.send(f"Command recognized {msg}".encode(FORMAT))
                send_to_queue(msg, "command", "options", client_ip)

            else:
                # Handle invalid command
                print(f"[{addr}] Invalid command received: {msg}")
                conn.send(f"Command not recognized {msg}".encode(FORMAT))
    # close connection
    conn.close()


def start():
    server.listen()
    print(f"[LISTENING] server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"\n[ACTIVE CONNECTIONS] {threading.active_count() - 1}")


# callback function to process received messages
def callback(ch, method, properties, body):
    # print message
    print(f'Received message: {body}')

#
# channel.basic_consume(queue='activity_log', on_message_callback=callback, auto_ack=True)
# print("Waiting for messages. To exit press CTRL+C")
# channel.start_consuming()

print("[STARTING] server is starting...")
start()
