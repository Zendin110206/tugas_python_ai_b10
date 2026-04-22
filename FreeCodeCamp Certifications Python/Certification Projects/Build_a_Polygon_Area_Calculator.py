class Rectangle:
    def __init__(self, width: int | float, height: int | float) -> None: 
        self.width = width
        self.height = height

    def set_height(self, height: int | float) -> None:
        self.height = height

    def set_width(self, width: int | float) -> None:
        self.width = width

    def get_area(self) -> float:
        return self.width * self.height

    def get_perimeter(self) -> float:
        return 2*(self.width + self.height)

    def get_diagonal(self) -> float:
        return (self.width **2 + self.height ** 2)**0.5

    def get_picture(self) -> str:
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        
        text = f"{'*' * self.width}\n"
        text *= self.height
        return text  
 
    def get_amount_inside(self, shape):
        count = 0
        print(f"Rectangle height: {self.height}")
        print(f"Rectangle width: {self.width}")
        print(f"Square side length: {shape.width}")
    
        width_fit = self.width // shape.width
        height_fit = self.height // shape.height
    
        return width_fit * height_fit

    def __repr__(self) -> str:
        return f"Rectangle(width={self.width}, height={self.height})"

class Square(Rectangle):
    def __init__(self, length: int | float):
        super().__init__(length,length)

    def set_side(self, length):
        self.width = length
        self.height = length

    def set_height(self, length):
        self.width = length
        self.height = length

    def set_width(self, length):
        self.width = length
        self.height = length

    def __repr__(self) -> str:
        return f"Square(side={self.width})"



rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
