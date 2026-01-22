def merge(nums1, m, nums2, n):
    s = m - 1
    t = n - 1
    e = m + n - 1

    if m == 0:
        for i in range(n):
            nums1[i] = nums2[i]

    while e >= 0 and s >= 0 and t >= 0:
        if nums1[s] < nums2[t]:
            nums1[e] = nums2[t]
            t -= 1

        elif nums1[s] > nums2[t]:
            nums1[e] = nums1[s]
            if s != e:
                nums1[s] = 0
            s -= 1

        else:
            nums1[e] = nums2[t]
            e -= 1
            nums1[e] = nums1[s]
            if s != e:
                nums1[s] = 0
            t -= 1
            s -= 1

        e -= 1

    while e >= 0 and t >= 0:
        nums1[e] = nums2[t]
        e -= 1
        t -= 1
