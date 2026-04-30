from calc import square 

def main():
    testsquare()


def testsquare():
    
    try:
        assert square(2) ==4
    except AssertionError:
        print("2 sqaURED Wwas not 4")
    try:
        assert square(3)==9
    except AssertionError
        print("3 squared was not 9")
    



if __name__ == "__main__":
    main()
