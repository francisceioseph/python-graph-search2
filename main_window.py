from Tkinter import *
from input_dialog import *
from double_input_dialog import *
from graph import Graph
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import tkMessageBox
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use('TkAgg')

class MainWindow:
    def __init__(self, parent):
        self.parent = parent
        self.graph = None
        self.frame = None
        self.canvas = None
        
        self.__create_menubar(parent)
        self.__create_stage(parent)

    def __create_stage(self, parent):
        self.frame = Frame(parent)
        self.frame.pack()

    def __create_menubar(self, parent):
        menubar = Menu(parent)
        
        file_menu = Menu(menubar, tearoff=0)
        edit_menu = Menu(menubar, tearoff=0)
        view_menu = Menu(menubar, tearoff=0)            
        search_menu = Menu(menubar, tearoff=0)
        about_menu = Menu(menubar, tearoff=0)

        file_menu.add_command(label='Create a Graph...', command=self.create_graph)
        file_menu.add_separator()
        file_menu.add_command(label='Quit', command=self.quit)

        edit_menu.add_command(label='Create a Node...', command=self.create_node)
        edit_menu.add_command(label='Create an Arc...', command=self.create_arc) 

        view_menu.add_command(label='Redraw...', command=self.redraw_graph)

        search_menu.add_command(label='Depth Search First', command=self.perform_depth_search)
        search_menu.add_command(label='Breadth Search First', command=self.perform_breadth_search)

        about_menu.add_command(label='About', command=self.about)

        menubar.add_cascade(label="File", menu=file_menu)
        menubar.add_cascade(label="Edit", menu=edit_menu)     
        menubar.add_cascade(label="View", menu=view_menu)
        menubar.add_cascade(label="Search", menu=search_menu)
        menubar.add_cascade(label="About", menu=about_menu)

        parent.config(menu=menubar)

    def create_graph(self):
        input_string = InputDialog(self.frame, 'The max number of nodes').show()

        try:
            max_nodes = int(input_string)
            self.graph = Graph(max_nodes)
        except ValueError as e:
            tkMessageBox.showerror('Error', 'Plese, insert the number of nodes!')

    def quit(self):
        print self.parent.destroy()

    def create_node(self):

        if not self.graph:
            tkMessageBox.showerror('Error', 'Create a graph frist')
        else:
            label = InputDialog(self.frame, 'The label for this node:').show()
            
            if not label is None and len(label) > 0:
                self.graph.add_node_with_label(label)
            else:
                tkMessageBox.showerror('Error', 'Label entry is empty!')

    def create_arc(self):
        if not self.graph:
            tkMessageBox.showerror('Error', 'Create a graph frist')
        elif len(self.graph.nodes) < 2:
            tkMessageBox.showerror('Error', 'Create at least 2 nodes')
        else:
            entries = DoubleInputDialog(self.frame, 'Label of from node:', 'Label of to node:').show()
            self.graph.add_arc_with_labels(entries[0], entries[1])
            self.redraw_graph()

    def perform_depth_search(self):
        if not self.graph:
            tkMessageBox.showerror('Error', 'Create a graph frist')
        else:
            key =  InputDialog(self.frame, 'The label key for this search:').show()
            result = self.graph.depth_search(key)

            if result is None:
                tkMessageBox.showerror('Error', "Graph doesn\'t contain {0}".format(key))
            else:
                tkMessageBox.showinfo('Info', 'Found in graph: {0}'.format(result))

    def perform_breadth_search(self):
        if not self.graph:
            tkMessageBox.showerror('Error', 'Create a graph frist')
        else:
            key =  InputDialog(self.frame, 'The label key for this search:').show()
            result = self.graph.breadth_search(key)

            if result is None:
                tkMessageBox.showerror('Error', "Graph doesn\'t contain {0}".format(key))
            else:
                tkMessageBox.showinfo('Info', 'Found in graph: {0}'.format(result))

    def about(self):
        tkMessageBox.showinfo('Info', 'Developed by Francisco A. C. Souza' )

    def redraw_graph(self):
        if self.canvas:
            self.canvas.get_tk_widget().pack_forget()

        self.draw_graph(self.graph.connexions())

    def draw_graph(self, graph):
        graph_layout = 'shell'
        
        node_size = 800
        node_color = 'blue'
        node_alpha = 0.3
        node_text_size = 12

        edge_color = 'blue'
        edge_alpha = 0.3
        edge_tickness = 1.5

        nxGraph = nx.Graph()

        figure = Figure(figsize=(5, 4), dpi=100)
        plot_area = figure.add_subplot(111)

        for edge in graph:
            nxGraph.add_edge(edge[0], edge[1])

        graph_pos = nx.shell_layout(nxGraph)

        nx.draw_networkx_nodes(nxGraph, graph_pos, ax = plot_area, node_size = node_size, alpha = node_alpha, node_color = node_color)
        nx.draw_networkx_edges(nxGraph, graph_pos, ax = plot_area, width = edge_tickness, alpha = edge_alpha, edge_color = edge_color)
        nx.draw_networkx_labels(nxGraph, graph_pos, ax = plot_area, font_size=node_text_size)
        
        self.canvas = FigureCanvasTkAgg(figure, master=self.parent)
        self.canvas.show()
        self.canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)