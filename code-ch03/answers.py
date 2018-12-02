"""
# tag::exercise1[]
>>> from ecc import FieldElement
>>> prime = 223
>>> a = FieldElement(0, prime)
>>> b = FieldElement(7, prime)
>>> def on_curve(x,y):
...     return y**2 == x**3 + a*x + b
>>> print(on_curve(FieldElement(192, prime), FieldElement(105, prime)))
True
>>> print(on_curve(FieldElement(17, prime), FieldElement(56, prime)))
True
>>> print(on_curve(FieldElement(200, prime), FieldElement(119, prime)))
False
>>> print(on_curve(FieldElement(1, prime), FieldElement(193, prime)))
True
>>> print(on_curve(FieldElement(42, prime), FieldElement(99, prime)))
False

# end::exercise1[]
# tag::exercise2[]
>>> from ecc import FieldElement, Point
>>> prime = 223
>>> a = FieldElement(0, prime)
>>> b = FieldElement(7, prime)
>>> p1 = Point(FieldElement(170, prime), FieldElement(142, prime), a, b)
>>> p2 = Point(FieldElement(60, prime), FieldElement(139, prime), a, b)
>>> print(p1+p2)
Point(FieldElement_223(220),FieldElement_223(181))_FieldElement_223(0)_FieldElement_223(7)
>>> p1 = Point(FieldElement(47, prime), FieldElement(71, prime), a, b)
>>> p2 = Point(FieldElement(17, prime), FieldElement(56, prime), a, b)
>>> print(p1+p2)
Point(FieldElement_223(215),FieldElement_223(68))_FieldElement_223(0)_FieldElement_223(7)
>>> p1 = Point(FieldElement(143, prime), FieldElement(98, prime), a, b)
>>> p2 = Point(FieldElement(76, prime), FieldElement(66, prime), a, b)
>>> print(p1+p2)
Point(FieldElement_223(47),FieldElement_223(71))_FieldElement_223(0)_FieldElement_223(7)

# end::exercise2[]
# tag::exercise3[]
class ECCTest(TestCase):
...
    def test_add(self):
        prime = 223
        a = FieldElement(0, prime)
        b = FieldElement(7, prime)
        additions = (
            (192, 105, 17, 56, 170, 142),
            (47, 71, 117, 141, 60, 139),
            (143, 98, 76, 66, 47, 71),
        )
        for x1_raw, y1_raw, x2_raw, y2_raw, x3_raw, y3_raw in additions:
            x1 = FieldElement(x1_raw, prime)
            y1 = FieldElement(y1_raw, prime)
            p1 = Point(x1, y1, a, b)
            x2 = FieldElement(x2_raw, prime)
            y2 = FieldElement(y2_raw, prime)
            p2 = Point(x2, y2, a, b)
            x3 = FieldElement(x3_raw, prime)
            y3 = FieldElement(y3_raw, prime)
            p3 = Point(x3, y3, a, b)
            self.assertEqual(p1+p2, p3)
# end::exercise3[]
# tag::exercise4[]
>>> from ecc import FieldElement, Point
>>> prime = 223
>>> a = FieldElement(0, prime)
>>> b = FieldElement(7, prime)
>>> x1 = FieldElement(num=192, prime=prime)
>>> y1 = FieldElement(num=105, prime=prime)
>>> p = Point(x1,y1,a,b)
>>> print(p+p)
Point(FieldElement_223(49),FieldElement_223(71))_FieldElement_223(0)_FieldElement_223(7)
>>> x1 = FieldElement(num=143, prime=prime)
>>> y1 = FieldElement(num=98, prime=prime)
>>> p = Point(x1,y1,a,b)
>>> print(p+p)
Point(FieldElement_223(64),FieldElement_223(168))_FieldElement_223(0)_FieldElement_223(7)
>>> x1 = FieldElement(num=47, prime=prime)
>>> y1 = FieldElement(num=71, prime=prime)
>>> p = Point(x1,y1,a,b)
>>> print(p+p)
Point(FieldElement_223(36),FieldElement_223(111))_FieldElement_223(0)_FieldElement_223(7)
>>> print(p+p+p+p)
Point(FieldElement_223(194),FieldElement_223(51))_FieldElement_223(0)_FieldElement_223(7)
>>> print(p+p+p+p+p+p+p+p)
Point(FieldElement_223(116),FieldElement_223(55))_FieldElement_223(0)_FieldElement_223(7)
>>> print(p+p+p+p+p+p+p+p+p+p+p+p+p+p+p+p+p+p+p+p+p)
Point(infinity)

# end::exercise4[]
# tag::exercise5[]
>>> prime = 223
>>> a = FieldElement(0, prime)
>>> b = FieldElement(7, prime)
>>> x = FieldElement(15, prime)
>>> y = FieldElement(86, prime)
>>> p = Point(x, y, a, b)
>>> inf = Point(None, None, a, b)
>>> product = p
>>> count = 1
>>> while product != inf:
...     product += p
...     count += 1
>>> print(count)
7

# end::exercise5[]
# tag::exercise6[]
>>> from ecc import S256Point, N, G
>>> point = S256Point(
...     0x887387e452b8eacc4acfde10d9aaf7f6d9a0f975aabb10d006e4da568744d06c, 
...     0x61de6d95231cd89026e286df3b6ae4a894a3378e393e93a0f45b666329a0ae34)
>>> z = 0xec208baa0fc1c19f708a9ca96fdeff3ac3f230bb4a7ba4aede4942ad003c0f60
>>> r = 0xac8d1c87e51d0d441be8b3dd5b05c8795b48875dffe00b7ffcfac23010d3a395
>>> s = 0x68342ceff8935ededd102dd876ffd6ba72d6a427a3edb13d26eb0781cb423c4
>>> u = z * pow(s, N-2, N) % N
>>> v = r * pow(s, N-2, N) % N
>>> print((u*G + v*point).x.num == r)
True
>>> z = 0x7c076ff316692a3d7eb3c3bb0f8b1488cf72e1afcd929e29307032997a838a3d
>>> r = 0xeff69ef2b1bd93a66ed5219add4fb51e11a840f404876325a1e8ffe0529a2c
>>> s = 0xc7207fee197d27c618aea621406f6bf5ef6fca38681d82b2f06fddbdce6feab6
>>> u = z * pow(s, N-2, N) % N
>>> v = r * pow(s, N-2, N) % N
>>> print((u*G + v*point).x.num == r)
True

# end::exercise6[]
# tag::exercise7[]
>>> from ecc import S256Point, G, N
>>> from helper import hash256
>>> e = 12345
>>> z = int.from_bytes(hash256(b'Programming Bitcoin!'), 'big')
>>> k = 1234567890
>>> r = (k*G).x.num
>>> k_inv = pow(k, N-2, N)
>>> s = (z+r*e) * k_inv % N
>>> print(e*G)
S256Point(f01d6b9018ab421dd410404cb869072065522bf85734008f105cf385a023a80f,
0eba29d0f0c5408ed681984dc525982abefccd9f7ff01dd26da4999cf3f6a295)
>>> print(hex(z))
0x969f6056aa26f7d2795fd013fe88868d09c9f6aed96965016e1936ae47060d48
>>> print(hex(r))
0x2b698a0f0a4041b77e63488ad48c23e8e8838dd1fb7520408b121697b782ef22
>>> print(hex(s))
0x1dbc63bfef4416705e602a7b564161167076d8b20990a0f26f316cff2cb0bc1a

# end::exercise7[]
"""
