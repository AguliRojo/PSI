def function(celc):
    temperatura = {
        "Celciusz" : celc,
        "Fahrenheit" : (celc * (9/5)) + 32,
        "Rankine" : celc * (9/5) + 491.67,
        "Kelvin" : celc + 273.15
    }
    return temperatura

print(function(42)["Rankine"])
