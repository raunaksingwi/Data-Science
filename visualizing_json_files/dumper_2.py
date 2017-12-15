import json
import matplotlib.pyplot as plt

with open("dumper_2.json") as file:
  data = json.load(file)
  data = data['dumper_engine']

EngineTemperature = []
AmbientTemperature = []
CoolantLevel = []
BenchGradient = []
Gear = []
Speed = []
LubeOilLevel = []
CloggingInRadiator = []
ThermostatValveTemperature = []
AltitudeOfOperation = []



ThermostatValveTemperature = []
AltitudeOfOperation = []
TimeStamp = []

for record in data:
  TimeStamp.append(record['TimeStamp'])
  EngineTemperature.append(record['EngineTemperature'])
  CoolantLevel.append(record['CoolantLevel'])
  LubeOilLevel.append(record['LubeOilLevel'])
  CloggingInRadiator.append(record['CloggingInRadiator'])
  Gear.append(record['Gear'])
  Speed.append(record['Speed'])
  AmbientTemperature.append(record['AmbientTemperature'])
  BenchGradient.append(record['BenchGradient'])
  ThermostatValveTemperature.append(record['ThermostatValveTemperature'])
  AltitudeOfOperation.append(record['AltitudeOfOperation'])


plt.plot(TimeStamp,EngineTemperature)
plt.xlabel("TimeStamp")
plt.ylabel("EngineTemperature")
plt.title("Dumper Engine")
plt.show()

plt.plot(TimeStamp,CoolantLevel)
plt.xlabel("TimeStamp")
plt.ylabel("CoolantLevel")
plt.title("Dumper Engine")
plt.show()

plt.plot(TimeStamp,LubeOilLevel)
plt.xlabel("TimeStamp")
plt.ylabel("LubeOilLevel")
plt.title("Dumper Engine")
plt.show()

plt.plot(TimeStamp,CloggingInRadiator)
plt.xlabel("TimeStamp")
plt.ylabel("CloggingInRadiator")
plt.title("Dumper Engine")
plt.show()

plt.plot(TimeStamp,Gear)
plt.xlabel("TimeStamp")
plt.ylabel("Gear")
plt.title("Dumper Engine")
plt.show()

plt.plot(TimeStamp,Speed)
plt.xlabel("TimeStamp")
plt.ylabel("Speed")
plt.title("Dumper Engine")
plt.show()

plt.plot(TimeStamp,AmbientTemperature)
plt.xlabel("TimeStamp")
plt.ylabel("AmbientTemperature")
plt.title("Dumper Engine")
plt.show()

plt.plot(TimeStamp,BenchGradient)
plt.xlabel("TimeStamp")
plt.ylabel("BenchGradient")
plt.title("Dumper Engine")
plt.show()

plt.plot(TimeStamp,ThermostatValveTemperature)
plt.xlabel("TimeStamp")
plt.ylabel("ThermostatValveTemperature")
plt.title("Dumper Engine")
plt.show()

plt.plot(TimeStamp,AltitudeOfOperation)
plt.xlabel("TimeStamp")
plt.ylabel("AltitudeOfOperation")
plt.title("Dumper Engine")
plt.show()

