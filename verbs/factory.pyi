from service import Service

def create_verb_service(dbpath: str) -> Service:
    """To simplify Controller code, isolate anything needed to here
    Only 1 service to date

    Injects an empty string to the tokeniser, as the actual content will
    appear later

    return Service
    """
