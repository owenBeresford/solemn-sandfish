from _typeshed import Incomplete
from io import TextIOBase
from text_tokeniser import TextTokeniser as TextTokeniser
from verb_model import VerbModel as VerbModel

class Service:
    """The wrapper/ abstraction for the transform to suggest alternatives to common and 'weak' verbs.

    This first edition is useless as it removes punctuation.
    """

    tokr: Incomplete
    verb: Incomplete
    def __init__(self, a: TextTokeniser, b: VerbModel) -> None: ...
    def transform(self, sample: str) -> list[str | list[str]]:
        """Converts the sample from the user into a list of tokens,
        and injects alternative strong verbs at the relevant point
        """

    def transform_stream(self, src: TextIOBase) -> TextIOBase:
        """
        EMPTY METHOD to keep pylint happy.
        Unless I add a lot more server-side work, this isn't actually used
        """
