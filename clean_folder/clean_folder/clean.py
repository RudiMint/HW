import os
import pathlib
import shutil

TRANS = {
        ord('а'): 'a', ord('б'): 'b', ord('в'): 'v', ord('г'): 'g', ord('д'): 'd', ord('е'): 'e',
        ord('ё'): 'yo', ord('ж'): 'zh', ord('з'): 'z', ord('и'): 'i', ord('й'): 'y', ord('к'): 'k',
        ord('л'): 'l', ord('м'): 'm', ord('н'): 'n', ord('о'): 'o', ord('п'): 'p', ord('р'): 'r',
        ord('с'): 's', ord('т'): 't', ord('у'): 'u', ord('ф'): 'f', ord('х'): 'h', ord('ц'): 'ts',
        ord('ч'): 'ch', ord('ш'): 'sh', ord('щ'): 'shch', ord('ъ'): 'y', ord('ы'): 'y', ord('ь'): "'",
        ord('э'): 'e', ord('ю'): 'yu', ord('я'): 'ya', ord('А'): 'A', ord('Б'): 'B', ord('В'): 'V',
        ord('Г'): 'G', ord('Д'): 'D', ord('Е'): 'E', ord('Ё'): 'Yo', ord('Ж'): 'Zh', ord('З'): 'Z',
        ord('И'): 'I', ord('Й'): 'Y', ord('К'): 'K', ord('Л'): 'L', ord('М'): 'M', ord('Н'): 'N',
        ord('О'): 'O', ord('П'): 'P', ord('Р'): 'R', ord('С'): 'S', ord('Т'): 'T', ord('У'): 'U',
        ord('Ф'): 'F', ord('Х'): 'H', ord('Ц'): 'Ts', ord('Ч'): 'Ch', ord('Ш'): 'Sh', ord('Щ'): 'Shch',
        ord('Ъ'): 'Y', ord('Ы'): 'Y', ord('Ь'): "'", ord('Э'): 'E', ord('Ю'): 'Yu', ord('Я'): 'Ya',
        ord("("): "_", ord(")"): "_", ord(","): "_", ord("!"): "_", ord("?"): "_", ord("-"): "_"
}

dirPath = input("enter path")

def normalize(text:str):
    return text.translate(TRANS)

def main():
    sortFiles(dirPath)

def sortFiles(path, createFolres = True):
    if os.path.exists(path):
        print(path + " exist")
        dirs = ["Videos", "Images", "Documents", "Music", "Archives", "Unknown"]
        imageExt = [".JPEG", ".PNG", ".JPG", ".SVG"]
        videoExt = [".AVI", ".MP4", ".MOV", ".MKV"]
        documentExt = [".DOC", ".DOCX", ".TXT", ".PDF", ".XLSX", ".PPTX"]
        musicExt = [".MP3", ".OGG", ".WAV", ".AMR"]
        archiveExt = [".ZIP", ".GZ", ".TAR"]
        if createFolres:
            for dirr in dirs:
                if not os.path.exists(os.path.join(path, dirr)):
                    os.mkdir(os.path.join(path, dirr))
        files = os.listdir(path)
        print(files)
        for item in files:
            if item in dirs:
                continue
            if os.path.isdir(os.path.join(path, item)):
                print(item + " is directory")
                sortFiles(os.path.join(path, item), False)
                os.rmdir(os.path.join(path, item))
            elif os.path.isfile(os.path.join(path, item)):
                print(item + " is file")
                if imageExt.count(pathlib.Path(os.path.join(path, item)).suffix.upper()):
                    shutil.move(os.path.join(path, item), os.path.join(dirPath, "Images", normalize(item)))
                elif videoExt.count(pathlib.Path(os.path.join(path, item)).suffix.upper()):
                    shutil.move(os.path.join(path, item), os.path.join(dirPath, "Videos", normalize(item)))
                elif documentExt.count(pathlib.Path(os.path.join(path, item)).suffix.upper()):
                    shutil.move(os.path.join(path, item), os.path.join(dirPath, "Documents", normalize(item)))
                elif musicExt.count(pathlib.Path(os.path.join(path, item)).suffix.upper()):
                    shutil.move(os.path.join(path, item), os.path.join(dirPath, "Music", normalize(item)))
                elif archiveExt.count(pathlib.Path(os.path.join(path, item)).suffix.upper()):
                    shutil.move(os.path.join(path, item), os.path.join(dirPath, "Archives", normalize(item)))
                else:
                    shutil.move(os.path.join(path, item), os.path.join(dirPath, "Unknown", normalize(item)))
    else:
        print(path + " do not exist")


