# Take an Array and join it into a String - Only useful in the pre-discord implementation?
def stringify(delim, arr):
    output = ""
    length = len(arr)
    for i in range(length):
        output += arr[i] + ("", delim) [i < length - 1]
    return output

# Check for NaN- unused atm.
def isNaN(value):
    return int(value) != int(value)
