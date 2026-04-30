def my_function():
    class innerClass:
        def greet(self):
            return "Hello from innerClass"
      
    obj=innerClass()
    print(obj.greet())
    
my_function()    