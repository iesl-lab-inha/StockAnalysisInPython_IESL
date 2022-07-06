Python 3.7.8 (tags/v3.7.8:4b47a5b6ba, Jun 28 2020, 08:53:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

>>> def func1():
	pass

>>> def func2():
	return

>>> def func3():
	return None

>>> print(func1()); print(func2()); print(func3())
None
None
None

>>> type(None)
<class 'NoneType'>
>>> func1() == None
True
>>> func1() is None
True
>>> 
>>> 
================================================================================================= RESTART: Shell ================================================================================================
>>> def myFunc():
	var1 = 'a'
	var2 = [1, 2, 3]
	var3 = max
	return var1, var2, var3

>>> myFunc()
('a', [1, 2, 3], <built-in function max>)
>>> s, l, f = myFunc()
>>> s
'a'
>>> l
[1, 2, 3]
>>> f
<built-in function max>
>>> 
================================================================================================= RESTART: Shell ================================================================================================
>>> insertComma = lambda x : format(x, ',')
>>> insertComma(1234567890)
'1,234,567,890'
>>> 
================================================================================================= RESTART: Shell ================================================================================================
>>> abs = 1
>>> abs(-100)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    abs(-100)
TypeError: 'int' object is not callable
>>> 
================================================================================================= RESTART: Shell ================================================================================================
>>> help('modules')

Please wait a moment while I gather a list of all available modules...

__future__          atexit              html                search
__main__            audioop             http                searchbase
_abc                autocomplete        hyperparser         searchengine
_ast                autocomplete_w      idle                secrets
_asyncio            autoexpand          idle_test           select
_bisect             base64              idlelib             selectors
_blake2             bdb                 imaplib             setuptools
_bootlocale         binascii            imghdr              shelve
_bz2                binhex              imp                 shlex
_codecs             bisect              importlib           shutil
_codecs_cn          browser             inspect             sidebar
_codecs_hk          builtins            io                  signal
_codecs_iso2022     bz2                 iomenu              site
_codecs_jp          cProfile            ipaddress           smtpd
_codecs_kr          calendar            itertools           smtplib
_codecs_tw          calltip             json                sndhdr
_collections        calltip_w           keyword             socket
_collections_abc    cgi                 lib2to3             socketserver
_compat_pickle      cgitb               linecache           sqlite3
_compression        chunk               locale              squeezer
_contextvars        cmath               logging             sre_compile
_csv                cmd                 lzma                sre_constants
_ctypes             code                macosx              sre_parse
_ctypes_test        codecontext         macpath             ssl
_datetime           codecs              mailbox             stackviewer
_decimal            codeop              mailcap             stat
_dummy_thread       collections         mainmenu            statistics
_elementtree        colorizer           marshal             statusbar
_functools          colorsys            math                string
_hashlib            compileall          mimetypes           stringprep
_heapq              concurrent          mmap                struct
_imp                config              modulefinder        subprocess
_io                 config_key          msilib              sunau
_json               configdialog        msvcrt              symbol
_locale             configparser        multicall           symtable
_lsprof             contextlib          multiprocessing     sys
_lzma               contextvars         netrc               sysconfig
_markupbase         copy                nntplib             tabnanny
_md5                copyreg             nt                  tarfile
_msi                crypt               ntpath              telnetlib
_multibytecodec     csv                 nturl2path          tempfile
_multiprocessing    ctypes              numbers             test
_opcode             curses              opcode              textview
_operator           dataclasses         operator            textwrap
_osx_support        datetime            optparse            this
_overlapped         dbm                 os                  threading
_pickle             debugger            outwin              time
_py_abc             debugger_r          parenmatch          timeit
_pydecimal          debugobj            parser              tkinter
_pyio               debugobj_r          pathbrowser         token
_queue              decimal             pathlib             tokenize
_random             delegator           pdb                 tooltip
_sha1               difflib             percolator          trace
_sha256             dis                 pickle              traceback
_sha3               distutils           pickletools         tracemalloc
_sha512             doctest             pip                 tree
_signal             dummy_threading     pipes               tty
_sitebuiltins       dynoption           pkg_resources       turtle
_socket             easy_install        pkgutil             turtledemo
_sqlite3            editor              platform            types
_sre                email               plistlib            typing
_ssl                encodings           poplib              undo
_stat               ensurepip           posixpath           unicodedata
_string             enum                pprint              unittest
_strptime           errno               profile             urllib
_struct             faulthandler        pstats              uu
_symtable           filecmp             pty                 uuid
_testbuffer         fileinput           py_compile          venv
_testcapi           filelist            pyclbr              warnings
_testconsole        fnmatch             pydoc               wave
_testimportmultiple format              pydoc_data          weakref
_testmultiphase     formatter           pyexpat             webbrowser
_thread             fractions           pyparse             window
_threading_local    ftplib              pyshell             winreg
_tkinter            functools           query               winsound
_tracemalloc        gc                  queue               wsgiref
_warnings           genericpath         quopri              xdrlib
_weakref            getopt              random              xml
_weakrefset         getpass             re                  xmlrpc
_winapi             gettext             redirector          xxsubtype
abc                 glob                replace             zipapp
aifc                grep                reprlib             zipfile
antigravity         gzip                rlcompleter         zipimport
argparse            hashlib             rpc                 zlib
array               heapq               run                 zoomheight
ast                 help                runpy               zzdummy
asynchat            help_about          runscript           
asyncio             history             sched               
asyncore            hmac                scrolledlist        

Enter any module name to get more help.  Or, type "modules spam" to search
for modules whose name or summary contain the string "spam".

>>> 
