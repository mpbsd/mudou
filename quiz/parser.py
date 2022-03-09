#!/usr/bin/env python3


import jinja2


class seeder:
    def __init__(self, payload, rdata):
        self.payload = payload
        self.rdata = rdata

    def generate_latex_main_file(self):
        title = self.payload["title"]
        filename = self.payload["filename"]
        dir = jinja2.FileSystemLoader('quiz/template')
        env = jinja2.Environment(loader=dir)
        tpl = env.get_template('latex_main_file.tex')
        main_file = tpl.render(quiz_name=title, questions_file=filename)
        print("\nCreating brew/main.tex")
        with open("brew/main.tex", "w") as f:
            print(main_file, file=f)
        print("Done.")

    def generate_questions(self, n):
        directory = "quiz/template/{}".format(self.payload["directory"])
        filename = self.payload["filename"]
        if isinstance(n, int) and n > 1:
            dir = jinja2.FileSystemLoader(directory)
            env = jinja2.Environment(loader=dir)
            tpl = env.get_template(filename)
            questions = ""
            for i in range(n):
                questions += tpl.render(rdata=self.rdata(), qNumber=i)
                if i < n - 1:
                    questions += "\n\n"
            print("\nCreating brew/%s" % filename)
            with open("brew/%s" % filename, "w") as f:
                print(questions, file=f)
            print("Done.\n")
        else:
            print("There must be at least 2 versions of each question\n")
