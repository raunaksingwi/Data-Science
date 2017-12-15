import json
import matplotlib.pyplot as plt

with open("excavator.json") as file:
  data = json.load(file)
  data = data['excavator']

HydraulicPumpPressure = []
OilLevel = []
BucketCapacity = []
AmbientTemperature = []
RockDensity = []
ProperBlasting = []
OilTemperature = []
OperatingPressureTravelCircuits = []
OperatingPressureSwingCircuits = []
OperatingPressurePilotCircuit = []
AmbientHumidity = []
BenchGradient = []
AltitudeOfOperation = []
TimeStamp = []

for record in data:
  TimeStamp.append(record['TimeStamp'])
  OilLevel.append(record['OilLevel'])
  AmbientHumidity.append(record['AmbientHumidity'])
  BucketCapacity.append(record['BucketCapacity'])
  HydraulicPumpPressure.append(record['HydraulicPumpPressure'])
  RockDensity.append(record['RockDensity'])
  ProperBlasting.append(record['ProperBlasting'])
  OilTemperature.append(record['OilTemperature'])
  OperatingPressureTravelCircuits.append(record['OperatingPressureTravelCircuits'])
  AmbientTemperature.append(record['AmbientTemperature'])
  BenchGradient.append(record['BenchGradient'])
  OperatingPressureSwingCircuits.append(record['OperatingPressureSwingCircuits'])
  AltitudeOfOperation.append(record['AltitudeOfOperation'])
  OperatingPressurePilotCircuit.append(record['OperatingPressurePilotCircuit'])


plt.plot(TimeStamp,BucketCapacity)
plt.xlabel("TimeStamp")
plt.ylabel("BucketCapacity")
plt.title("Excavator BucketCapacity")
plt.show()

plt.plot(TimeStamp,HydraulicPumpPressure)
plt.xlabel("TimeStamp")
plt.ylabel("HydraulicPumpPressure")
plt.title("Excavator HydraulicPumpPressure")
plt.show()

plt.plot(TimeStamp,RockDensity)
plt.xlabel("TimeStamp")
plt.ylabel("RockDensity")
plt.title("Excavator RockDensity")
plt.show()

plt.plot(TimeStamp,ProperBlasting)
plt.xlabel("TimeStamp")
plt.ylabel("ProperBlasting")
plt.title("Excavator ProperBlasting")
plt.show()

plt.plot(TimeStamp,OilTemperature)
plt.xlabel("TimeStamp")
plt.ylabel("OilTemperature")
plt.title("Excavator OilTemperature")
plt.show()

plt.plot(TimeStamp,OperatingPressureTravelCircuits)
plt.xlabel("TimeStamp")
plt.ylabel("OperatingPressureTravelCircuits")
plt.title("Excavator OperatingPressureTravelCircuits")
plt.show()

plt.plot(TimeStamp,AmbientTemperature)
plt.xlabel("TimeStamp")
plt.ylabel("AmbientTemperature")
plt.title("Excavator AmbientTemperature")
plt.show()

plt.plot(TimeStamp,BenchGradient)
plt.xlabel("TimeStamp")
plt.ylabel("BenchGradient")
plt.title("Excavator BenchGradient")
plt.show()

plt.plot(TimeStamp,OperatingPressureSwingCircuits)
plt.xlabel("TimeStamp")
plt.ylabel("OperatingPressureSwingCircuits")
plt.title("Excavator OperatingPressureSwingCircuits")
plt.show()

plt.plot(TimeStamp,AltitudeOfOperation)
plt.xlabel("TimeStamp")
plt.ylabel("AltitudeOfOperation")
plt.title("Excavator AltitudeOfOperation")
plt.show()

plt.plot(TimeStamp,OperatingPressurePilotCircuit)
plt.xlabel("TimeStamp")
plt.ylabel("OperatingPressurePilotCircuit")
plt.title("Excavator OperatingPressurePilotCircuit")
plt.show()

plt.plot(TimeStamp,OilLevel)
plt.xlabel("TimeStamp")
plt.ylabel("OilLevel")
plt.title("Excavator OilLevel")
plt.show()

plt.plot(TimeStamp,AmbientHumidity)
plt.xlabel("TimeStamp")
plt.ylabel("AmbientHumidity")
plt.title("Excavator AmbientHumidity")
plt.show()