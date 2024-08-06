import settings

def calc_height(height_percent):
    return (settings.HEIGHT / 100) * height_percent

def calc_width(width_percent):
    return (settings.WIDTH / 100) * width_percent

# print(calc_width(25))