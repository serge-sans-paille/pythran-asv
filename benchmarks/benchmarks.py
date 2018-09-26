# Write the benchmarking functions here.
# See "Writing benchmarks" in the asv docs for more information.

import pythran
import os.path
import glob
import re
import sys
import shutil
import tempfile


kernels = sorted(glob.glob(os.path.join(os.path.dirname(__file__),
                                        '..', 'numpy-benchmarks', 'benchmarks', '*.py')))

class TimeSuite:
    """
    An example benchmark that times the performance of various kinds
    of iterating over dictionaries in Python.
    """

    timeout = 100000000.

    def __init__(self):
        #self.repeat = 11
        #self.number = 40
        pass

    def setup_cache(self):
        for filename in kernels:
            _setup, _run = _extract(filename)
            basename = os.path.basename(filename)
            function, _ = os.path.splitext(basename)
            output = os.path.join(".", function + ".so")
            try:
                pythran.compile_pythranfile(filename, output_file=output)
            except Exception:
                # workaround pythran annotation change
                tmpd = tempfile.mkdtemp()
                tmpf = os.path.join(tmpd, basename)
                with open(tmpf, 'w') as fout:
                    with open(filename) as fin:
                        outlines = []
                        for line in fin.readlines():
                            if line.startswith('#pythran'):
                                line = re.sub(r'\[\d+', '[:', line)
                                line = re.sub(r'\d+\]', ':]', line)
                                line = re.sub(r',\s*\d+\s*,', ',:,', line)
                            outlines.append(line)
                        fout.write(''.join(outlines))
                try:
                    pythran.compile_pythranfile(tmpf, output_file=output)
                except Exception as e:
                    pass
                finally:
                    shutil.rmtree(tmpd)

    def setup(self):
        sys.path.insert(0, ".")



re_setup = re.compile('^#setup: (.*)$')
re_run = re.compile('^#run: (.*)$')

def _process_lines(filename, lines):
    for line in lines:
        m = re_setup.match(line)
        if m:
            setup = m.group(1)
        m = re_run.match(line)
        if m:
            run = m.group(1)
    try:
        return setup, run
    except NameError as n:
        raise RuntimeError('%s has invalid header' % filename)

def _extract(filename):
    with open(filename) as fd:
        return _process_lines(filename, fd)

def make_eval(filename, function, r, e):
    def runner(self):
        e[function] = getattr(__import__(function), function)
        eval(r, e)
    with open(filename) as src:
        runner.__doc__ = src.read()
    return runner

for filename in kernels:
    _setup, _run = _extract(filename)
    basename = os.path.basename(filename)
    function, _ = os.path.splitext(basename)
    env = {}
    exec(_setup, env)
    assert not hasattr(TimeSuite, function)
    setattr(TimeSuite, 'time_' + function, make_eval(filename, function, _run, env))
