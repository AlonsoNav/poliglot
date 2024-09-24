def comments_score(loc, comments):
    """
    Función que determina si hay comentarios descriptivos, se basa en la siguiente cuantificación:
    Proporción alta (>10%): Puntaje completo (ej. 10 puntos).
    Proporción moderada (5-10%): Puntaje reducido (ej. 7 puntos).
    Proporción baja (<5%): Puntaje bajo (ej. 4 puntos).
    """
    if loc == 0:
        return 0
    ratio = comments / loc
    if ratio > 0.1:
        return 10
    elif ratio > 0.05:
        return 7
    else:
        return 4