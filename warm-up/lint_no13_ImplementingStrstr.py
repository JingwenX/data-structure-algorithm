class Solution:
    """
    @param source: 
    @param target: 
    @return: return the index
    Example 1:
    	Input: source = "source" ，target = "target"
    	Output: -1
    	
    	Explanation: 
    	If the source does not contain the target content, return - 1.    

    Example 2:
    	Input:source = "abcdabcdefg" ，target = "bcd"
    	Output: 1
    	
    	Explanation: 
    	If the source contains the target content, return the location where the target first appeared in the source.
    test 1:
        Input: source = "source", target = "sourcez"
    test 2:
        Input: source = "source", target = "source"
    first submission:
        cannot pass
        Input: source = "tartarget", target = "target"
        expected: 3
        real: -1

    """
    def strStr(self, source, target):
        # Write your code here
        # thinking: one pointer, when encounter something starting with target, then index starting from that index, until the last one is comfirmed to be align. If encounter something diff, restart the i.
        i_source = 0
        i_target = 0
        first_ocr_index = -1
        if not target:
            return 0
        #while 3 < 9 - 6 + 1; source[3] == target[0], first_ocr_index = 3.
        while i_source < len(source) - len(target) + 1:
            print(i_source)
            if source[i_source] == target[0]:
                first_ocr_index = i_source

                #check if the later ones are align
                while i_target < len(target):
                    if i_target == len(target) - 1:
                        return first_ocr_index
                    elif source[i_source] == target[i_target]:
                        i_target += 1
                        i_source += 1
                    #corner case: when new i_source cannot keep aligning, but could possibly start a new alignment.
                    elif source[i_source] == target[0]:
                        first_ocr_index = i_source
                        continue
                    else:
                        first_ocr_index = -1
                        i_source += 1
                        break
            else:
                i_source += 1
                    
        return first_ocr_index

# this one has not pass the test yet...
            