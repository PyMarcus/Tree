import multiprocessing
import socket
import argparse


class ArgumentLine:
    """Lê a linha de comandos"""

    @staticmethod
    def arg(choices):
        parser = argparse.ArgumentParser(description="Servidor e cliente simples para testar o uso de multiprocessos")
        parser.add_argument("funcao", choices=choices, metavar="Servidor/Cliente", help="Informe se quer executar "
                                                                                        "cliente ou servidor",
                            type=str)
        parser.add_argument("--H", "-host", metavar="ip", required=False, help="Se quiser, informe um endereço para o "
                                                                               "servidor", type=str,
                            default="localhost")
        parser.add_argument("--p", "-port", metavar="porta", required=False, help="Se quiser, defina uma porta de "
                                                                                  "comunicação, acima de 7000",
                            type=int, default=7777)
        args = parser.parse_args()
        function = choices[args.funcao]
        return function(args.H, args.p)


class Serv:
    """Cria soquetes de escuta de rede"""

    def __init__(self, host: str = "", port: int = 7777):
        assert port >= 7000
        self.__host = host
        self.__port = port

    @property
    def host(self):
        return self.__host

    @property
    def port(self):
        return self.__port

    @host.setter
    def host(self, new_host):
        self.__host = new_host

    @port.setter
    def port(self, new_port):
        self.__port = new_port

    # @override
    def __str__(self):
        return str((self.__host, self.__port))

    def listener(self):
        """Socket identificador para o sistema"""
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind((self.__host, self.__port))
        sock.listen(64)
        print(f"Escutando no endereço {sock.getsockname()}")
        return sock

    def conect(self):
        sock = self.listener()
        while True:
            nSock, addr = sock.accept()
            print(f"Recebendo conexão de {addr}")
            try:
                while True:
                    msg = nSock.recv(4096)
                    if not msg:
                        raise EOFError("Socket fechado!")
                    else:
                        print(f"{addr} diz: {msg.decode()}")
                    nSock.sendall("[*] Recebido, cliente".encode('utf-8'))
            except EOFError:
                print(f"Soquete do cliente {addr} foi fechado")
            except Exception as e:
                print(f"Error: {e}")
            finally:
                nSock.close()


class Client:
    """Cliente que envia mensagens e recebe respostas do servidor"""
    @staticmethod
    def client(ip_servidor, porta_servidor):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((ip_servidor, porta_servidor))
        sock.sendall("Olá, servidor!".encode('utf-8'))
        resposta = ''
        resposta += sock.recv(4096).decode('utf-8')
        print(f"Servidor diz: {resposta}")

        sock.close()


class PcProcess:
    """Cria multiprocessos para executar os soquetes de comunicação do servidor"""

    @staticmethod
    def run_process(host: str = "", port: int = 7777):
        assert port >= 7000
        serv = Serv()
        mp = multiprocessing.Process(target=serv.conect, args=())
        mp.start()


if __name__ == '__main__':
    choices: dict = {
        "servidor": PcProcess.run_process,
        "cliente": Client.client
    }

    ArgumentLine.arg(choices=choices)
