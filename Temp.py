class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        Kelvin=celsius+273.15
        Farhieght=(celsius)*1.8+32
        return[Kelvin, Farhieght]
