def square_numbers(start,end):
    all_squares=[]
    even_squares=[]
    odd_squares=[]
    
    
    for num in range(start,end+1):
        square=num*num
        all_squares.append(square)
        if square%2==0:
            even_squares.append(square)
        else:
            odd_squares.append(square)
            
    
    print("All squares:",all_squares)
    print("Even squares:",even_squares)
    print("Odd squares:",odd_squares)

start=int(input("Enter start number: "))
end=int(input("Enter end number: "))

square_numbers(start,end)
