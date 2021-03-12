from __future__ import annotations

import string

EOL_PUNCTUATION = ".!?"


class Document:

    TRANSLATION_TABLE = str.maketrans("", "", string.punctuation)

    def __init__(self):
        self.lines = []

    def add_line(self, line: str, index: int = None) -> Document:
        """Add a new line to the document.

        Args:
            line (str): The line,
                expected to end with some kind of punctuation.
            index (int, optional): The place where to add the line into the document.
                If None, the line is added at the end. Defaults to None.

        Returns:
            Document: The changed document with the new line.
        """
        index = len(self) if index is None else index
        self.lines.insert(index, line)

        return self

    def swap_lines(self, index_one: int, index_two: int) -> Document:
        """Swap two lines.

        Args:
            index_one (int): The first line.
            index_two (int): The second line.

        Returns:
            Document: The changed document with the swapped lines.
        """
        self.lines[index_one], self.lines[index_two] = (
            self.lines[index_two],
            self.lines[index_one],
        )

        return self

    def merge_lines(self, indices: list) -> Document:
        """Merge several lines into a single line.

        The merged lines are added at the minimum index.
        Lines are merged in order of their index, ascending.

        Args:
            indices (list): The lines to be merged.

        Returns:
            Document: The changed document with the merged lines.
        """
        lines_to_keep = [self.lines[i] for i in range(len(self)) if i not in indices]
        lines_to_merge = [self.lines[i] for i in sorted(indices)]

        self.lines = lines_to_keep
        self.add_line(" ".join(lines_to_merge), min(indices))

        return self

    def add_punctuation(self, punctuation: str, index: int) -> Document:
        """Add punctuation to the end of a sentence.

        Overwrites existing punctuation.

        Args:
            punctuation (str): The punctuation. One of EOL_PUNCTUATION.
            index (int): The line to change.

        Returns:
            Document: The document with the changed line.
        """
        line = self.lines[index]

        if line and line[-1] in EOL_PUNCTUATION:
            line = line[:-1] + punctuation
        else:
            line += punctuation

        self.lines[index] = line

        return self

    def word_count(self) -> int:
        """Return the total number of words in the document."""
        lines = map(self._remove_punctuation, self.lines)

        return sum(len(line.split()) for line in lines)

    @property
    def words(self) -> list:
        """Return a list of unique words, sorted and case insensitive."""

        def _parse_line(line: str) -> list:
            """Remove any punctuation and return all unique words."""
            line = self._remove_punctuation(line)
            words = line.lower().split()
            return words

        words = set()
        for line in self.lines:
            words.update(_parse_line(line))

        return sorted(words)

    def _remove_punctuation(self, line: str) -> str:
        """Remove punctuation from a line."""
        # you can use this function as helper method for
        # Document.word_count() and Document.words
        return line.translate(Document.TRANSLATION_TABLE)

    def __len__(self):
        """Return the length of the document (i.e. line count)."""
        return len(self.lines)

    def __str__(self):
        """Return the content of the document as string."""
        return "\n".join(self.lines)
