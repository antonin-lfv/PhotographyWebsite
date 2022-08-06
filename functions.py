from datetime import date


def extract_image_title_from_path(path: str):
    """Automate the title of images"""
    print(path)
    split_path = path.split("/")
    fileName = split_path[-1]
    date_str = fileName.split('_')[1].split('.')[0].split('-')
    final_date = date(day=int(date_str[0]), month=int(date_str[1]), year=int(date_str[2])).strftime('%A %d %B %Y')
    category = split_path[3]
    return final_date + " " + category
