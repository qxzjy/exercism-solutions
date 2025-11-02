def is_triangle(sides: list[int | float]) -> bool:
    """
    Determine if the shape is a triangle.
 
    :param sides: list[int | float] - sides length of the shape.
    :return bool - is the shape a triangle ?
    """
    sides = sorted(sides)
    
    return sum(sides[:2]) > sides[2]

def equilateral(sides: list[int | float]) -> bool:
    """
    Determine if a triangle is equilateral.
 
    :param sides: list[int | float] - sides length of the triangle.
    :return bool - is the triangle equilateral ?
    """
    
    return is_triangle(sides) and len(set(sides)) == 1


def isosceles(sides: list[int | float]) -> bool:
    """
    Determine if a triangle is isosceles.
 
    :param sides: list[int | float] - sides length of the triangle.
    :return bool - is the triangle isosceles ?
    """
    
    return is_triangle(sides) and len(set(sides)) < 3


def scalene(sides: list[int | float]) -> bool:
    """
    Determine if a triangle is scalene.
 
    :param sides: list[int | float] - sides length of the triangle.
    :return bool - is the triangle scalene ?
    """
    
    return is_triangle(sides) and len(set(sides)) == 3
