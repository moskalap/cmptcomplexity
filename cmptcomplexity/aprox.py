import logging
import sys

import cmptcomplexity.scripts.controller as cntrl
import cmptcomplexity.scripts.task as ctask


def count_it(pattern_invoke,  # pattern of invoking code, with __N__ for problem size
             init_code="",  # code which make set-up of envoriemnt (__N__ for problem size)
             clean_up_code="",
             timeout=30,
             log_verbose=True):
    if log_verbose:
        if isinstance(log_verbose, str):  # logging to file
            logging.basicConfig(filename=log_verbose, level=logging.DEBUG,
                                format='%(asctime)s  - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        else:
            logging.basicConfig(level=logging.DEBUG, format='%(asctime)s  - %(levelname)s - %(message)s',
                                datefmt='%m/%d/%Y %I:%M:%S %p')
    else:
        logging.basicConfig(level=logging.WARN, format='%(asctime)s  - %(levelname)s - %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p')

    logging.info('started program with arguments %s', sys.argv)
    import cmptcomplexity.scripts.exceptions as excp
    task = []
    try:
        task = ctask.Task(init_code, clean_up_code, example_invoke=pattern_invoke)
        controller = cntrl.Controller(task, timeout)
        data = controller.get_data()

    except excp.WrongTimeoutCCException:
        print("The time out must be > 0.5")
        exit(-1)
    except excp.ArgumentPatternError:
        print('There must be "__N__" as a size-problem parameter')
        exit(-1)

    finally:

        if task.clean_up_code != "":
            try:
                exec(clean_up_code)
            except Exception:
                # Ignoring others exception, data is very important
                logging.error('Something went wrong, returned tuple("err", partial_data)')
                return 'err', data
        else:
            return data
