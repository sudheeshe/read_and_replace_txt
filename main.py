from pathlib import Path

def find_and_replace(file, find_txt, replace_txt):
    """
    Description: This Function finds the text to be replaced and replace it with the given text
    Parameters : file : filename in which the text to be found and replace
                find_txt: The text to locate in the given file
                replace_txt: the text to replace the located text

    return: None
    """



    try:
        file = Path(file)
        data = file.read_text()
        data = data.replace(find_txt, replace_txt)
        file.write_text(data)


    except Exception as e:
        raise e


if __name__ == '__main__':
    find_and_replace(file = 'example.txt', find_txt='placement', replace_txt='screening')