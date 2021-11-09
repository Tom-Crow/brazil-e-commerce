from unidecode import unidecode


def remove_accents(string: str) -> str:
    """
    The data is from Brazil, and so place names can (inconsistently) have accents in them.
    This function removes these accents to keep values consistent across the project.
    :param string:
    :return:
    """
    return unidecode(string)
