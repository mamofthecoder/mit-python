# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    # base case if the is only one character return that charcter
    if len(sequence)==1:
        return [sequence]
    # get all n-1(n is the length of the string) permutations using recursion
    subsequence_perms = get_permutations(sequence[1:])
    # keep the first letter of the string for later use
    first_letter = sequence[0]
    permus = list()
    # for subsequence permutation in subsequence permutations
    for subsequence_perm in subsequence_perms:
        # the range of the subsequence permutations plus one for first character
        for i in range(len(subsequence_perm)+1):
            # make the complete permutation 
            perm = subsequence_perm[:i] + first_letter + subsequence_perm[i:]
            # check for duplicates and add the permutations to a list
            if perm not in permus:
                permus.append(perm)
    permus.sort()
    return permus
        


if __name__ == '__main__':
#    #EXAMPLE
    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))
    print()
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    example_input = 'bed'
    print('Input:', example_input)
    print('Expected Output:', ['bde', 'bed', 'dbe', 'deb', 'ebd', 'edb'])
    print('Actual Output:', get_permutations(example_input))
    print()

    example_input = 'ti'
    print('Input:', example_input)
    print('Expected Output:', ['it', 'ti'])
    print('Actual Output:', get_permutations(example_input))
    print()

    example_input = 'a'
    print('Input:', example_input)
    print('Expected Output:', ['a'])
    print('Actual Output:', get_permutations(example_input))
    print()
