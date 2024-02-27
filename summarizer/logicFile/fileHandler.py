def handle_uploaded_file(f):
    resultPara = ""
    for chunk in f.chunks():
        resultPara += str(chunk)
    return resultPara