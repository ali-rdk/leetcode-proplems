def read():
    n = int(input())
    heights = input().split(" ")
    
    if n > 10**6:
        raise Exception("n is too big")

    for i in range(len(heights)):
        if int(heights[i]) >= 0:
            heights[i] = int(heights[i])

    return heights, n

def largest_rectangle(heights):
    max_area = 0 
    stack = []

    for i, h in enumerate(heights):
        start = i 
        while stack and stack[-1][1] > h:
            index, height = stack.pop()
            max_area = max(max_area, height * (i - index))
            start = index
        stack.append((start, h))
    
    for i, h in stack:
        max_area = max(max_area, h * (len(heights) - i))
    
    return max_area

def main():
    heights, n  = read()
    max_area = largest_rectangle(heights)
    print(f"{max_area}")
 
if __name__ == "__main__":
    main()