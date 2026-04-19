def merge_sorted(nums1, m, nums2, n):
    pt1 = m - 1
    pt2 = n - 1
    for i in range(m+n-1, -1, -1):
        if pt2 < 0:
            break
        if pt1 >= 0 and nums1[pt1] > nums2[pt2]:
            nums1[i] =  nums1[pt1]
            pt1 -= 1
        else:
            nums1[i] =  nums2[pt2]
            pt2 -= 1
    return nums1
    

# Driver code
def main():
    m = [9, 2, 3, 1, 8]
    n = [6, 1, 4, 2, 1]
    nums1 = [[23, 33, 35, 41, 44, 47, 56, 91, 105, 0, 0, 0, 0, 0, 0], [1, 2, 0], [1, 1, 1, 0, 0, 0, 0], [6, 0, 0], [12, 34, 45, 56, 67, 78, 89, 99, 0]]
    nums2 = [[32, 49, 50, 51, 61, 99], [7], [1, 2, 3, 4], [-99, -45], [100]]
    k = 1
    for i in range(len(m)):
        print(k, ".\tnums1: ", nums1[i], ", m: ", m[i], sep = "")
        print("\tnums2: ", nums2[i], ", n: ", n[i], sep = "")
        print("\n\tMerged list: ", merge_sorted(nums1[i], m[i], nums2[i], n[i]), sep = "")
        print("---")
        k += 1


if __name__ == "__main__":
    main()