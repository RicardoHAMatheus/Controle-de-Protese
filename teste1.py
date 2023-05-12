from pymyo import Myo

@myo.stream_emg
def on_emg_data(myo, timestamp, emg):
  print(emg)

# Configura o Myo armband
myo = Myo()
myo.connect()

myo.init()
hub = myo.Hub()
myo_device = None
while not myo_device:
    try:
        myo_device = hub.wait_for_myos(1)[0]
    except IndexError:
        pass
      
myo_device.stream_emg(True)
