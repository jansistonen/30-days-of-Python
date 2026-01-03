# Filter only negative and zero in the list using list comprehension

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

negatives = [i for i in numbers if i <= 0]
print(negatives)

# Flatten the following list of lists of lists to a one dimensional list :
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

#output
#[1, 2, 3, 4, 5, 6, 7, 8, 9]
flattened_list = [ number for outer in list_of_lists for inner in outer for number in inner]
print(flattened_list)

