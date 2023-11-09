fakeH, w = map(int, input().split())
blocks = list(map(int, input().split()))
h = max(blocks)
water = h * w - sum(blocks)
idxFromLeft = 0
spillLeft = h - blocks[0]
while spillLeft:
    water -= spillLeft
    idxFromLeft += 1
    spillLeft = min(spillLeft, h - blocks[idxFromLeft])
idxFromRight = w - 1
spillRight = h - blocks[w - 1]
while spillRight:
    water -= spillRight
    idxFromRight -= 1
    spillRight = min(spillRight, h - blocks[idxFromRight])
print(water)
