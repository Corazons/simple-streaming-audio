import socket

# Konfigurasi host dan port server
host = 'localhost'  # Alamat IP atau hostname server
port = 9999

# Membuka file audio
file_name = 'audio.wav'  # Nama file audio yang akan dikirim
file = open(file_name, 'rb')

# Membaca konten file audio
file_data = file.read()

# Membuat koneksi socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)

print("Menunggu koneksi dari client...")

# Menerima koneksi dari client
conn, addr = s.accept()
print("Terhubung dengan client:", addr)

try:
    # Mengirimkan data file audio ke client
    conn.send(file_data)
    print("Streaming audio berhasil dikirim ke client")

except Exception as e:
    print("Terjadi kesalahan:", str(e))

finally:
    file.close()
    conn.close()
    s.close()
