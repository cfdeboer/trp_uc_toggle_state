# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    This module copyright (C) 2012 Therp BV (<http://therp.nl>).
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
    "name": "Use Case Toggle buttons for state change (draft/open/done) ",
    "version": "0.1",
    "author": "Therp BV",
    "category":'Depends on trp_use_case - from https://github.com/hbrunn/therp-addons',
    'complexity': "normal",
    "description": """
    
    Toggle buttons for state change between draft/open/done,only visible for base.group_user
    
    """,
    'website': 'http://therp.nl',
    'images': [],
    'depends': [
        'trp_use_case',
    ],
    'data': [
        'view/use_case.xml',
        'view/use_case_collection.xml',
    ],
    "license": 'AGPL-3',
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
