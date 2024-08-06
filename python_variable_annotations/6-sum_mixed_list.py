#!/usr/bin/env python3

""" Complex types - mixed list """
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """type-annotated function sum_mixed_list which takes a list mxd_lst of integers and floats and returns their sum as a float."""
<<<<<<< HEAD
    return sum(sum_mixed_list)
=======
    return sum(mxd_lst)

>>>>>>> 4164cae0417dc6e120e3601285e7a733876f606a
