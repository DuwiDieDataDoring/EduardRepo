from mypackage import myFunction, recursion, sorting

def test_top_n():
    """
    make sure top_n works correctly
    """

    assert myFunction.top_n([8, 3, 2, 7, 4], 3) == [8, 7, 4], 'incorrect'
    assert myFunction.top_n([10, 1, 12, 9, 2], 2) == [12, 10], 'incorrect'
    assert myFunction.top_n([1, 2, 3, 4, 5], 5) == [5, 4, 3, 2, 1], 'incorrect'

##Recursion testing
def sum_array():

    assert recursion.sum_array([1,2,3]) == 6
    assert recursion.sum_array([4,5,6]) == 15
    assert recursion.sum_array([7,8,9]) == 24

def fibonacci():

    assert recursion.fibonacci(10) == 55
    assert recursion.fibonacci(20) == 6765
    assert recursion.fibonacci(30) == 832040

def factorial():

    assert recursion.factorial(3) == 6
    assert recursion.factorial(6) == 720
    assert recursion.factorial(9) == 362880

def reverse():

    assert recursion.reverse('Eduard') == 'draudE'
    assert recursion.reverse('Emil') == 'limE'
    assert recursion.reverse('Senekal') == 'lakeneS'

##Sorting testing
def bubble_sort():

    assert.sorting.bubble_sort([88,93,43,44,12,23,3]) == [3, 12, 23, 43, 44, 88, 93]
    assert.sorting.bubble_sort([33,55,78,23,11,3,4]) == [3, 4, 11, 23, 33, 55, 78]
    assert.sorting.bubble_sort([9,2,15,67,12,26,3]) == [2, 3, 9, 12, 15, 26, 67]

def merge_sort():

    assert.sorting.merge_sort([54,26,93,17,77,31,44,55,20]) == [17, 20, 26, 31, 44, 54, 55, 77, 93]
    assert.sorting.merge_sort([24,33,63,97,37,2,5,44,20]) == [2, 5, 20, 24, 33, 37, 44, 63, 97]
    assert.sorting.merge_sort([12,8,43,22,89,1,25,76,20]) == [1, 8, 12, 20, 22, 25, 43, 76, 89]

def quick_sort():

    assert.sorting.quick_sort([99,88,77,66,55,44,33,22,11,0]) == [0, 11, 22, 33, 44, 55, 66, 77, 88, 99]
    assert.sorting.quick_sort([999,888,777,666,555,444,333,222,111,0]) == [0, 111, 222, 333, 444, 555, 666, 777, 888, 999]
    assert.sorting.quick_sort([98,87,76,65,54,43,32,21,10,0]) == [0, 10, 21, 32, 43, 54, 65, 76, 87, 98]
