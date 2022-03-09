#!/usr/bin/env python3


from quiz.parser import seeder
from quiz.seeder.calculus_1.differentials import payload, rdata


def main():
    moodle_quiz = seeder(payload, rdata)
    moodle_quiz.generate_latex_main_file()
    moodle_quiz.generate_questions(256)


if __name__ == "__main__":
    main()
