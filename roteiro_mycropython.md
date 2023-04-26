# Conectar o Myo armband ao Raspberry Pi Pico com Thonny

**1.** Certifique-se de que o Raspberry Pi Pico esteja configurado com o MicroPython. Se você ainda não configurou o MicroPython no Raspberry Pi Pico.

    - Abra o Thonny IDE em seu computador.

    - Clique no menu "Run" e selecione "Configure interpreter..."

    - Selecione o tipo de interprtador será utilizado 

    - instale ou atualize MicroPython no dispositivo se necessário
        - segurar o botão de BOOT do dispositivo e desconectar e reconectar ele no computador para selecionar o dispositivo

    - Aperte "OK" para finalizar

Obs: lique no menu "View" e selecione "Files" para visualizar os arquivos presentes no dispositivo

**2.** Conecte o módulo Bluetooth ao Raspberry Pi Pico.

(exemplo para ligar e desligar um LED)

![Conexão bluetooth](https://capsistema.com.br/wp-content/uploads/2021/10/imagem-90-1024x446.png)

![Conexão bluetooth](https://embarcados.com.br/wp-content/uploads/2022/06/image-130.png.webp)

**3.** Crie um novo arquivo de projeto no Thonny.

**4.** Escreva o código necessário para se comunicar com o Myo armband. Você pode usar a biblioteca PyMyo para se comunicar com o Myo armband. Para instalá-la, clique no menu "Tools" e selecione "Manage Packages". Na janela "Package Manager", pesquise por "pymyo" e instale a biblioteca.

**5.** Depois que a biblioteca PyMyo estiver instalada, você pode usar o seguinte código para se conectar ao Myo armband:

```python
from machine import UART
from pymyo import Myo

# Configura o UART para se comunicar com o módulo Bluetooth
uart = UART(0, 115200)
uart.init(115200, bits=8, parity=None, stop=1)

# Configura o Myo armband
myo = Myo()
myo.connect()

# Loop principal
while True:
    # Recebe os dados do módulo Bluetooth
    data = uart.read()

    # Processa os dados do Myo armband
    accel = myo.acceleration
    print('Acceleration: x={}, y={}, z={}'.format(accel[0], accel[1], accel[2]))
```

