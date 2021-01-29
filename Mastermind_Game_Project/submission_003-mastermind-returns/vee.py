def values_(num1, num2, num3):
    answer = (num1 +(num2 * num3))
    tuple1 = (answer, num1, num2)
    return answer, num1, num2
if __name__ == "__main__":
    tuple1 = values_(3,2,2)
    print (tuple1)
    print (tuple1[2])