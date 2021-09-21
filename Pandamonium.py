"""
Pandamonium
------------
Serialize + compress Pandas DataFrames.
"""

import pandas

def compress(dataframe, file_):
    csv = dataframe.to_csv()
    
    csv = csv.replace(",1", "¹")
    csv = csv.replace(",2", "º")
    csv = csv.replace(",3", chr(127))
    csv = csv.replace(",4", "¦")
    csv = csv.replace(",5", "¯")
    csv = csv.replace(",6", "«")
    csv = csv.replace(",8", chr(18))
    csv = csv.replace(",9", chr(19))
    csv = csv.replace(",7", chr(17)).encode(encoding="UTF-8")
    
    file = open(file_, "wb") # Fix this part 
    file.write(csv)
    file.close()
    return "Success!"
def decompress(file):
    a = open(file, "rb")
    a = a.read().decode(encoding="UTF-8")
    a = a.replace("«", ",6")
    a = a.replace("¦", ",4")
    a = a.replace("¹", ",1")
    a = a.replace("º", ",2")
    a = a.replace(chr(127), ",3")[1:]
    a = a.replace("¯", ",5")
    a = a.replace(chr(17), ",7")
    a = a.replace(chr(18), ",8")
    a = a.replace(chr(19), ",9")
    b = open(file, "w")
    b.write(a)
    b.close()
    df = pandas.read_csv(file)
    return df
if __name__ == "__main__":
    import time
    a = pandas.DataFrame({"Test 1-3": [12, 23, 34], "Test 4-6": [48, 65, 53], "Test 7-9": [93, 88, 70]})
    print(compress(dataframe=a, file_="C:/Users/jacob/Desktop/testing.pdc"))
    time.sleep(15)
    print("Waiting...")
    print(decompress("C:/Users/jacob/Desktop/testing.pdc"))
    ""
