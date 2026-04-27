def main():
    word = input("Word")
    print(shorten(word))


def shorten(word):
    vowels = "AEIOUaeiou"
    return "".join(ch for ch in word if ch not in vowels)


if __name__ == "__main__":
    main()

#not done 

from twttr import shorten 

def test_lowercase_vowels
    assert shorten("twitter")== "twttr"

def test_upper

def test_mixed case
def test_no_vowels
def test_all_vowels 