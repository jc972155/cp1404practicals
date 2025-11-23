"""
CP1404 Practical
SilverServiceTaxi Class
"""
from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Represent a Silver Service Taxi"""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """ Initialise a SilverServiceTaxi instance

        fanciness: float, scales price_per_km
        """
        super().__init__(name, fuel)
        self.price_per_km = Taxi.price_per_km * fanciness

    def __str__(self):
        """Return a string like Taxi with added flagfall"""
        return f"{super().__str__()} plus flagfall of $4.50"

    def get_fare(self):
        """Return the price for the taxi trip plus flagfall"""
        return super().get_fare() + SilverServiceTaxi.flagfall
