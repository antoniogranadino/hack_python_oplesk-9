"""
text: "fooziman" output => "foozimaN"
"""

def fn_hack_4():
    result = "fooziman"
    last_index = len(result) -1
    result = result[:last_index] + result[last_index].upper()
    return result