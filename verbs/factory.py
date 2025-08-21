from service import Service
from text_tokeniser import TextTokeniser
from verb_model import VerbModel, connect

# Should I make unit-tests use this func?
# TODO: I would need to allow injecting dbCreat for that to work


def createVerbService(dbPath: str) -> Service:
    obj1 = VerbModel(connect(dbPath))
    obj2 = TextTokeniser("")
    obj3 = Service(obj2, obj1)
    return obj3
