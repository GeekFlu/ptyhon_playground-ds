"""
Given a linked list, swap the two nodes present at position i and j, assuming 0 <= i <= j. The positions are based on 0-based indexing.

Note: You have to swap the nodes and not just the values.

Example:

    linked_list = 3 4 5 2 6 1 9
    positions = 2 5
    output = 3 4 1 2 6 5 9

Explanation:
    The node at position 3 has the value 2
    The node at position 4 has the value 6
    Swapping these nodes will result in a final order of nodes of 3 4 5 6 2 1 9

Algorithm:

    PL -> Previous Left Node
    CL -> Current Left Node

    PR -> Previous Right Node
    CR -> Current Right Node

    1) General case, when head node or/and tail node are not swapped

        PL.next = CR
        temp = CR.next
        CR.next = CL.next
        PR.next = CL
        CL = temp

    2) If head needs to ber swapped

        2.1 We create a Temporal Head and apply 1) algorithm
            TH -> Temporal Head
"""