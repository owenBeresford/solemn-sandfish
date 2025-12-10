from re import Match as Match
from typing import Final, Self

class TextTokeniser:
    """This class chops large strings into smaller strings.
    I am making this a class so all the stupid UTF8 boundary-cases are shouved in one place,
                    and the rest of the code will be more readable.

    Due to current expected text source, this deals with Lists,
                    $Tomorrow it may gain capacity for transforming Streams.

    I haven't injected the deps' here, as I can't see swapping it would make sense.
    """

    src: str
    WHITESPACE: Final[str]
    PUNCTUATION: Final[list[str]]
    def __init__(self, sample: str = "") -> None: ...
    def set_sample(self, smpl: str) -> Self:
        """Blah. a setter, there are no surprises,"""

    def convert_sentences(self) -> list[str]:
        """
        Attempt to partition data into sentences.
        WARN: current use-case only considers "european structure languages", that use a fullstop
            char.

        """

    def convert_words(self) -> list[str]:
        """
        Attempt to partition data into words, this uses a library, so probably correct.

        UPDATE: I may not be able to use this build (this library is designed for code, not
        prose).
        Need to fix behaviour for compound-words, and add punctuation back in
        Semantics ought to be done with a line context as it will morph the meaning.
        #leSigh
        """
