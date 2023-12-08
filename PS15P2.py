class Car:
  def __init__(self, make, model, sticker_price):
      self.make = make
      self.model = model
      self.stickerPrice = sticker_price
      self.discountPrice = 0.9 * sticker_price

  def displayInfo(self):
      print(f"Make: {self.make}\nModel: {self.model}\nSticker Price: ${self.stickerPrice}\nDiscount Price: ${self.discountPrice}")

class Sport(Car):
  def __init__(self, make, model, sticker_price):
      super().__init__(make, model, sticker_price)
      self.optionPrices = {'SportWheels': 1000.00, 'SportEngine': 3000.00, 'SportInterior': 2000.00}
      self.selectedOptions = {'SportWheels': False, 'SportEngine': False, 'SportInterior': False}

  def setOption(self, option):
      if option in self.selectedOptions:
          self.selectedOptions[option] = True

  def priceWithOptions(self):
      updatedPrice = self.discountPrice
      for option, selected in self.selectedOptions.items():
          if selected:
              updatedPrice += self.optionPrices[option]

      print(f"Updated Price with Options: ${updatedPrice}")

if __name__ == "__main__":
 
  car1 = Car("Toyota", "Camry", 25000)
  car1.displayInfo()

 
  sport1 = Sport("Ford", "Mustang", 40000)
  sport1.displayInfo()

 
  sport1.setOption('SportWheels')
  sport1.setOption('SportEngine')


  sport1.priceWithOptions()
