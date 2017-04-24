# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
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
# Generated by the Odoo plugin for Dia !
from odoo import api, fields, models

class EventRegistrationTIL(models.Model):
    _inherit = 'event.registration'

    partner_id = fields.Many2one('regtil.persona')

    @api.onchange('partner_id')
    def _onchange_partner(self):
        if self.partner_id:
            self.name = self.partner_id.primer_nombre + ' ' + self.partner_id.primer_apellido
            self.email = self.partner_id.email
            self.phone = self.partner_id.telefono