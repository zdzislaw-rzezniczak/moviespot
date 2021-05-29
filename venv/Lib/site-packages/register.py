# The MIT License (MIT)
#
# Copyright (c) 2015 Alexander Weigl
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.



"""
.. see:: :py:class:`register.Registry`
"""

__author__ = "Alexander Weigl <Alexander.Weigl@student.kit.edu>"

__date__ = "2015-03-16"

__version__ = "0.1"

__all__ = ['Registry']



def get_name(obj, attribs=("__name__", "func_name")):
    """Try to get the name of an function or a class.

    :param obj:
    :return:
    """

    for a in attribs:
        if hasattr(obj, a):
            return getattr(obj, a)


class Registry(object):
    """Registry collects functions or class

    """

    def __init__(self):
        self._register = dict()


    def register(self, fn, name, meta=None):
        self._register[name] = (fn, meta or {})

    def __call__(self, fn_or_name=None, **kwargs):
        if fn_or_name and callable(fn_or_name):
            name = get_name(fn_or_name)
            self.register(fn_or_name, name)
            return fn_or_name

        else:
            def r(fn):
                name = fn_or_name or get_name(fn)
                self.register(fn, name, kwargs)
                return fn

            return r


    def __contains__(self, item):
        return item in self._register

    def lookup(self, name, default=None):
        try:
            return self._register[name][0]
        except:
            return default

    def meta(self, name):
        return self._register[name][1]
