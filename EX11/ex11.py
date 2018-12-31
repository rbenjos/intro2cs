import itertools
import copy

class Node:
    """
    represents a single node in the decision tree. a node can either be
    a branch or a leaf, its a branch if it's data is a question, and if it
    leads to other nodes. its a leaf if it doesnt lead to any more nodes
    """

    def __init__(self, data, pos=None, neg=None):
        """
        the default will be to handle every node as its a leaf,
        meaning to set the children to None
        :param data: either an illness if the node is a leaf, or a symptom
        if the node is not a leaf
        :param pos: the positive child, the node that handles the illnesses
        that do have the symptom in the data
        :param neg: the negative child, the node that handles the illnesses
        that don't have the symptom in the data
        """
        self.data = data
        self.positive_child = pos
        self.negative_child = neg

    def get_data(self):
        """

        :return: the data of the node
        """
        return self.data

    def get_pos(self):
        """

        :return: the positive child of the node
        """
        return self.positive_child

    def get_neg(self):
        """

        :return: the negative child of the node
        """
        return self.negative_child

    def set_data(self, data):
        """
        sets the data to a new one
        :param data: our new data
        :return:
        """
        self.data = data

    def set_pos(self, pos):
        """
        sets the positive child of the node to a new one
        :param pos: the new positive child
        :return:
        """
        self.positive_child = pos

    def set_neg(self, neg):
        """
        sets the negative child of the node to a new one
        :param neg: the new negative child
        :return:
        """
        self.negative_child = neg

    def is_leaf(self):
        """

        :return: True if the node is a leaf, False if its not
        """
        if self.positive_child is None:
            return True
        else:
            return False

    def print_node(self):
        """

        :return: a printable list of all the leaves this branch has
        """
        if self.is_leaf():
            return self.data
        else:
            list_of_leaves = []
            list_of_leaves = self.all_leaves(list_of_leaves)
            return str(list_of_leaves)


    def all_leaves(self,list_of_leaves):
        if self.is_leaf():
            return [self.data]
        else:
            list_of_leaves += self.get_pos().all_leaves(list_of_leaves)
            list_of_leaves += self.get_neg().all_leaves(list_of_leaves)
            return list_of_leaves


class Record:
    """
    represent a single illness, has a name and a list of symptoms defining it
    """

    def __init__(self, illness, symptoms):
        """

        :param illness: the name of our illness
        :param symptoms: the list of symptoms defining that illness
        """
        self.illness = illness
        self.symptoms = symptoms

    def print_record(self):
        """

        :return: a string that represents that record
        """
        string = "[ "
        string += str(self.illness) +', '
        string += str(self.symptoms)
        string += " ]"
        return string

    def get_illness(self):
        """

        :return:
        """
        return self.illness

    def get_symptoms(self):
        """

        :return:
        """
        return self.symptoms

def parse_data(filepath):
    with open(filepath) as data_file:
        records = []
        for line in data_file:
            words = line.strip().split()
            records.append(Record(words[0], words[1:]))
        return records


class Diagnoser:
    """
    represents a tool used to diagnose different illnesses based on a decision
    tree (Node type)
    in addition, the Diagnoser class has additional functions that can asses
    the quality of the diagnosis, and give information about the decision tree
    """

    def __init__(self, root):
        """

        :param root: the first node of the decision tree
        """
        self.root = root

    def diagnose(self, symptoms):
        """

        :param symptoms: the list of symptoms we use to diagnose the illness
        :return: the name of the illness our tree diagnosed
        """
        node = self.root
        return self.diagnose_helper(node, symptoms)

    def diagnose_helper(self, cur_node, symptoms):
        """
        does most of the diagnostic work.
        :param cur_node:
        :param symptoms:
        :return:
        """

        if cur_node.is_leaf():
            '''
            adding for now the code to handle a case of symptoms outside the
            tree
            
            if len(symptoms) == 0:
                return cur_node.get_data()
            else:
                return None
            
            '''
            # if its a leaf, we reached a diagnosis and can return it
            return cur_node.get_data()

        else:
            # if its not a leaf we need to keep diagnosing

            cur_node_symptom = cur_node.get_data()

            if cur_node_symptom in symptoms:
                return self.diagnose_helper(cur_node.get_pos(), symptoms)
            else:
                return self.diagnose_helper(cur_node.get_neg(), symptoms)

    def calculate_success_rate(self, records):
        """
        this function calculates the success rate of our decision tree
        its given a list of illnesses and their symptoms, and gives those
        symptoms to our decision tree, if our tree returns the right name of
        the illness, it counts it as a success.
        :param records: our list of illnesses and their symptoms
        :return: the ratio of succesful diagnoses to the number of records
        in general
        """
        counter = 0
        for record in records:
            illness = record.get_illness()
            sympotms = record.get_symptoms()
            if self.diagnose(sympotms) == illness:
                counter += 1
        ratio = counter / len(records)
        return ratio

    def all_illnesses(self):
        """

        :return: a list of all the illnesses our tree has as leaves, ordered
        by their frequency of appearance
        """

        # first we will make a dictionary of illnesses, with their names
        # as keys, and their number of appearances as the value
        self.illness_dic = {}
        all_illnesses_helper(self.root)

        # then we will convert this dictionary to an ordered list and return it
        all_illnesses_list = sorted(self.illness_dic, key=self.illness_dic.get,
                                    reverse=True)
        return all_illnesses_list

    def all_illnesses_helper(self, cur_node):
        """
        fills the dictionary of illnesses
        :param cur_node: our current node in the tree
        :return:
        """
        if cur_node.is_leaf():
            # if we are on a leaf, we will add 1 to the relevant illness
            # in the dictionary
            self.illness_dic[cur_node.get_data()] += 1
        else:
            # if its not a leaf, we will call this function upon the negative
            # and positive child of this branch
            pos = cur_node.get_pos()
            neg = cur_node.get_neg()
            self.all_illnesses_helper(pos)
            self.all_illnesses_helper(neg)

    # def all_illnesses_sort(self, illnesses_dic):
    #     """
    #     this function takes the dictionary of illnesses from our diagnoser
    #     and converts it into a list of illnesses ordered by their number
    #     of appearances.
    #     it does so recursively
    #     :return: the list of illnesses ordered by their number of appearances
    #     """
    #
    #     # if there are no more illnesses, we will an empty list
    #     if len(illnesses_dic) == 0:
    #         return []
    #     cur_list = list()
    #
    #     cur_maximal = None
    #     maximal_index = 0
    #     for illness in illnesses_dic:
    #         if illnesses_dic[illness] > maximal_index:
    #             cur_maximal = illness
    #             maximal_index = illnesses_dic[illness]
    #     cur_list.append(cur_maximal)
    #     illnesses_dic.pop(cur_maximal)
    #     cur_list += self.all_illnesses_sort(illnesses_dic)
    #     return cur_list

    def most_rare_illness(self, records):
        """
        this will return the rarest illness in our tree based on the list of
        records its given (and not on the illnesses that are in our decision
        tree)
        :param records: the list of illnesses need to pick the most rare one
         from
        :return: the most rare illness in our list
        """
        illnesses_dic = {}
        for record in records:
            illness = self.diagnose(record.get_symptoms)
            illnesses_dic[illness] += 1
        illnesses_list = sorted(illnesses_dic, key=illnesses_dic.get,
                                       reverse=True)
        return illnesses_list[-1]

    def paths_to_illness(self, illness):
        """

        :param illness: the illness we want to find the paths for
        :return: a list of all possible paths to get to this illness
        """
        path = []
        root = self.root
        list_of_paths = []
        return self.paths_to_illness_helper(illness, path, root, list_of_paths)

    def paths_to_illness_helper(self, illness, path, cur_node, list_of_paths):
        """
        we will find all our paths by backtracking. trying all paths and
        if we get to a leaf that has our illness, we will append the path
        to the list of all paths
        :param illness: the illness we find the paths for
        :param path: our current path
        :param cur_node: the node we are currently on
        :param list_of_paths: the list of all paths leading to this illness
        :return: list_of_paths
        """

        # if we got to a leaf that has our illness, we will append the current
        # path to this list and return it (with or without the path)
        if cur_node.is_leaf():
            if cur_node.get_data() == illness:
                list_of_paths.append(path)
            return list_of_paths
        # if we are not on a leaf yet, we will run this function on the
        # positive/negative child node, and note our choice in the current path
        else:
            path.append(True)
            self.paths_to_illness_helper(illness, path, cur_node.get_pos(),
                                         list_of_paths)
            path[-1] = False
            self.paths_to_illness_helper(illness, path, cur_node.get_neg(),
                                         list_of_paths)
            return list_of_paths


def build_tree(records, symptoms):
    """
    this is our decision tree builder. most of the work will be done on the
    helper. here we just set the root of the tree, and return the full tree
    once its complete

    :param records: the list of illnesses we are currently handling
    :param symptoms: the list of symptoms we use to diagnose those illnesses
    :return: the complete decision tree
    """
    root = Node(symptoms[0])
    root = build_tree_helper(records, symptoms)
    return root


def build_tree_helper(all_records,symptoms):
    """
    most of the building is done here. every time we will take our first
    symptom in the list, and make it a question, dividing our illnesses to
    2 lists, those who have the symptom, and those who dont. once we did that
    our current symptom is no longer relevant and we can remove it from the
    list of symptoms. then we will run this function again on the positive
    child (who handles all the illnesses that do have this symptom)
    and on the negative child (who handles all the illnesses that dont have
    this symptom)

    :param all_records: the list of illnesses we are currently handling
    :param symptoms: the list of symptoms we use to diagnose those illnesses
    :return: our current branch of the desicion tree, the node we just handled
    """
    if len(symptoms) == 0:
        '''
        if there are no more symptoms to check, we diagnosed our illness
        and this is a leaf. so we are going to set the data to the name of the
        illness , and the leaf's children to None
        if there is more then one illness, we will choose the most common
        one
        '''
        most_common = most_common_ill(all_records)
        cur_node = Node(most_common)
        cur_node.set_pos(None)
        cur_node.set_neg(None)
        return cur_node

    else:
        '''
        if there are still symptoms to check, we will divide our illnesses
        to 2 groups. those who have the first symptom in our list, and those
        who have'nt. then we will remove that symptom from the list, and
        run the function again on the 2 lists of records
        '''

        # our records divider, later to be refactored
        records_w_symptom = []
        records_wo_symptom = []
        # print ('!!!',symptoms[0],'!!!')
        cur_node = Node(symptoms[0])
        for record in all_records:
            if symptoms[0] in record.get_symptoms():
                records_w_symptom.append(record)
            else:
                records_wo_symptom.append(record)
        # print(records_w_symptom)
        # print(records_wo_symptom)

        symptoms_for_pos = copy.deepcopy(symptoms)
        symptoms_for_neg = copy.deepcopy(symptoms)
        symptoms_for_pos.pop(0)
        symptoms_for_neg.pop(0)

        # handling both the illnesses with our symptom and w/o it

        pos = build_tree_helper(records_w_symptom, symptoms_for_pos)
        cur_node.set_pos(pos)
        neg = build_tree_helper(records_wo_symptom, symptoms_for_neg)
        cur_node.set_neg(neg)

        return cur_node


def optimal_tree(records, symptoms, depth):
    """

    :param records: the list of illnesses and their symptoms
    :param symptoms: the list of symptoms we can use in our tree
    :param depth: the number of symptoms we are allowed to check
    :return: the best decision tree with the given depth
    """

    symptoms_subsets_of_depth = list(itertools.combinations(symptoms,depth))

    # we will make dictionary of trees, with the subsets of symptoms as their
    # keys, and theirs success rates as values

    dic_of_trees = {}
    for subset_of_symptoms in symptoms_subsets_of_depth:
        root = build_tree(records, subset_of_symptoms)
        subset_diagnoser = Diagnoser(root)
        success_rate = subset_diagnoser.calculate_success_rate(records)
        dic_of_trees[subset_of_symptoms] = success_rate

    # then we will convert it into an ordered list, and take the first tree

    ordered_list_of_trees = sorted(dic_of_trees,key=dic_of_trees.get,
                                   reverse=True)




def most_common_ill(records):
    """

    :param records: a list of illnesses and their symptoms
    :return: the most common illness in the list
    """
    if len(records) == 0:
        return 'Unknown'
    illness_dic = {}
    for record in records:
        if record.get_illness() in illness_dic.keys():
            illness_dic[record.get_illness()] += 1
        else:
            illness_dic[record.get_illness()] = 1
    ordered_illness_list = sorted(illness_dic,key=illness_dic.get,reverse=True)
    return ordered_illness_list[0]

if __name__ == "__main__":

    # Manually build a simple tree.
    #                cough
    #          Yes /       \ No
    #        fever           healthy
    #   Yes /     \ No
    # influenza   cold
    #
    # flu_leaf = Node("influenza", None, None)
    # cold_leaf = Node("cold", None, None)
    # inner_vertex = Node("fever", flu_leaf, cold_leaf)
    # healthy_leaf = Node("healthy", None, None)
    # root = Node("cough", inner_vertex, healthy_leaf)
    #
    # diagnoser = Diagnoser(root)
    #
    # # Simple test
    # diagnosis = diagnoser.diagnose(["cough"])
    # if diagnosis == "cold":
    #     print("Test passed")
    # else:
    #     print("Test failed. Should have printed cold, printed: ", diagnosis)

    records = parse_data('small_data.txt')
    symptoms = ['cough','fever','nausea','fatigue','sore_throat','muscle_ache',
                'cngestion','rigidity','irritability']
    # diagnoser = Diagnoser(build_tree(records,symptoms))
    # print (diagnoser.root.print_node())
    for record in records:
        print(record.print_record())
        # print (diagnoser.diagnose(symptoms))



# Add more tests for sections 2-7 here.
