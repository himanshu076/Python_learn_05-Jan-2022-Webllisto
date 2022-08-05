'''***********PEP8 Style Guide************'''
'''
1. "Code Lay-out"

    1. Indentation - 
        Use 4 spaces per indentation level.

        # Correct :

        # Aligned with opening delimiter.
        foo = long_function_name(var_one, var_two,
                                 var_three, var_four)

        # Add 4 spaces (an extra level of indentation) to distinguish arguments from the rest.
        def long_function_name(
                var_one, var_two, var_three,
                var_four):
            print(var_one)

        # Hanging indents should add a level.
        foo = long_function_name(
            var_one, var_two,
            var_three, var_four)
        
        # No extra indentation.
        if (this_is_one_thing and
            that_is_another_thing):
            do_something()

        # Add a comment, which will provide some distinction in editors
        # supporting syntax highlighting.
        if (this_is_one_thing and
            that_is_another_thing):
            # Since both conditions are true, we can frobnicate.
            do_something()

        # Add some extra indentation on the conditional continuation line.
        if (this_is_one_thing
                and that_is_another_thing):
            do_something()

    2. Tabs or Spaces? - 
        Spaces are the preferred indentation method.

        Tabs should be used solely to remain consistent with code that is already indented with tabs.

        Python disallows mixing tabs and spaces for indentation.

    3. Maximum Line Length - 
        1. Limit all lines to a maximum of 79 characters.

        2. For flowing long blocks of text with fewer structural restrictions(docstrings or comments), the line length should be limited to 72 characters.

        3. Backslashes may still be appropriate at times. For example, long, multiple with-statements could not use implicit continuation before Python 3.10, so backslashes were acceptable for that case:

            with open('/path/to/some/file/you/want/to/read') as file_1, \
                open('/path/to/some/file/being/written', 'w') as file_2:
                file_2.write(file_1.read())\

    4. Should a Line Break Before or After a Binary Operator? - 
        # Wrong:
        # operators sit far away from their operands
        income = (gross_wages +
                taxable_interest +
                (dividends - qualified_dividends) -
                ira_deduction -
                student_loan_interest)

        # Correct:
            # easy to match operators with operands
            income = (gross_wages
                    + taxable_interest
                    + (dividends - qualified_dividends)
                    - ira_deduction
                    - student_loan_interest)

    5. Blank Lines - 
        Use blank lines in functions, sparingly, to indicate logical sections.

    6. Source File Encoding - 
        Code in the core Python distribution should always use UTF-8, and should not have an encoding declaration.

        In the standard library, non-UTF-8 encodings should be used only for test purposes. Use non-ASCII characters sparingly, preferably only to denote places and human names. If using non-ASCII characters as data, avoid noisy Unicode characters like z̯̯͡a̧͎̺l̡͓̫g̹̲o̡̼̘ and byte order marks.

        All identifiers in the Python standard library MUST use ASCII-only identifiers, and SHOULD use English words wherever feasible (in many cases, abbreviations and technical terms are used which aren't English).

    7. Imports - 
        1. Imports should usually be on separate lines:

            # Correct:
            import os
            import sys

            # Wrong:
            import sys, os

            # Correct:
            from subprocess import Popen, PIPE

        2. Imports are always put at the top of the file, just after any module comments and docstrings, and before module globals and constants.

        Imports should be grouped in the following order:

            1. Standard library imports.
            2. Related third party imports.
            3. Local application/library specific imports.
            You should put a blank line between each group of imports.

        3. Absolute imports are recommended, - 

            import mypkg.sibling
            from mypkg import sibling
            from mypkg.sibling import example

            However, explicit relative imports are an acceptable alternative to absolute imports, - 

                from . import sibling
                from .sibling import example

        4. When importing a class from a class-containing module, it's usually okay to spell this:

            from myclass import MyClass
            from foo.bar.yourclass import YourClass

            If this spelling causes local name clashes, then spell them explicitly:

                import myclass
                import foo.bar.yourclass

                and use "myclass.MyClass" and "foo.bar.yourclass.YourClass".

        5. Wildcard imports (from <module> import *) should be avoided.

    8. Module Level Dunder Names - 
        Module level "dunders" (i.e. names with two leading and two trailing underscores) such as __all__, __author__, __version__, etc. should be placed after the module docstring but before any import statements except from __future__ imports. Python mandates that future-imports must appear in the module before any other code except docstrings:

        """This is the example module.

            This module does stuff.
            """

            from __future__ import barry_as_FLUFL

            __all__ = ['a', 'b', 'c']
            __version__ = '0.1'
            __author__ = 'Cardinal Biggles'

            import os
            import sys

2. String Quotes - 
    In Python, single-quoted strings and double-quoted strings are the same. This PEP does not make a recommendation for this. Pick a rule and stick to it. When a string contains single or double quote characters, however, use the other one to avoid backslashes in the string. It improves readability.

    For triple-quoted strings, always use double quote characters to be consistent with the docstring convention in PEP 257.

3. Whitespace in Expressions and Statements - 

    1. Pet Peeves - 
        Avoid extraneous whitespace in the following situations:

        1. Immediately inside parentheses, brackets or braces:

            # Correct:
            spam(ham[1], {eggs: 2})

            # Wrong:
            spam( ham[ 1 ], { eggs: 2 } )

        2. Between a trailing comma and a following close parenthesis:

            # Correct:
            foo = (0,)

            # Wrong:
            bar = (0, )

        3. Immediately before a comma, semicolon, or colon:

            # Correct:
            if x == 4: print(x, y); x, y = y, x

            # Wrong:
            if x == 4 : print(x , y) ; x , y = y , 

        4. However, in a slice the colon acts like a binary operator, and should have equal amounts on either side (treating it as the operator with the lowest priority). In an extended slice, both colons must have the same amount of spacing applied. Exception: when a slice parameter is omitted, the space is omitted:

            # Correct:
            ham[1:9], ham[1:9:3], ham[:9:3], ham[1::3], ham[1:9:]
            ham[lower:upper], ham[lower:upper:], ham[lower::step]
            ham[lower+offset : upper+offset]
            ham[: upper_fn(x) : step_fn(x)], ham[:: step_fn(x)]
            ham[lower + offset : upper + offset]

            # Wrong:
            ham[lower + offset:upper + offset]
            ham[1: 9], ham[1 :9], ham[1:9 :3]
            ham[lower : : upper]
            ham[ : upper]

        5. Immediately before the open parenthesis that starts the argument list of a function call:

            # Correct:
            spam(1)

            # Wrong:
            spam (1)

        6. Immediately before the open parenthesis that starts an indexing or slicing:

            # Correct:
            dct['key'] = lst[index]

            # Wrong:
            dct ['key'] = lst [index]

        7. More than one space around an assignment (or other) operator to align it with another:

            # Correct:
            x = 1
            y = 2
            long_variable = 3

            # Wrong:
            x             = 1
            y             = 2
            long_variable = 3            

    2. Other Recommendations
        1. Avoid trailing whitespace anywhere.

        2. If operators with different priorities are used, consider adding whitespace around the operators with the lowest priority(ies). Use your own judgment; however, never use more than one space, and always have the same amount of whitespace on both sides of a binary operator:

            # Correct:
            i = i + 1
            submitted += 1
            x = x*2 - 1
            hypot2 = x*x + y*y
            c = (a+b) * (a-b)

            # Wrong:
            i=i+1
            submitted +=1
            x = x * 2 - 1
            hypot2 = x * x + y * y
            c = (a + b) * (a - b)

        3. Function annotations should use the normal rules for colons and always have spaces around the -> arrow if present. (See Function Annotations below for more about function annotations.):

            # Correct:
            def munge(input: AnyStr): ...
            def munge() -> PosInt: ...

            # Wrong:
            def munge(input:AnyStr): ...
            def munge()->PosInt: ...

        4. Don't use spaces around the = sign when used to indicate a keyword argument, or when used to indicate a default value for an unannotated function parameter:

            # Correct:
            def complex(real, imag=0.0):
                return magic(r=real, i=imag)

            # Wrong:
            def complex(real, imag = 0.0):
                return magic(r = real, i = imag)

            When combining an argument annotation with a default value, however, do use spaces around the = sign:

                # Correct:
                def munge(sep: AnyStr = None): ...
                def munge(input: AnyStr, sep: AnyStr = None, limit=1000): ...

                # Wrong:
                def munge(input: AnyStr=None): ...
                def munge(input: AnyStr, limit = 1000): ...

        5. Compound statements (multiple statements on the same line) are generally discouraged:

            # Correct:
            if foo == 'blah':
                do_blah_thing()
            do_one()
            do_two()
            do_three()

            Rather not:

            # Wrong:
            if foo == 'blah': do_blah_thing()
            do_one(); do_two(); do_three()

        6. While sometimes it's okay to put an if/for/while with a small body on the same line, never do this for multi-clause statements. Also avoid folding such long lines!

            Rather not:

            # Wrong:
            if foo == 'blah': do_blah_thing()
            for x in lst: total += x
            while t < 10: t = delay()
            Definitely not:

            # Wrong:
            if foo == 'blah': do_blah_thing()
            else: do_non_blah_thing()

            try: something()
            finally: cleanup()

            do_one(); do_two(); do_three(long, argument,
                                        list, like, this)

            if foo == 'blah': one(); two(); three()

4. When to Use Trailing Commas
    Trailing commas are usually optional, except they are mandatory when making a tuple of one element. For clarity, it is recommended to surround the latter in (technically redundant) parentheses:

        # Correct:
        FILES = ('setup.cfg',)
        
        # Wrong:
        FILES = 'setup.cfg',


    When trailing commas are redundant, they are often helpful when a version control system is used, when a list of values, arguments or imported items is expected to be extended over time. The pattern is to put each value (etc.) on a line by itself, always adding a trailing comma, and add the close parenthesis/bracket/brace on the next line. However it does not make sense to have a trailing comma on the same line as the closing delimiter (except in the above case of singleton tuples):

        # Correct:
        FILES = [
            'setup.cfg',
            'tox.ini',
            ]
        initialize(FILES,
                error=True,
                )

        # Wrong:
        FILES = ['setup.cfg', 'tox.ini',]
        initialize(FILES, error=True,)

5. Comments - 
    Comments that contradict the code are worse than no comments. Always make a priority of keeping the comments up-to-date when the code changes!

    Comments should be complete sentences. The first word should be capitalized, unless it is an identifier that begins with a lower case letter (never alter the case of identifiers!).

    Block comments generally consist of one or more paragraphs built out of complete sentences, with each sentence ending in a period.

    You should use two spaces after a sentence-ending period in multi- sentence comments, except after the final sentence.

    Ensure that your comments are clear and easily understandable to other speakers of the language you are writing in.

    Python coders from non-English speaking countries: please write your comments in English, unless you are 120% sure that the code will never be read by people who don't speak your language.

    1. Block Comments - 
        Block comments generally apply to some (or all) code that follows them, and are indented to the same level as that code. Each line of a block comment starts with a # and a single space (unless it is indented text inside the comment).

        Paragraphs inside a block comment are separated by a line containing a single #.

    2. Inline Comments - 
        Use inline comments sparingly.

        An inline comment is a comment on the same line as a statement. Inline comments should be separated by at least two spaces from the statement. They should start with a # and a single space.

        Inline comments are unnecessary and in fact distracting if they state the obvious. Don't do this:

        x = x + 1                 # Increment x
        But sometimes, this is useful:

        x = x + 1                 # Compensate for border

    3. Documentation Strings - 
        Conventions for writing good documentation strings (a.k.a. "docstrings") are immortalized in PEP 257.

        1. Write docstrings for all public modules, functions, classes, and methods. Docstrings are not necessary for non-public methods, but you should have a comment that describes what the method does. This comment should appear after the def line.

        2. PEP 257 describes good docstring conventions. Note that most importantly, the """ that ends a multiline docstring should be on a line by itself:

            """Return a foobang

            Optional plotz says to frobnicate the bizbaz first.
            """
        3. For one liner docstrings, please keep the closing """ on the same line:

            """Return an ex-parrot."""

6. Naming Conventions - 
    The naming conventions of Python's library are a bit of a mess, so we'll never get this completely consistent -- nevertheless, here are the currently recommended naming standards. New modules and packages (including third party frameworks) should be written to these standards, but where an existing library has a different style, internal consistency is preferred.

    1. Overriding Principle - 
        Names that are visible to the user as public parts of the API should follow conventions that reflect usage rather than implementation.

    2. Descriptive: Naming Styles

        There are a lot of different naming styles. It helps to be able to recognize what naming style is being used, independently from what they are used for.

        The following naming styles are commonly distinguished:

            1. b (single lowercase letter)

            2. B (single uppercase letter)

            3. lowercase

            4. lower_case_with_underscores

            5. UPPERCASE

            6. UPPER_CASE_WITH_UNDERSCORES

            7. CapitalizedWords (or CapWords, or CamelCase -- so named because of the bumpy look of its letters [4]). This is also sometimes known as StudlyCaps.

            Note: When using acronyms in CapWords, capitalize all the letters of the acronym. Thus HTTPServerError is better than HttpServerError.

            8. mixedCase (differs from CapitalizedWords by initial lowercase character!)

            9. Capitalized_Words_With_Underscores (ugly!)

        There's also the style of using a short unique prefix to group related names together. This is not used much in Python, but it is mentioned for completeness. For example, the os.stat() function returns a tuple whose items traditionally have names like st_mode, st_size, st_mtime and so on. (This is done to emphasize the correspondence with the fields of the POSIX system call struct, which helps programmers familiar with that.)

        The X11 library uses a leading X for all its public functions. In Python, this style is generally deemed unnecessary because attribute and method names are prefixed with an object, and function names are prefixed with a module name.

        In addition, the following special forms using leading or trailing underscores are recognized (these can generally be combined with any case convention):

        10. _single_leading_underscore: weak "internal use" indicator. E.g. from M import * does not import objects whose names start with an underscore.

        11. single_trailing_underscore_: used by convention to avoid conflicts with Python keyword, e.g.

        12. tkinter.Toplevel(master, class_='ClassName')
        __double_leading_underscore: when naming a class attribute, invokes name mangling (inside class FooBar, __boo becomes _FooBar__boo; see below).

        13. __double_leading_and_trailing_underscore__: "magic" objects or attributes that live in user-controlled namespaces. E.g. __init__, __import__ or __file__. Never invent such names; only use them as documented.

    3. Prescriptive: Naming Conventions - 

        1. Names to Avoid - 
            Never use the characters 'l' (lowercase letter el), 'O' (uppercase letter oh), or 'I' (uppercase letter eye) as single character variable names.

            In some fonts, these characters are indistinguishable from the numerals one and zero. When tempted to use 'l', use 'L' instead.

        2. ASCII Compatibility -
            Identifiers used in the standard library must be ASCII compatible as described in the policy section of PEP 3131.

        3. Package and Module Names - 
            Modules should have short, all-lowercase names. Underscores can be used in the module name if it improves readability. Python packages should also have short, all-lowercase names, although the use of underscores is discouraged.

            When an extension module written in C or C++ has an accompanying Python module that provides a higher level (e.g. more object oriented) interface, the C/C++ module has a leading underscore (e.g. _socket).

        4. Class Names - 
            Class names should normally use the CapWords convention.

            The naming convention for functions may be used instead in cases where the interface is documented and used primarily as a callable.

            Note that there is a separate convention for builtin names: most builtin names are single words (or two words run together), with the CapWords convention used only for exception names and builtin constants.

        5. Type Variable Names - 
            Names of type variables introduced in PEP 484 should normally use CapWords preferring short names: T, AnyStr, Num. It is recommended to add suffixes _co or _contra to the variables used to declare covariant or contravariant behavior correspondingly:

            from typing import TypeVar

            VT_co = TypeVar('VT_co', covariant=True)
            KT_contra = TypeVar('KT_contra', contravariant=True)

        6. Exception Names - 
            Because exceptions should be classes, the class naming convention applies here. However, you should use the suffix "Error" on your exception names (if the exception actually is an error).

        7. Global Variable Names
            (Let's hope that these variables are meant for use inside one module only.) The conventions are about the same as those for functions.

            Modules that are designed for use via from M import * should use the __all__ mechanism to prevent exporting globals, or use the older convention of prefixing such globals with an underscore (which you might want to do to indicate these globals are "module non-public").

        8. Function and Variable Names
            Function names should be lowercase, with words separated by underscores as necessary to improve readability.

            Variable names follow the same convention as function names.

            mixedCase is allowed only in contexts where that's already the prevailing style (e.g. threading.py), to retain backwards compatibility.

        9. Function and Method Arguments
            Always use self for the first argument to instance methods.

            Always use cls for the first argument to class methods.

            If a function argument's name clashes with a reserved keyword, it is generally better to append a single trailing underscore rather than use an abbreviation or spelling corruption. Thus class_ is better than clss. (Perhaps better is to avoid such clashes by using a synonym.)

        10. Method Names and Instance Variables
            Use the function naming rules: lowercase with words separated by underscores as necessary to improve readability.

            Use one leading underscore only for non-public methods and instance variables.

            To avoid name clashes with subclasses, use two leading underscores to invoke Python's name mangling rules.

            Python mangles these names with the class name: if class Foo has an attribute named __a, it cannot be accessed by Foo.__a. (An insistent user could still gain access by calling Foo._Foo__a.) Generally, double leading underscores should be used only to avoid name conflicts with attributes in classes designed to be subclassed.

            Note: there is some controversy about the use of __names (see below).

        11. Constants
            Constants are usually defined on a module level and written in all capital letters with underscores separating words. Examples include MAX_OVERFLOW and TOTAL.

        12. 

    
'''