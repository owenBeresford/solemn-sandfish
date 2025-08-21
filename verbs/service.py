from io import TextIOBase
from typing import List, Self

from text_tokeniser import TextTokeniser
from verb_model import VerbModel


class Service:
    """The wrapper/ abstraction for the transform to suggest alternatives to common and 'weak' verbs.

    This first edition is useless as it removes punctuation.
    """

    def __init__(self: Self, a: TextTokeniser, b: VerbModel) -> Self:
        self.tokr = a
        self.verb = b

    def transform(self: Self, sample: str) -> List[str | list[str]]:
        """Converts the sample from the user into a list of tokens,
        and injects alternative strong verbs at the relevant point
        """
        norm: str = sample.strip().lower()
        self.tokr.set_sample(norm)
        ar: List[str] = self.tokr.convert_words()
        # TODO: support punctuation, support original casing, think about preserve white-space

        out: List[str] = []
        for i in ar:
            if self.verb.matchWeakVerb(i):
                tmp: list[str] = ["list_follows"]
                tmp.extend(self.verb.replaceVerb(i))
                out.append(tmp)

            else:
                out.append(i)
        return out

    def transform_stream(self: Self, src: TextIOBase) -> TextIOBase:
        """
        EMPTY METHOD to keep pylint happy.
        Unless I add a lot more server-side work, this isn't actually used
        """
        return src
