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
from openerp import api, models, fields
from datetime import datetime


class use_case(models.Model):
     _inherit = 'use_case'
     _description = 'Use Case Toggle State'
     state = fields.Selection( [('draft', 'Draft'),
                 ('open', 'Open'),('done', 'Done')],
                  string='State', default='draft')
     @api.one
     def draft_open_done_toggle(self):
       if (self.state == 'draft'):
        self.state = 'open'
       elif(self.state == 'open'):
         self.state = 'done'
       elif(self.state == 'done'):
         self.state = 'draft'
       return True



class use_case_collection(use_case):
     _inherit = 'use_case.collection'
     


