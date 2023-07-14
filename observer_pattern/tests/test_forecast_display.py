import pytest
from ..forecast_display import ForecastDisplay
from ..weather_data import WeatherData

def test_forecast_display():
    weather_data = WeatherData()
    forecast_display = ForecastDisplay(weather_data)

    weather_data.set_measurements(80, 65)

    assert forecast_display._temperature == 80
    assert forecast_display._humidity == 65
