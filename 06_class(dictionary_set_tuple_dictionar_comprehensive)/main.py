from typing import Dict, Union, Set


Key = Union[int, str]  # create custom type
Value = Union[int, str, list, dict, tuple]

data : Dict[Key, Value] = {
                         "fName":"Muhammad Aslan", 
                         "name":"Muhammad Qasim", 
                         "education":"MSDS",
                         "abc": [1,2,3],
                         "efg": {1:"hello"},
                         "hij": [(123, 456), ('123', '456')],
                         "klm": (123, 456),
                        #  set:{4,5,6,3,2,1} 
                        #   [1,2,3]: 'pakistan', # error
                        #   (1,2,3): "Pakistan", # error 
                        #   {1,2,3}: "Pakistan", # error
                         }
print(data['efg'][1])