import pandas as pd

df = pd.DataFrame({
    'Buah-buahan' : ['Nanas', 'Anggur', 'Lengkeng'],
    'Sayuran' : ['Kentang', 'Kubis', 'Brokoli']
})
print(df.rename(index={0:'',1:'',2:''}))