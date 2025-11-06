def score(x: float, y: float) -> int:
    """
    Determine the score of the player depending where the dart lands,
    using Cartesian coordinates (x, y).

    If the dart lands :
        - outside the target, payer earns 0 points.
        - in the outer circle of the target, player earns 1 point.
        - in the middle circle of the target, player earns 5 points.
        - in the inner circle of the target, player earns 10 points.

    Note : (radius<=x) will be 0 if False and 1 if True.
    
    :param x: float - x coordinates.
    :param y: float - y coordinates.
    :return int - points earn by the player.
    """
    radius = (x**2+y**2)**0.5
    
    return (radius<=1)*5+(radius<=5)*4+(radius<=10)*1
