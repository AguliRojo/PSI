def function(a_list,b_list):
    return a_list[1:len(a_list):2] + b_list[0:len(a_list):2]

print(function([i for i in range(5,43,3)],[i for i in range(5,22,3)]))
#list must be called by square brackets , because list is not a callable funtion