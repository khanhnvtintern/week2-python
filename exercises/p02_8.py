
#Cho một danh sách các số, hãy tìm và in tất cả các phần tử lớn hơn phần tử trước 
def hw() : 
    lst = [1,5,2,4,3]
    #lst = [5,5,5,5,5]
    fst = lst[0]
    r = []
    #print(len(lst)) #debug
    for i in range(1, len(lst)): 
        #print(i,lst[i])#debug :3
        if lst[i] >= fst : 
            r.append(lst[i])
        fst = lst[i]
    return r
if __name__ == "__main__":
    r = hw()
    print(r)