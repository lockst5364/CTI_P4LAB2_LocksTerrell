first_int = int(input())
second_int = int(input())

if first_int <= second_int:
    for i in range(first_int, second_int+1, 5,):
        print(i, end=' ')
    print()
else:
    print("Second integer can't be less than the first.")