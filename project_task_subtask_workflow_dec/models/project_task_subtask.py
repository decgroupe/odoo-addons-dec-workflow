# -*- coding: utf-8 -*-
# Copyright (C) DEC SARL, Inc - All Rights Reserved.
# Written by Yann Papouin <ypa at decgroupe.com>, Mar 2021

from odoo import models, api, fields


class ProjectTaskSubtask(models.Model):
    _inherit = "project.task.subtask"
