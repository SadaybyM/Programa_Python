import random   

def main():
    numerbers = [16.2, 75.1, 52.3]
    print(numerbers)
    append_random_numbers(numerbers)
    print(numerbers)

def append_random_numbers(numlist,quantity=1):
    for _ in range(quantity):
        num=random.uniform(0,100)
        num=round(num,1)
        numlist.append(num)

if __name__=="__main__":
    main()
