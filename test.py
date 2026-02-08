A = float(input("Enter a number: "))

if A != int(A):
    print("đây k phải số nguyên")
else:
    A = int(A)
    print("đây là số nguyên")

    # kiểm tra chẵn / lẻ
    if A % 2 == 0:
        print("đây là số chẵn")
    else:
        print("đây là số lẻ")

    # kiểm tra số chính phương
    if A >= 0:
        k = int(A ** 0.5)
        if k * k == A:
            print("đây là số chính phương")
        else:
            print("đây k phải số chính phương")
    else:
        print("đây k phải số chính phương")

    # kiểm tra số hoàn hảo
    if A > 1:
        tong = 0
        for i in range(1, A // 2 + 1):
            if A % i == 0:
                tong += i

        if tong == A:
            print("đây là số hoàn hảo")
        else:
            print("đây k phải số hoàn hảo")
    else:
        print("đây k phải số hoàn hảo")
