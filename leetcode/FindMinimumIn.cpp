
#include <vector>
using std::vector;

class FindMinimumIn{
public:
  //leetcode 153
  int findMin(vector<int>& nums){
    int left = 0,right = nums.size()-1;
    while(left < right){
      int mid = left + (right-left)/2;
      if(nums[mid] < nums[right]){
        right = mid;
      }else if(nums[mid] > nums[right]){
          left = mid + 1;
      }
    }
    return nums[left];
  }

  //leetcode 33
  int search(vector<int>& nums,int target){
    int left = 0,right = nums.size()-1;
    while(left <= right){
      int mid = left + (right-left)/2;
      if(nums[mid] == target){
        return mid;
      }
      if(nums[left] <= nums[mid]){
        if(nums[left] <= target&&target < nums[mid]){
          right = mid - 1;
        }else{
          left = mid+1;
        }
      }else{
        if(nums[mid] < target && target <= nums[right]){
          left = mid+1;
        }else{
          right = mid - 1;
        }
      }
    }
    return -1;
  }

  int main(){
    
  }
};