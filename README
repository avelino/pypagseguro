API Pagseguro
============

Installation
============
If you have _setuptools_ you can use 
    $ easy_install -U pypagseguro
Otherwise, you can download the source from [GitHub][git] and run 
    $ python setup.py install

[git]: https://github.com/avelino/pypagseguro "pyPagSeguro"

Examples
========
Some simple examples of what pyPagSeguro code looks like:
    # -*- coding: utf-8 -*-
    from pypagseguro import *
    carrinho = Pagseguro(email_cobranca='pagseguro@visie.com.br',tipo='CP')
    carrinho.item(id=1, descr='Um produto de exemplo', quant=5, valor=10)
    carrinho.item(id=2, descr='Outro produto de exemplo', quant=2, valor=100)
    print carrinho.mostra()
