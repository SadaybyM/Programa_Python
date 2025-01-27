def add_one():
    print(f"mum inside function {num}")
    num+=1
    print(f"num inside function ater adding 1{num}")

var=1
print(f"var before calling function {var}")
add_one(var)
print(f"var after calling function {var}")