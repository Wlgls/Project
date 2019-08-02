import time
from pathlib import Path
import readline

class conf(object):

    def __init__(self):

        self.base_dir = '/home/smith/myblog/_posts/'

        self.title_format = '%Y-%m-%d-{}.md'

        self.layout = 'post'

        self.base_program_dir = '/home/smith/Script/create_file/'

        self.content_format_file = self.base_program_dir + 'content_format.txt'

        self.param = []

    def get_title_format(self):

        return time.strftime(self.title_format, time.localtime())

    def get_content_param_name(self):
        
        p = Path(self.content_format_file)

        if p.exists():

            with p.open() as f:
                
                lines = f.readlines()

                self.content_first = 1
                self.content_end = lines[1:].index('---\n')

                # print(self.content_first, self.content_end)

                for line in lines[self.content_first: self.content_end+1]:
                    self.param.append(line.split(':')[0])

        return self.param

    def get_content_format(self):
        
        params_name = self.get_content_param_name()

        # print(params_name)

        params_value = [eval("input('{}:')".format(item)) for item in params_name[1:]]

        params_value.insert(0, self.layout)
        
        # params_value = ['test', 'test', 'test']

        params = dict(zip(params_name, params_value))

        self.title = params['title']

        with open(self.content_format_file) as f:

            content = f.read()

        """ 
            I was going to use the dictionary, but because of '{:toc}', I always meet IndexError, 
            I tried to solve this problem in some ways  but I failed. 
        """

        content_list = content.split('---\n\n')
            
        content_list[0] = content_list[0].format(**params)

        content = '---\n\n'.join(content_list)
        
        return content


class create_file(object):

    def __init__(self):

        self.conf = conf()

        self.content_format = self.conf.get_content_format()

        self.file_title = self.conf.get_title_format().format(self.conf.title)

        self.base_dir = self.conf.base_dir



    def make_file(self):
        
        p = Path(self.base_dir + self.file_title)

        if not p.exists():
            p.touch()

        p.write_text(self.content_format)

    


if __name__ == '__main__':

    create_file().make_file()