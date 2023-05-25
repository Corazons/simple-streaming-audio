import socket
import pyaudio

# Konfigurasi host dan port server
host = 'localhost'  # Alamat IP atau hostname server
port = 9999

# Membuat koneksi socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

# Menerima data file audio dari server
file_data = b""
while True:
    chunk = s.recv(2097152)
    if not chunk:
        break
    file_data += chunk

# Menyimpan data file audio dalam file
file_name = 'received_audio.wav'  # Nama file untuk menyimpan audio yang diterima
file = open(file_name, 'wb')
file.write(file_data)
file.close()

# Memainkan file audio yang diterima
p = pyaudio.PyAudio()
stream = p.open(format=p.get_format_from_width(2),
                channels=2,
                rate=44100,
                output=True)
stream.write(file_data)

stream.stop_stream()
stream.close()
p.terminate()
s.close()
