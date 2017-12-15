import json
import matplotlib.pyplot as plt

with open("dumper_1.json") as file:
  data = json.load(file)
  data = data['dumper_transmission']

TransmissionTemperature = []
DumperLoad = []
OilLevel = []
LowPressure = []
Gear = []
Speed = []
AmbientTemperature = []
BenchGradient = []
TorqueConvertorOilTemperature = []
TorqueConvertorInletPressure = []
TimeStamp = []

for record in data:
  TimeStamp.append(record['TimeStamp'])
  TransmissionTemperature.append(record['TransmissionTemperature'])
  DumperLoad.append(record['DumperLoad'])
  OilLevel.append(record['OilLevel'])
  LowPressure.append(record['LowPressure'])
  Gear.append(record['Gear'])
  Speed.append(record['Speed'])
  AmbientTemperature.append(record['AmbientTemperature'])
  BenchGradient.append(record['BenchGradient'])
  TorqueConvertorOilTemperature.append(record['TorqueConvertorOilTemperature'])
  TorqueConvertorInletPressure.append(record['TorqueConvertorInletPressure'])


plt.plot(TimeStamp,TransmissionTemperature)
plt.xlabel("TimeStamp")
plt.ylabel("TransmissionTemperature")
plt.title("Dumper TransmissionTemperature")
plt.show()

plt.plot(TimeStamp,DumperLoad)
plt.xlabel("TimeStamp")
plt.ylabel("DumperLoad")
plt.title("Dumper Load")
plt.show()

plt.plot(TimeStamp,OilLevel)
plt.xlabel("TimeStamp")
plt.ylabel("OilLevel")
plt.title("Dumper OilLevel")
plt.show()

plt.plot(TimeStamp,LowPressure)
plt.xlabel("TimeStamp")
plt.ylabel("LowPressure")
plt.title("Dumper LowPressure")
plt.show()

plt.plot(TimeStamp,Gear)
plt.xlabel("TimeStamp")
plt.ylabel("Gear")
plt.title("Dumper Gear")
plt.show()

plt.plot(TimeStamp,Speed)
plt.xlabel("TimeStamp")
plt.ylabel("Speed")
plt.title("Dumper Speed")
plt.show()

plt.plot(TimeStamp,AmbientTemperature)
plt.xlabel("TimeStamp")
plt.ylabel("AmbientTemperature")
plt.title("Dumper AmbientTemperature")
plt.show()

plt.plot(TimeStamp,BenchGradient)
plt.xlabel("TimeStamp")
plt.ylabel("BenchGradient")
plt.title("Dumper BenchGradient")
plt.show()

plt.plot(TimeStamp,TorqueConvertorOilTemperature)
plt.xlabel("TimeStamp")
plt.ylabel("TorqueConvertorOilTemperature")
plt.title("Dumper TorqueConvertorOilTemperature")
plt.show()

plt.plot(TimeStamp,TorqueConvertorInletPressure)
plt.xlabel("TimeStamp")
plt.ylabel("TorqueConvertorInletPressure")
plt.title("Dumper TorqueConvertorInletPressure")
plt.show()

