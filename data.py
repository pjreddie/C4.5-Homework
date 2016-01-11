class Point:
    def __str__(self):
        return "<" + self.label + ": " +  `self.values` + ">"
    def __repr__(self):
        return "<" + self.label + ": " +  `self.values` + ">"
    def __init__(self, label, values):
        self.label = label
        self.values = values

def get_label(s, labels):
    for l in labels:
        if l in s:
            return l
    raise Exception('Label not found', s)

def string_statistics(s):
    s = s.lower()
    values = [0]*32
    total = len(s)
    for c in s:
        n = ord(c)
        if 97 <= n <= 122:
            values[n-97] += 1
        elif c == '.':
            values[26] += 1
        elif c == ',':
            values[27] += 1
        elif c == '?':
            values[28] += 1
        elif c == '!':
            values[29] += 1
        elif c in '0123456789':
            values[30] += 1
        else:
            values[31] += 1
    for i in range(len(values)):
        values[i] /= float(total)
    return values

def get_data(filename, labels):
    f = open(filename)
    data = []
    for line in f:
        line = line.strip()
        label = get_label(line.split("."), labels)
        s = open(line).read()
        values = string_statistics(s)
        data.append(Point(label, values))
    return data

def get_spam_train_data():
    labels = ("ham", "spam")
    return get_data("spam/train.list", labels)

def get_spam_valid_data():
    labels = ("ham", "spam")
    return get_data("spam/valid.list", labels)

def get_college_data():
    data = [
        Point('College', [24, 40000]),
        Point('No College', [53, 52000]),
        Point('No College', [23, 25000]),
        Point('College', [25, 77000]),
        Point('College', [32, 48000]),
        Point('College', [52, 110000]),
        Point('College', [22, 38000]),
        Point('No College', [43, 44000]),
        Point('No College', [52, 27000]),
        Point('College', [48, 65000])
    ]
    return data



