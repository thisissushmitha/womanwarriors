import joblib
import numpy as np
import pandas as pd

model = joblib.load("model.pkl")
p="India"
y=2023
while (y!=2050):
        y+=1
        p=str(y)+"-01-01T00:00:00"
        input_sample = pd.DataFrame({"Economy": pd.Series([p], dtype="object"), "Report Year": pd.Series([p], dtype="object")})
        x=model.predict(input_sample)
        if(x==100.00)
                print("Congradulations",p,"will reach 100% by",y)
                break
if(y == 2051)
        print("Oops need to work harder to reach 100% before 2050")
  

