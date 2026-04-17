impl Solution {
    pub fn single_number(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        for i in 0..n {
            let mut flag = true;
            for j in 0..n {
                if i != j && nums[i] == nums[j] {
                    flag = false;
                    break;
                }
            }
            if flag {
                return nums[i];
            }
        }
        -1
    }
}