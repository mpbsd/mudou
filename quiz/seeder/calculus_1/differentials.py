import random


payload = {
    "directory": "calculus_1",
    "filename": "differentials.tex",
    "title": "Diferenciais",
}


def rdata():
    r = random.randint(11, 22)
    e = round(random.uniform(0, 1), 2)
    dV_over_V = 3 * (e / r)
    rand = {
        0: {
            0: r,
            1: e,
            2: round(dV_over_V, 3),
        },
    }
    return rand
