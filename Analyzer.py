from Folder import Folder
from Message import Message
from HandlerMessage import HandlerMessage
from queue import *
from queue import Empty


class Analyzer:

    def __init__(self, path_to_folder, input_queue, output_queue):
        self.path_to_folder = path_to_folder
        self.in_queue = input_queue
        self.out_queue = output_queue
        self.my_log = {}
        self.another_log_copy = {}

    def run(self):
        self.folder = Folder(self.path_to_folder)
        self.my_log = self.folder.get_log_file()
        self.out_queue.put(Message('__GET_LOG__', '', ''))
        while True:
            try:
                item = self.in_queue.get()
                HandlerMessage(item, self.folder, self.out_queue).run()
                self.out_queue.join()
            except Empty:
                pass

