import os

def analyze_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        print(text)
    paragraphs = text.split('\n\n')
    sentences = text.split('.')
    words = text.split()
    file_size = os.path.getsize(file_path)

    return {
        "paragraphs": len(paragraphs),
        "sentences": len(sentences),
        "words": len(words),
        "size": file_size
    }

input_file=input("Enter file path: ")
counts=analyze_text(input_file)
print(counts)