# bounce.py
#
# Exercise 1.5

def bounce():
    h = 100
    for i in range(10):
        h *= 3/5
        print(i + 1, round(h, 4))

if __name__ == "__main__":
    bounce()
