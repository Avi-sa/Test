def find_two(target, lst):
    st = {}
    for i in lst:
        if (target-i) not in st:
            st.add(i)
        else:
            return [i, target-i]
    return [-1, -1]


target = int(input("Enter a target value == "))
lst = [int(it) for it in input("Enter the list of elements: ").split()]

print("Two elements which give the target sum is == ")
print(find_two(target, lst))
