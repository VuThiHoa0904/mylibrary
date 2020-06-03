# -*- coding: utf-8 -*-

{
    'name': 'My Library',
    'summary': 'Manager my library',
    'version': '10.0.1.0.0',
    'author': 'HoaVu',
    'category': 'Book Application',
    'license': 'AGPL-3',
    'website': 'http://www.domain.com',
    'sequence': 1,
    'depends': ['website'],
    'data': [
        'views/book.xml',
        'views/author.xml',
        'views/category.xml',
        'views/book_loan.xml',
        'views/employees.xml',
        'views/res_partner.xml',
        'views/menu.xml',
        'security/group.xml',
        'security/ir.model.access.csv',
        'security/record_rules.xml',
        'views/template.xml',
        'data/sequence.xml',
        'reports/book_card.xml',

    ],
    'demo': [
         'demo/demo.xml',
    ],
    'css': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'description': """
		Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do 
		eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut 
		enim ad minim veniam, quis nostrud exercitation ullamco laboris
		nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor 
		in reprehenderit in voluptate velit esse cillum dolore eu fugiat
		nulla pariatur. Excepteur sint occaecat cupidatat non proident, 
		sunt in culpa qui officia deserunt mollit anim id est laborum.
	""",
}


