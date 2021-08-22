import os


class Dir(object):
    def __init__(self, path):
        self.__path = path
        self.__error_list = list()

    def check(self):
        self.__error_list = list()
        self.__error_list.append(
            {
                'path': self.__path,
                'error_type': 'HasNonAscII',
                'error_msg': 'The dirs exist non ASCII character need modify.'
            }
            if not self.__check_path_name() else {}
        )

    def __check_path_name(self):
        global gCheckEncodeResult
        result = len(self.__path) == len(self.__path.encode())
        if not result:
            gCheckEncodeResult = False
            print('HasNoAscII: \'{}\' exist not ASCII character '
                  'need to modify.'.format(self.__path))
        return result


class File(object):
    def __init__(self, path):
        self.__path = path
        self.__content = self.__read()

    def check(self):
        self.__error_list = list()
        self.__error_list.append(
            {
                'path': self.__path,
                'error_type': 'HasNonAscII',
                'error_msg': 'The content name exist not ASCII '
                             'character need to modify.'
            }
            if not self.__check_content() else {}
        )
        self.__error_list.append(
            {
                'path': self.__path,
                'error_type': 'HasNonAscII',
                'error_msg': 'The dirs exist non ASCII character need modify.'
            }
            if not self.__check_path_name() else {}
        )

    def __check_path_name(self):
        global gCheckEncodeResult
        result = len(self.__path) == len(self.__path.encode())
        if not result:
            gCheckEncodeResult = False
            print('HasNoAscII: \'{}\' exist not ASCII character '
                  'need to modify.'.format(self.__path))
        return result

    def __check_content(self):
        global gCheckEncodeResult

        def print_error(result):
            for i in range(len(result)):
                if result[i]:
                    pass
                else:
                    print('[ERROR] \'{}\':{}  Has non-ascii character '
                          'please modify!'.format(self.__path, i+1))

        result = list(map(lambda x: len(x) == len(x.encode()), self.__content))

        if len(result) != sum(result):
            gCheckEncodeResult = False
            print_error(result)
            return False
        else:
            return True

    def __read(self):
        # TODO: If file not fetch success.
        result = list()

        try:
            fp = open(self.__path, 'r', encoding='utf8')
            result = fp.readlines()
        except UnicodeDecodeError:
            print('[INFO] \'{}\' Skip check not a text file.'
                  .format(self.__path))
        fp.close()
        return result


class CheckEncode(object):
    def __init__(self, path):
        self.__path = path
        self.__dirs_list, self.__files_list = self.__get_files_path()

    def get_dirs_files_data(self):
        return self.__dirs_list, self.__files_list

    def __get_files_path(self):
        #
        # To exclude the folder name as the following.
        # Prevent local-side CI check would fail.
        #
        files_list = list()
        dirs_list = list()
        exclude_dirs = set([
            '.git', '.venv', 'build', 'dist', 'htmlcov',
            '__pycache__', '.pytest_cache'
            ])
        exclude_files = set(['LICENSE'])
        for root, dirs, files in os.walk(self.__path, topdown=True):
            dirs[:] = [d for d in dirs if d not in exclude_dirs]
            files[:] = [f for f in files if f not in exclude_files]
            for name in files:
                files_list.append(os.path.join(root, name))
            for name in dirs:
                dirs_list.append(os.path.join(root, name))
        return dirs_list, files_list


if __name__ == '__main__':
    gCheckEncodeResult = True

    dirs_list, files_list = CheckEncode(os.getcwd()).get_dirs_files_data()

    dirs_obj_list = list(map(lambda x: Dir(x), dirs_list))
    dirs_obj_check_list = list(map(lambda x: x.check(), dirs_obj_list))

    files_obj_list = list(map(lambda x: File(x), files_list))
    files_obj_check_list = list(map(lambda x: x.check(), files_obj_list))

    print('[Result] Check encode result: {}'.format(gCheckEncodeResult))
    if gCheckEncodeResult:
        print('[Result] Check encode pass!')
        exit(0)
    else:
        print('[Result] Check encode fail!')
        exit(1)
