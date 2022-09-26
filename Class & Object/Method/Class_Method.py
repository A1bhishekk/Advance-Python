class Mobile:

    price=19000
    
    @classmethod
    def show_model(cls, model):
        print(f"Model : {model} Price: {cls.price}")

mi=Mobile()
Mobile.show_model("MI 10i")