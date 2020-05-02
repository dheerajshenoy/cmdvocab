def combine_arr(arr):
    STR = ""
    for i in range(0,len(arr)):
        STR = STR + arr[i]
    return STR
        
def pos(search_ele,arr):
    for i in range(0,len(arr)):
        if(arr[i] == search_ele):
            return i

def combine_indele(arr):
    comb = []
    STR = ""
    for i in range(0,len(arr)):
        STR=""
        for l in range(0,len(arr[i])):
            STR = STR + arr[i][l]
        comb.append(STR)
    return comb

def FileVarValueChange(filename,keyword,value,splitter):
    with open(filename,'a+') as f:
        items = []
        for lines in f:
            items.append(lines)
        for i in range(len(items)):
            p = pos(splitter,items[i])
            if(keyword == items[i][0:p]):
                items[i] = str(keyword)+ str(splitter) + '\"'+ str(value) + '\"' + '\n'
                f.truncate(0)
                for i in items:
                    f.write(i)
    f.close()

def FileVarGetValue(filename,keyword,splitter):
    with open(filename,'a+') as f:
        items = []
        var = ""
        for lines in f:
            items.append(lines)
        
        for i in range(len(items)):
            p = pos(splitter,items[i])
            if(keyword == items[i][0:p]):
                var = items[i][p+1:]
                break
        
        return(var)
    f.close()            
def have_internet():
    conn = httplib.HTTPConnection("www.google.com", timeout=5)
    try:
        conn.request("HEAD", "/")
        conn.close()
        return True
    except:
        conn.close()
        return False
    
def cmd_hr_line(column,symbol):
    ch = ""
    for i in range(column):
        ch = ch + str(symbol)
    return(ch)
    
    
        
    
