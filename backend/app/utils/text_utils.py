from rapidfuzz import fuzz


def fuzzy_match(word: str, keywords: list, threshold: int = 80):
    """
    Returns True if the word closely matches any keyword.
    """

    word = word.lower()

    for keyword in keywords:
        score = fuzz.ratio(word, keyword.lower())

        if score >= threshold:
            return True

    return False