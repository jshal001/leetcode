def merge(nums1, m, nums2, n):
        if n == 0:
            return
        elif m == 0:
            #populate nums 1 with nums2
            for i in range(len(nums2)):
                nums1[i] = nums2[i]
        else: 
            while (n > 0 and m > 0):
                if(nums2[n-1] >= nums1[m -1]):
                    nums1[m + n - 1] = nums2[n-1]
                    n -= 1
                else:
                    nums1[m + n - 1] = nums1[m - 1]
                    m-= 1
            if m == 0:
                while (n > 0):
                    nums1[n - 1] = nums2[n - 1]



nums1 = [1,2,3,0,0,0]
nums2 = [1]
m = 3
n = 1

print(merge(nums1, m, nums2, n))