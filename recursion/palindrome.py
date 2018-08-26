def is_palindrome(s):
    if s[0] == s[-1]:
        return is_palindrome(s[1:-1])
    else:
        return False


def iter_palindrome(s):
    for i in range(0, len(s) // 2):
        if s[i] != s[-(i + 1)]:
            return False
        return True


word_to_test = 'beammaeb'
print(is_palindrome(word_to_test))
print(iter_palindrome(word_to_test))
