import pytest
from ..statistic_display import StatisticDisplay
from ..weather_data import WeatherData

def test_statistic_display():
    weather_data = WeatherData()
    statistic_display = StatisticDisplay(weather_data)

    weather_data.set_measurements(80, 65)

    assert statistic_display._temperature == 80
