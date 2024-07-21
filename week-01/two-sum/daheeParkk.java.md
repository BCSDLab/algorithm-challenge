# Intuition
주어진 배열을 정렬하고, target과 가깝게 큰 숫자를 찾는다.
합쳐서 target이 되는 값들을 for문으로 찾을 때의 범위를 0부터 target과 가깝게 큰 숫자로 하여 경우의 수를 줄인다.

# Approach
```java
1. 주어진 배열을 copyNums에 복사한 후 copyNums를 오름차순으로 정렬한다.
2. copyNums에서 target과 가깝게 큰 숫자의 index를 찾는다.
3. copyNums에서 0부터 target과 가깝게 큰 숫자의 index까지를 범위로 설정한 for문을 반복한다.
4. 이중 for문으로 범위 내의 모든 수를 더해보며 target과 동일한지 찾고, 동일하면 두 수를 반환한다.
5. 처음 주어진 배열에서 for문으로 두 수를 찾으며 각각의 index를 반환한다.
```

# Code
```java
class Solution {
    public int[] twoSum(int[] nums, int target) {
        int size = nums.length;
        int[] copyNums = new int[size];
        System.arraycopy(nums, 0, copyNums, 0, size);
        Arrays.sort(copyNums);

        int nearIndex = findTargetNear(copyNums, size, target);
        int[] resultNums = findSumTarget(copyNums, nearIndex, target);
        return findIndex(nums, size, resultNums);
    }

    public int[] findIndex(int[] nums, int size, int[] resultNums) {
        int firstNum = resultNums[0];
        int secondNum = resultNums[1];
        int[] resultIndex = new int[]{-1, -1};

        for (int i=0; i<size; i++) {
            int num = nums[i];

            if ((firstNum == num || secondNum == num) && resultIndex[0] == -1) {
                resultIndex[0] = i;
            } else if (firstNum == num || secondNum == num) {
                resultIndex[1] = i;
                return resultIndex;
            }
        }
        return resultIndex;
    }

    public int findTargetNear(int[] nums, int size, int target) {
        if (nums[size-1] > target) {
            return size-1;
        }
        int minNear = -1;
        int index = size;
        index /= 2;
        while (index >= 1) {
            if (nums[index] < target) {
                if (minNear == -1) {
                    if (index == size-1) {
                        return index;
                    } 
                    index = (index+size) / 2;
                } else {
                    return minNear;
                }
            } else {
                minNear = index;
                index /= 2;
            }
        }
        return 1;
    }

    public int[] findSumTarget(int[] nums, int index, int target) {
        for (int i=0; i<=index-1; i++) {
            int firstNum = nums[i];
            for (int j=i+1; j<=index; j++) {
                int secondNum = nums[j];

                if (firstNum + secondNum == target) {
                    return new int[]{firstNum, secondNum};
                }
            }
        }
        return new int[]{0, 0};
    }
}
```
