import pywhatkit as pw
#storing in the text to be converted to handwritten piece in txt variable
#using 3 " because we want our to be represented in a proper format with divided paragraph changing at required instances
txt=input("Insert Text to covert to Handwriting: ")
output_path= r"C:\PYTHON311\PythonProjects\handrwitingConvertion.png"
pw.text_to_handwriting(txt,
                       output_path,
                       [47, 79, 79])
print("executed")
#printing to check whether execution is successful or not