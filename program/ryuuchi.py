import pandas as pd

a = ['Black coffee original','Vietnam drip','Espresso','Caffe Latte','Hazelnut Latte','Mocha Latte','White Choco Mocha','Affogato','Choco Mint','Delnaco']
b = ['25 K','27 k','28 K','30 K','35 K','37 K','40 K','40 K','42 K','43 K']

df = pd.DataFrame({
'abc' : a,
'Cost' : b
})
