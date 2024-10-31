"""
text: "fooziman" output => ["F","0","0","Z","1","M","@","N"]
"""

def fn_hack_10():
    result = "fooziman"
    result_dic = {
        'f': 'F',
        'o': '0',
        'o': '0',
        'z': 'Z',
        'i': '1',
        'm': 'M',
        'a': '@',
        'n': 'N'
    }
    result = [result_dic.get(char, char) for char in result]
    return result  

