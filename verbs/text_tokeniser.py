import re
import tokenize
from io import StringIO
from re import Match
from types import NoneType
from typing import Any, Final, List, Self  # , Optional


class TextTokeniser(object):
    """This class chops large strings into smaller strings.
    I am making this a class so all the stupid UTF8 boundary-cases are shouved in one place,
                    and the rest of the code will be more readable.
    TODO findout if tokenise returns something useful.

    Due to current expected text source, this deals with Lists,
                    $Tomorrow it may gain capacity for transforming Streams.

    I haven't injected the deps' here, as I can't see swapping it would make sense.
    """

    src: str
    WHITESPACE: Final[str] = " \t\n\r\n\v\f\x1c\x1d\x1e\x85\u2028\u2029"
    PUNCTUATION: Final[list[str]] = [",", ".", "-", "[", "]", "!", '"', "'", "&"]

    def __init__(self: Self, sample: str = "") -> Self:
        self.src = sample
        # maybe move the regex flags to a class var

    def setSample(self: Self, smpl: str) -> Self:
        self.src = smpl
        return self

    def convert_sentences(self: Self) -> List[str]:
        """
        Attempt to partition data into sentences.
        WARN: current use-case only considers "european structure languages", that use a fullstop char.

        """
        ret: list[str] = []
        low = 0
        high = len(self.src)
        for i in re.compile("(?:\\.[ \\t\\n\\r]+\\b|\\.\\Z)").finditer(self.src):
            high = i.start() + 1
            ret.append(self.src[low:high].strip())
            low = high
        return ret

    def convert_words(self: Self) -> List[str]:
        """
        Attempt to partition data into words, this uses a library, so probably correct.

        UPDATE: I may not be able to use this build (this library is designed for code, not prose).
        Need to fix behaviour for compound-words, and add punctuation back in
        Semantics ought to be done with a line context as it will morph the meaning.
        #leSigh
        """
        ret: list[str] = []
        src2 = StringIO(self.src)

        for x in tokenize.generate_tokens(src2.readline):
            buf: str = x.string
            buf = buf.strip()
            if len(buf) and not buf in self.PUNCTUATION:
                ret.append(buf)

        return ret
