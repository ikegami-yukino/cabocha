# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _CaboCha
else:
    import _CaboCha

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _CaboCha.SWIG_PyInstanceMethod_New
_swig_new_static_method = _CaboCha.SWIG_PyStaticMethod_New

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


CABOCHA_EUC_JP = _CaboCha.CABOCHA_EUC_JP
CABOCHA_CP932 = _CaboCha.CABOCHA_CP932
CABOCHA_UTF8 = _CaboCha.CABOCHA_UTF8
CABOCHA_ASCII = _CaboCha.CABOCHA_ASCII
CABOCHA_IPA = _CaboCha.CABOCHA_IPA
CABOCHA_JUMAN = _CaboCha.CABOCHA_JUMAN
CABOCHA_UNIDIC = _CaboCha.CABOCHA_UNIDIC
CABOCHA_FORMAT_TREE = _CaboCha.CABOCHA_FORMAT_TREE
CABOCHA_FORMAT_LATTICE = _CaboCha.CABOCHA_FORMAT_LATTICE
CABOCHA_FORMAT_TREE_LATTICE = _CaboCha.CABOCHA_FORMAT_TREE_LATTICE
CABOCHA_FORMAT_XML = _CaboCha.CABOCHA_FORMAT_XML
CABOCHA_FORMAT_CONLL = _CaboCha.CABOCHA_FORMAT_CONLL
CABOCHA_FORMAT_NONE = _CaboCha.CABOCHA_FORMAT_NONE
CABOCHA_INPUT_RAW_SENTENCE = _CaboCha.CABOCHA_INPUT_RAW_SENTENCE
CABOCHA_INPUT_POS = _CaboCha.CABOCHA_INPUT_POS
CABOCHA_INPUT_CHUNK = _CaboCha.CABOCHA_INPUT_CHUNK
CABOCHA_INPUT_SELECTION = _CaboCha.CABOCHA_INPUT_SELECTION
CABOCHA_INPUT_DEP = _CaboCha.CABOCHA_INPUT_DEP
CABOCHA_OUTPUT_RAW_SENTENCE = _CaboCha.CABOCHA_OUTPUT_RAW_SENTENCE
CABOCHA_OUTPUT_POS = _CaboCha.CABOCHA_OUTPUT_POS
CABOCHA_OUTPUT_CHUNK = _CaboCha.CABOCHA_OUTPUT_CHUNK
CABOCHA_OUTPUT_SELECTION = _CaboCha.CABOCHA_OUTPUT_SELECTION
CABOCHA_OUTPUT_DEP = _CaboCha.CABOCHA_OUTPUT_DEP
CABOCHA_TRAIN_NE = _CaboCha.CABOCHA_TRAIN_NE
CABOCHA_TRAIN_CHUNK = _CaboCha.CABOCHA_TRAIN_CHUNK
CABOCHA_TRAIN_DEP = _CaboCha.CABOCHA_TRAIN_DEP
class Chunk(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    link = property(_CaboCha.Chunk_link_get)
    head_pos = property(_CaboCha.Chunk_head_pos_get)
    func_pos = property(_CaboCha.Chunk_func_pos_get)
    token_size = property(_CaboCha.Chunk_token_size_get)
    token_pos = property(_CaboCha.Chunk_token_pos_get)
    score = property(_CaboCha.Chunk_score_get)
    additional_info = property(_CaboCha.Chunk_additional_info_get)
    feature_list_size = property(_CaboCha.Chunk_feature_list_size_get)
    feature_list = _swig_new_instance_method(_CaboCha.Chunk_feature_list)

# Register Chunk in _CaboCha:
_CaboCha.Chunk_swigregister(Chunk)

class Token(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    surface = property(_CaboCha.Token_surface_get)
    normalized_surface = property(_CaboCha.Token_normalized_surface_get)
    feature = property(_CaboCha.Token_feature_get)
    feature_list_size = property(_CaboCha.Token_feature_list_size_get)
    ne = property(_CaboCha.Token_ne_get)
    additional_info = property(_CaboCha.Token_additional_info_get)
    chunk = property(_CaboCha.Token_chunk_get)
    feature_list = _swig_new_instance_method(_CaboCha.Token_feature_list)

# Register Token in _CaboCha:
_CaboCha.Token_swigregister(Token)

EUC_JP = _CaboCha.EUC_JP
CP932 = _CaboCha.CP932
UTF8 = _CaboCha.UTF8
ASCII = _CaboCha.ASCII
IPA = _CaboCha.IPA
JUMAN = _CaboCha.JUMAN
UNIDIC = _CaboCha.UNIDIC
FORMAT_TREE = _CaboCha.FORMAT_TREE
FORMAT_LATTICE = _CaboCha.FORMAT_LATTICE
FORMAT_TREE_LATTICE = _CaboCha.FORMAT_TREE_LATTICE
FORMAT_XML = _CaboCha.FORMAT_XML
FORMAT_CONLL = _CaboCha.FORMAT_CONLL
FORMAT_NONE = _CaboCha.FORMAT_NONE
INPUT_RAW_SENTENCE = _CaboCha.INPUT_RAW_SENTENCE
INPUT_POS = _CaboCha.INPUT_POS
INPUT_CHUNK = _CaboCha.INPUT_CHUNK
INPUT_SELECTION = _CaboCha.INPUT_SELECTION
INPUT_DEP = _CaboCha.INPUT_DEP
OUTPUT_RAW_SENTENCE = _CaboCha.OUTPUT_RAW_SENTENCE
OUTPUT_POS = _CaboCha.OUTPUT_POS
OUTPUT_CHUNK = _CaboCha.OUTPUT_CHUNK
OUTPUT_SELECTION = _CaboCha.OUTPUT_SELECTION
OUTPUT_DEP = _CaboCha.OUTPUT_DEP
TRAIN_NE = _CaboCha.TRAIN_NE
TRAIN_CHUNK = _CaboCha.TRAIN_CHUNK
TRAIN_DEP = _CaboCha.TRAIN_DEP
class Tree(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    set_sentence = _swig_new_instance_method(_CaboCha.Tree_set_sentence)
    sentence = _swig_new_instance_method(_CaboCha.Tree_sentence)
    sentence_size = _swig_new_instance_method(_CaboCha.Tree_sentence_size)
    chunk = _swig_new_instance_method(_CaboCha.Tree_chunk)
    token = _swig_new_instance_method(_CaboCha.Tree_token)
    read = _swig_new_instance_method(_CaboCha.Tree_read)
    empty = _swig_new_instance_method(_CaboCha.Tree_empty)
    clear = _swig_new_instance_method(_CaboCha.Tree_clear)
    clear_chunk = _swig_new_instance_method(_CaboCha.Tree_clear_chunk)
    chunk_size = _swig_new_instance_method(_CaboCha.Tree_chunk_size)
    token_size = _swig_new_instance_method(_CaboCha.Tree_token_size)
    size = _swig_new_instance_method(_CaboCha.Tree_size)
    toString = _swig_new_instance_method(_CaboCha.Tree_toString)
    charset = _swig_new_instance_method(_CaboCha.Tree_charset)
    set_charset = _swig_new_instance_method(_CaboCha.Tree_set_charset)
    posset = _swig_new_instance_method(_CaboCha.Tree_posset)
    set_posset = _swig_new_instance_method(_CaboCha.Tree_set_posset)
    output_layer = _swig_new_instance_method(_CaboCha.Tree_output_layer)
    set_output_layer = _swig_new_instance_method(_CaboCha.Tree_set_output_layer)
    what = _swig_new_instance_method(_CaboCha.Tree_what)

    def __init__(self):
        _CaboCha.Tree_swiginit(self, _CaboCha.new_Tree())
    __swig_destroy__ = _CaboCha.delete_Tree

# Register Tree in _CaboCha:
_CaboCha.Tree_swigregister(Tree)

class Parser(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    parseToString = _swig_new_instance_method(_CaboCha.Parser_parseToString)
    parse = _swig_new_instance_method(_CaboCha.Parser_parse)
    what = _swig_new_instance_method(_CaboCha.Parser_what)
    version = _swig_new_static_method(_CaboCha.Parser_version)
    __swig_destroy__ = _CaboCha.delete_Parser

    def __init__(self, *args):
        _CaboCha.Parser_swiginit(self, _CaboCha.new_Parser(*args))

# Register Parser in _CaboCha:
_CaboCha.Parser_swigregister(Parser)
Parser_version = _CaboCha.Parser_version

getLastError = _CaboCha.getLastError
runDependencyTraining = _CaboCha.runDependencyTraining
runChunkingTraining = _CaboCha.runChunkingTraining
runNETraining = _CaboCha.runNETraining
VERSION = _CaboCha.VERSION


