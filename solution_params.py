def area(shape, params):
    '''
    :param shape: Shape
    :type shape: string
    :param params: Parameters of the shape
    :type params: dict

    :return: Area of the shape
    :rtype: float
    '''
    
    import math

    # Berechnung für einen Kreis
    if shape == 'circle':
        # Überprüfen, ob der 'radius'-Schlüssel im Dictionary 'params' vorhanden ist
        if 'radius' in params:
            # Extrahieren des Werts für 'radius' aus dem Dictionary 'params'
            radius = params['radius']
            # Berechnung der Fläche des Kreises mit der Formel π * radius^2
            return math.pi * radius ** 2
        else:
            # Fehler auslösen, wenn 'radius' nicht im Dictionary vorhanden ist
            raise ValueError("Radius parameter is required for a circle.")
    
    # Berechnung für ein Dreieck
    elif shape == 'triangle':
        # Überprüfen, ob die Schlüssel 'base' und 'height' im Dictionary 'params' vorhanden sind
        if 'base' in params and 'height' in params:
            # Extrahieren der Werte für 'base' und 'height' aus dem Dictionary 'params'
            base = params['base']
            height = params['height']
            # Berechnung der Fläche des Dreiecks mit der Formel 0.5 * base * height
            return 0.5 * base * height
        else:
            # Fehler auslösen, wenn 'base' oder 'height' nicht im Dictionary vorhanden sind
            raise ValueError("Base and height parameters are required for a triangle.")
    
    # Berechnung für ein Rechteck
    elif shape == 'rectangle':
        # Überprüfen, ob die Schlüssel 'base' und 'height' im Dictionary 'params' vorhanden sind
        if 'base' in params and 'height' in params:
            # Extrahieren der Werte für 'base' und 'height' aus dem Dictionary 'params'
            base = params['base']
            height = params['height']
            # Berechnung der Fläche des Rechtecks mit der Formel base * height
            return base * height
        else:
            # Fehler auslösen, wenn 'base' oder 'height' nicht im Dictionary vorhanden sind
            raise ValueError("Base and height parameters are required for a rectangle.")
    
    # Fehlerbehandlung für nicht unterstützte Formen
    else:
        # Fehler auslösen, wenn die Form nicht 'circle', 'triangle' oder 'rectangle' ist
        raise ValueError("Unsupported shape type. Supported shapes: circle, triangle, rectangle.")

# Beispielaufrufe der Funktion
print(area('circle', {'radius': 1.0}))         # Ausgabe: 3.141592653589793
print(area('triangle', {'base': 2, 'height': 1}))  # Ausgabe: 1.0
print(area('rectangle', {'base': 2, 'height': 1})) # Ausgabe: 2.0
print(area('rectangle', {'base': 2, 'height': 1})) # Ausgabe: 2.0
print(area('rectangle', {'base': 2, 'height': 1})) # Ausgabe: 2.0
print(area('rectangle', {'base': 2, 'height': 3})) # Ausgabe: 2.0
print(area('rectangle', {'base': 2, 'height': 1})) # Ausgabe: 2.0
