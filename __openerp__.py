# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2014 Business Tec Systems S.A.(<http://businesstec.net>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Invoice Extended Days Overdue',
    'version': '1.0',
    'author': 'Business Tec Systems',
    'summary': 'Adding field to account.invoice model with calculation of days overdue to display nicely in UI',
    'description': """
Invoice Extended Days Overduue
==============================
Adding field to account.invoice model with calculation of days overdue to display nicely in UI
    """,
    'website': 'https://businesstec.net',
    'images': [],
    'depends': ['account', 'sale'],
    'sequence': 18,
    'data': [
        'invoice_days_extended.xml',
    ],
    'installable': True,
    'auto_install': False,
}
