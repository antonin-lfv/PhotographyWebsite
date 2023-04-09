import glob


class images:
    """
    Name of images per category
    """
    MOON_FILES = list(map(lambda x: x[7:], glob.glob("static/img/img/moon/*")))
    SUN_FILES = list(map(lambda x: x[7:], glob.glob("static/img/img/sun/*")))
    LANDSCAPE_FILES = list(map(lambda x: x[7:], glob.glob("static/img/img/landscape/*")))
    OTHER_FILES = list(map(lambda x: x[7:], glob.glob("static/img/img/other/*")))
    ALL = MOON_FILES+SUN_FILES+LANDSCAPE_FILES+OTHER_FILES
