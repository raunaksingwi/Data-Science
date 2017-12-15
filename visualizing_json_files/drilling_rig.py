import json
import matplotlib.pyplot as plt

with open("drilling_rig.json") as file:
  data = json.load(file)
  data = data['drilling_rig']


TimeStamp = []
Pressure = []
AmbientTemperature = []
ExternalCoolerCloggingLevel = []
SafetyValvePressure = []
Altitude = []
RockDensity = []
Humidity = []
CompressorTemperature = []
ISO_VG32OilViscosity = []
SulphateAshContent = []
ProperBlasting = []


for record in data:
  TimeStamp.append(record['TimeStamp'])
  Pressure.append(record["Pressure"])
  AmbientTemperature.append(record["AmbientTemperature"])
  ExternalCoolerCloggingLevel.append(record["ExternalCoolerCloggingLevel"])
  SafetyValvePressure.append(record["SafetyValvePressure"])
  Altitude.append(record["Altitude"])
  RockDensity.append(record["RockDensity"])
  Humidity.append(record["Humidity"])
  CompressorTemperature.append(record["CompressorTemperature"])
  ISO_VG32OilViscosity.append(record["ISO_VG32OilViscosity"])
  SulphateAshContent.append(record["SulphateAshContent"])
  ProperBlasting.append(record["ProperBlasting"])



plt.plot(TimeStamp,Pressure)
plt.xlabel("TimeStamp")
plt.ylabel("Pressure")
plt.title("Driller Pressure")
plt.show()



plt.plot(TimeStamp,AmbientTemperature)
plt.xlabel("TimeStamp")
plt.ylabel("AmbientTemperature")
plt.title("Driller AmbientTemperature")
plt.show()




plt.plot(TimeStamp,ExternalCoolerCloggingLevel)
plt.xlabel("TimeStamp")
plt.ylabel("ExternalCoolerCloggingLevel")
plt.title("Driller ExternalCoolerCloggingLevel")
plt.show()

plt.plot(TimeStamp,SafetyValvePressure)
plt.xlabel("TimeStamp")
plt.ylabel("SafetyValvePressure")
plt.title("Driller SafetyValvePressure")
plt.show()

plt.plot(TimeStamp,Altitude)
plt.xlabel("TimeStamp")
plt.ylabel("Altitude")
plt.title("Driller Altitude")
plt.show()

plt.plot(TimeStamp,RockDensity)
plt.xlabel("TimeStamp")
plt.ylabel("RockDensity")
plt.title("Driller RockDensity")
plt.show()

plt.plot(TimeStamp,Humidity)
plt.xlabel("TimeStamp")
plt.ylabel("Humidity")
plt.title("Driller Humidity")
plt.show()

plt.plot(TimeStamp,CompressorTemperature)
plt.xlabel("TimeStamp")
plt.ylabel("CompressorTemperature")
plt.title("Driller CompressorTemperature")
plt.show()

plt.plot(TimeStamp,ISO_VG32OilViscosity)
plt.xlabel("TimeStamp")
plt.ylabel("ISO_VG32OilViscosity")
plt.title("Driller ISO_VG32OilViscosity")
plt.show()

plt.plot(TimeStamp,SulphateAshContent)
plt.xlabel("TimeStamp")
plt.ylabel("SulphateAshContent")
plt.title("Driller SulphateAshContent")
plt.show()

plt.plot(TimeStamp,ProperBlasting)
plt.xlabel("TimeStamp")
plt.ylabel("ProperBlasting")
plt.title("Driller ProperBlasting")
plt.show()

