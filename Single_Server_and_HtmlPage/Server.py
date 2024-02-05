import socket

def create_response(client_socket):
    fin = open('Page.html')
    content = fin.read()
    fin.close()
    response = 'HTTP/1.0 200 OK\n\n' + content
    client_socket.send(response.encode())

def create_file_response():
    with open("image.jpg", "rb") as image_file:
        file_content = image_file.read()

    response = """HTTP/1.1 200 OK
Content-type: image/png
Content-Disposition: attachment; filename="imagem.jpg"

{}""".format(file_content.decode('latin-1'))

    return response.encode('latin-1')

def start_server():
    host = '192.168.1.100'
    port = 8000

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print(f"Servidor rodando em http://{host}:{port}")
    cont = 0 
    while True:
        cont = cont +1
        print(cont)
        client_socket, client_address = server_socket.accept()
        request = client_socket.recv(1024).decode('utf-8')
        print(request)

        if request.startswith('GET / '):
            create_response(client_socket)
        elif request.startswith('GET /download '):
            response = create_file_response()
            client_socket.sendall(response)  
        else:
            response = 'HTTP/1.1 404 Not Found\nContent-type: text/html\n\n<h1>404 Not Found</h1>'

        client_socket.close()

if __name__ == "__main__":
    start_server()
# http://192.168.1.100:8000/
