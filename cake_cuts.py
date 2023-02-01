"""
leetcode 1465
https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/
"""

def max_area(horizental_cuts, vertical_cuts):
    horizental_cuts.sort()
    vertical_cuts.sort()

    max_height = 0
    max_width = 0
    perv_height = 0
    perv_width = 0

    for cut in horizental_cuts:
        max_height = max(max_height, cut - perv_height)
        perv_height = cut

    for cut in vertical_cuts:
        max_width = max(max_width, cut - perv_width)
        perv_width = cut
    
    return (max_height * max_width) % 1000000007

def main():
    info = input().split(" ")
    q = int(info.pop())
    info = list(map(int, info))

    horizental_cuts = [info[1]]
    vertical_cuts = [info[0]]
    results = []
    for _ in range(q):
        tmp = input().split(" ")
        if tmp[0] == "H":
            horizental_cuts.append(int(tmp[1]))
        else:
            vertical_cuts.append(int(tmp[1]))

        results.append(max_area(horizental_cuts, vertical_cuts)) 

    for result in results:
        print(result)

if __name__ == "__main__":
    main()
