from service import Service
from text_tokeniser import TextTokeniser
from verb_model import VerbModel, connect

# Should I make unit-tests use this func?
# TODO: I would need to allow injecting dbCreat for that to work

def create_verb_service(dbpath: str) -> Service:
	""" To simplify Controller code, isolate anything needed to here
		Only 1 service to date

		Injects an empty string to the tokeniser, as the actual content will 
		appear later

		return Service
	"""
    obj1 = VerbModel(connect(dbpath))
    obj2 = TextTokeniser("")
    obj3 = Service(obj2, obj1)
    return obj3
