def cat_and_mouse(x: int, y: int, z: int) -> str:
    distA = abs(x - z)
    distB = abs(y - z)
  
    if distA == distB: 
        return "Mouse C" 
    elif distA < distB: 
        return "Cat A"
    else: 
        return "Cat B"
