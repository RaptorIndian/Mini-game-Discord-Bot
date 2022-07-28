def stringify(delim, arr):
    output = ""
    length = len(arr)
    for i in range(length):
        output += arr[i] + ("", delim) [i < length - 1]
    return output

def isNaN(value):
    return int(value) != int(value)