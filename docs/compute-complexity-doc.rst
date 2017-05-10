CMPTCOMPLEXITY
++++++++++++++



.. Contents::


INTRODUCTION
============


cmptcomplexity is a Python module, providing a way to deduce computational complexity of given Python code bits.




PREREQUISITES
=============

cmptcomplexity requires the following software installed for your platform:


1) NumPy__

__ http://www.numpy.org/

2) MatPlotLib__

__ http://matplotlib.org/

3)  Scipy__

__ https://www.scipy.org/

INSTALLING CMPTCOMPLEXITY
=========================

Development version from Git
----------------------------
Use the command::

  pip3 install git+https://github.com/AGHPythonCourse2017/zad2-moskalap.git

UNINSTALLING
============
Type::

  pip3 uninstall cmptcomplexity


USING CMPTCOMPLEXITY
====================

BASIC USE
---------

To run cmptcomplexity after installation, first, you have to import module

   >>> import cmptcomplexity.aprox as cmpt

To get information about complexity of sorting list, you could type


   >>> results = cmpt.count_it(pattern_invoke= 'sorted(list)',init_code='import random; list = [random.randint(1,10000) for i in range (__N__)]')

After executing this, you can:

    >>> results.complexity #'O(N log N)'
    >>> how_long = results.how_long()
    >>> how_long(100000) #42.769611954961221
    >>> in_time = results.in_time()
    >>> in_time(42.76) # 99979.94052065522
    >>> results.show() #shows a plot
    >>> results.show('sorted') #saves a plot to file sorted_plot.png
    >>>


    .. image:: https://raw.githubusercontent.com/AGHPythonCourse2017/zad2-moskalap/master/docs/img/sorted_plot.png?token=AWCREl9JX-_57k3FLB0UyIl52kAYEdNHks5ZFyCJwA%3D%3D



For more information read `PYTHON INTERFACE`_


.. _`PYTHON INTERFACE`

PYTHON INTERFACE
================

INPUTS
------

The main function (count_it) is included in cmptcomplexity.aprox.


*cmptcomplexity.aprox.*
**count_it(pattern_invoke, init_code, clean_up_code, timeout, verbose)**

Before using this function, it is necessary to prepare a simple structures for an algorithm:

pattern_invoke
    An invoking pattern of tested function/method/class, with '__N__' as a size-problem parameter.
    pattern_invoke could be string or a path to file, where this string is typed.

    example
        Let's assume an object **example_object** with the method **example_method(arg1, arg2, arg3, arg4)**, where **arg3** is problem-sized parameter.
        Proper structure assignment would be like

        >>> pattern_invoke = 'example_object.example_method(arg1,arg2,__N__,arg4)'

        alternatively, you could create a file **/home/user/dir0/dir1/pattern.py'** with following content

        .. code-block:: python

            example_object.example_method(arg1,arg2,__N__,arg4)

        and then assign pattern_invoke to a path to this file

        >>> pattern_invoke = '/home/user/dir0/dir1/pattern.py'


init_code(optional)
    This structure contains a code, which time execution shouldn't be measured.
    The creation of this structure is similar to **pattern_invoke**. If you want to test a self-defined class/method/function, in this structure you should include all functions definitions.

    example
        Let's assume we want deduce a computional complexity of sorting a list. It is necessary to create a list with randomly generated numbers. If it depends on problem size, you have to write '__N__' as an problem-size argument.
    >>> init_code = 'import random; list = [random.randint(0,10000) for i in range(__N__)]'

    alternatively, you could also create a *.py file with

    .. code-block:: python

        import random
        list = [random.randint(0,10000) for i in range(__N__)]

    and then assign a path to *init_code* variable

    >>> init_code = '/home/user/path/to/file.py'

clean_up_code(optional)
    This code would be executed after measuring times. Type a string or path to file.
    example
        .. code-block:: python

        clean_up_code ='import shutil; shutil.rmtree("./temporary_files_tree/")'


timeout
    Sets a time for algorithm in seconds. Default 30s.

log_verbose
    Specify a logger options.

      .. code-block:: python

        log_verbose = True `Puts all logging message to Standard output.`
        log_verbose = False `Puts only warning messages to Standard output.`
        log_verbose = 'path/to/file.log' `creates a log file at given path`

    default: True


RETURN VALUE
------------
count_it(pattern_invoke, init_code, clean_up_code, timeout, verbose) returns an object of Result class, with:

.. code-block:: python

    class Result:
        self.complexity `information about complexity of algorithm <- ['O(N), O(N^2)']`
        self.in_time() #returns a function time-> size(time), which count, how big problem can be solved in time msec
        self.how_long() #returns a function n-> time(n), which says, how long it take to solve n - sized problem (in msec)
        self.show() #shows a plot of masaured
        self.show('path-to-file/plot.png') #saves the plot


EXAMPLE USES
============

Binary Search
-------------

0) Create a file *init-b-search.py* with content

    .. code-block:: python

        def binarySearch(alist, item):
            first = 0
            last = len(alist)-1
            found = False
        while first<=last and not found:
            midpoint = (first + last)//2
            if alist[midpoint] == item:
                found = True
            else:
                if item < alist[midpoint]:
                    last = midpoint-1
                else:
                    first = midpoint+1
        return found

        import random
        list = [random.randint(0,100000) for i in range(__N__)]

1) Create a file *exec-b-search.py* with content

    .. code-block:: python

        binarySearch(list,random.randint(0,100000))

2) In Python interactive mode type:

    >>> import cmptcomplexity.aprox as ap
    >>> results = ap.countit(pattern_invoke = 'path/to/exec-b-search.py',init_code='path/to/init-b-search.py',timeout=30,log_verbose=True)
    >>> r # shows a graph
    >>> results.show() # shows a graph


    .. image:: https://raw.githubusercontent.com/AGHPythonCourse2017/zad2-moskalap/master/docs/img/binarySearch_plot.png?token=AWCREgQTcOXWrQP64Nlo66HK7RxWGwrnks5ZFyp3wA%3D%3D

BubbleSort
----------

0) Create a file *init-b-sort.py* with content

    .. code-block:: python

        def bubbleSort(alist):
            for passnum in range(len(alist)-1,0,-1):
                for i in range(passnum):
                    if alist[i]>alist[i+1]:
                        temp = alist[i]
                        alist[i] = alist[i+1]
                        alist[i+1] = temp

        import random
        list = [random.randint(0,100000) for i in range(__N__)]

1) Create a file *exec-b-sort.py* with content

    .. code-block:: python

        bubbleSort(list)


2) In Python interactive mode type:

    >>> import cmptcomplexity.aprox as ap
    >>> results = ap.countit(pattern_invoke = 'path/to/exec-b-sort.py',init_code='path/to/init-b-sort.py',timeout=30,log_verbose=True)
    >>> results.show() # shows a graph

    .. image:: https://raw.githubusercontent.com/AGHPythonCourse2017/zad2-moskalap/master/docs/img/bubblesort_plot.png?token=AWCREshMKaFLjCfQh5Gj9xrVjK_x_O5aks5ZFysEwA%3D%3D




HeapSort
--------


0) Create a file *exec-h-sort.py* with content

    .. code-block:: python


        heapsort(array)


1) Create a file *init-h-sort.py* with content

    .. code-block:: python


        def heapsort(lst):
        ''' Heapsort. Note: this function sorts in-place (it mutates the list). '''
         # in pseudo-code, heapify only called once, so inline it here
            for start in range((len(lst) - 2) // 2, -1, -1):
                siftdown(lst, start, len(lst) - 1)

            for end in range(len(lst) - 1, 0, -1):
                lst[end], lst[0] = lst[0], lst[end]
                siftdown(lst, 0, end - 1)
            return lst


        def siftdown(lst, start, end):
            root = start
            while True:
                child = root * 2 + 1
                if child > end: break
                if child + 1 <= end and lst[child] < lst[child + 1]:
                    child += 1
                if lst[root] < lst[child]:
                    lst[root], lst[child] = lst[child], lst[root]
                    root = child
                else:
                    break

        import random
        array = [random.randint(0,1000000) for i in range(__N__)]

2) In Python interactive mode type:

    >>> import cmptcomplexity.aprox as ap
    >>> results = ap.countit(pattern_invoke = 'path/to/exec-h-sort.py',init_code='path/to/init-h-sort.py',timeout=30,log_verbose=True)
    >>> results.show() # shows a graph


    .. image:: https://raw.githubusercontent.com/AGHPythonCourse2017/zad2-moskalap/master/docs/img/heapsort_plot.png?token=AWCREnwS_SzUL6cbAeYbTv0KrY38BIJSks5ZFys5wA%3D%3D


list append
-----------
0) In Python interactive mode type:

    >>> import cmptcomplexity.aprox as ap
    >>> results = ap.countit(pattern_invoke = 'l.append(513)',init_code='import random; l = [random.randint(0,1000000) for i in range(__N__)]',timeout=30,log_verbose=True)
    >>> results.show() # shows a graph

    .. image:: https://raw.githubusercontent.com/AGHPythonCourse2017/zad2-moskalap/master/docs/img/list.append()_plot.png?token=AWCREskpk9JyJ-UJFbKWHkvZsSFoGgLtks5ZFytuwA%3D%3D
