class WordsFinder:
    file_names = []
    all_words = {}

    def __init__(self, *name):
        self.file_names = name

    def get_all_words(self):
        for file_name in self.file_names:
            list_ = []
            with open(file_name, encoding='utf-8') as file:
                for line in file:
                    line.lower()
                    for p in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                        line = line.replace(p, '')
                    list_.extend(line.split())
            self.all_words[file_name] = list_
        return self.all_words

    def find(self, word):
        dict_ = {}
        for name, words in self.get_all_words().items():
            a = 1
            for n in words:
                if word.lower() in n.lower():
                    dict_[name] = a
                    break
                a += 1
        return dict_

    def count(self, word):
        dict_ = {}
        for name, words in self.get_all_words().items():
            a = 0
            for n in words:
                if word.lower() in n.lower():
                    a += 1
            dict_[name] = a
        return dict_


finder2 = WordsFinder('test_file.txt', 'Rudyard Kipling - If.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
