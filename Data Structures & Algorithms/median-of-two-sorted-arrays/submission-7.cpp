class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        if (nums1.size() > nums2.size()) {
            return findMedianSortedArrays(nums2, nums1);
        }

        int n = nums1.size();
        int m = nums2.size();
        int half = (n + m) / 2;

        // Define i as the number of elements in nums1 that is left of the median
        int start = 0, end = n;
        while (start <= end) {
            int i = (start + end) / 2;
            int j = half - i;
            int left1 = (i > 0) ? nums1[i-1] : INT_MIN;
            int right1 = (i < n) ? nums1[i] : INT_MAX;
            int left2 = (j > 0) ? nums2[j-1] : INT_MIN;
            int right2 = (j < m) ? nums2[j] : INT_MAX;

            if (left1 > right2) {
                end = i - 1;
            } else if (left2 > right1) {
                start = i + 1;
            } else {
                if ((n + m) % 2 == 0) {
                    return 0.5 * (max(left1, left2) + min(right1, right2));
                } else {
                    return min(right1, right2);
                }
            }
        }

        return -1.0;
    }
};