from django.shortcuts import render
from .models import Admins,User,Department,UserhasDep,AdminsHasDep
from django.contrib import messages
from .forms import UserForm,AdminsForm
from nltk.corpus import stopwords,wordnet
from pdfminer.high_level import extract_text
import aspose.pydrawing as drawing
import aspose.words as aw
import pytesseract
import docx2txt
import PIL.Image
import random
import fitz
import math
import glob
import io
import os
import cv2
#===============================================================
#===============================================================
def Portition(lest, P, R):
    pivot = lest[P]
    k = P + 1
    j = R
    while j >= k:
        up = lest[k]
        down = lest[j]
        if up >= pivot:
            k += 1
        elif down <= pivot:
            j -= 1
        else:
            lest[k], lest[j] = lest[j], lest[k]
    if j < k or lest[j] <= pivot:
        lest[P], lest[j] = lest[j], lest[P]
        Q = j
        return Q
def Randomaized_Partition(lest, P, R):
    Rand = random.randint(P, R)
    lest[P], lest[Rand] = lest[Rand], lest[P]
    Q = Portition(lest, P, R)
    return Q
def Quick_Sort(lest, P, R):
    if P < R:
        Q = Randomaized_Partition(lest, P, R)
        Quick_Sort(lest, P, Q-1)
        Quick_Sort(lest, Q+1, R)
#===============================================================
#===============================================================
def query(querys):
    stop_words_english = set(stopwords.words('english'))
    stop_words_Arabic = set(stopwords.words('Arabic'))
    punctuations = '''!()-[]{}\;:'",\n<>./?@#$%^&*_~'''
    list_querys = []
    text = ''
    for word_query in querys:
        for char in word_query:
            if char not in punctuations:
                text += char
        if text != '':
            if text[0] in 'abcdefghigklmnopqrstuvwxyz':
                if text not in stop_words_english:
                    list_querys.append(text)
            else:
                if text[0] in 'د ج ح خ ه ع غ ف ق ث ص ض ذ ط ك م ن ت ا ل ب ي س ش ظ ز و ة ى ر ؤ ء ئ لا':
                    if text not in stop_words_Arabic:
                        list_querys.append(text)
        text = ''
    set_querys = set(list_querys)
    return set_querys
#===============================================================
#===============================================================
def IMAGES(path):
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\\tesseract.exe'
    img = cv2.imread(path)
    img_text = pytesseract.image_to_string(img).lower().replace('\n', ' ')
    return img_text
#===============================================================
#===============================================================
def ChiakImageFormat(path):
    if path[len(path)-4:].lower() == "jpeg":
        result = True
    elif path[len(path)-3:].lower() in ["png", "jpg"]:
        result = True
    else:
        result = False
    return result
#===============================================================
#===============================================================
def Text(path):
    with open(path) as file_txt:
        text_read = file_txt.read().lower().replace('\n', ' ')
    return text_read
#===============================================================
#===============================================================
def Word(path):
    # open the file and read text
    all_text_word = docx2txt.process(path).lower().replace('\n', ' ')
    # load the Word document
    doc = aw.Document(r''+path)
    # retrieve all shapes
    shapes = doc.get_child_nodes(aw.NodeType.SHAPE, True)
    imageIndex = 1
    # loop through shapes
    for shape in shapes:
        shape = shape.as_shape()
        if (shape.has_image) :
            # set image file's name
            path_of_image = f"Image{imageIndex}{aw.FileFormatUtil.image_type_to_extension(shape.image_data.image_type)}"
            # save image
            shape.image_data.save(path_of_image)
            # check if type image in image format
            if bool(ChiakImageFormat(path_of_image)):
                # read text from image
                img_text_png = IMAGES(path_of_image)
                # check if image contain on text
                if img_text_png != '':
                    # add text image in all text
                    all_text_word += ' ' + img_text_png
            # delete image
            os.remove(path_of_image)
            # number of image
            imageIndex += 1
    return all_text_word
#===============================================================
#===============================================================
def PDF(path):
    pdf = fitz.open(path)
    imageIndex = 1
    all_text_pdf = extract_text(path).lower().replace('\n', ' ')
    for i in range(len(pdf)):
        page = pdf[i]
        images = page.get_images()
        for imag in images:
            base_img = pdf.extract_image(imag[0])
            image_data = base_img['image']
            img = PIL.Image.open(io.BytesIO(image_data))
            extension = base_img['ext']
            # save image
            img.save(open(f'image{imageIndex}.{extension}', 'wb'))
            # path the image
            path_of_image = f'image{imageIndex}.{extension}'
            # check if type image in image format
            if bool(ChiakImageFormat(path_of_image)):
                # read text from image
                img_text_png = IMAGES(path_of_image)
                # check if image contain on text
                if img_text_png != '':
                    # add text image in all text
                    all_text_pdf += ' ' + img_text_png
            # delete image
            os.remove(path_of_image)
            # number of image
            imageIndex += 1
    return all_text_pdf
#===============================================================
#===============================================================
#index
from nltk.corpus import stopwords
from nltk.corpus import wordnet
def fre_word_doc(text_read):
    punctuations = '''!()-[]{}\;:'",\n<>./?@#$%^&*_~'''
    stop_words_english = set(stopwords.words('english'))
    stop_words_Arabic = set(stopwords.words('Arabic'))
    set_fre_word = {}
    list_final_text2 = []
    list_lemmas_text = []
    final_list_lemmas = []
    text = ''
    list_text_read = list(map(str, text_read.split()))
    for word in list_text_read:
        for char in word:
            if char not in punctuations:
                text += char
        if text != '':
            if text[0] in 'abcdefghigklmnopqrstuvwxyz':
                if text not in stop_words_english:
                    list_final_text2.append(text)
            else:
                if text[0] in 'د ج ح خ ه ع غ ف ق ث ص ض ذ ط ك م ن ت ا ل ب ي س ش ظ ز و ة ى ر ؤ ء ئ لا':
                    if text not in stop_words_Arabic:
                        list_final_text2.append(text)
        text = ''
    for index in range(len(list_final_text2)):
        for synset in wordnet.synsets(list_final_text2[index]):
            for lemma in synset.lemmas():
                if lemma.name() not in list_lemmas_text:
                    list_lemmas_text.append(lemma.name())
        if list_final_text2[index] not in list_lemmas_text:
            list_lemmas_text.append(list_final_text2[index])
        for word in list_lemmas_text:
            final_list_lemmas.append(word)
        list_lemmas_text = []
    set_lemmas_text = set(final_list_lemmas)
    for word in set_lemmas_text:
        set_fre_word.setdefault(word, final_list_lemmas.count(word))
    return set_fre_word
#===============================================================
#===============================================================
#ReadAllFile
def ReadFile(path):
    list_path_files = path.copy()
    index_file = 0
    Index_File_NotDefindType = []
    pointer_fre_word = []
    while index_file < len(path):
        if path[index_file][len(path[index_file])-3:].lower() == 'txt':
            text_read = Text(path[index_file])
            index_file += 1
        elif path[index_file][len(path[index_file])-4:].lower() == 'docx':
            text_read = Word(path[index_file])
            index_file += 1
        elif path[index_file][len(path[index_file])-3:].lower() == 'pdf':
            text_read = PDF(path[index_file])
            index_file += 1
        elif bool(ChiakImageFormat(path[index_file])):
            text_read = IMAGES(path[index_file])
            index_file += 1
        else:
            Index_File_NotDefindType .append(index_file)
            list_path_files.remove(path[index_file])
            index_file += 1
            continue
        pointer_fre_word.append(fre_word_doc(text_read))
        
    return pointer_fre_word, Index_File_NotDefindType, list_path_files
#===============================================================
#===============================================================
#Ranhedretrieval
def Rank(ReadAllTypeFiles, Querys):
    frequnency_word, Index_File_NotDefindType, list_path_files = ReadAllTypeFiles
    set_querys = Querys
    set_fre_text = {}
    list_fre_text = []
    query_idf_weight = []
    tf_idf_weight = {}
    tf_idf_list = []
    list_score = []
    set_score = {}
    cosine_score = {}
    list_cosine_score = []
    list_cosine_score_text = []
    index2 = 0
    index_list_count_fre_text = 0
    index4 = 0
    list_count_fre_text = list(0 for j in range(len(set_querys)))
    for index1 in range(len(list_path_files)):
        for word in set_querys:
            if word in frequnency_word[index1]:
                list_fre_text.append(frequnency_word[index1].get(word))
                list_count_fre_text[index_list_count_fre_text] += 1
                index_list_count_fre_text += 1
            else:
                list_fre_text.append(0)
        index_list_count_fre_text = 0
        set_fre_text.setdefault(list_path_files[index1], list_fre_text)
        list_fre_text = []
    for index3 in range(len(list_count_fre_text)):
        if list_count_fre_text[index3] != 0:
            idf = math.log(len(list_path_files) / list_count_fre_text[index3])
            query_idf_weight.append(idf)
        else:
            query_idf_weight.append(0)
    if len(list_path_files) == 1:
        if sum(set_fre_text.get(list_path_files[0])) < 1:
            return 'No results were found'
    else:
        for path in list_path_files:
            while index2 < len(set_fre_text.get(path)):
                if set_fre_text.get(path)[index2] != 0 and list_count_fre_text[index2] != 0:
                    tf_idf = (1 + math.log(set_fre_text.get(path)[index2])) * math.log(len(list_path_files) / list_count_fre_text[index2])
                    index2 += 1
                    tf_idf_list.append(tf_idf)
                else:
                    tf_idf_list.append(0)
                    index2 += 1
            index2 = 0
            tf_idf_weight.setdefault(path, tf_idf_list)
            tf_idf_list = []
            for index3 in range(len(query_idf_weight)):
                score = tf_idf_weight.get(path)[index3] * query_idf_weight[index3]
                list_score.append(score)
            set_score.setdefault(path, list_score)
            list_score = []
            cosine_score.setdefault(path, sum(set_score.get(path)))
            if cosine_score.get(path) != 0:
                list_cosine_score.append(cosine_score.get(path))
    Quick_Sort(list_cosine_score, 0, len(list_cosine_score)-1)
    list_order = list(cosine_score.items())
    if len(list_cosine_score) != 0:
        while index4 < len(list_cosine_score):
            for item in list_order:
                if item[1] == list_cosine_score[index4] and item[1] != 0:
                    if item[0] not in list_cosine_score_text:
                        list_cosine_score_text.append('files/'+item[0][14:])
                        index4 += 1
                        break
        return str(list_cosine_score_text[:10])
    else:
        return 'No results were found'
#===============================================================
#===============================================================
def Result(q):
    querys = q.split()
    files = glob.glob("testfile/file/*")
    files = list(files)
    result_text = Rank(ReadFile(files), query(querys))
    return result_text
#===============================================================
#===============================================================
#===============================================================
#===============================================================
def admins(request): 
    if request.method == 'POST':
        userid = request.POST['AdminName']
        pass_word = request.POST['pass']
        if bool(Admins.objects.filter(UserName = userid,Password=pass_word)):
            return render(request,'pages/index.html')
    return render(request,'pages/admin.html')

def signup(request):  
    if request.method == 'POST':    
        userid = request.POST['signup_username']
        password = request.POST['signup_password']
        email = request.POST['signup_email']
        if not bool(User.objects.filter(username = userid)) and not bool(User.objects.filter(e_mail = email)):
            User.objects.create(username=userid, Password=password,e_mail=email)
            return render(request,'pages/login.html')
    return render(request,'pages/login.html')

def login(request):  
    if request.method == 'POST':    
        userid = request.POST['Username']
        pass_word = request.POST['Password']
        if bool(User.objects.filter(username = userid,Password=pass_word)) :
            return render(request,'pages/index.html')
    return render(request,'pages/login.html')


def index(request):
    input_search = request.POST.get('department')
    if input_search != None:
        k = Result(input_search)
        k = k[1:len(k)-1]
        k2 = []
        text = ''
        char={'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0,'.':0,'/':0}
        for i in k:
            if i != ',':
                if char.get(i.lower()) != None:
                    text += i
            else:
                k2.append(text)
                text = ''
        k2.append(text)
        text = ''
        return render(request,'pages/search.html',{'data':Department.objects.filter(path_file__in=k2)})
    else:
        return render(request,'pages/index.html')
    
def search(request):
    return render(request,'pages/search.html')

def cis(request):
    return render(request,'pages/cis.html')

def bit(request):
    return render(request,'pages/bit.html')

def cs(request):
    return render(request,'pages/cs.html')

def subject(request):
    return render(request,'pages/subject.html')

def subject1(request):
    return render(request,'pages/subject1.html')

def subject2(request):
    return render(request,'pages/subject2.html')