def check_extend(l, i):
    """Check that appending i to l gives a valid sequence.
    Assumes that l is a valid sequence."""
    upfound = False
    downfound = (i == 1)
    for j in l[::-1]:
        # if we see an occurence of i without an intervening i-1 and i+1
        # no joy.
        if j == i:
            return False
        if j == i - 1:
            if upfound:
                return True
            downfound = True
        if j == i + 1:
            if downfound:
                return True
            upfound = True
    return True


def extend_to_length(base, n):
    """Return all valid sequences of length n starting with base"""
    m = max(base)
    for i in range(1, m + 2):
        if check_extend(base, i):
            if len(base) >= n - 1:
                yield base + [i]
            else:
                for l in extend_to_length(base + [i], n):
                    yield l

if __name__ == '__main__':
    for l in extend_to_length([1], 6):
        print l
