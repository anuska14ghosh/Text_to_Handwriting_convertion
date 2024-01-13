import pywhatkit as pw
#storing in the text to be converted to handwritten piece in txt variable
#use 3 ""(quotations), while you input the text-to-be-converted here, it will represent text in a proper format with divided paragraphs, changing at required instances, else you can also using 1 " (quote) or 2 " (quotes)
txt=input("Insert Text to covert to Handwriting: ")
output_path= r"C:\PYTHON311\PythonProjects\handrwitingConvertion.png"
pw.text_to_handwriting(txt,
                       output_path,
                       [47, 79, 79])
print("executed")
#printing to check whether execution is successful or not
