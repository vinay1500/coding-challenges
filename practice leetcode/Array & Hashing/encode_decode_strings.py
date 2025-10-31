class Solution:
    def encode(self, strs):
        encoded_string = ""
        for str in strs:
            encoded_string += f"{len(str)}#{str}"
        return encoded_string

    def decode(self, str):
        result , i = [], 0
        while i < len(str):
            j = i
            while str[j] != "#":
                j += 1
            length = int(str[i:j])
            result.append(str[j+1 : j+1+length])
            i = j + 1 + length
        
        return result


strs = ["lintlintlint","code","love","you"]
myObj = Solution()
encoding = myObj.encode(strs)
print(encoding)
decoding = myObj.decode(encoding)
print(decoding)



        #encoded_string = f"{lambda for str in strs: len(str)}"
        #len(str in strs)";".join(strs)




        #encoded_string = ";".join(strs)
        #for str in strs:
        #    print(str)
        #    encoded_string = "".join(strs)
        #    print(encoded_string)
        #print(encoded_string)
        #return encoded_string
        # write your code here
'''
        result, i = [],0
        for i in range(len(str)):
            j = i
            while str[j] != "#":
                j +=1
                i +=1
            result.append(str.)
            print(range(len(str)))
            x = ""
            print(i,str[i].isdigit())
            if str[i].isdigit():
                x +=f"{x}{str[i]}"
                print(x,i)
                i +=1
                print(x,i)
            elif str[i] == "#":
                print("in elif")
                n = int(x)
                for j in range(n):
                    str = "".join(str[i+j+1])
                    result.append(str)
                    i = i + x + 1
            else:
                print("this is an else loop for testing")
        return result
         '''




        #for i in range(len(str)):
        #    words = str.split(';')
        #return words

        # write your code here