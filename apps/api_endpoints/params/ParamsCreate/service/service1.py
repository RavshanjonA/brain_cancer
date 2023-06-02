g1 = [[0.1, 0.1, 0.1, 0.1, 0.1, 0.1],
      [0.1, 0.1, 0.1, 0.1, 0.1, 0.2],
      [0.1, 0.1, 0.3, 0.1, 0.1, 0.2],
      [0.1, 0.1, 0.1, 0.1, 0.1, 0.4],
      [0.1, 0.1, 0.1, 0.1, 0.1, 0.3],
      [0.1, 0.1, 0.1, 0.1, 1, 9],
      [0, 1, 1, 1, 1, 2],
      [1, 0, 1, 1, 1, 2],
      [1, 1, 1, 1, 1, 7],
      [1, 1, 1, 1, 1, 10]]
g2 = [
    [1, 1, 1, 2, 1, 2],
    [0, 1, 1, 2, 1, 2],
    [1, 1, 1, 2, 2, 2],
    [1, 1, 2, 2, 1, 2],
    [1, 1, 1, 2, 1, 1]
]
g3 = [
    [1, 1, 2, 1, 1, 1],
    [1, 1, 2, 2, 1, 1]
]
g4 = [
    [1, 1, 2, 1, 1, 2],
    [1, 1, 2, 1, 2, 2]

]


def predictor(params_data):
    data = [
        params_data['x2'],
        params_data['x6'],
        params_data['x11'],
        params_data['x12'],
        params_data['x18'],
        params_data['x19']
    ]
    j1, j2, j3, j4 = 0, 0, 0, 0

    for row in g1:
        j1 += int(row[0] == data[0]) + int(row[1] == data[1]) + int(row[2] == data[2]) + int(row[3] == data[3]) + int(
            row[4] == data[4])
    for row in g2:
        j2 += int(row[0] == data[0]) + int(row[1] == data[1]) + int(row[2] == data[2]) + int(row[3] == data[3]) + int(
            row[4] == data[4])
    for row in g3:
        j3 += int(row[0] == data[0]) + int(row[1] == data[1]) + int(row[2] == data[2]) + int(row[3] == data[3]) + int(
            row[4] == data[4])
    for row in g4:
        j4 += int(row[0] == data[0]) + int(row[1] == data[1]) + int(row[2] == data[2]) + int(row[3] == data[3]) + int(
            row[4] == data[4])
    return {"class1": j1 / 10, "class2": j2 / 5, "class3": j3 / 2, "class4": j4 / 2}


print(predictor({"x2": 1, "x6": 2, "x11": 1, "x12": 1, "x18": 1, "x19": 1}))
