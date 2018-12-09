import math


def print_k_subsets(n, k):
    if k <= n:
        cur_set = [None]*n
        index = 0
        picked = 0
        fill_k_subsets_helper(k, cur_set, index, picked, )

def k_subsets_helper(k, cur_set, index, picked):
    if picked==k:
        print_set(cur_set)
        return
    if index == len(cur_set):
        return
    cur_set[index]=True
    fill_k_subsets_helper(k, cur_set, index + 1, picked + 1, )
    cur_set[index]=False
    fill_k_subsets_helper(k, cur_set, index + 1, picked, )

def print_set(cur_set):
    print ('{',end=' ')
    for (index, in_cur_set) in enumerate(cur_set):
        if in_cur_set:
            print(index, end=' ')
    print('}')


def fill_k_subsets(n, k, lst):
    if k <= n:
        cur_set = [None]*n
        index = 0
        picked = 0
        fill_k_subsets_helper(k, cur_set, index, picked, lst)

def fill_k_subsets_helper(k, cur_set, index, picked, lst):
    if picked==k:
        lst.append(build_set(cur_set))
        return
    if index == len(cur_set):
        return
    cur_set[index]=True
    fill_k_subsets_helper(k, cur_set, index + 1, picked + 1, lst)
    cur_set[index]=False
    fill_k_subsets_helper(k, cur_set, index + 1, picked, lst)

def build_set(cur_set):
    numbered_set = []
    for (index, in_cur_set) in enumerate(cur_set):
        if in_cur_set:
            numbered_set.append(index)
    return  numbered_set

def nCk(n,k):
    value = math.factorial(n)/(math.factorial(k)*math.factorial(n-k))
    return value
fill_k_subsets(10, 6, [])



def return_k_subsets(n, k):
    if k <= n:
        index = 0
        return return_k_subsets_helper(n,k,index)

def return_k_subsets_helper(n,k,index):
    lst_of_lsts=[]
    if index>=n:
        return []
    else:

        lst =[index]+return_k_subsets_helper(n,k,index+1)
        lst2= []+return_k_subsets_helper(n,k,index+1)

        print (lst,lst2 )
        print(index)
        if len(lst)>k:
            return[]
        print (lst)

        if len(lst) == k:
            lst_of_lsts.append(lst)
            if lst_of_lsts:
                if len(lst_of_lsts) == nCk(n,k):
                    return lst_of_lsts
        return lst


def build_set_from_number(cur_set):
    numbered_set = []
    for (index, in_cur_set) in enumerate(cur_set):
        if in_cur_set:
            numbered_set.append(index)
    return  numbered_set

return_k_subsets(8,5)
