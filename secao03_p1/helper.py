from typing import Any, List


def binarySearch(array: List, target: Any, match_by_obj_id: bool = False) -> int:
    def binarySearchHelper(array: List, target: Any, left: int, right: int) -> int:
        if left > right:
            return -1

        middle: int = (left + right) // 2
        potentialMatch: Any = array[middle].id if match_by_obj_id else array[middle]

        if target == potentialMatch:
            return middle
        elif target < potentialMatch:
            return binarySearchHelper(array, target, left, middle - 1)

        return binarySearchHelper(array, target, middle + 1, right)

    return binarySearchHelper(array, target, 0, len(array) - 1)
