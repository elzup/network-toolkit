import socket


def initialize_server(host="0.0.0.0", port=12345):
    """サーバーを初期化し、ソケットを設定する"""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((host, port))
    s.listen()
    print(f"サーバーが {host}:{port} で起動しました。")
    return s


def handle_client(conn, addr):
    """クライアントからの接続を処理する"""
    print(f"{addr} からの接続を受け付けました。")
    while True:
        data = conn.recv(1024)
        if not data:
            break
        display_data_summary(data)
    print(f"{addr} からの接続が終了しました。")


def display_data_summary(data):
    """受信データのサマリーを表示する"""
    print(f"受信データ: {data[:50]}... (全長: {len(data)} バイト)")


def start_server(host="0.0.0.0", port=12345):
    """サーバーを起動し、クライアントの接続を待ち受ける"""
    with initialize_server(host, port) as s:
        while True:
            conn, addr = s.accept()
            with conn:
                handle_client(conn, addr)


if __name__ == "__main__":
    start_server()
