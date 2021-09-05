# -*- coding: utf-8 -*-
# Copyright (C) DEC SARL, Inc - All Rights Reserved.
# Written by Yann Papouin <ypa at decgroupe.com>, Jan 2021

from odoo import models, api, fields


class Project(models.Model):
    _inherit = "project.project"

    privacy_visibility = fields.Selection(default='employees', )
