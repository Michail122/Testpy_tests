import time
def prov_prost(a):
    # time.sleep(1)
    a=int(a)
    if a == 0:
        return False
    if 0 < a  and a <= 3:
        return True
    elif a%2 == 0:
        return False
    else:
        if (a**0.5)<=3:
            sqrt_a=a
        else:
            sqrt_a=int(a**0.5)
        # print(sqrt_a)
        for n in range(3, sqrt_a+2, 2):
            if a!=n and a % n == 0:
                return False
            # if sqrt_a <= n:
    return True
        # print(n)
# def pp(v):
#     print(v)

if __name__=='__main__':
    a = input('Введите число ')
    print(prov_prost(a))
    # pp(input("введите что то: "))

# class TestProv_prost(unittest.TestCase):
#     def test_add(self):
#         self.assertEqual(prov_prost(5), True)
#         self.assertEqual(prov_prost(100),False)
#         self.assertEqual(prov_prost(4),False)
# unittest.main(exit=False)
